---
title: '15 Datasets for Word Segmentation on the Hugging Face Hub'
date: 2022-09-03
permalink: /posts/2022/09/word-segmentation-datasets/
tags:
  - cool posts
  - category1
  - category2
---

# 15 Datasets for Word Segmentation on the Hugging Face Hub

Word segmentation is the task of adding spaces between words. It can be an important preprocessing step in Natural Language Processing pipelines for tasks such as sentiment analysis and hate speech detection on social media.

**Hashtags** are very common on social media platforms such as Twitter and Instagram. These tags appear usually at the end of a post and start with the # symbol.

**Identifiers** are simply names of entities in source code. Variable names, class names and function names are examples of identifiers.

A few examples of word segmentation for hashtags and identifiers:

Hashtags: the Instagram hashtag #photooftheday is segmented as # photo of the day.

Identifiers: the variable name abspath is segmented as abs path .

Word segmentation of hashtags is called hashtag segmentation, and word segmentation of identifiers is called identifier splitting.

The Hugging Face Hub is a great place to share datasets, so I uploaded 15 word segmentation datasets to 
the Hub. I have also written readers for all datasets, so they follow the same standard data format.

You can read more about how to use the Hub on the datasets library documentation.

Hashtag Segmentation

Here we have hashtag segmentation datasets for English, Hindi and Russian hashtags.
SNAP, HashSet Distant and HashSet Distant Sampled have been automatically generated. All other datasets have been segmented by hand.
HashSet Manual is also annotated for a named entity detection task. STAN Small and STAN Large also give alternative segmentations with characters corrected to uppercase.
English:
BOUN
STAN Small
STAN Large
Dev-Stanford
Test-Stanford
SNAP

Hindi and English (code-mixed):
HashSet Distant
HashSet Manual
HashSet Distant Sampled

Russian:
NRU-HSE

The hashformers library has a tutorial that shows the evaluation of a distilgpt2 model on the first 100 hashtags of each dataset.
I was quite surprised to see such high scores for NRU-HSE, a Russian dataset, even though DistilGPT2 is an English language model. HashSet Manual is the hardest one, as its authors deliberately did not include easy to segment hashtags on the dataset.
Identifier Splitting
Our identifier splitting datasets cover programming languages such as C, C++ and Java.
Lynx also includes an abbreviation expansion task.
Loyola
Lynx
Jhotdraw
Binkley
BT11

More
Please let me know in the comments if you are aware of any other public word segmentation datasets.
Besides hashtags and identifiers, URLs deserve an honorary mention, as word segmentation of URLs is relevant to malicious domain detection. You can read more about it on the Breaking Bad paper and more recent papers that cite it.