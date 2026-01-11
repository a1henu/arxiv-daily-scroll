---
layout: default
title: Crystal Generation using the Fully Differentiable Pipeline and Latent Space Optimization
---

# Crystal Generation using the Fully Differentiable Pipeline and Latent Space Optimization
**arXiv**：[2601.04606v1](https://arxiv.org/abs/2601.04606) · [PDF](https://arxiv.org/pdf/2601.04606.pdf)  
**作者**：Osman Goni Ridwan, Gilles Frapper, Hongfei Xue, Qiang Zhu  

**一句话要点**：提出全可微管道与潜在空间优化框架，用于生成满足目标局部环境的晶体结构

**关键词**：晶体生成, 可微管道, 潜在空间优化, 变分自编码器, SO(3)功率谱, 材料设计

## 3 点简述
- 核心问题：在晶体学约束下生成具有指定局部环境的材料结构，面临局部障碍和计算效率挑战
- 方法要点：结合对称条件变分自编码器和可微SO(3)功率谱目标，实现直接与潜在表示的双层优化
- 实验或效果：GPU加速实现约五倍速度提升，双级松弛策略提高复杂结构生成成功率，可扩展至多组分系统

## 摘要（原文）

> We present a materials generation framework that couples a symmetry-conditioned variational autoencoder (CVAE) with a differentiable SO(3) power spectrum objective to steer candidates toward a specified local environment under the crystallographic constraints. In particular, we implement a fully differentiable pipeline that performs batch-wise optimization on both direct and latent crystallographic representations. Using the GPU acceleration, the implementation achieves about fivefold speed compared to our previous CPU workflow, while yielding comparable outcomes. In addition, we introduce the optimization strategy that alternatively performs optimization on the direct and latent crystal representations. This dual-level relaxation approach can effectively overcome local barrier defined by different objective gradients, thus increasing the success rate of generating complex structures satisfying the targe local environments. This framework can be extended to systems consisting of multi-components and multi-environments, providing a scalable route to generate material structures with the target local environment.

