---
layout: default
title: One Adapts to Any: Meta Reward Modeling for Personalized LLM Alignment
---

# One Adapts to Any: Meta Reward Modeling for Personalized LLM Alignment
**arXiv**：[2601.18731v1](https://arxiv.org/abs/2601.18731) · [PDF](https://arxiv.org/pdf/2601.18731.pdf)  
**作者**：Hongru Cai, Yongqi Li, Tiezheng Yu, Fengbin Zhu, Wenjie Wang, Fuli Feng, Wenjie Li  

**一句话要点**：提出元奖励建模以解决个性化大语言模型对齐中用户反馈稀缺和快速适应新用户的挑战。

**关键词**：个性化对齐, 元学习, 奖励建模, 大语言模型, 少样本适应

## 3 点简述
- 核心问题：个性化对齐依赖奖励模型，但面临用户反馈稀缺和适应新用户效率低的双重挑战。
- 方法要点：将个性化奖励建模重构为元学习问题，使用MAML框架优化基础奖励函数权重的初始化，并引入鲁棒个性化目标增强对难学习用户的关注。
- 实验或效果：在个性化偏好数据集上验证，MRM提升少样本个性化性能，改善用户鲁棒性，并优于基线方法。

## 摘要（原文）

> Alignment of Large Language Models (LLMs) aims to align outputs with human preferences, and personalized alignment further adapts models to individual users. This relies on personalized reward models that capture user-specific preferences and automatically provide individualized feedback. However, developing these models faces two critical challenges: the scarcity of feedback from individual users and the need for efficient adaptation to unseen users. We argue that addressing these constraints requires a paradigm shift from fitting data to learn user preferences to learn the process of preference adaptation. To realize this, we propose Meta Reward Modeling (MRM), which reformulates personalized reward modeling as a meta-learning problem. Specifically, we represent each user's reward model as a weighted combination of base reward functions, and optimize the initialization of these weights using a Model-Agnostic Meta-Learning (MAML)-style framework to support fast adaptation under limited feedback. To ensure robustness, we introduce the Robust Personalization Objective (RPO), which places greater emphasis on hard-to-learn users during meta optimization. Extensive experiments on personalized preference datasets validate that MRM enhances few-shot personalization, improves user robustness, and consistently outperforms baselines.

