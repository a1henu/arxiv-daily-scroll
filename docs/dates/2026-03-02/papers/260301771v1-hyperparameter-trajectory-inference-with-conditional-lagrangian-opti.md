---
layout: default
title: Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport
---

# Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport
**arXiv**：[2603.01771v1](https://arxiv.org/abs/2603.01771) · [PDF](https://arxiv.org/pdf/2603.01771.pdf)  
**作者**：Harry Amad, Mihaela van der Schaar  

**一句话要点**：提出基于条件拉格朗日最优传输的超参数轨迹推断方法，以应对部署后用户偏好变化导致的神经网络重训练问题。

**关键词**：超参数轨迹推断, 条件最优传输, 代理模型, 神经网络部署, 拉格朗日函数, 轨迹学习

## 3 点简述
- 核心问题：神经网络超参数在部署后可能因用户偏好变化而失效，重训练成本高。
- 方法要点：扩展轨迹推断至条件设置，通过条件拉格朗日最优传输学习超参数动态并构建代理模型。
- 实验或效果：在多种超参数谱上优于其他方法，能更好地重建神经网络输出。

## 摘要（原文）

> Neural networks (NNs) often have critical behavioural trade-offs that are set at design time with hyperparameters-such as reward weights in reinforcement learning or quantile targets in regression. Post-deployment, however, user preferences can evolve, making initial settings undesirable, necessitating potentially expensive retraining. To circumvent this, we introduce the task of Hyperparameter Trajectory Inference (HTI): to learn, from observed data, how a NN's conditional output distribution changes with its hyperparameters, and construct a surrogate model that approximates the NN at unobserved hyperparameter settings. HTI requires extending existing trajectory inference approaches to incorporate conditions, exacerbating the challenge of ensuring inferred paths are feasible. We propose an approach based on conditional Lagrangian optimal transport, jointly learning the Lagrangian function governing hyperparameter-induced dynamics along with the associated optimal transport maps and geodesics between observed marginals, which form the surrogate model. We incorporate inductive biases based on the manifold hypothesis and least-action principles into the learned Lagrangian, improving surrogate model feasibility. We empirically demonstrate that our approach reconstructs NN outputs across various hyperparameter spectra better than other alternatives.

