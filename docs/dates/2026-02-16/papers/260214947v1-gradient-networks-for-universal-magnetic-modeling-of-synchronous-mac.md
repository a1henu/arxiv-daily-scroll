---
layout: default
title: Gradient Networks for Universal Magnetic Modeling of Synchronous Machines
---

# Gradient Networks for Universal Magnetic Modeling of Synchronous Machines
**arXiv**：[2602.14947v1](https://arxiv.org/abs/2602.14947) · [PDF](https://arxiv.org/pdf/2602.14947.pdf)  
**作者**：Junyi Li, Tim Foissner, Floran Martin, Antti Piippo, Marko Hinkkanen  

**一句话要点**：提出梯度网络方法，用于同步电机的通用磁建模，解决饱和与空间谐波问题。

**关键词**：梯度网络, 同步电机建模, 物理信息神经网络, 磁饱和, 能量平衡, 模型反演

## 3 点简述
- 核心问题：同步电机动态建模中非线性电磁关系的准确描述，包括饱和与空间谐波。
- 方法要点：将梯度网络融入基本电机方程，学习磁场能量梯度，确保能量平衡与物理一致性。
- 实验或效果：基于实测与FEM数据验证，模型在有限训练数据下实现准确、平滑输出，支持模型反演与控制优化。

## 摘要（原文）

> This paper presents a physics-informed neural network approach for dynamic modeling of saturable synchronous machines, including cases with spatial harmonics. We introduce an architecture that incorporates gradient networks directly into the fundamental machine equations, enabling accurate modeling of the nonlinear and coupled electromagnetic constitutive relationship. By learning the gradient of the magnetic field energy, the model inherently satisfies energy balance (reciprocity conditions). The proposed architecture can universally approximate any physically feasible magnetic behavior and offers several advantages over lookup tables and standard machine learning models: it requires less training data, ensures monotonicity and reliable extrapolation, and produces smooth outputs. These properties further enable robust model inversion and optimal trajectory generation, often needed in control applications. We validate the proposed approach using measured and finite-element method (FEM) datasets from a 5.6-kW permanent-magnet (PM) synchronous reluctance machine. Results demonstrate accurate and physically consistent models, even with limited training data.

