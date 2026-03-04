---
layout: default
title: Leveraging Label Proportion Prior for Class-Imbalanced Semi-Supervised Learning
---

# Leveraging Label Proportion Prior for Class-Imbalanced Semi-Supervised Learning
**arXiv**：[2603.02957v1](https://arxiv.org/abs/2603.02957) · [PDF](https://arxiv.org/pdf/2603.02957.pdf)  
**作者**：Kohki Akiba, Shinnosuke Matsuo, Shota Harada, Ryoma Bise  

**一句话要点**：提出比例损失正则化框架以解决类别不平衡半监督学习中的伪标签偏差问题

**关键词**：半监督学习, 类别不平衡, 比例损失, 伪标签, 正则化, 长尾分布

## 3 点简述
- 核心问题：类别不平衡导致半监督学习中伪标签放大多数类偏差，抑制少数类性能。
- 方法要点：首次将标签比例学习中的比例损失引入半监督学习作为正则项，对齐模型预测与全局类别分布。
- 实验或效果：在长尾CIFAR-10基准上，集成比例损失到FixMatch和ReMixMatch，优于基线，在稀缺标签条件下表现竞争或更优。

## 摘要（原文）

> Semi-supervised learning (SSL) often suffers under class imbalance, where pseudo-labeling amplifies majority bias and suppresses minority performance. We address this issue with a lightweight framework that, to our knowledge, is the first to introduce Proportion Loss from learning from label proportions (LLP) into SSL as a regularization term. Proportion Loss aligns model predictions with the global class distribution, mitigating bias across both majority and minority classes. To further stabilize training, we formulate a stochastic variant that accounts for fluctuations in mini-batch composition. Experiments on the Long-tailed CIFAR-10 benchmark show that integrating Proportion Loss into FixMatch and ReMixMatch consistently improves performance over the baselines across imbalance severities and label ratios, and achieves competitive or superior results compared to existing CISSL methods, particularly under scarce-label conditions.

