---
layout: default
title: Speech Emotion Recognition Leveraging OpenAI's Whisper Representations and Attentive Pooling Methods
---

# Speech Emotion Recognition Leveraging OpenAI's Whisper Representations and Attentive Pooling Methods
**arXiv**：[2602.06000v1](https://arxiv.org/abs/2602.06000) · [PDF](https://arxiv.org/pdf/2602.06000.pdf)  
**作者**：Ali Shendabadi, Parnia Izadirad, Mostafa Salehi, Mahmoud Bijankhan  

**一句话要点**：提出基于Whisper表示和注意力池化的语音情感识别方法，提升多语言数据集性能。

**关键词**：语音情感识别, Whisper表示, 注意力池化, 多语言数据集, 轻量模型

## 3 点简述
- 语音情感识别因缺乏标准大数据集而受限，研究利用预训练模型提取特征。
- 提出多头注意力平均池化和QKV池化方法，高效降维并保留情感特征。
- 在英语和波斯语数据集上实验，QKV架构在ShEMO上取得最优结果，提升准确率2.47%。

## 摘要（原文）

> Speech Emotion Recognition (SER) research has faced limitations due to the lack of standard and sufficiently large datasets. Recent studies have leveraged pre-trained models to extract features for downstream tasks such as SER. This work explores the capabilities of Whisper, a pre-trained ASR system, in speech emotion recognition by proposing two attention-based pooling methods, Multi-head Attentive Average Pooling and QKV Pooling, designed to efficiently reduce the dimensionality of Whisper representations while preserving emotional features. We experiment on English and Persian, using the IEMOCAP and ShEMO datasets respectively, with Whisper Tiny and Small. Our multi-head QKV architecture achieves state-of-the-art results on the ShEMO dataset, with a 2.47% improvement in unweighted accuracy. We further compare the performance of different Whisper encoder layers and find that intermediate layers often perform better for SER on the Persian dataset, providing a lightweight and efficient alternative to much larger models such as HuBERT X-Large. Our findings highlight the potential of Whisper as a representation extractor for SER and demonstrate the effectiveness of attention-based pooling for dimension reduction.

