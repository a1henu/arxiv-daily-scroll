---
layout: default
title: A Model-Free Universal AI
---

# A Model-Free Universal AI
**arXiv**：[2602.23242v1](https://arxiv.org/abs/2602.23242) · [PDF](https://arxiv.org/pdf/2602.23242.pdf)  
**作者**：Yegon Kim, Juho Lee  

**一句话要点**：提出AIQI模型，首次在通用强化学习中实现无模型渐进最优性

**关键词**：通用强化学习, 无模型代理, 渐进最优性, 分布动作值函数, AIXI

## 3 点简述
- 核心问题：通用强化学习中现有最优代理均为基于模型，缺乏无模型方法
- 方法要点：AIQI通过分布动作值函数的通用归纳，替代传统策略或环境模型
- 实验或效果：在真实条件下证明AIQI具有渐进ε-最优性和贝叶斯最优性

## 摘要（原文）

> In general reinforcement learning, all established optimal agents, including AIXI, are model-based, explicitly maintaining and using environment models. This paper introduces Universal AI with Q-Induction (AIQI), the first model-free agent proven to be asymptotically $\varepsilon$-optimal in general RL. AIQI performs universal induction over distributional action-value functions, instead of policies or environments like previous works. Under a grain of truth condition, we prove that AIQI is strong asymptotically $\varepsilon$-optimal and asymptotically $\varepsilon$-Bayes-optimal. Our results significantly expand the diversity of known universal agents.

