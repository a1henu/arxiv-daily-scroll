---
layout: default
title: AStF: Motion Style Transfer via Adaptive Statistics Fusor
---

# AStF: Motion Style Transfer via Adaptive Statistics Fusor
**arXiv**：[2511.04192v1](https://arxiv.org/abs/2511.04192) · [PDF](https://arxiv.org/pdf/2511.04192.pdf)  
**作者**：Hanmo Chen, Chenghao Xu, Jiexi Yan, Cheng Deng  

**一句话要点**：提出自适应统计融合器以改进人体运动风格迁移

**关键词**：运动风格迁移, 自适应统计融合, 高阶统计, 风格解耦, 时空一致性, 生成对抗网络

## 3 点简述
- 传统方法依赖均值和方差，不足以捕捉运动数据的复杂动态模式。
- 引入偏度和峰度，结合风格解耦模块和高阶多统计注意力机制。
- 实验显示在运动风格迁移中优于现有方法，提供更全面的时空统计建模。

## 摘要（原文）

> Human motion style transfer allows characters to appear less rigidity and
> more realism with specific style. Traditional arbitrary image style transfer
> typically process mean and variance which is proved effective. Meanwhile,
> similar methods have been adapted for motion style transfer. However, due to
> the fundamental differences between images and motion, relying on mean and
> variance is insufficient to fully capture the complex dynamic patterns and
> spatiotemporal coherence properties of motion data. Building upon this, our key
> insight is to bring two more coefficient, skewness and kurtosis, into the
> analysis of motion style. Specifically, we propose a novel Adaptive Statistics
> Fusor (AStF) which consists of Style Disentanglement Module (SDM) and
> High-Order Multi-Statistics Attention (HOS-Attn). We trained our AStF in
> conjunction with a Motion Consistency Regularization (MCR) discriminator.
> Experimental results show that, by providing a more comprehensive model of the
> spatiotemporal statistical patterns inherent in dynamic styles, our proposed
> AStF shows proficiency superiority in motion style transfers over
> state-of-the-arts. Our code and model are available at
> https://github.com/CHMimilanlan/AStF.

