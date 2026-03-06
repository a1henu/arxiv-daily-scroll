---
layout: default
title: PersianPunc: A Large-Scale Dataset and BERT-Based Approach for Persian Punctuation Restoration
---

# PersianPunc: A Large-Scale Dataset and BERT-Based Approach for Persian Punctuation Restoration
**arXiv**：[2603.05314v1](https://arxiv.org/abs/2603.05314) · [PDF](https://arxiv.org/pdf/2603.05314.pdf)  
**作者**：Mohammad Javad Ranjbar Kalahroodi, Heshaam Faili, Azadeh Shakery  

**一句话要点**：提出PersianPunc数据集与BERT方法，用于波斯语标点恢复以提升ASR输出质量。

**关键词**：波斯语标点恢复, 序列标注任务, BERT微调, ASR后处理, 低资源语言处理, 公开数据集

## 3 点简述
- 波斯语标点恢复研究不足，影响ASR输出可读性与下游应用。
- 构建大规模数据集，采用序列标注任务微调ParsBERT实现高效恢复。
- BERT方法在测试集上F1达91.33%，优于大模型避免过校正与高计算成本。

## 摘要（原文）

> Punctuation restoration is essential for improving the readability and downstream utility of automatic speech recognition (ASR) outputs, yet remains underexplored for Persian despite its importance. We introduce PersianPunc, a large-scale, high-quality dataset of 17 million samples for Persian punctuation restoration, constructed through systematic aggregation and filtering of existing textual resources. We formulate punctuation restoration as a token-level sequence labeling task and fine-tune ParsBERT to achieve strong performance. Through comparative evaluation, we demonstrate that while large language models can perform punctuation restoration, they suffer from critical limitations: over-correction tendencies that introduce undesired edits beyond punctuation insertion (particularly problematic for speech-to-text pipelines) and substantially higher computational requirements. Our lightweight BERT-based approach achieves a macro-averaged F1 score of 91.33% on our test set while maintaining efficiency suitable for real-time applications. We make our dataset (https://huggingface.co/datasets/MohammadJRanjbar/persian-punctuation-restoration) and model (https://huggingface.co/MohammadJRanjbar/parsbert-persian-punctuation) publicly available to facilitate future research in Persian NLP and provide a scalable framework applicable to other morphologically rich, low-resource languages.

