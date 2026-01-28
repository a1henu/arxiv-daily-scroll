---
layout: default
title: SharpNet: Enhancing MLPs to Represent Functions with Controlled Non-differentiability
---

# SharpNet: Enhancing MLPs to Represent Functions with Controlled Non-differentiability
**arXiv**：[2601.19683v1](https://arxiv.org/abs/2601.19683) · [PDF](https://arxiv.org/pdf/2601.19683.pdf)  
**作者**：Hanting Niu, Junkai Deng, Fei Hou, Wencheng Wang, Ying He  

**一句话要点**：提出SharpNet以增强MLP表示可控非可微函数的能力

**关键词**：多层感知机, 函数逼近, 非可微特征, 泊松方程, CAD模型重建

## 3 点简述
- MLP难以表示连续但非可微函数，需后处理
- SharpNet通过辅助特征函数和泊松方程编码用户定义的尖锐特征
- 在2D和3D任务中准确恢复尖锐边缘，优于现有方法

## 摘要（原文）

> Multi-layer perceptrons (MLPs) are a standard tool for learning and function approximation, but they inherently yield outputs that are globally smooth. As a result, they struggle to represent functions that are continuous yet deliberately non-differentiable (i.e., with prescribed $C^0$ sharp features) without relying on ad hoc post-processing. We present SharpNet, a modified MLP architecture capable of encoding functions with user-defined sharp features by enriching the network with an auxiliary feature function, which is defined as the solution to a Poisson equation with jump Neumann boundary conditions. It is evaluated via an efficient local integral that is fully differentiable with respect to the feature locations, enabling our method to jointly optimize both the feature locations and the MLP parameters to recover the target functions/models. The $C^0$-continuity of SharpNet is precisely controllable, ensuring $C^0$-continuity at the feature locations and smoothness elsewhere. We validate SharpNet on 2D problems and 3D CAD model reconstruction, and compare it against several state-of-the-art baselines. In both types of tasks, SharpNet accurately recovers sharp edges and corners while maintaining smooth behavior away from those features, whereas existing methods tend to smooth out gradient discontinuities. Both qualitative and quantitative evaluations highlight the benefits of our approach.

