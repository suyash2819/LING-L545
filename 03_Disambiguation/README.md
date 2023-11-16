The three taggers used are udpipe, perceptron tagger and nltk tagger for which the code is in the file named nltk_tagger.py
The output file names of all the three taggers are:

fi_tdt-ud-test_output.conllu - nltk tagger
fi_tdt-ud-test_output_perceptron.conllu - perceptron tagger
fi_tdt-ud-test_udpipe_output.conllu - udpipe tagger

Below are the screenshots of the evaluation from the evaluation script:

nltk tagger:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/271cfef5-1793-4e51-b6ba-8ffac6d740a2)

Perceptron tagger:

![perceptron_based_performance](https://github.com/suyash2819/LING-L545/assets/28905722/b66eb758-775c-42c7-8715-494481061d3b)

Udpipe:

![udpipe_performance](https://github.com/suyash2819/LING-L545/assets/28905722/606db43d-13cd-4336-b989-3bb10cfa4e49)

since we are majorly looking at the UPOs (universal part of speech) the comparison looks like:
According to the above evaluation, it seems nltk_tagger was most effective in tagging correctly with UPOS accuracy of 100%, this result indicates perfect performance in POS tagging, with every tag matching the gold standard.

The Perceptron Tagger shows high accuracy but not perfect with accuracy of 90.36%

UDPipe shows a strong performance, with a high accuracy with 94.69% accuracy.

 UDPipe, likely benefiting from more sophisticated algorithms and perhaps more comprehensive training data, outperforms the Perceptron Tagger by a small margin.
