Le projet Word Count est une application Hadoop MapReduce de base utilisée pour compter la fréquence des mots dans un grand fichier texte. Les données d’entrée sont divisées et traitées par le Mapper, qui émet chaque mot avec la valeur 1. Ensuite, Hadoop regroupe les mots identiques pendant la phase de shuffle and sort. Enfin, le Reducer calcule le nombre total d’occurrences de chaque mot. Ce projet démontre le principe de base du traitement distribué avec Hadoop.

## 2. Hiérarchie du projet

hadoop-wordcount-project/
│
├── src/
│   └── WordCount.java
│
├── input/
│   └── words.txt
│
├── output_sample/
│   └── part-r-00000
│
├── screenshots/
│   ├── hdfs-input.png
│   ├── job-running.png
│   └── output-result.png
│
├── README.md
└── .gitignore