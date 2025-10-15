---
layout: default
title: DiffEM: Learning from Corrupted Data with Diffusion Models via Expectation Maximization
---

# DiffEM: Learning from Corrupted Data with Diffusion Models via Expectation Maximization
**arXiv**：[2510.12691v1](https://arxiv.org/abs/2510.12691) · [PDF](https://arxiv.org/pdf/2510.12691.pdf)  
**作者**：Danial Hosseintabar, Fan Chen, Giannis Daras, Antonio Torralba, Constantinos Daskalakis  

**一句话要点**：提出DiffEM方法以从损坏数据中训练扩散模型

**关键词**：扩散模型, 期望最大化, 图像重建, 损坏数据学习, 条件扩散模型

## 3 点简述
- 核心问题：扩散模型在仅有损坏或噪声观测数据时训练困难
- 方法要点：使用期望最大化算法，E步重建干净数据，M步优化模型
- 实验或效果：在多种图像重建任务中验证方法有效性

## 摘要（原文）

> Diffusion models have emerged as powerful generative priors for
> high-dimensional inverse problems, yet learning them when only corrupted or
> noisy observations are available remains challenging. In this work, we propose
> a new method for training diffusion models with Expectation-Maximization (EM)
> from corrupted data. Our proposed method, DiffEM, utilizes conditional
> diffusion models to reconstruct clean data from observations in the E-step, and
> then uses the reconstructed data to refine the conditional diffusion model in
> the M-step. Theoretically, we provide monotonic convergence guarantees for the
> DiffEM iteration, assuming appropriate statistical conditions. We demonstrate
> the effectiveness of our approach through experiments on various image
> reconstruction tasks.

