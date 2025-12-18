---
layout: default
title: SeBERTis: A Framework for Producing Classifiers of Security-Related Issue Reports
---

# SeBERTis: A Framework for Producing Classifiers of Security-Related Issue Reports
**arXiv**：[2512.15003v1](https://arxiv.org/abs/2512.15003) · [PDF](https://arxiv.org/pdf/2512.15003.pdf)  
**作者**：Sogol Masoumzadeh, Yufei Li, Shane McIntosh, Dániel Varró, Lili Wei  

**一句话要点**：提出SEBERTIS框架以训练独立于词汇线索的深度神经网络，用于实时检测安全相关软件问题报告。

**关键词**：安全相关问题检测, 深度神经网络分类器, 掩码语言模型, 语义替代词, 软件维护自动化

## 3 点简述
- 核心问题：现有自动检测技术依赖词汇线索，对复杂问题报告检测率低，难以满足实时安全检测需求。
- 方法要点：基于双向Transformer架构，通过掩码语言模型在语义替代词上微调，使分类器独立于词汇线索。
- 实验或效果：在10,000个GitHub问题报告数据集上，F1分数达0.9880，显著优于机器学习和大型语言模型基线。

## 摘要（原文）

> Monitoring issue tracker submissions is a crucial software maintenance activity. A key goal is the prioritization of high risk, security-related bugs. If such bugs can be recognized early, the risk of propagation to dependent products and endangerment of stakeholder benefits can be mitigated. To assist triage engineers with this task, several automatic detection techniques, from Machine Learning (ML) models to prompting Large Language Models (LLMs), have been proposed. Although promising to some extent, prior techniques often memorize lexical cues as decision shortcuts, yielding low detection rate specifically for more complex submissions. As such, these classifiers do not yet reach the practical expectations of a real-time detector of security-related issues. To address these limitations, we propose SEBERTIS, a framework to train Deep Neural Networks (DNNs) as classifiers independent of lexical cues, so that they can confidently detect fully unseen security-related issues. SEBERTIS capitalizes on fine-tuning bidirectional transformer architectures as Masked Language Models (MLMs) on a series of semantically equivalent vocabulary to prediction labels (which we call Semantic Surrogates) when they have been replaced with a mask. Our SEBERTIS-trained classifier achieves a 0.9880 F1-score in detecting security-related issues of a curated corpus of 10,000 GitHub issue reports, substantially outperforming state-of-the-art issue classifiers, with 14.44%-96.98%, 15.40%-93.07%, and 14.90%-94.72% higher detection precision, recall, and F1-score over ML-based baselines. Our classifier also substantially surpasses LLM baselines, with an improvement of 23.20%-63.71%, 36.68%-85.63%, and 39.49%-74.53% for precision, recall, and F1-score.

