---
layout: default
title: Reverse Flow Matching: A Unified Framework for Online Reinforcement Learning with Diffusion and Flow Policies
---

# Reverse Flow Matching: A Unified Framework for Online Reinforcement Learning with Diffusion and Flow Policies
**arXiv**：[2601.08136v1](https://arxiv.org/abs/2601.08136) · [PDF](https://arxiv.org/pdf/2601.08136.pdf)  
**作者**：Zeyang Li, Sunbochen Tang, Navid Azizan  

**一句话要点**：提出反向流匹配框架，统一在线强化学习中扩散与流策略的训练方法。

**关键词**：在线强化学习, 扩散策略, 流策略, 方差减少, 统一框架, 连续控制

## 3 点简述
- 核心问题：在线强化学习缺乏目标分布样本，训练扩散与流策略效率低。
- 方法要点：基于后验均值估计，引入Langevin Stein算子构建低方差估计器。
- 实验或效果：在连续控制基准测试中，流策略性能优于扩散策略基线。

## 摘要（原文）

> Diffusion and flow policies are gaining prominence in online reinforcement learning (RL) due to their expressive power, yet training them efficiently remains a critical challenge. A fundamental difficulty in online RL is the lack of direct samples from the target distribution; instead, the target is an unnormalized Boltzmann distribution defined by the Q-function. To address this, two seemingly distinct families of methods have been proposed for diffusion policies: a noise-expectation family, which utilizes a weighted average of noise as the training target, and a gradient-expectation family, which employs a weighted average of Q-function gradients. Yet, it remains unclear how these objectives relate formally or if they can be synthesized into a more general formulation. In this paper, we propose a unified framework, reverse flow matching (RFM), which rigorously addresses the problem of training diffusion and flow models without direct target samples. By adopting a reverse inferential perspective, we formulate the training target as a posterior mean estimation problem given an intermediate noisy sample. Crucially, we introduce Langevin Stein operators to construct zero-mean control variates, deriving a general class of estimators that effectively reduce importance sampling variance. We show that existing noise-expectation and gradient-expectation methods are two specific instances within this broader class. This unified view yields two key advancements: it extends the capability of targeting Boltzmann distributions from diffusion to flow policies, and enables the principled combination of Q-value and Q-gradient information to derive an optimal, minimum-variance estimator, thereby improving training efficiency and stability. We instantiate RFM to train a flow policy in online RL, and demonstrate improved performance on continuous-control benchmarks compared to diffusion policy baselines.

