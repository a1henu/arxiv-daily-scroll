---
layout: default
title: AMIR-GRPO: Inducing Implicit Preference Signals into GRPO
---

# AMIR-GRPO: Inducing Implicit Preference Signals into GRPO
**arXiv**：[2601.03661v1](https://arxiv.org/abs/2601.03661) · [PDF](https://arxiv.org/pdf/2601.03661.pdf)  
**作者**：Amir Hossein Yari, Fajri Koto  

**一句话要点**：提出AMIR-GRPO以增强GRPO在复杂推理任务中的对齐效果

**关键词**：强化学习对齐, 大语言模型后训练, 组相对策略优化, 隐式偏好信号, 数学推理基准

## 3 点简述
- GRPO在推理任务中存在长度偏差、轨迹惩罚稀释和偏好信息丢弃问题
- AMIR-GRPO通过基于组内奖励排名的隐式对比正则器增强监督
- 在数学推理基准上表现优于GRPO，提升正确与错误推理链的区分度

## 摘要（原文）

> Reinforcement learning has become the primary paradigm for aligning large language models (LLMs) on complex reasoning tasks, with group relative policy optimization (GRPO) widely used in large-scale post-training. However, GRPO faces structural limitations in reasoning-heavy settings: sequence-level advantage normalization introduces systematic length bias, penalties for low-quality trajectories are diluted, and the scalar objective discards rich pairwise preference information embedded in within-group reward rankings. As a result, valuable supervision from costly rollouts remains underutilized.
>   We propose AMIR-GRPO, which augments GRPO with an implicit DPO-style contrastive regularizer constructed directly from intra-group reward rankings, requiring no additional annotations. This mechanism amplifies suppression of low-reward trajectories, attenuates response-level length bias, and transforms each rollout group into a denser set of supervision constraints. Across multiple mathematical reasoning benchmarks, AMIR-GRPO consistently outperforms strong GRPO baselines, yields clearer separation between correct and incorrect reasoning chains, and delivers broader coverage gains beyond the subset of instances solved by standard GRPO.

