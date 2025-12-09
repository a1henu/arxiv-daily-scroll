---
layout: default
title: Model-Based Reinforcement Learning Under Confounding
---

# Model-Based Reinforcement Learning Under Confounding
**arXiv**：[2512.07528v1](https://arxiv.org/abs/2512.07528) · [PDF](https://arxiv.org/pdf/2512.07528.pdf)  
**作者**：Nishanth Venkatesh, Andreas A. Malikopoulos  

**一句话要点**：提出基于代理变量的近端离策略评估方法，以解决上下文未观测下的混淆模型强化学习问题。

**关键词**：模型强化学习, 混淆环境, 离策略评估, 代理变量, 最大因果熵, 上下文MDPs

## 3 点简述
- 研究上下文未观测的C-MDPs中，离线数据存在混淆导致传统模型学习不一致。
- 利用代理变量可逆性，识别混淆奖励期望，结合行为平均转移模型构建替代MDP。
- 该方法与最大因果熵框架兼容，支持在混淆环境中进行原则性模型学习和规划。

## 摘要（原文）

> We investigate model-based reinforcement learning in contextual Markov decision processes (C-MDPs) in which the context is unobserved and induces confounding in the offline dataset. In such settings, conventional model-learning methods are fundamentally inconsistent, as the transition and reward mechanisms generated under a behavioral policy do not correspond to the interventional quantities required for evaluating a state-based policy. To address this issue, we adapt a proximal off-policy evaluation approach that identifies the confounded reward expectation using only observable state-action-reward trajectories under mild invertibility conditions on proxy variables. When combined with a behavior-averaged transition model, this construction yields a surrogate MDP whose Bellman operator is well defined and consistent for state-based policies, and which integrates seamlessly with the maximum causal entropy (MaxCausalEnt) model-learning framework. The proposed formulation enables principled model learning and planning in confounded environments where contextual information is unobserved, unavailable, or impractical to collect.

