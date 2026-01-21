---
layout: default
title: StoTAM: Stochastic Alternating Minimization for Tucker-Structured Tensor Sensing
---

# StoTAM: Stochastic Alternating Minimization for Tucker-Structured Tensor Sensing
**arXiv**：[2601.13522v1](https://arxiv.org/abs/2601.13522) · [PDF](https://arxiv.org/pdf/2601.13522.pdf)  
**作者**：Shuang Li  

**一句话要点**：提出随机交替最小化算法以高效解决低Tucker秩张量感知问题

**关键词**：张量感知, Tucker分解, 随机优化, 交替最小化, 低秩张量恢复

## 3 点简述
- 核心问题：低Tucker秩张量感知，用于高维数据多模式子空间结构恢复
- 方法要点：基于Tucker分解，直接在核心张量和因子矩阵上进行随机交替最小化，避免重复张量投影
- 实验或效果：数值实验显示，在合成张量感知中，相比基线方法，该算法在运行时间上表现出更优的收敛行为

## 摘要（原文）

> Low-rank tensor sensing is a fundamental problem with broad applications in signal processing and machine learning. Among various tensor models, low-Tucker-rank tensors are particularly attractive for capturing multi-mode subspace structures in high-dimensional data. Existing recovery methods either operate on the full tensor variable with expensive tensor projections, or adopt factorized formulations that still rely on full-gradient computations, while most stochastic factorized approaches are restricted to tensor decomposition settings. In this work, we propose a stochastic alternating minimization algorithm that operates directly on the core tensor and factor matrices under a Tucker factorization. The proposed method avoids repeated tensor projections and enables efficient mini-batch updates on low-dimensional tensor factors. Numerical experiments on synthetic tensor sensing demonstrate that the proposed algorithm exhibits favorable convergence behavior in wall-clock time compared with representative stochastic tensor recovery baselines.

