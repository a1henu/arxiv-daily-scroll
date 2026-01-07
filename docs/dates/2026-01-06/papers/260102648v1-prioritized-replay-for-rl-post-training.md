---
layout: default
title: Prioritized Replay for RL Post-training
---

# Prioritized Replay for RL Post-training
**arXiv**：[2601.02648v1](https://arxiv.org/abs/2601.02648) · [PDF](https://arxiv.org/pdf/2601.02648.pdf)  
**作者**：Mehdi Fatemi  

**一句话要点**：提出基于问题级优先级的RL后训练框架，用于大语言模型GRPO后训练

**关键词**：强化学习后训练, 优先级回放, 大语言模型, GRPO, 课程学习, 自适应采样

## 3 点简述
- 核心问题：传统课程策略在RL后训练中可能无法有效选择提供强学习信号的问题
- 方法要点：基于经验成功率计算优先级分数，自动聚焦于中等成功率问题，无需预定义难度或外部标签
- 实验或效果：方法提供连续自适应优先级过程，通过堆采样和定期重测缓解饥饿和遗忘，提升训练效率

## 摘要（原文）

> We introduce a problem-level prioritization framework for RL post-training of large language models. Building on insights from prioritized replay in deep RL, as well as prior observations that rollouts with intermediate success rates tend to produce stronger learning signals under methods such as GRPO, our approach selects problems according to a simple, model-driven priority score derived from empirical success statistics. In contrast to conventional curriculum strategies that emphasize easier tasks early in training, the resulting schedule naturally focuses training on problems that are neither consistently solved nor consistently failed, while deprioritizing those that contribute little gradient information. The method yields a continuously adapting and automatic prioritization process that requires no predefined difficulty tiers, auxiliary predictors, or external labels. We further introduce lightweight mechanisms for practical deployment, including heap-based prioritized sampling and periodic retesting of solved and unsolved problems to mitigate starvation and forgetting. Overall, the approach offers a principled and scalable alternative to manually designed curricula while aligning data selection directly with the dynamics of GRPO-based post-training.

