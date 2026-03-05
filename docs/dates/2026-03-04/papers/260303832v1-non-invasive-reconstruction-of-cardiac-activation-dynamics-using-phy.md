---
layout: default
title: Non-Invasive Reconstruction of Cardiac Activation Dynamics Using Physics-Informed Neural Networks
---

# Non-Invasive Reconstruction of Cardiac Activation Dynamics Using Physics-Informed Neural Networks
**arXiv**：[2603.03832v1](https://arxiv.org/abs/2603.03832) · [PDF](https://arxiv.org/pdf/2603.03832.pdf)  
**作者**：Nathan Dermul, Hans Dierckx  

**一句话要点**：提出基于物理信息神经网络的非侵入性心脏激活动态重建方法，用于简化左心室几何结构。

**关键词**：心脏激活重建, 物理信息神经网络, 非侵入性计算, 电机械相互作用, 有限元损失函数, 数字表型分析

## 3 点简述
- 核心问题：心脏心律失常的复杂电机械相互作用在体内无法直接观测，需非侵入性计算重建三维激活动态。
- 方法要点：集成非线性各向异性本构模型、异质纤维取向、弱形式力学方程和有限元损失函数，将物理约束嵌入训练。
- 实验或效果：在噪声和低空间分辨率下准确重建时空激活动态，保持全局传播模式和激活时序。

## 摘要（原文）

> Cardiac arrhythmogenesis is governed by complex electromechanical interactions that are not directly observable in vivo, motivating the development of non-invasive computational approaches for reconstructing three-dimensional activation dynamics. We present a physics-informed neural network framework for recovering cardiac activation patterns, active tension propagation, deformation fields, and hydrostatic pressure from measurable deformation data in simplified left ventricular geometries. Our approach integrates nonlinear anisotropic constitutive modeling, heterogeneous fiber orientation, weak formulations of the governing mechanics, and finite-element-based loss functions to embed physical constraints directly into training.
>   We demonstrate that the proposed framework accurately reconstructs spatiotemporal activation dynamics under varying levels of measurement noise and reduced spatial resolution, while preserving global propagation patterns and activation timing. By coupling mechanistic modeling with data-driven inference, this method establishes a pathway toward patient-specific, non-invasive reconstruction of cardiac activation, with potential applications in digital phenotyping and computational support for arrhythmia assessment.

