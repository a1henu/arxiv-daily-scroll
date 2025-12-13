---
layout: default
title: T-SKM-Net: Trainable Neural Network Framework for Linear Constraint Satisfaction via Sampling Kaczmarz-Motzkin Method
---

# T-SKM-Net: Trainable Neural Network Framework for Linear Constraint Satisfaction via Sampling Kaczmarz-Motzkin Method
**arXiv**：[2512.10461v1](https://arxiv.org/abs/2512.10461) · [PDF](https://arxiv.org/pdf/2512.10461.pdf)  
**作者**：Haoyu Zhu, Yao Zhang, Jiashen Ren, Qingchun Hou  

**一句话要点**：提出可训练的T-SKM-Net框架，首次将采样Kaczmarz-Motzkin方法系统集成到神经网络约束满足中

**关键词**：约束满足神经网络, 采样Kaczmarz-Motzkin方法, 线性不等式系统, 可微优化, 电力系统优化, 安全关键应用

## 3 点简述
- 现有约束满足方法面临效率与适用性权衡，SKM方法虽收敛性好但非可微操作阻碍神经网络应用
- 通过零空间变换将混合约束转为纯不等式问题，利用SKM迭代求解并映射回原空间，支持标准反向传播
- 在DCOPF基准测试中实现25倍加速且保持零约束违反，提供后处理与联合训练两种模式

## 摘要（原文）

> Neural network constraint satisfaction is crucial for safety-critical applications such as power system optimization, robotic path planning, and autonomous driving. However, existing constraint satisfaction methods face efficiency-applicability trade-offs, with hard constraint methods suffering from either high computational complexity or restrictive assumptions on constraint structures. The Sampling Kaczmarz-Motzkin (SKM) method is a randomized iterative algorithm for solving large-scale linear inequality systems with favorable convergence properties, but its argmax operations introduce non-differentiability, posing challenges for neural network applications. This work proposes the Trainable Sampling Kaczmarz-Motzkin Network (T-SKM-Net) framework and, for the first time, systematically integrates SKM-type methods into neural network constraint satisfaction. The framework transforms mixed constraint problems into pure inequality problems through null space transformation, employs SKM for iterative solving, and maps solutions back to the original constraint space, efficiently handling both equality and inequality constraints. We provide theoretical proof of post-processing effectiveness in expectation and end-to-end trainability guarantees based on unbiased gradient estimators, demonstrating that despite non-differentiable operations, the framework supports standard backpropagation. On the DCOPF case118 benchmark, our method achieves 4.27ms/item GPU serial forward inference with 0.0025% max optimality gap with post-processing mode and 5.25ms/item with 0.0008% max optimality gap with joint training mode, delivering over 25$\times$ speedup compared to the pandapower solver while maintaining zero constraint violations under given tolerance.

