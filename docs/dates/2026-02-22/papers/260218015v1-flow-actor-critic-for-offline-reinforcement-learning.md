---
layout: default
title: Flow Actor-Critic for Offline Reinforcement Learning
---

# Flow Actor-Critic for Offline Reinforcement Learning
**arXiv**：[2602.18015v1](https://arxiv.org/abs/2602.18015) · [PDF](https://arxiv.org/pdf/2602.18015.pdf)  
**作者**：Jongseong Chae, Jongeui Park, Yongjae Shin, Gyeongmin Kim, Seungyul Han, Youngchul Sung  

**一句话要点**：提出Flow Actor-Critic方法，基于流模型处理离线强化学习中复杂多模态数据集。

**关键词**：离线强化学习, 流模型, 演员-评论家方法, 多模态分布, 保守评论家, 基准测试

## 3 点简述
- 离线强化学习中数据集分布复杂多模态，需表达性强的策略超越高斯策略。
- 方法联合使用流模型于演员和保守评论家获取，防止数据外区域Q值爆炸。
- 在D4RL和OGBench基准测试中实现新的最先进性能。

## 摘要（原文）

> The dataset distributions in offline reinforcement learning (RL) often exhibit complex and multi-modal distributions, necessitating expressive policies to capture such distributions beyond widely-used Gaussian policies. To handle such complex and multi-modal datasets, in this paper, we propose Flow Actor-Critic, a new actor-critic method for offline RL, based on recent flow policies. The proposed method not only uses the flow model for actor as in previous flow policies but also exploits the expressive flow model for conservative critic acquisition to prevent Q-value explosion in out-of-data regions. To this end, we propose a new form of critic regularizer based on the flow behavior proxy model obtained as a byproduct of flow-based actor design. Leveraging the flow model in this joint way, we achieve new state-of-the-art performance for test datasets of offline RL including the D4RL and recent OGBench benchmarks.

