---
layout: default
title: Polyharmonic Cascade
---

# Polyharmonic Cascade
**arXiv**：[2512.17671v1](https://arxiv.org/abs/2512.17671) · [PDF](https://arxiv.org/pdf/2512.17671.pdf)  
**作者**：Yuriy N. Bakhvalov  

**一句话要点**：提出多谐级联架构，通过全局线性系统训练以高效逼近复杂非线性函数。

**关键词**：多谐级联, 深度学习架构, 全局线性系统训练, 多谐样条, 概率解释, GPU加速

## 3 点简述
- 核心问题：如何设计深度学习架构以逼近任意复杂非线性函数，同时保持全局平滑性和概率解释。
- 方法要点：基于随机函数理论和无差别原则，构建多谐样条包序列，采用全局线性系统替代梯度下降进行训练。
- 实验或效果：在MNIST上实现快速学习且无过拟合，计算高效，可GPU加速执行2D矩阵运算。

## 摘要（原文）

> This paper presents a deep machine learning architecture, the "polyharmonic cascade" -- a sequence of packages of polyharmonic splines, where each layer is rigorously derived from the theory of random functions and the principles of indifference. This makes it possible to approximate nonlinear functions of arbitrary complexity while preserving global smoothness and a probabilistic interpretation. For the polyharmonic cascade, a training method alternative to gradient descent is proposed: instead of directly optimizing the coefficients, one solves a single global linear system on each batch with respect to the function values at fixed "constellations" of nodes. This yields synchronized updates of all layers, preserves the probabilistic interpretation of individual layers and theoretical consistency with the original model, and scales well: all computations reduce to 2D matrix operations efficiently executed on a GPU. Fast learning without overfitting on MNIST is demonstrated.

