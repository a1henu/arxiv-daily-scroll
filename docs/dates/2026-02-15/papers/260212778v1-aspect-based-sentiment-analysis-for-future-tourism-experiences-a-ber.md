---
layout: default
title: Aspect-Based Sentiment Analysis for Future Tourism Experiences: A BERT-MoE Framework for Persian User Reviews
---

# Aspect-Based Sentiment Analysis for Future Tourism Experiences: A BERT-MoE Framework for Persian User Reviews
**arXiv**：[2602.12778v1](https://arxiv.org/abs/2602.12778) · [PDF](https://arxiv.org/pdf/2602.12778.pdf)  
**作者**：Hamidreza Kazemi Taskooh, Taha Zare Harofte  

**一句话要点**：提出基于BERT-MoE的混合模型，用于波斯语旅游评论的方面级情感分析，以解决低资源语言挑战。

**关键词**：方面级情感分析, 波斯语处理, BERT-MoE模型, 旅游评论分析, 低资源语言NLP

## 3 点简述
- 针对波斯语旅游评论的低资源语言问题，进行方面级情感分析研究。
- 采用BERT结合Top-K路由和辅助损失的混合模型，提升效率并防止路由崩溃。
- 在Jabama数据集上实现90.6%的加权F1分数，比基线模型更优，且GPU功耗降低39%。

## 摘要（原文）

> This study advances aspect-based sentiment analysis (ABSA) for Persian-language user reviews in the tourism domain, addressing challenges of low-resource languages. We propose a hybrid BERT-based model with Top-K routing and auxiliary losses to mitigate routing collapse and improve efficiency. The pipeline includes: (1) overall sentiment classification using BERT on 9,558 labeled reviews, (2) multi-label aspect extraction for six tourism-related aspects (host, price, location, amenities, cleanliness, connectivity), and (3) integrated ABSA with dynamic routing. The dataset consists of 58,473 preprocessed reviews from the Iranian accommodation platform Jabama, manually annotated for aspects and sentiments. The proposed model achieves a weighted F1-score of 90.6% for ABSA, outperforming baseline BERT (89.25%) and a standard hybrid approach (85.7%). Key efficiency gains include a 39% reduction in GPU power consumption compared to dense BERT, supporting sustainable AI deployment in alignment with UN SDGs 9 and 12. Analysis reveals high mention rates for cleanliness and amenities as critical aspects. This is the first ABSA study focused on Persian tourism reviews, and we release the annotated dataset to facilitate future multilingual NLP research in tourism.

