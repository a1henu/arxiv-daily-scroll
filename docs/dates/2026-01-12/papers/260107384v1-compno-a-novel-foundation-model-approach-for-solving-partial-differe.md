---
layout: default
title: CompNO: A Novel Foundation Model approach for solving Partial Differential Equations
---

# CompNO: A Novel Foundation Model approach for solving Partial Differential Equations
**arXiv**：[2601.07384v1](https://arxiv.org/abs/2601.07384) · [PDF](https://arxiv.org/pdf/2601.07384.pdf)  
**作者**：Hamda Hmida, Hsiu-Wen Chang Joly, Youssef Mesri  

**一句话要点**：提出CompNO框架，通过组合基础块解决参数化偏微分方程的高效求解问题。

**关键词**：组合式神经算子, 参数化偏微分方程, 基础模型, 傅里叶神经算子, 边界条件处理, PDEBench基准

## 3 点简述
- 针对参数化偏微分方程求解计算成本高的问题，提出组合式神经算子框架。
- 方法先学习基础微分算子的专用块，再通过轻量适配块组装成任务特定求解器。
- 实验在PDEBench上验证，线性系统误差更低，非线性保持竞争力，边界条件精确满足。

## 摘要（原文）

> Partial differential equations (PDEs) govern a wide range of physical phenomena, but their numerical solution remains computationally demanding, especially when repeated simulations are required across many parameter settings. Recent Scientific Foundation Models (SFMs) aim to alleviate this cost by learning universal surrogates from large collections of simulated systems, yet they typically rely on monolithic architectures with limited interpretability and high pretraining expense. In this work we introduce Compositional Neural Operators (CompNO), a compositional neural operator framework for parametric PDEs. Instead of pretraining a single large model on heterogeneous data, CompNO first learns a library of Foundation Blocks, where each block is a parametric Fourier neural operator specialized to a fundamental differential operator (e.g. convection, diffusion, nonlinear convection). These blocks are then assembled, via lightweight Adaptation Blocks, into task-specific solvers that approximate the temporal evolution operator for target PDEs. A dedicated boundary-condition operator further enforces Dirichlet constraints exactly at inference time. We validate CompNO on one-dimensional convection, diffusion, convection--diffusion and Burgers' equations from the PDEBench suite. The proposed framework achieves lower relative L2 error than strong baselines (PFNO, PDEFormer and in-context learning based models) on linear parametric systems, while remaining competitive on nonlinear Burgers' flows. The model maintains exact boundary satisfaction with zero loss at domain boundaries, and exhibits robust generalization across a broad range of Peclet and Reynolds numbers. These results demonstrate that compositional neural operators provide a scalable and physically interpretable pathway towards foundation models for PDEs.

