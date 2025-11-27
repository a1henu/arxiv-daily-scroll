---
layout: default
title: BanglaASTE: A Novel Framework for Aspect-Sentiment-Opinion Extraction in Bangla E-commerce Reviews Using Ensemble Deep Learning
---

# BanglaASTE: A Novel Framework for Aspect-Sentiment-Opinion Extraction in Bangla E-commerce Reviews Using Ensemble Deep Learning
**arXiv**：[2511.21381v1](https://arxiv.org/abs/2511.21381) · [PDF](https://arxiv.org/pdf/2511.21381.pdf)  
**作者**：Ariful Islam, Md Rifat Hossen, Abir Ahmed, B M Taslimul Haque  

**一句话要点**：提出BanglaASTE框架以解决孟加拉语电商评论中方面-情感-观点三元组提取问题

**关键词**：方面情感三元组提取, 孟加拉语情感分析, 集成深度学习, 电商评论分析, 低资源语言处理

## 3 点简述
- 核心问题：孟加拉语方面情感分析缺乏数据集和框架，难以提取三元组。
- 方法要点：结合图匹配与语义相似度，集成BanglaBERT和XGBoost模型。
- 实验或效果：准确率达89.9%，F1分数89.1%，优于基线模型。

## 摘要（原文）

> Aspect-Based Sentiment Analysis (ABSA) has emerged as a critical tool for extracting fine-grained sentiment insights from user-generated content, particularly in e-commerce and social media domains. However, research on Bangla ABSA remains significantly underexplored due to the absence of comprehensive datasets and specialized frameworks for triplet extraction in this language. This paper introduces BanglaASTE, a novel framework for Aspect Sentiment Triplet Extraction (ASTE) that simultaneously identifies aspect terms, opinion expressions, and sentiment polarities from Bangla product reviews. Our contributions include: (1) creation of the first annotated Bangla ASTE dataset containing 3,345 product reviews collected from major e-commerce platforms including Daraz, Facebook, and Rokomari; (2) development of a hybrid classification framework that employs graph-based aspect-opinion matching with semantic similarity techniques; and (3) implementation of an ensemble model combining BanglaBERT contextual embeddings with XGBoost boosting algorithms for enhanced triplet extraction performance. Experimental results demonstrate that our ensemble approach achieves superior performance with 89.9% accuracy and 89.1% F1-score, significantly outperforming baseline models across all evaluation metrics. The framework effectively addresses key challenges in Bangla text processing including informal expressions, spelling variations, and data sparsity. This research advances the state-of-the-art in low-resource language sentiment analysis and provides a scalable solution for Bangla e-commerce analytics applications.

