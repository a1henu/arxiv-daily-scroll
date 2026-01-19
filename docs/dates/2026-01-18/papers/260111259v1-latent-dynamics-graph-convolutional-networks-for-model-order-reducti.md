---
layout: default
title: Latent Dynamics Graph Convolutional Networks for model order reduction of parameterized time-dependent PDEs
---

# Latent Dynamics Graph Convolutional Networks for model order reduction of parameterized time-dependent PDEs
**arXiv**：[2601.11259v1](https://arxiv.org/abs/2601.11259) · [PDF](https://arxiv.org/pdf/2601.11259.pdf)  
**作者**：Lorenzo Tomada, Federico Pichi, Gianluigi Rozza  

**一句话要点**：提出LD-GCN以结合几何归纳偏置与可解释潜在行为，用于参数化时变PDE的模型降阶

**关键词**：图神经网络, 模型降阶, 参数化偏微分方程, 潜在动力学, 几何归纳偏置, 零样本预测

## 3 点简述
- 现有GNN方法难以融合几何归纳偏置与可解释潜在行为，忽略动态特征或空间信息
- LD-GCN为无编码器架构，在潜在空间建模时间演化，通过GNN解码到几何参数化域
- 方法经数学验证和数值测试，支持零样本预测，应用于Navier-Stokes方程分岔检测

## 摘要（原文）

> Graph Neural Networks (GNNs) are emerging as powerful tools for nonlinear Model Order Reduction (MOR) of time-dependent parameterized Partial Differential Equations (PDEs). However, existing methodologies struggle to combine geometric inductive biases with interpretable latent behavior, overlooking dynamics-driven features or disregarding spatial information. In this work, we address this gap by introducing Latent Dynamics Graph Convolutional Network (LD-GCN), a purely data-driven, encoder-free architecture that learns a global, low-dimensional representation of dynamical systems conditioned on external inputs and parameters. The temporal evolution is modeled in the latent space and advanced through time-stepping, allowing for time-extrapolation, and the trajectories are consistently decoded onto geometrically parameterized domains using a GNN. Our framework enhances interpretability by enabling the analysis of the reduced dynamics and supporting zero-shot prediction through latent interpolation. The methodology is mathematically validated via a universal approximation theorem for encoder-free architectures, and numerically tested on complex computational mechanics problems involving physical and geometric parameters, including the detection of bifurcating phenomena for Navier-Stokes equations. Code availability: https://github.com/lorenzotomada/ld-gcn-rom

