---
layout: default
title: Determinants of Training Corpus Size for Clinical Text Classification
---

# Determinants of Training Corpus Size for Clinical Text Classification
**arXiv**：[2601.15846v1](https://arxiv.org/abs/2601.15846) · [PDF](https://arxiv.org/pdf/2601.15846.pdf)  
**作者**：Jaya Chaturvedi, Saniya Deshpande, Chenkai Ma, Robert Cobb, Angus Roberts, Robert Stewart, Daniel Stahl, Diana Shamsutdinova  

**一句话要点**：确定临床文本分类训练语料库规模的影响因素，基于词汇属性分析优化数据需求

**关键词**：临床文本分类, 训练数据规模, 词汇属性分析, BERT嵌入, 随机森林, MIMIC-III数据集

## 3 点简述
- 核心问题：临床文本分类中训练数据规模缺乏理论依据，受限于标注成本与时间。
- 方法要点：使用MIMIC-III数据集，结合BERT嵌入和随机森林，分析不同训练规模下的性能与词汇预测力。
- 实验或效果：600文档可达到10,000文档95%性能，词汇中强预测词提升准确率，噪声词降低准确率。

## 摘要（原文）

> Introduction: Clinical text classification using natural language processing (NLP) models requires adequate training data to achieve optimal performance. For that, 200-500 documents are typically annotated. The number is constrained by time and costs and lacks justification of the sample size requirements and their relationship to text vocabulary properties.
>   Methods: Using the publicly available MIMIC-III dataset containing hospital discharge notes with ICD-9 diagnoses as labels, we employed pre-trained BERT embeddings followed by Random Forest classifiers to identify 10 randomly selected diagnoses, varying training corpus sizes from 100 to 10,000 documents, and analyzed vocabulary properties by identifying strong and noisy predictive words through Lasso logistic regression on bag-of-words embeddings.
>   Results: Learning curves varied significantly across the 10 classification tasks despite identical preprocessing and algorithms, with 600 documents sufficient to achieve 95% of the performance attainable with 10,000 documents for all tasks. Vocabulary analysis revealed that more strong predictors and fewer noisy predictors were associated with steeper learning curves, where every 100 additional noisy words decreased accuracy by approximately 0.02 while 100 additional strong predictors increased maximum accuracy by approximately 0.04.

