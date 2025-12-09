---
layout: default
title: MIDG: Mixture of Invariant Experts with knowledge injection for Domain Generalization in Multimodal Sentiment Analysis
---

# MIDG: Mixture of Invariant Experts with knowledge injection for Domain Generalization in Multimodal Sentiment Analysis
**arXiv**：[2512.07430v1](https://arxiv.org/abs/2512.07430) · [PDF](https://arxiv.org/pdf/2512.07430.pdf)  
**作者**：Yangle Li, Danli Luo, Haifeng Hu  

**一句话要点**：提出MIDG框架，通过混合不变专家和跨模态适配器解决多模态情感分析中的领域泛化问题。

**关键词**：多模态情感分析, 领域泛化, 不变特征提取, 跨模态知识注入, 混合专家模型

## 3 点简述
- 现有方法在提取不变特征时忽视模态间协同，导致语义信息捕获不准确。
- MIDG结合混合不变专家模型提取领域不变特征，增强模态间协同学习能力。
- 在三个数据集上的实验显示，MIDG在领域泛化任务中表现优异。

## 摘要（原文）

> Existing methods in domain generalization for Multimodal Sentiment Analysis (MSA) often overlook inter-modal synergies during invariant features extraction, which prevents the accurate capture of the rich semantic information within multimodal data. Additionally, while knowledge injection techniques have been explored in MSA, they often suffer from fragmented cross-modal knowledge, overlooking specific representations that exist beyond the confines of unimodal. To address these limitations, we propose a novel MSA framework designed for domain generalization. Firstly, the framework incorporates a Mixture of Invariant Experts model to extract domain-invariant features, thereby enhancing the model's capacity to learn synergistic relationships between modalities. Secondly, we design a Cross-Modal Adapter to augment the semantic richness of multimodal representations through cross-modal knowledge injection. Extensive domain experiments conducted on three datasets demonstrate that the proposed MIDG achieves superior performance.

