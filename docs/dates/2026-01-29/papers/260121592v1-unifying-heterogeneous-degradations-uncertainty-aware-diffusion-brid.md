---
layout: default
title: Unifying Heterogeneous Degradations: Uncertainty-Aware Diffusion Bridge Model for All-in-One Image Restoration
---

# Unifying Heterogeneous Degradations: Uncertainty-Aware Diffusion Bridge Model for All-in-One Image Restoration
**arXiv**：[2601.21592v1](https://arxiv.org/abs/2601.21592) · [PDF](https://arxiv.org/pdf/2601.21592.pdf)  
**作者**：Luwei Tu, Jiawei Wu, Xing Luo, Zhi Jin  

**一句话要点**：提出不确定性感知扩散桥模型，以解决全场景图像修复中异构退化冲突问题。

**关键词**：图像修复, 扩散模型, 不确定性建模, 异构退化, 传输问题, 单步推理

## 3 点简述
- 核心问题：全场景图像修复面临异构退化优化目标冲突，现有方法控制机制粗糙或映射固定。
- 方法要点：引入松弛扩散桥建模像素级不确定性，通过双调制策略对齐退化到共享高熵空间并自适应调节传输轨迹。
- 实验或效果：在单步推理中实现多种修复任务的先进性能，有效修正传输几何与动力学。

## 摘要（原文）

> All-in-One Image Restoration (AiOIR) faces the fundamental challenge in reconciling conflicting optimization objectives across heterogeneous degradations. Existing methods are often constrained by coarse-grained control mechanisms or fixed mapping schedules, yielding suboptimal adaptation. To address this, we propose an Uncertainty-Aware Diffusion Bridge Model (UDBM), which innovatively reformulates AiOIR as a stochastic transport problem steered by pixel-wise uncertainty. By introducing a relaxed diffusion bridge formulation which replaces the strict terminal constraint with a relaxed constraint, we model the uncertainty of degradations while theoretically resolving the drift singularity inherent in standard diffusion bridges. Furthermore, we devise a dual modulation strategy: the noise schedule aligns diverse degradations into a shared high-entropy latent space, while the path schedule adaptively regulates the transport trajectory motivated by the viscous dynamics of entropy regularization. By effectively rectifying the transport geometry and dynamics, UDBM achieves state-of-the-art performance across diverse restoration tasks within a single inference step.

