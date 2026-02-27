---
layout: default
title: A Proper Scoring Rule for Virtual Staining
---

# A Proper Scoring Rule for Virtual Staining
**arXiv**：[2602.23305v1](https://arxiv.org/abs/2602.23305) · [PDF](https://arxiv.org/pdf/2602.23305.pdf)  
**作者**：Samuel Tonks, Steve Hood, Ryan Musso, Ceridwen Hopely, Steve Titus, Minh Doan, Iain Styles, Alexander Krull  

**一句话要点**：提出信息增益作为细胞级评估框架，以解决虚拟染色模型后验分布评估问题。

**关键词**：虚拟染色, 后验分布评估, 信息增益, 高通量筛选, 生成模型, 评分规则

## 3 点简述
- 现有评估协议仅检查数据集边际分布准确性，无法直接评估预测后验分布。
- 引入信息增益作为严格适当评分规则，提供理论动机，支持跨模型和特征比较。
- 在广泛高通量筛选数据集上评估扩散和GAN模型，显示信息增益能揭示其他指标无法检测的性能差异。

## 摘要（原文）

> Generative virtual staining (VS) models for high-throughput screening (HTS) can provide an estimated posterior distribution of possible biological feature values for each input and cell. However, when evaluating a VS model, the true posterior is unavailable. Existing evaluation protocols only check the accuracy of the marginal distribution over the dataset rather than the predicted posteriors. We introduce information gain (IG) as a cell-wise evaluation framework that enables direct assessment of predicted posteriors. IG is a strictly proper scoring rule and comes with a sound theoretical motivation allowing for interpretability, and for comparing results across models and features. We evaluate diffusion- and GAN-based models on an extensive HTS dataset using IG and other metrics and show that IG can reveal substantial performance differences other metrics cannot.

