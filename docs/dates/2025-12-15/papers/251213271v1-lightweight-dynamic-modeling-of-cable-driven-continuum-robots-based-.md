---
layout: default
title: Lightweight Dynamic Modeling of Cable-Driven Continuum Robots Based on Actuation-Space Energy Formulation
---

# Lightweight Dynamic Modeling of Cable-Driven Continuum Robots Based on Actuation-Space Energy Formulation
**arXiv**：[2512.13271v1](https://arxiv.org/abs/2512.13271) · [PDF](https://arxiv.org/pdf/2512.13271.pdf)  
**作者**：Fangju Yang, Hang Yang, Ibrahim Alsarraj, Yuhao Wang, Ke Wu  

**一句话要点**：提出基于驱动空间能量公式的轻量动态建模框架，以提升缆驱连续体机器人的实时动态预测与控制效率。

**关键词**：缆驱连续体机器人, 轻量动态建模, 驱动空间能量公式, 实时预测, 模型简化, 计算效率

## 3 点简述
- 核心问题：缆驱连续体机器人需高精度实时动态模型，现有方法计算复杂或功能受限。
- 方法要点：在驱动空间直接公式化势能，简化模型结构，避免显式计算接触力，支持力/位移输入模式。
- 实验或效果：通过模态离散化，计算速度比先进实时方法平均提升62.3%。

## 摘要（原文）

> Cable-driven continuum robots (CDCRs) require accurate, real-time dynamic models for high-speed dynamics prediction or model-based control, making such capability an urgent need. In this paper, we propose the Lightweight Actuation-Space Energy Modeling (LASEM) framework for CDCRs, which formulates actuation potential energy directly in actuation space to enable lightweight yet accurate dynamic modeling. Through a unified variational derivation, the governing dynamics reduce to a single partial differential equation (PDE), requiring only the Euler moment balance while implicitly incorporating the Newton force balance. By also avoiding explicit computation of cable-backbone contact forces, the formulation simplifies the model structure and improves computational efficiency while preserving geometric accuracy and physical consistency. Importantly, the proposed framework for dynamic modeling natively supports both force-input and displacement-input actuation modes, a capability seldom achieved in existing dynamic formulations. Leveraging this lightweight structure, a Galerkin space-time modal discretization with analytical time-domain derivatives of the reduced state further enables an average 62.3% computational speedup over state-of-the-art real-time dynamic modeling approaches.

