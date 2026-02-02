---
layout: default
title: Stabilizing Consistency Training: A Flow Map Analysis and Self-Distillation
---

# Stabilizing Consistency Training: A Flow Map Analysis and Self-Distillation
**arXiv**：[2601.22679v1](https://arxiv.org/abs/2601.22679) · [PDF](https://arxiv.org/pdf/2601.22679.pdf)  
**作者**：Youngjoong Kim, Duhoe Kim, Woosung Kim, Jaesik Park  

**一句话要点**：提出基于流图分析的稳定性理论与自蒸馏方法，以解决一致性模型训练不稳定问题

**关键词**：一致性模型, 流图分析, 自蒸馏, 训练稳定性, 生成建模, 扩散模型

## 3 点简述
- 核心问题：一致性模型训练不稳定，理论关系不清晰，导致退化解
- 方法要点：从流图视角分析训练稳定性，重新设计自蒸馏以避免梯度爆炸
- 实验或效果：应用于图像生成和扩散策略学习，无需预训练模型初始化

## 摘要（原文）

> Consistency models have been proposed for fast generative modeling, achieving results competitive with diffusion and flow models. However, these methods exhibit inherent instability and limited reproducibility when training from scratch, motivating subsequent work to explain and stabilize these issues. While these efforts have provided valuable insights, the explanations remain fragmented, and the theoretical relationships remain unclear. In this work, we provide a theoretical examination of consistency models by analyzing them from a flow map-based perspective. This joint analysis clarifies how training stability and convergence behavior can give rise to degenerate solutions. Building on these insights, we revisit self-distillation as a practical remedy for certain forms of suboptimal convergence and reformulate it to avoid excessive gradient norms for stable optimization. We further demonstrate that our strategy extends beyond image generation to diffusion-based policy learning, without reliance on a pretrained diffusion model for initialization, thereby illustrating its broader applicability.

