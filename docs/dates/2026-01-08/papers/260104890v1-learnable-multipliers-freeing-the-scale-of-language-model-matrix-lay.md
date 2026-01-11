---
layout: default
title: Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers
---

# Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers
**arXiv**：[2601.04890v1](https://arxiv.org/abs/2601.04890) · [PDF](https://arxiv.org/pdf/2601.04890.pdf)  
**作者**：Maksim Velikanov, Ilyas Chahed, Jingwei Zuo, Dhia Eddine Rhaiem, Younes Belkada, Hakim Hacid  

**一句话要点**：提出可学习乘子以优化语言模型矩阵层尺度，提升性能并减少调参开销。

**关键词**：语言模型训练, 权重衰减, 可学习乘子, 矩阵层优化, 性能提升, 调参简化

## 3 点简述
- 核心问题：权重衰减与噪声平衡导致矩阵层尺度次优，影响模型性能。
- 方法要点：引入可学习的标量、行和列乘子，自适应数据调整矩阵尺度。
- 实验或效果：在Adam和Muon优化器上验证，下游评估性能提升，优于muP基线。

## 摘要（原文）

> Applying weight decay (WD) to matrix layers is standard practice in large-language-model pretraining. Prior work suggests that stochastic gradient noise induces a Brownian-like expansion of the weight matrices W, whose growth is counteracted by WD, leading to a WD-noise equilibrium with a certain weight norm \|\|W\|\|. In this work, we view the equilibrium norm as a harmful artifact of the training procedure, and address it by introducing learnable multipliers to learn the optimal scale. First, we attach a learnable scalar multiplier to W and confirm that the WD-noise equilibrium norm is suboptimal: the learned scale adapts to data and improves performance. We then argue that individual row and column norms are similarly constrained, and free their scale by introducing learnable per-row and per-column multipliers. Our method can be viewed as a learnable, more expressive generalization of muP multipliers. It outperforms a well-tuned muP baseline, reduces the computational overhead of multiplier tuning, and surfaces practical questions such as forward-pass symmetries and the width-scaling of the learned multipliers. Finally, we validate learnable multipliers with both Adam and Muon optimizers, where it shows improvement in downstream evaluations matching the improvement of the switching from Adam to Muon.

