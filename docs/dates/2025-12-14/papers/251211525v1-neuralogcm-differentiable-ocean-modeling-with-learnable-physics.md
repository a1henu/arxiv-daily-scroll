---
layout: default
title: NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics
---

# NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics
**arXiv**：[2512.11525v1](https://arxiv.org/abs/2512.11525) · [PDF](https://arxiv.org/pdf/2512.11525.pdf)  
**作者**：Hao Wu, Yuan Gao, Fan Xu, Fan Zhang, Guangliang Liu, Yuxuan Liang, Xiaomeng Huang  

**一句话要点**：提出NeuralOGCM框架，融合可微分编程与深度学习以解决海洋建模中计算效率与物理保真度的权衡问题。

**关键词**：可微分海洋建模, 学习物理, 深度学习校正, 科学计算, 端到端训练

## 3 点简述
- 核心问题：高精度科学模拟面临计算效率与物理保真度的长期权衡。
- 方法要点：结合可微分动力学求解器与深度神经网络，通过端到端训练优化物理参数并校正子网格过程。
- 实验或效果：模型保持长期稳定性和物理一致性，在速度和准确性上优于传统数值模型与纯AI基线。

## 摘要（原文）

> High-precision scientific simulation faces a long-standing trade-off between computational efficiency and physical fidelity. To address this challenge, we propose NeuralOGCM, an ocean modeling framework that fuses differentiable programming with deep learning. At the core of NeuralOGCM is a fully differentiable dynamical solver, which leverages physics knowledge as its core inductive bias. The learnable physics integration captures large-scale, deterministic physical evolution, and transforms key physical parameters (e.g., diffusion coefficients) into learnable parameters, enabling the model to autonomously optimize its physical core via end-to-end training. Concurrently, a deep neural network learns to correct for subgrid-scale processes and discretization errors not captured by the physics model. Both components work in synergy, with their outputs integrated by a unified ODE solver. Experiments demonstrate that NeuralOGCM maintains long-term stability and physical consistency, significantly outperforming traditional numerical models in speed and pure AI baselines in accuracy. Our work paves a new path for building fast, stable, and physically-plausible models for scientific computing.

