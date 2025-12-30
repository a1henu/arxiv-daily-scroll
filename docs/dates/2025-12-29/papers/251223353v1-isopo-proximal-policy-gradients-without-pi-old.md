---
layout: default
title: ISOPO: Proximal policy gradients without pi-old
---

# ISOPO: Proximal policy gradients without pi-old
**arXiv**：[2512.23353v1](https://arxiv.org/abs/2512.23353) · [PDF](https://arxiv.org/pdf/2512.23353.pdf)  
**作者**：Nilin Abrahamsen  

**一句话要点**：提出ISOPO方法，通过单步梯度近似自然策略梯度，避免旧策略依赖。

**关键词**：策略优化, 自然梯度, 强化学习, 计算效率, 单步梯度

## 3 点简述
- 核心问题：现有近端策略方法需多步梯度与重要性采样，计算效率低。
- 方法要点：ISOPO在Fisher度量下归一化对数概率梯度，或基于神经正切核变换优势。
- 实验或效果：单次反向传播实现，计算开销可忽略，相比REINFORCE更高效。

## 摘要（原文）

> This note introduces Isometric Policy Optimization (ISOPO), an efficient method to approximate the natural policy gradient in a single gradient step. In comparison, existing proximal policy methods such as GRPO or CISPO use multiple gradient steps with variants of importance ratio clipping to approximate a natural gradient step relative to a reference policy. In its simplest form, ISOPO normalizes the log-probability gradient of each sequence in the Fisher metric before contracting with the advantages. Another variant of ISOPO transforms the microbatch advantages based on the neural tangent kernel in each layer. ISOPO applies this transformation layer-wise in a single backward pass and can be implemented with negligible computational overhead compared to vanilla REINFORCE.

