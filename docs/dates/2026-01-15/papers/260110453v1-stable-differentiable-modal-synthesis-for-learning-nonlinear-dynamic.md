---
layout: default
title: Stable Differentiable Modal Synthesis for Learning Nonlinear Dynamics
---

# Stable Differentiable Modal Synthesis for Learning Nonlinear Dynamics
**arXiv**：[2601.10453v1](https://arxiv.org/abs/2601.10453) · [PDF](https://arxiv.org/pdf/2601.10453.pdf)  
**作者**：Victor Zheleznov, Stefan Bilbao, Alec Wright, Simon King  

**一句话要点**：提出稳定可微模态合成方法，结合标量辅助变量与神经常微分方程以学习非线性动力学。

**关键词**：模态合成, 非线性动力学, 神经常微分方程, 标量辅助变量, 物理建模, 稳定数值求解

## 3 点简述
- 核心问题：模态方法用于非线性物理建模时，常微分方程组密集耦合，需稳定数值求解。
- 方法要点：融合标量辅助变量技术与神经常微分方程，构建稳定可微模型，保留物理参数可访问性。
- 实验或效果：以非线性弦振动合成数据为概念验证，模型能学习并复现系统非线性动力学。

## 摘要（原文）

> Modal methods are a long-standing approach to physical modelling synthesis. Extensions to nonlinear problems are possible, including the case of a high-amplitude vibration of a string. A modal decomposition leads to a densely coupled nonlinear system of ordinary differential equations. Recent work in scalar auxiliary variable techniques has enabled construction of explicit and stable numerical solvers for such classes of nonlinear systems. On the other hand, machine learning approaches (in particular neural ordinary differential equations) have been successful in modelling nonlinear systems automatically from data. In this work, we examine how scalar auxiliary variable techniques can be combined with neural ordinary differential equations to yield a stable differentiable model capable of learning nonlinear dynamics. The proposed approach leverages the analytical solution for linear vibration of system's modes so that physical parameters of a system remain easily accessible after the training without the need for a parameter encoder in the model architecture. As a proof of concept, we generate synthetic data for the nonlinear transverse vibration of a string and show that the model can be trained to reproduce the nonlinear dynamics of the system. Sound examples are presented.

