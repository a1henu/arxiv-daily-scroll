---
layout: default
title: Kinetic-based regularization: Learning spatial derivatives and PDE applications
---

# Kinetic-based regularization: Learning spatial derivatives and PDE applications
**arXiv**：[2603.06380v1](https://arxiv.org/abs/2603.06380) · [PDF](https://arxiv.org/pdf/2603.06380.pdf)  
**作者**：Abhisek Ganguly, Santosh Ansumali, Sauro Succi  

**一句话要点**：提出基于动力的正则化方法，以学习空间导数并应用于偏微分方程求解

**关键词**：空间导数学习, 基于动力的正则化, 偏微分方程求解, 局部化核回归, 噪声自适应估计, 二阶精度

## 3 点简述
- 核心问题：从离散噪声数据准确估计空间导数，对科学机器学习和偏微分方程数值解至关重要
- 方法要点：扩展基于动力的正则化，提供显式和隐式方案，实现局部化、二阶精度的导数学习
- 实验或效果：方法在干净数据上展现二次收敛，初步应用于一维双曲偏微分方程实现稳定激波捕捉

## 摘要（原文）

> Accurate estimation of spatial derivatives from discrete and noisy data is central to scientific machine learning and numerical solutions of PDEs. We extend kinetic-based regularization (KBR), a localized multidimensional kernel regression method with a single trainable parameter, to learn spatial derivatives with provable second-order accuracy in 1D. Two derivative-learning schemes are proposed: an explicit scheme based on the closed-form prediction expressions, and an implicit scheme that solves a perturbed linear system at the points of interest. The fully localized formulation enables efficient, noise-adaptive derivative estimation without requiring global system solving or heuristic smoothing. Both approaches exhibit quadratic convergence, matching second-order finite difference for clean data, along with a possible high-dimensional formulation. Preliminary results show that coupling KBR with conservative solvers enables stable shock capture in 1D hyperbolic PDEs, acting as a step towards solving PDEs on irregular point clouds in higher dimensions while preserving conservation laws.

