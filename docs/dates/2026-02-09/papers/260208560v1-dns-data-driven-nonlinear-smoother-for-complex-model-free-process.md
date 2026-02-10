---
layout: default
title: DNS: Data-driven Nonlinear Smoother for Complex Model-free Process
---

# DNS: Data-driven Nonlinear Smoother for Complex Model-free Process
**arXiv**：[2602.08560v1](https://arxiv.org/abs/2602.08560) · [PDF](https://arxiv.org/pdf/2602.08560.pdf)  
**作者**：Fredrik Cumlin, Anubhab Ghosh, Saikat Chatterjee  

**一句话要点**：提出数据驱动非线性平滑器以估计无模型复杂动态过程的隐藏状态序列

**关键词**：数据驱动平滑, 非线性状态估计, 无模型动态过程, 循环架构, 无监督学习

## 3 点简述
- 核心问题：从噪声线性测量序列估计无模型复杂动态过程的隐藏状态序列，无状态转移模型可用。
- 方法要点：使用循环架构提供闭式后验，以无监督方式仅从测量数据学习。
- 实验或效果：在多个随机动态过程（包括洛伦兹系统）中，性能显著优于深度卡尔曼平滑器和迭代数据驱动非线性状态估计平滑器。

## 摘要（原文）

> We propose data-driven nonlinear smoother (DNS) to estimate a hidden state sequence of a complex dynamical process from a noisy, linear measurement sequence. The dynamical process is model-free, that is, we do not have any knowledge of the nonlinear dynamics of the complex process. There is no state-transition model (STM) of the process available. The proposed DNS uses a recurrent architecture that helps to provide a closed-form posterior of the hidden state sequence given the measurement sequence. DNS learns in an unsupervised manner, meaning the training dataset consists of only measurement data and no state data. We demonstrate DNS using simulations for smoothing of several stochastic dynamical processes, including a benchmark Lorenz system. Experimental results show that the DNS is significantly better than a deep Kalman smoother (DKS) and an iterative data-driven nonlinear state estimation (iDANSE) smoother.

