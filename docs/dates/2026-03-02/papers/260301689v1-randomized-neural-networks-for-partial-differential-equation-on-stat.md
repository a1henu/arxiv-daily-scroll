---
layout: default
title: Randomized Neural Networks for Partial Differential Equation on Static and Evolving Surfaces
---

# Randomized Neural Networks for Partial Differential Equation on Static and Evolving Surfaces
**arXiv**：[2603.01689v1](https://arxiv.org/abs/2603.01689) · [PDF](https://arxiv.org/pdf/2603.01689.pdf)  
**作者**：Jingbo Sun, Fei Wang  

**一句话要点**：提出随机神经网络方法以解决静态和演化曲面上的偏微分方程数值求解问题

**关键词**：随机神经网络, 曲面偏微分方程, 演化曲面, 最小二乘求解, 无网格方法, 数值模拟

## 3 点简述
- 核心问题：曲面偏微分方程在几何复杂或演化时，传统网格方法面临计算成本高和精度不足的挑战
- 方法要点：使用随机生成隐藏层参数的神经网络，通过最小二乘求解输出层系数，避免非凸训练
- 实验或效果：数值实验显示该方法在多种曲面几何上具有广泛适用性和良好的精度-效率性能

## 摘要（原文）

> Surface partial differential equations arise in numerous scientific and engineering applications. Their numerical solution on static and evolving surfaces remains challenging due to geometric complexity and, for evolving geometries, the need for repeated mesh updates and geometry or solution transfer. While neural-network-based methods offer mesh-free discretizations, approaches based on nonconvex training can be costly and may fail to deliver high accuracy in practice. In this work, we develop a randomized neural network (RaNN) method for solving PDEs on both static and evolving surfaces: the hidden-layer parameters are randomly generated and kept fixed, and the output-layer coefficients are determined efficiently by solving a least-squares problem. For static surfaces, we present formulations for parametrized surfaces, implicit level-set surfaces, and point-cloud geometries, and provide a corresponding theoretical analysis for the parametrization-based formulation with interface compatibility. For evolving surfaces with topology preserved over time, we introduce a RaNN-based strategy that learns the surface evolution through a flow-map representation and then solves the surface PDE on a space--time collocation set, avoiding remeshing. Extensive numerical experiments demonstrate broad applicability and favorable accuracy--efficiency performance on representative benchmarks.

