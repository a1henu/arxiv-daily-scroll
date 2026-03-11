---
layout: default
title: Towards Understanding Adam Convergence on Highly Degenerate Polynomials
---

# Towards Understanding Adam Convergence on Highly Degenerate Polynomials
**arXiv**：[2603.09581v1](https://arxiv.org/abs/2603.09581) · [PDF](https://arxiv.org/pdf/2603.09581.pdf)  
**作者**：Zhiwei Bai, Jiajie Zhao, Zhangchen Zhou, Zhi-Qin John Xu, Yaoyu Zhang  

**一句话要点**：揭示Adam在高度退化多项式上的自动收敛特性，优于梯度下降和动量法。

**关键词**：Adam优化算法, 高度退化多项式, 自动收敛, 局部线性收敛, 超参数相图, 二阶矩解耦

## 3 点简述
- 研究Adam在无外部调度器下的自然收敛性，聚焦高度退化多项式场景。
- 理论推导局部渐近稳定条件，实验验证与理论界限高度一致。
- 发现Adam通过二阶矩与梯度平方解耦机制，实现局部线性收敛加速。

## 摘要（原文）

> Adam is a widely used optimization algorithm in deep learning, yet the specific class of objective functions where it exhibits inherent advantages remains underexplored. Unlike prior studies requiring external schedulers and $β_2$ near 1 for convergence, this work investigates the "natural" auto-convergence properties of Adam. We identify a class of highly degenerate polynomials where Adam converges automatically without additional schedulers. Specifically, we derive theoretical conditions for local asymptotic stability on degenerate polynomials and demonstrate strong alignment between theoretical bounds and experimental results. We prove that Adam achieves local linear convergence on these degenerate functions, significantly outperforming the sub-linear convergence of Gradient Descent and Momentum. This acceleration stems from a decoupling mechanism between the second moment $v_t$ and squared gradient $g_t^2$, which exponentially amplifies the effective learning rate. Finally, we characterize Adam's hyperparameter phase diagram, identifying three distinct behavioral regimes: stable convergence, spikes, and SignGD-like oscillation.

