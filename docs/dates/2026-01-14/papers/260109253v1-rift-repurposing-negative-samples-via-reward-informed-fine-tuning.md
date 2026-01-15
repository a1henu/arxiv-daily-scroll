---
layout: default
title: RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
---

# RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
**arXiv**：[2601.09253v1](https://arxiv.org/abs/2601.09253) · [PDF](https://arxiv.org/pdf/2601.09253.pdf)  
**作者**：Zehua Liu, Shuqi Liu, Tao Zhong, Mingxuan Yuan  

**一句话要点**：提出RIFT框架，通过奖励加权损失利用自生成负样本，提升大语言模型对齐的数据效率。

**关键词**：大语言模型对齐, 奖励加权训练, 自生成数据利用, 负样本重利用, 稳定损失设计, 数据效率优化

## 3 点简述
- 核心问题：SFT依赖专家数据成本高，RFT丢弃负样本导致数据效率低。
- 方法要点：RIFT利用所有自生成样本，通过奖励加权损失学习正负轨迹，引入稳定损失避免训练崩溃。
- 实验或效果：在数学基准测试中，RIFT一致优于RFT，证明其作为数据高效对齐方法的鲁棒性。

## 摘要（原文）

> While Supervised Fine-Tuning (SFT) and Rejection Sampling Fine-Tuning (RFT) are standard for LLM alignment, they either rely on costly expert data or discard valuable negative samples, leading to data inefficiency. To address this, we propose Reward Informed Fine-Tuning (RIFT), a simple yet effective framework that utilizes all self-generated samples. Unlike the hard thresholding of RFT, RIFT repurposes negative trajectories, reweighting the loss with scalar rewards to learn from both the positive and negative trajectories from the model outputs. To overcome the training collapse caused by naive reward integration, where direct multiplication yields an unbounded loss, we introduce a stabilized loss formulation that ensures numerical robustness and optimization efficiency. Extensive experiments on mathematical benchmarks across various base models show that RIFT consistently outperforms RFT. Our results demonstrate that RIFT is a robust and data-efficient alternative for alignment using mixed-quality, self-generated data.

