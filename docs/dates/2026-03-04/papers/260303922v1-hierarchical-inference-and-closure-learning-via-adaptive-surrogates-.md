---
layout: default
title: Hierarchical Inference and Closure Learning via Adaptive Surrogates for ODEs and PDEs
---

# Hierarchical Inference and Closure Learning via Adaptive Surrogates for ODEs and PDEs
**arXiv**：[2603.03922v1](https://arxiv.org/abs/2603.03922) · [PDF](https://arxiv.org/pdf/2603.03922.pdf)  
**作者**：Pengyu Zhang, Arnaud Vadeboncoeur, Alex Glyn-Davies, Mark Girolami  

**一句话要点**：提出分层推理与闭包学习方法，通过自适应代理模型解决ODE/PDE逆问题

**关键词**：逆问题求解, 分层贝叶斯推理, 闭包学习, 代理模型优化, ODE/PDE建模, 神经网络嵌入

## 3 点简述
- 核心问题：处理物理系统参数未知和动态规律不完整的逆问题，需联合估计参数并学习共享闭包模型
- 方法要点：采用分层贝叶斯框架进行稳健推理，嵌入神经网络学习闭包，并引入双层优化策略训练代理模型以降低计算成本
- 实验或效果：评估了傅里叶神经算子和参数化物理信息神经网络等代理架构，利用集成MALA算法实现高效采样

## 摘要（原文）

> Inverse problems are the task of calibrating models to match data. They play a pivotal role in diverse engineering applications by allowing practitioners to align models with reality. In many applications, engineers and scientists do not have a complete picture of i) the detailed properties of a system (such as material properties, geometry, initial conditions, etc.); ii) the complete laws describing all dynamics at play (such as friction laws, complicated damping phenomena, and general nonlinear interactions). In this paper, we develop a principled methodology for leveraging data from collections of distinct yet related physical systems to jointly estimate the individual model parameters of each system, and learn the shared unknown dynamics in the form of an ML-based closure model. To robustly infer the unknown parameters for each system, we employ a hierarchical Bayesian framework, which allows for the joint inference of multiple systems and their population-level statistics. To learn the closures, we use a maximum marginal likelihood estimate of a neural network embeded within the ODE/PDE formulation of the problem. To realize this framework we utilize the ensemble Metropolis-Adjusted Langevin Algorithm (MALA) for stable and efficient sampling. To mitigate the computational bottleneck of repetitive forward evaluations in solving inverse problems, we introduce a bilevel optimization strategy to simultaneously train a surrogate forward model alongside the inference. Within this framework, we evaluate and compare distinct surrogate architectures, specifically Fourier Neural Operators (FNO) and parametric Physics-Informed Neural Network (PINNs).

