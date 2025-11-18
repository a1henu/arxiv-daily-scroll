---
layout: default
title: Opt3DGS: Optimizing 3D Gaussian Splatting with Adaptive Exploration and Curvature-Aware Exploitation
---

# Opt3DGS: Optimizing 3D Gaussian Splatting with Adaptive Exploration and Curvature-Aware Exploitation
**arXiv**：[2511.13571v1](https://arxiv.org/abs/2511.13571) · [PDF](https://arxiv.org/pdf/2511.13571.pdf)  
**作者**：Ziyang Huang, Jiagang Chen, Jin Liu, Shunping Ji  

**一句话要点**：提出Opt3DGS以解决3D高斯泼溅优化中的局部最优和收敛质量问题

**关键词**：3D高斯泼溅, 优化算法, 新视角合成, 自适应探索, 曲率引导开发

## 3 点简述
- 核心问题：3D高斯泼溅优化易陷局部最优且收敛质量不足
- 方法要点：采用自适应探索与曲率引导开发两阶段优化框架
- 实验或效果：在多个基准数据集上实现最先进的渲染质量

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a leading framework for novel view synthesis, yet its core optimization challenges remain underexplored. We identify two key issues in 3DGS optimization: entrapment in suboptimal local optima and insufficient convergence quality. To address these, we propose Opt3DGS, a robust framework that enhances 3DGS through a two-stage optimization process of adaptive exploration and curvature-guided exploitation. In the exploration phase, an Adaptive Weighted Stochastic Gradient Langevin Dynamics (SGLD) method enhances global search to escape local optima. In the exploitation phase, a Local Quasi-Newton Direction-guided Adam optimizer leverages curvature information for precise and efficient convergence. Extensive experiments on diverse benchmark datasets demonstrate that Opt3DGS achieves state-of-the-art rendering quality by refining the 3DGS optimization process without modifying its underlying representation.

