---
layout: default
title: Equalized Generative Treatment: Matching f-divergences for Fairness in Generative Models
---

# Equalized Generative Treatment: Matching f-divergences for Fairness in Generative Models
**arXiv**：[2602.08660v1](https://arxiv.org/abs/2602.08660) · [PDF](https://arxiv.org/pdf/2602.08660.pdf)  
**作者**：Alexandre Verine, Rafael Pinot, Florian Le Bronnec  

**一句话要点**：提出平等化生成处理以解决生成模型中敏感群体生成质量差异的公平性问题

**关键词**：生成模型公平性, f-散度匹配, 最小-最大优化, 敏感群体平衡, 图像生成, 文本生成

## 3 点简述
- 现有公平性标准脆弱，可能掩盖不同敏感群体生成质量差异
- 引入平等化生成处理，要求所有敏感群体生成质量可比，以f-散度衡量
- 实验验证最小-最大微调方法在图像和文本生成任务中实现更公平结果

## 摘要（原文）

> Fairness is a crucial concern for generative models, which not only reflect but can also amplify societal and cultural biases. Existing fairness notions for generative models are largely adapted from classification and focus on balancing the probability of generating samples from each sensitive group. We show that such criteria are brittle, as they can be met even when different sensitive groups are modeled with widely varying quality. To address this limitation, we introduce a new fairness definition for generative models, termed as equalized generative treatment (EGT), which requires comparable generation quality across all sensitive groups, with quality measured via a reference f-divergence. We further analyze the trade-offs induced by EGT, demonstrating that enforcing fairness constraints necessarily couples the overall model quality to that of the most challenging group to approximate. This indicates that a simple yet efficient min-max fine-tuning method should be able to balance f-divergences across sensitive groups to satisfy EGT. We validate this theoretical insight through a set of experiments on both image and text generation tasks. We demonstrate that min-max methods consistently achieve fairer outcomes compared to other approaches from the literature, while maintaining competitive overall performance for both tasks.

