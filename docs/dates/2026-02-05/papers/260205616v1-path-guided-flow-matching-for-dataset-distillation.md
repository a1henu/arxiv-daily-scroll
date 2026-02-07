---
layout: default
title: Path-Guided Flow Matching for Dataset Distillation
---

# Path-Guided Flow Matching for Dataset Distillation
**arXiv**：[2602.05616v1](https://arxiv.org/abs/2602.05616) · [PDF](https://arxiv.org/pdf/2602.05616.pdf)  
**作者**：Xuhui Li, Zhengquan Luo, Xiwei Liu, Yongqiang Yu, Zhiqiang Xu  

**一句话要点**：提出路径引导流匹配以解决数据集蒸馏中基于扩散方法的采样低效与轨迹不稳定问题

**关键词**：数据集蒸馏, 流匹配, 路径引导, 确定性合成, 高效采样, 潜空间学习

## 3 点简述
- 核心问题：基于扩散的数据集蒸馏依赖启发式引导或原型分配，导致采样耗时、轨迹不稳定，影响下游泛化。
- 方法要点：在冻结VAE的潜空间进行流匹配，学习从高斯噪声到数据分布的类条件传输，实现快速确定性合成。
- 实验或效果：在高分辨率基准测试中，PGFM匹配或超越先前扩散方法，采样步骤更少，效率显著提升，如比扩散方法快7.6倍。

## 摘要（原文）

> Dataset distillation compresses large datasets into compact synthetic sets with comparable performance in training models. Despite recent progress on diffusion-based distillation, this type of method typically depends on heuristic guidance or prototype assignment, which comes with time-consuming sampling and trajectory instability and thus hurts downstream generalization especially under strong control or low IPC. We propose \emph{Path-Guided Flow Matching (PGFM)}, the first flow matching-based framework for generative distillation, which enables fast deterministic synthesis by solving an ODE in a few steps. PGFM conducts flow matching in the latent space of a frozen VAE to learn class-conditional transport from Gaussian noise to data distribution. Particularly, we develop a continuous path-to-prototype guidance algorithm for ODE-consistent path control, which allows trajectories to reliably land on assigned prototypes while preserving diversity and efficiency. Extensive experiments across high-resolution benchmarks demonstrate that PGFM matches or surpasses prior diffusion-based distillation approaches with fewer steps of sampling while delivering competitive performance with remarkably improved efficiency, e.g., 7.6$\times$ more efficient than the diffusion-based counterparts with 78\% mode coverage.

