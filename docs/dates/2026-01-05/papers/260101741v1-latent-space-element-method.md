---
layout: default
title: Latent Space Element Method
---

# Latent Space Element Method
**arXiv**：[2601.01741v1](https://arxiv.org/abs/2601.01741) · [PDF](https://arxiv.org/pdf/2601.01741.pdf)  
**作者**：Seung Whan Chung, Youngsoo Choi, Christopher Miller, H. Keo Springer, Kyle T. Sullivan  

**一句话要点**：提出潜在空间单元方法以构建可扩展的代理求解器，无需PDE算子介入。

**关键词**：代理求解器, 潜在空间建模, 单元组装, 偏微分方程求解, 可扩展性

## 3 点简述
- 核心问题：如何构建代理求解器，能在小域训练并扩展到大域，避免依赖PDE算子。
- 方法要点：基于学习子域模型，通过潜在空间耦合和窗口混合，组装成全局系统。
- 实验或效果：在1D Burgers和KdV方程上验证，保持预测精度并扩展到更大空间域。

## 摘要（原文）

> How can we build surrogate solvers that train on small domains but scale to larger ones without intrusive access to PDE operators? Inspired by the Data-Driven Finite Element Method (DD-FEM) framework for modular data-driven solvers, we propose the Latent Space Element Method (LSEM), an element-based latent surrogate assembly approach in which a learned subdomain ("element") model can be tiled and coupled to form a larger computational domain. Each element is a LaSDI latent ODE surrogate trained from snapshots on a local patch, and neighboring elements are coupled through learned directional interaction terms in latent space, avoiding Schwarz iterations and interface residual evaluations. A smooth window-based blending reconstructs a global field from overlapping element predictions, yielding a scalable assembled latent dynamical system. Experiments on the 1D Burgers and Korteweg-de Vries equations show that LSEM maintains predictive accuracy while scaling to spatial domains larger than those seen in training. LSEM offers an interpretable and extensible route toward foundation-model surrogate solvers built from reusable local models.

