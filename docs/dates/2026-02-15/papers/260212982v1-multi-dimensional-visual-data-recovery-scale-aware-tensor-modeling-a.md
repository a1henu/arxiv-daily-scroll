---
layout: default
title: Multi-Dimensional Visual Data Recovery: Scale-Aware Tensor Modeling and Accelerated Randomized Computation
---

# Multi-Dimensional Visual Data Recovery: Scale-Aware Tensor Modeling and Accelerated Randomized Computation
**arXiv**：[2602.12982v1](https://arxiv.org/abs/2602.12982) · [PDF](https://arxiv.org/pdf/2602.12982.pdf)  
**作者**：Wenjin Qin, Hailin Wang, Jiangjun Peng, Jianjun Wang, Tingwen Huang  

**一句话要点**：提出基于FCTN分解的尺度感知张量建模与随机加速计算，以提升多维视觉数据恢复的效率和建模能力。

**关键词**：张量分解, 数据恢复, 随机算法, 非凸优化, 计算加速, 多维视觉

## 3 点简述
- 针对FCTN分解在多维数据恢复中计算效率低和建模能力不足的问题，提出广义非凸正则化范式。
- 基于ADMM框架设计高效优化算法，并利用草图技术开发随机压缩算法以加速大规模数据处理。
- 理论分析证明近似误差上界和收敛性，实验显示在定量指标、视觉质量和运行时间上优于现有方法。

## 摘要（原文）

> The recently proposed fully-connected tensor network (FCTN) decomposition has demonstrated significant advantages in correlation characterization and transpositional invariance, and has achieved notable achievements in multi-dimensional data processing and analysis. However, existing multi-dimensional data recovery methods leveraging FCTN decomposition still have room for further enhancement, particularly in computational efficiency and modeling capability. To address these issues, we first propose a FCTN-based generalized nonconvex regularization paradigm from the perspective of gradient mapping. Then, reliable and scalable multi-dimensional data recovery models are investigated, where the model formulation is shifted from unquantized observations to coarse-grained quantized observations. Based on the alternating direction method of multipliers (ADMM) framework, we derive efficient optimization algorithms with convergence guarantees to solve the formulated models. To alleviate the computational bottleneck encountered when processing large-scale multi-dimensional data, fast and efficient randomized compression algorithms are devised in virtue of sketching techniques in numerical linear algebra. These dimensionality-reduction techniques serve as the computational acceleration core of our proposed algorithm framework. Theoretical results on approximation error upper bounds and convergence analysis for the proposed method are derived. Extensive numerical experiments illustrate the effectiveness and superiority of the proposed algorithm over other state-of-the-art methods in terms of quantitative metrics, visual quality, and running time.

