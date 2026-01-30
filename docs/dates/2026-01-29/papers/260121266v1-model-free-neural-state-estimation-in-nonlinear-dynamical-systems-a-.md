---
layout: default
title: Model-Free Neural State Estimation in Nonlinear Dynamical Systems: A Comparative Study of Neural Architectures and Classical Filters
---

# Model-Free Neural State Estimation in Nonlinear Dynamical Systems: A Comparative Study of Neural Architectures and Classical Filters
**arXiv**：[2601.21266v1](https://arxiv.org/abs/2601.21266) · [PDF](https://arxiv.org/pdf/2601.21266.pdf)  
**作者**：Zhuochen Liu, Hans Walker, Rahul Jain  

**一句话要点**：比较无模型神经网络与经典滤波器在非线性系统中的状态估计性能

**关键词**：状态估计, 非线性动态系统, 无模型学习, 神经网络架构, 经典滤波器, 推理吞吐量

## 3 点简述
- 核心问题：神经网络在非线性动态系统中是否作为原则性滤波器行为，缺乏系统模型知识
- 方法要点：系统比较Transformer、状态空间网络、循环架构与粒子滤波、非线性卡尔曼滤波
- 实验或效果：状态空间模型接近强非线性卡尔曼滤波性能，推理吞吐量显著更高

## 摘要（原文）

> Neural network models are increasingly used for state estimation in control and decision-making problems, yet it remains unclear to what extent they behave as principled filters in nonlinear dynamical systems. Unlike classical filters, which rely on explicit knowledge of system dynamics and noise models, neural estimators can be trained purely from data without access to the underlying system equations. In this work, we present a systematic empirical comparison between such model-free neural network models and classical filtering methods across multiple nonlinear scenarios. Our study evaluates Transformer-based models, state-space neural networks, and recurrent architectures alongside particle filters and nonlinear Kalman filters. The results show that neural models (in particular, state-space models (SSMs)) achieve state estimation performance that approaches strong nonlinear Kalman filters in nonlinear scenarios and outperform weaker classical baselines despite lacking access to system models, while also attaining substantially higher inference throughput.

