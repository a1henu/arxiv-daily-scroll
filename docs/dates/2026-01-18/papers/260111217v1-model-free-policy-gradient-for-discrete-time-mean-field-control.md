---
layout: default
title: Model-free policy gradient for discrete-time mean-field control
---

# Model-free policy gradient for discrete-time mean-field control
**arXiv**：[2601.11217v1](https://arxiv.org/abs/2601.11217) · [PDF](https://arxiv.org/pdf/2601.11217.pdf)  
**作者**：Matthieu Meunier, Huyên Pham, Christoph Reisinger  

**一句话要点**：提出模型无关策略梯度方法MF-REINFORCE，用于解决离散时间平均场控制问题。

**关键词**：平均场控制, 策略梯度, 模型无关学习, 离散时间系统, 状态分布扰动

## 3 点简述
- 研究离散时间平均场控制问题，状态空间有限、动作空间紧致，策略方法未充分探索。
- 引入状态分布流扰动方案，构建模型无关梯度估计器，基于模拟轨迹和分布敏感性。
- 开发MF-REINFORCE算法，建立偏差和均方误差定量界，数值实验验证有效性。

## 摘要（原文）

> We study model-free policy learning for discrete-time mean-field control (MFC) problems with finite state space and compact action space. In contrast to the extensive literature on value-based methods for MFC, policy-based approaches remain largely unexplored due to the intrinsic dependence of transition kernels and rewards on the evolving population state distribution, which prevents the direct use of likelihood-ratio estimators of policy gradients from classical single-agent reinforcement learning. We introduce a novel perturbation scheme on the state-distribution flow and prove that the gradient of the resulting perturbed value function converges to the true policy gradient as the perturbation magnitude vanishes. This construction yields a fully model-free estimator based solely on simulated trajectories and an auxiliary estimate of the sensitivity of the state distribution. Building on this framework, we develop MF-REINFORCE, a model-free policy gradient algorithm for MFC, and establish explicit quantitative bounds on its bias and mean-squared error. Numerical experiments on representative mean-field control tasks demonstrate the effectiveness of the proposed approach.

