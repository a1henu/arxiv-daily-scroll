---
layout: default
title: Benchmarking BERT-based Models for Sentence-level Topic Classification in Nepali Language
---

# Benchmarking BERT-based Models for Sentence-level Topic Classification in Nepali Language
**arXiv**：[2602.23940v1](https://arxiv.org/abs/2602.23940) · [PDF](https://arxiv.org/pdf/2602.23940.pdf)  
**作者**：Nischal Karki, Bipesh Subedi, Prakash Poudyal, Rupak Raj Ghimire, Bal Krishna Bal  

**一句话要点**：基准测试BERT模型在尼泊尔语句级主题分类中的性能，确立Indic模型为最优基线。

**关键词**：尼泊尔语处理, 主题分类, BERT基准测试, 低资源语言, Indic模型, 句子级分类

## 3 点简述
- 研究针对尼泊尔语这一低资源语言，评估多种BERT变体在主题分类任务中的有效性。
- 方法包括微调10个预训练模型，如mBERT、XLM-R、MuRIL等，使用平衡数据集进行测试。
- 实验结果显示Indic模型（如MuRIL-large）表现最佳，F1分数达90.60%，为未来应用提供基准。

## 摘要（原文）

> Transformer-based models such as BERT have significantly advanced Natural Language Processing (NLP) across many languages. However, Nepali, a low-resource language written in Devanagari script, remains relatively underexplored. This study benchmarks multilingual, Indic, Hindi, and Nepali BERT variants to evaluate their effectiveness in Nepali topic classification. Ten pre-trained models, including mBERT, XLM-R, MuRIL, DevBERT, HindiBERT, IndicBERT, and NepBERTa, were fine-tuned and tested on the balanced Nepali dataset containing 25,006 sentences across five conceptual domains and the performance was evaluated using accuracy, weighted precision, recall, F1-score, and AUROC metrics. The results reveal that Indic models, particularly MuRIL-large, achieved the highest F1-score of 90.60%, outperforming multilingual and monolingual models. NepBERTa also performed competitively with an F1-score of 88.26%. Overall, these findings establish a robust baseline for future document-level classification and broader Nepali NLP applications.

