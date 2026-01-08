---
layout: default
title: AI Generated Text Detection
---

# AI Generated Text Detection
**arXiv**：[2601.03812v1](https://arxiv.org/abs/2601.03812) · [PDF](https://arxiv.org/pdf/2601.03812.pdf)  
**作者**：Adilkhan Alikhanov, Aidar Amangeldi, Diar Demeubay, Dilnaz Akhmetzhan, Nurbek Moldakhmetov, Omar Polat, Galymzhan Zharas  

**一句话要点**：评估AI生成文本检测方法，基于主题分割数据集提升泛化能力。

**关键词**：AI生成文本检测, Transformer模型, 主题分割, 学术诚信, 基准评估

## 3 点简述
- 核心问题：大语言模型生成文本增多，学生滥用破坏学术诚信。
- 方法要点：结合传统机器学习与Transformer模型，采用主题分割防止信息泄露。
- 实验或效果：DistilBERT表现最佳，准确率88.11%，ROC-AUC达0.96。

## 摘要（原文）

> The rapid development of large language models has led to an increase in AI-generated text, with students increasingly using LLM-generated content as their own work, which violates academic integrity. This paper presents an evaluation of AI text detection methods, including both traditional machine learning models and transformer-based architectures. We utilize two datasets, HC3 and DAIGT v2, to build a unified benchmark and apply a topic-based data split to prevent information leakage. This approach ensures robust generalization across unseen domains. Our experiments show that TF-IDF logistic regression achieves a reasonable baseline accuracy of 82.87%. However, deep learning models outperform it. The BiLSTM classifier achieves an accuracy of 88.86%, while DistilBERT achieves a similar accuracy of 88.11% with the highest ROC-AUC score of 0.96, demonstrating the strongest overall performance. The results indicate that contextual semantic modeling is significantly superior to lexical features and highlight the importance of mitigating topic memorization through appropriate evaluation protocols. The limitations of this work are primarily related to dataset diversity and computational constraints. In future work, we plan to expand dataset diversity and utilize parameter-efficient fine-tuning methods such as LoRA. We also plan to explore smaller or distilled models and employ more efficient batching strategies and hardware-aware optimization.

