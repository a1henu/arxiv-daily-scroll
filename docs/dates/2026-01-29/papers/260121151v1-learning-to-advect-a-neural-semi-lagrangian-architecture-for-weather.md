---
layout: default
title: Learning to Advect: A Neural Semi-Lagrangian Architecture for Weather Forecasting
---

# Learning to Advect: A Neural Semi-Lagrangian Architecture for Weather Forecasting
**arXiv**：[2601.21151v1](https://arxiv.org/abs/2601.21151) · [PDF](https://arxiv.org/pdf/2601.21151.pdf)  
**作者**：Carlos A. Pereira, Stéphane Gaudreault, Valentin Dallerit, Christopher Subich, Shoyon Panday, Siqi Wei, Sasa Zhang, Siddharth Rout, Eldad Haber, Raymond J. Spiteri, David Millard, Emilia Diaconescu  

**一句话要点**：提出PARADIS模型，通过神经半拉格朗日算子改进天气预测中的平流处理

**关键词**：天气预测, 神经半拉格朗日算子, 物理启发模型, 功能分解, 轨迹传输, 训练效率

## 3 点简述
- 传统机器学习天气预测模型在平流处理上存在全局交互成本高或卷积层深的问题
- PARADIS采用功能分解为平流、扩散和反应块，引入神经半拉格朗日算子实现轨迹传输
- 在ERA5基准测试中，以更低训练成本达到或超越高分辨率基线性能

## 摘要（原文）

> Recent machine-learning approaches to weather forecasting often employ a monolithic architecture, where distinct physical mechanisms (advection, transport), diffusion-like mixing, thermodynamic processes, and forcing are represented implicitly within a single large network. This representation is particularly problematic for advection, where long-range transport must be treated with expensive global interaction mechanisms or through deep, stacked convolutional layers. To mitigate this, we present PARADIS, a physics-inspired global weather prediction model that imposes inductive biases on network behavior through a functional decomposition into advection, diffusion, and reaction blocks acting on latent variables. We implement advection through a Neural Semi-Lagrangian operator that performs trajectory-based transport via differentiable interpolation on the sphere, enabling end-to-end learning of both the latent modes to be transported and their characteristic trajectories. Diffusion-like processes are modeled through depthwise-separable spatial mixing, while local source terms and vertical interactions are modeled via pointwise channel interactions, enabling operator-level physical structure. PARADIS provides state-of-the-art forecast skill at a fraction of the training cost. On ERA5-based benchmarks, the 1 degree PARADIS model, with a total training cost of less than a GPU month, meets or exceeds the performance of 0.25 degree traditional and machine-learning baselines, including the ECMWF HRES forecast and DeepMind's GraphCast.

