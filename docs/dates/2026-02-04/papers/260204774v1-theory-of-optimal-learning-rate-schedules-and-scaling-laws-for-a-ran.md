---
layout: default
title: Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model
---

# Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model
**arXiv**：[2602.04774v1](https://arxiv.org/abs/2602.04774) · [PDF](https://arxiv.org/pdf/2602.04774.pdf)  
**作者**：Blake Bordelon, Francesco Mori  

**一句话要点**：提出随机特征模型的最优学习率调度理论，揭示易难两相中的多项式衰减与预热稳定衰减模式。

**关键词**：最优学习率调度, 随机特征模型, 随机梯度下降, 缩放定律, 最优控制, 训练动态

## 3 点简述
- 研究随机特征模型在SGD训练中的最优学习率调度问题，避免经验性调参。
- 使用最优控制方法分析易相和难相，分别得出多项式衰减和预热稳定衰减的调度形式。
- 理论预测计算最优缩放定律，并在简单实验设置中验证优于恒定和幂律基准。

## 摘要（原文）

> Setting the learning rate for a deep learning model is a critical part of successful training, yet choosing this hyperparameter is often done empirically with trial and error. In this work, we explore a solvable model of optimal learning rate schedules for a powerlaw random feature model trained with stochastic gradient descent (SGD). We consider the optimal schedule $η_T^\star(t)$ where $t$ is the current iterate and $T$ is the total training horizon. This schedule is computed both numerically and analytically (when possible) using optimal control methods. Our analysis reveals two regimes which we term the easy phase and hard phase. In the easy phase the optimal schedule is a polynomial decay $η_T^\star(t) \simeq T^{-ξ} (1-t/T)^δ$ where $ξ$ and $δ$ depend on the properties of the features and task. In the hard phase, the optimal schedule resembles warmup-stable-decay with constant (in $T$) initial learning rate and annealing performed over a vanishing (in $T$) fraction of training steps. We investigate joint optimization of learning rate and batch size, identifying a degenerate optimality condition. Our model also predicts the compute-optimal scaling laws (where model size and training steps are chosen optimally) in both easy and hard regimes. Going beyond SGD, we consider optimal schedules for the momentum $β(t)$, where speedups in the hard phase are possible. We compare our optimal schedule to various benchmarks in our task including (1) optimal constant learning rates $η_T(t) \sim T^{-ξ}$ (2) optimal power laws $η_T(t) \sim T^{-ξ} t^{-χ}$, finding that our schedule achieves better rates than either of these. Our theory suggests that learning rate transfer across training horizon depends on the structure of the model and task. We explore these ideas in simple experimental pretraining setups.

