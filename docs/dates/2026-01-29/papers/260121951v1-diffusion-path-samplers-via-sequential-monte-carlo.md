---
layout: default
title: Diffusion Path Samplers via Sequential Monte Carlo
---

# Diffusion Path Samplers via Sequential Monte Carlo
**arXiv**：[2601.21951v1](https://arxiv.org/abs/2601.21951) · [PDF](https://arxiv.org/pdf/2601.21951.pdf)  
**作者**：James Matthew Young, Paula Cordero-Encinar, Sebastian Reich, Andrew Duncan, O. Deniz Akyildiz  

**一句话要点**：提出基于扩散路径的序贯蒙特卡洛采样器，用于归一化常数未知的目标分布采样。

**关键词**：扩散模型, 序贯蒙特卡洛, 朗之万蒙特卡洛, 分数估计, 控制变量, 分布采样

## 3 点简述
- 核心问题：目标分布归一化常数未知，传统采样方法受限，需高效估计扩散路径中的时变分数函数。
- 方法要点：结合扩散退火朗之万蒙特卡洛与序贯蒙特卡洛，通过辅助变量演化提供分数估计，并设计控制变量调度降低方差。
- 实验或效果：理论保证收敛性，在合成和真实数据集上验证有效性，提升采样效率与准确性。

## 摘要（原文）

> We develop a diffusion-based sampler for target distributions known up to a normalising constant. To this end, we rely on the well-known diffusion path that smoothly interpolates between a (simple) base distribution and the target distribution, widely used in diffusion models. Our approach is based on a practical implementation of diffusion-annealed Langevin Monte Carlo, which approximates the diffusion path with convergence guarantees. We tackle the score estimation problem by developing an efficient sequential Monte Carlo sampler that evolves auxiliary variables from conditional distributions along the path, which provides principled score estimates for time-varying distributions. We further develop novel control variate schedules that minimise the variance of these score estimates. Finally, we provide theoretical guarantees and empirically demonstrate the effectiveness of our method on several synthetic and real-world datasets.

