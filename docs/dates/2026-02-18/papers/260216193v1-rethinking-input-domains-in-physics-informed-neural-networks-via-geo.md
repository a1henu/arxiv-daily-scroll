---
layout: default
title: Rethinking Input Domains in Physics-Informed Neural Networks via Geometric Compactification Mappings
---

# Rethinking Input Domains in Physics-Informed Neural Networks via Geometric Compactification Mappings
**arXiv**：[2602.16193v1](https://arxiv.org/abs/2602.16193) · [PDF](https://arxiv.org/pdf/2602.16193.pdf)  
**作者**：Zhenzhen Huang, Haoyu Bian, Jiaquan Zhang, Yibei Liu, Kuien Liu, Caiyan Qin, Guoqing Wang, Yang Yang, Chaoning Zhang  

**一句话要点**：提出几何紧化映射以解决PINN中多尺度PDE求解的梯度刚性问题

**关键词**：物理信息神经网络, 几何紧化映射, 多尺度偏微分方程, 梯度刚性, 输入域优化, 训练稳定性

## 3 点简述
- 核心问题：多尺度PDE中几何结构与固定坐标输入不匹配导致梯度刚性和收敛困难
- 方法要点：通过可微几何紧化映射重塑输入坐标，耦合PDE几何结构与残差算子谱特性
- 实验或效果：在1D和2D代表性PDE上实现更均匀残差分布、更高精度及更快收敛

## 摘要（原文）

> Several complex physical systems are governed by multi-scale partial differential equations (PDEs) that exhibit both smooth low-frequency components and localized high-frequency structures. Existing physics-informed neural network (PINN) methods typically train with fixed coordinate system inputs, where geometric misalignment with these structures induces gradient stiffness and ill-conditioning that hinder convergence. To address this issue, we introduce a mapping paradigm that reshapes the input coordinates through differentiable geometric compactification mappings and couples the geometric structure of PDEs with the spectral properties of residual operators. Based on this paradigm, we propose Geometric Compactification (GC)-PINN, a framework that introduces three mapping strategies for periodic boundaries, far-field scale expansion, and localized singular structures in the input domain without modifying the underlying PINN architecture. Extensive empirical evaluation demonstrates that this approach yields more uniform residual distributions and higher solution accuracy on representative 1D and 2D PDEs, while improving training stability and convergence speed.

