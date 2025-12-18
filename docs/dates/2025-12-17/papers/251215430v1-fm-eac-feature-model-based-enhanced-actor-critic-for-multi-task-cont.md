---
layout: default
title: FM-EAC: Feature Model-based Enhanced Actor-Critic for Multi-Task Control in Dynamic Environments
---

# FM-EAC: Feature Model-based Enhanced Actor-Critic for Multi-Task Control in Dynamic Environments
**arXiv**：[2512.15430v1](https://arxiv.org/abs/2512.15430) · [PDF](https://arxiv.org/pdf/2512.15430.pdf)  
**作者**：Quanxi Zhou, Wencan Mao, Manabu Tsukada, John C. S. Lui, Yusheng Ji  

**一句话要点**：提出FM-EAC算法，结合模型与无模型强化学习，用于动态环境多任务控制。

**关键词**：强化学习, 多任务控制, 动态环境, 演员-评论家框架, 特征模型

## 3 点简述
- 核心问题：现有强化学习方法在跨任务和场景的迁移性方面存在不足。
- 方法要点：集成规划、行动和学习，采用基于特征的模型和增强的演员-评论家框架。
- 实验或效果：在城市和农业应用中模拟，性能优于多种先进方法，支持子网络定制。

## 摘要（原文）

> Model-based reinforcement learning (MBRL) and model-free reinforcement learning (MFRL) evolve along distinct paths but converge in the design of Dyna-Q [1]. However, modern RL methods still struggle with effective transferability across tasks and scenarios. Motivated by this limitation, we propose a generalized algorithm, Feature Model-Based Enhanced Actor-Critic (FM-EAC), that integrates planning, acting, and learning for multi-task control in dynamic environments. FM-EAC combines the strengths of MBRL and MFRL and improves generalizability through the use of novel feature-based models and an enhanced actor-critic framework. Simulations in both urban and agricultural applications demonstrate that FM-EAC consistently outperforms many state-of-the-art MBRL and MFRL methods. More importantly, different sub-networks can be customized within FM-EAC according to user-specific requirements.

