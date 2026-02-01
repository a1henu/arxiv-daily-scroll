---
layout: default
title: RecNet: Self-Evolving Preference Propagation for Agentic Recommender Systems
---

# RecNet: Self-Evolving Preference Propagation for Agentic Recommender Systems
**arXiv**：[2601.21609v1](https://arxiv.org/abs/2601.21609) · [PDF](https://arxiv.org/pdf/2601.21609.pdf)  
**作者**：Bingqian Li, Xiaolei Wang, Junyi Li, Weitao Li, Long Zhang, Sheng Chen, Wayne Xin Zhao, Ji-Rong Wen  

**一句话要点**：提出RecNet框架以解决推荐系统中实时偏好传播的稀疏与噪声问题

**关键词**：智能推荐系统, 偏好传播, 多智能体强化学习, 实时更新, 个性化过滤

## 3 点简述
- 核心问题：现有方法依赖稀疏、噪声的显式交互，无法建模用户与物品间的实时相互影响
- 方法要点：通过前向偏好路由与后向反馈优化，实现自演化的实时偏好传播
- 实验或效果：多场景实验验证了RecNet在建模偏好传播方面的有效性

## 摘要（原文）

> Agentic recommender systems leverage Large Language Models (LLMs) to model complex user behaviors and support personalized decision-making. However, existing methods primarily model preference changes based on explicit user-item interactions, which are sparse, noisy, and unable to reflect the real-time, mutual influences among users and items. To address these limitations, we propose RecNet, a self-evolving preference propagation framework that proactively propagates real-time preference updates across related users and items. RecNet consists of two complementary phases. In the forward phase, the centralized preference routing mechanism leverages router agents to integrate preference updates and dynamically propagate them to the most relevant agents. To ensure accurate and personalized integration of propagated preferences, we further introduce a personalized preference reception mechanism, which combines a message buffer for temporary caching and an optimizable, rule-based filter memory to guide selective preference assimilation based on past experience and interests. In the backward phase, the feedback-driven propagation optimization mechanism simulates a multi-agent reinforcement learning framework, using LLMs for credit assignment, gradient analysis, and module-level optimization, enabling continuous self-evolution of propagation strategies. Extensive experiments on various scenarios demonstrate the effectiveness of RecNet in modeling preference propagation for recommender systems.

