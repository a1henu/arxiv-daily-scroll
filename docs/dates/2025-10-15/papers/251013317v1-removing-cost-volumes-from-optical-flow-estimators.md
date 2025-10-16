---
layout: default
title: Removing Cost Volumes from Optical Flow Estimators
---

# Removing Cost Volumes from Optical Flow Estimators
**arXiv**：[2510.13317v1](https://arxiv.org/abs/2510.13317) · [PDF](https://arxiv.org/pdf/2510.13317.pdf)  
**作者**：Simon Kiefhaber, Stefan Roth, Simone Schaub-Meyer  

**一句话要点**：提出训练策略以移除光流估计器中的代价体积，提升推理速度与内存效率。

**关键词**：光流估计, 代价体积移除, 训练策略, 推理加速, 内存优化

## 3 点简述
- 核心问题：代价体积在光流估计中计算和空间复杂度高，限制处理速度和输入分辨率。
- 方法要点：基于训练后代价体积重要性降低的观察，设计策略在训练中移除代价体积。
- 实验或效果：模型在保持高精度下，推理速度提升1.2倍，内存占用降低6倍。

## 摘要（原文）

> Cost volumes are used in every modern optical flow estimator, but due to
> their computational and space complexity, they are often a limiting factor
> regarding both processing speed and the resolution of input frames. Motivated
> by our empirical observation that cost volumes lose their importance once all
> other network parts of, e.g., a RAFT-based pipeline have been sufficiently
> trained, we introduce a training strategy that allows removing the cost volume
> from optical flow estimators throughout training. This leads to significantly
> improved inference speed and reduced memory requirements. Using our training
> strategy, we create three different models covering different compute budgets.
> Our most accurate model reaches state-of-the-art accuracy while being
> $1.2\times$ faster and having a $6\times$ lower memory footprint than
> comparable models; our fastest model is capable of processing Full HD frames at
> $20\,\mathrm{FPS}$ using only $500\,\mathrm{MB}$ of GPU memory.

