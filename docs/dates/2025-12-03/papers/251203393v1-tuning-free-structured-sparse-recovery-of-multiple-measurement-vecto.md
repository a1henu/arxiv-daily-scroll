---
layout: default
title: Tuning-Free Structured Sparse Recovery of Multiple Measurement Vectors using Implicit Regularization
---

# Tuning-Free Structured Sparse Recovery of Multiple Measurement Vectors using Implicit Regularization
**arXiv**：[2512.03393v1](https://arxiv.org/abs/2512.03393) · [PDF](https://arxiv.org/pdf/2512.03393.pdf)  
**作者**：Lakshmi Jayalal, Sheetal Kalyani  

**一句话要点**：提出基于隐式正则化的免调参框架，用于多测量向量联合稀疏恢复。

**关键词**：多测量向量, 联合稀疏恢复, 隐式正则化, 免调参优化, 过参数化, 梯度下降

## 3 点简述
- 核心问题：传统MMV方法需调参或先验知识，限制了实际应用。
- 方法要点：通过过参数化重参数化估计矩阵，利用梯度下降动态自动促进行稀疏结构。
- 实验或效果：理论保证收敛至理想解，实证性能媲美现有方法，无需调参。

## 摘要（原文）

> Recovering jointly sparse signals in the multiple measurement vectors (MMV) setting is a fundamental problem in machine learning, but traditional methods like multiple measurement vectors orthogonal matching pursuit (M-OMP) and multiple measurement vectors FOCal Underdetermined System Solver (M-FOCUSS) often require careful parameter tuning or prior knowledge of the sparsity of the signal and/or noise variance. We introduce a novel tuning-free framework that leverages Implicit Regularization (IR) from overparameterization to overcome this limitation. Our approach reparameterizes the estimation matrix into factors that decouple the shared row-support from individual vector entries. We show that the optimization dynamics inherently promote the desired row-sparse structure by applying gradient descent to a standard least-squares objective on these factors. We prove that with a sufficiently small and balanced initialization, the optimization dynamics exhibit a "momentum-like" effect, causing the norms of rows in the true support to grow significantly faster than others. This formally guarantees that the solution trajectory converges towards an idealized row-sparse solution. Additionally, empirical results demonstrate that our approach achieves performance comparable to established methods without requiring any prior information or tuning.

