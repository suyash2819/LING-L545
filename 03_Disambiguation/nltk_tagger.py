from nltk.corpus.reader.conll import ConllCorpusReader
from nltk.tag import UnigramTagger

def read_conllu(file_path):
    sentences = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_sentence = []
        for line in file:
            if line.startswith('#'):
                continue
            elif line.strip() == "":
                if current_sentence:
                    sentences.append(current_sentence)
                    current_sentence = []
            else:
                parts = line.strip().split('\t')
                if len(parts) == 10:
                    current_sentence.append((parts[1], parts[3]))
                else:
                    # Handle non-standard lines here, e.g., skip or modify them
                    print(f"Skipping non-standard line: {line.strip()}")
        if current_sentence:  # add the last sentence if file doesn't end with a newline
            sentences.append(current_sentence)
    return sentences




train_file = 'fi_tdt-ud-train.conllu'
train_data = read_conllu(train_file)

unigram_tagger = UnigramTagger(train_data)

test_file = 'fi_tdt-ud-test.conllu'
test_data = read_conllu(test_file)

tagged_test_data = [unigram_tagger.tag(sent) for sent in test_data]

def format_to_conllu(tagged_sentence, original_sentence):
    conllu_formatted = []
    for line in original_sentence:
        # Preserve comment lines as they are
        if line.startswith('#'):
            conllu_formatted.append(line)
            continue

        # Process token lines
        parts = line.split('\t')
        if len(parts) == 10:
            word, original_pos = parts[1], parts[3]
            # Find the corresponding tagged POS for this word
            tagged_pos = next((pos for w, pos in tagged_sentence if w == word), original_pos)

            # Replace the POS tag with the tagged one
            parts[3] = tagged_pos
            conllu_formatted.append('\t'.join(parts))
    
    return '\n'.join(conllu_formatted)


def read_original_conllu(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')

original_test_data = read_original_conllu(test_file)

with open('fi_tdt-ud-test_output.conllu', 'w', encoding='utf-8') as f:
    for tagged_sent, original_sent in zip(tagged_test_data, original_test_data):
        original_sent_lines = [line for line in original_sent.split('\n') if not line.startswith('#')]
        f.write(format_to_conllu(tagged_sent, original_sent_lines))
        f.write('\n\n')

