---
layout: default
title: Efficient Neural Controlled Differential Equations via Attentive Kernel Smoothing
---

# Efficient Neural Controlled Differential Equations via Attentive Kernel Smoothing
**arXiv**：[2602.02157v1](https://arxiv.org/abs/2602.02157) · [PDF](https://arxiv.org/pdf/2602.02157.pdf)  
**作者**：Egor Serov, Ilya Kuleshov, Alexey Zaytsev  

**一句话要点**：提出基于核平滑与注意力机制的神经控制微分方程，以提升序列建模效率与精度

**关键词**：神经控制微分方程, 序列建模, 核平滑, 注意力机制, 计算效率

## 3 点简述
- 核心问题：神经控制微分方程中驱动路径粗糙导致求解器步长过小，增加计算开销
- 方法要点：用核与高斯过程平滑路径，结合注意力机制多视图重建以恢复细节
- 实验或效果：在保持高精度下显著减少函数评估次数和推理时间，优于基线

## 摘要（原文）

> Neural Controlled Differential Equations (Neural CDEs) provide a powerful continuous-time framework for sequence modeling, yet the roughness of the driving control path often restricts their efficiency. Standard splines introduce high-frequency variations that force adaptive solvers to take excessively small steps, driving up the Number of Function Evaluations (NFE). We propose a novel approach to Neural CDE path construction that replaces exact interpolation with Kernel and Gaussian Process (GP) smoothing, enabling explicit control over trajectory regularity. To recover details lost during smoothing, we propose an attention-based Multi-View CDE (MV-CDE) and its convolutional extension (MVC-CDE), which employ learnable queries to inform path reconstruction. This framework allows the model to distribute representational capacity across multiple trajectories, each capturing distinct temporal patterns. Empirical results demonstrate that our method, MVC-CDE with GP, achieves state-of-the-art accuracy while significantly reducing NFEs and total inference time compared to spline-based baselines.

