
Exercises with sed:
  ```
  1. sed 's/[^a-zA-Z]\+/\n/g' wiki.txt | sed 's/[aeiouAEIOU].*//g' | sort | uniq -c | sort -nr > initial-consonants.hist
  
  2. sed 's/[^a-zA-Z]\+/\n/g' wiki.txt| sed 's/.*[aeiouAEIOU]//g' | sort  | uniq -c | sort -nr > final-consonants.hist
  ```

