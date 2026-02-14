---
layout: default
title: Counterfactual Conditional Likelihood Rewards for Multiagent Exploration
---

# Counterfactual Conditional Likelihood Rewards for Multiagent Exploration
**arXiv**：[2602.11740v1](https://arxiv.org/abs/2602.11740) · [PDF](https://arxiv.org/pdf/2602.11740.pdf)  
**作者**：Ayhan Alp Aydeniz, Robert Loftin, Kagan Tumer  

**一句话要点**：提出反事实条件似然奖励以解决多智能体探索中的冗余问题

**关键词**：多智能体探索, 反事实奖励, 团队协调, 稀疏奖励, 连续域, 条件似然

## 3 点简述
- 核心问题：个体级探索在多智能体系统中易导致冗余，缺乏团队协调意识。
- 方法要点：CCL奖励通过反事实分析评估每个智能体对团队探索的独特贡献。
- 实验效果：在稀疏团队奖励的连续多智能体域中加速学习，尤其适用于紧密协调任务。

## 摘要（原文）

> Efficient exploration is critical for multiagent systems to discover coordinated strategies, particularly in open-ended domains such as search and rescue or planetary surveying. However, when exploration is encouraged only at the individual agent level, it often leads to redundancy, as agents act without awareness of how their teammates are exploring. In this work, we introduce Counterfactual Conditional Likelihood (CCL) rewards, which score each agent's exploration by isolating its unique contribution to team exploration. Unlike prior methods that reward agents solely for the novelty of their individual observations, CCL emphasizes observations that are informative with respect to the joint exploration of the team. Experiments in continuous multiagent domains show that CCL rewards accelerate learning for domains with sparse team rewards, where most joint actions yield zero rewards, and are particularly effective in tasks that require tight coordination among agents.

