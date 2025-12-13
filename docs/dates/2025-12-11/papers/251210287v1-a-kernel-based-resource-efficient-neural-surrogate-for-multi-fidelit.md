---
layout: default
title: A Kernel-based Resource-efficient Neural Surrogate for Multi-fidelity Prediction of Aerodynamic Field
---

# A Kernel-based Resource-efficient Neural Surrogate for Multi-fidelity Prediction of Aerodynamic Field
**arXiv**：[2512.10287v1](https://arxiv.org/abs/2512.10287) · [PDF](https://arxiv.org/pdf/2512.10287.pdf)  
**作者**：Apurba Sarker, Reza T. Batley, Darshan Sarojini, Sourav Saha  

**一句话要点**：提出KHRONOS核基神经代理模型，用于资源受限下的多保真度气动场预测。

**关键词**：多保真度预测, 核基神经代理, 气动场模拟, 资源效率优化, 张量分解

## 3 点简述
- 核心问题：传统气动模拟成本高，需高效代理模型平衡预测精度与计算资源。
- 方法要点：基于变分原理、插值理论和张量分解，融合稀疏高保真与低保真数据，实现参数大幅剪枝。
- 实验或效果：在AirfRANS数据集上，相比MLP、GNN和PINN，KHRONOS在资源受限时参数更少、训练推理更快，精度相当。

## 摘要（原文）

> Surrogate models provide fast alternatives to costly aerodynamic simulations and are extremely useful in design and optimization applications. This study proposes the use of a recent kernel-based neural surrogate, KHRONOS. In this work, we blend sparse high-fidelity (HF) data with low-fidelity (LF) information to predict aerodynamic fields under varying constraints in computational resources. Unlike traditional approaches, KHRONOS is built upon variational principles, interpolation theory, and tensor decomposition. These elements provide a mathematical basis for heavy pruning compared to dense neural networks. Using the AirfRANS dataset as a high-fidelity benchmark and NeuralFoil to generate low-fidelity counterparts, this work compares the performance of KHRONOS with three contemporary model architectures: a multilayer perceptron (MLP), a graph neural network (GNN), and a physics-informed neural network (PINN). We consider varying levels of high-fidelity data availability (0%, 10%, and 30%) and increasingly complex geometry parameterizations. These are used to predict the surface pressure coefficient distribution over the airfoil. Results indicate that, whilst all models eventually achieve comparable predictive accuracy, KHRONOS excels in resource-constrained conditions. In this domain, KHRONOS consistently requires orders of magnitude fewer trainable parameters and delivers much faster training and inference than contemporary dense neural networks at comparable accuracy. These findings highlight the potential of KHRONOS and similar architectures to balance accuracy and efficiency in multi-fidelity aerodynamic field prediction.

