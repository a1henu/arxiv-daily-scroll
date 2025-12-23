---
layout: default
title: Lag Operator SSMs: A Geometric Framework for Structured State Space Modeling
---

# Lag Operator SSMs: A Geometric Framework for Structured State Space Modeling
**arXiv**：[2512.18965v1](https://arxiv.org/abs/2512.18965) · [PDF](https://arxiv.org/pdf/2512.18965.pdf)  
**作者**：Sutashu Tomonaga, Kenji Doya, Noboru Murata  

**一句话要点**：提出基于滞后算子的几何框架，以直接构建离散时间结构化状态空间模型

**关键词**：结构化状态空间模型, 滞后算子, 离散时间建模, 序列建模, 几何框架, 模块化设计

## 3 点简述
- 核心问题：结构化状态空间模型理论依赖连续时间建模和离散化，过程复杂且直觉模糊
- 方法要点：引入滞后算子，通过几何方式推导离散时间递推，实现模块化设计
- 实验或效果：验证框架可精确恢复HiPPO模型递推，数值模拟支持理论推导

## 摘要（原文）

> Structured State Space Models (SSMs), which are at the heart of the recently popular Mamba architecture, are powerful tools for sequence modeling. However, their theoretical foundation relies on a complex, multi-stage process of continuous-time modeling and subsequent discretization, which can obscure intuition. We introduce a direct, first-principles framework for constructing discrete-time SSMs that is both flexible and modular. Our approach is based on a novel lag operator, which geometrically derives the discrete-time recurrence by measuring how the system's basis functions "slide" and change from one timestep to the next. The resulting state matrices are computed via a single inner product involving this operator, offering a modular design space for creating novel SSMs by flexibly combining different basis functions and time-warping schemes. To validate our approach, we demonstrate that a specific instance exactly recovers the recurrence of the influential HiPPO model. Numerical simulations confirm our derivation, providing new theoretical tools for designing flexible and robust sequence models.

