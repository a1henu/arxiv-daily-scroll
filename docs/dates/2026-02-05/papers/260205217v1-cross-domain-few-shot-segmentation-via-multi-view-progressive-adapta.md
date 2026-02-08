---
layout: default
title: Cross-Domain Few-Shot Segmentation via Multi-view Progressive Adaptation
---

# Cross-Domain Few-Shot Segmentation via Multi-view Progressive Adaptation
**arXiv**：[2602.05217v1](https://arxiv.org/abs/2602.05217) · [PDF](https://arxiv.org/pdf/2602.05217.pdf)  
**作者**：Jiahao Nie, Guanqiao Fu, Wenbin An, Yap-Peng Tan, Alex C. Kot, Shijian Lu  

**一句话要点**：提出多视图渐进适应方法以解决跨域少样本分割中目标域性能受限问题

**关键词**：跨域少样本分割, 渐进适应, 多视图学习, 数据增强, 监督学习, 图像分割

## 3 点简述
- 核心问题：跨域少样本分割中目标域样本少且多样性不足，源域模型在目标域初始能力弱，导致适应困难。
- 方法要点：从数据和策略角度渐进适应，包括混合渐进增强生成复杂视图，以及双链多视图预测利用监督学习路径。
- 实验或效果：在实验中显著超越现有方法，性能提升7.0%，证明能有效适应目标域。

## 摘要（原文）

> Cross-Domain Few-Shot Segmentation aims to segment categories in data-scarce domains conditioned on a few exemplars. Typical methods first establish few-shot capability in a large-scale source domain and then adapt it to target domains. However, due to the limited quantity and diversity of target samples, existing methods still exhibit constrained performance. Moreover, the source-trained model's initially weak few-shot capability in target domains, coupled with substantial domain gaps, severely hinders the effective utilization of target samples and further impedes adaptation. To this end, we propose Multi-view Progressive Adaptation, which progressively adapts few-shot capability to target domains from both data and strategy perspectives. (i) From the data perspective, we introduce Hybrid Progressive Augmentation, which progressively generates more diverse and complex views through cumulative strong augmentations, thereby creating increasingly challenging learning scenarios. (ii) From the strategy perspective, we design Dual-chain Multi-view Prediction, which fully leverages these progressively complex views through sequential and parallel learning paths under extensive supervision. By jointly enforcing prediction consistency across diverse and complex views, MPA achieves both robust and accurate adaptation to target domains. Extensive experiments demonstrate that MPA effectively adapts few-shot capability to target domains, outperforming state-of-the-art methods by a large margin (+7.0%).

