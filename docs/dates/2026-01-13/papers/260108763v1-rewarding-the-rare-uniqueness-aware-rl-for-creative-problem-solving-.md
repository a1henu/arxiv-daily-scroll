---
layout: default
title: Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs
---

# Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs
**arXiv**：[2601.08763v1](https://arxiv.org/abs/2601.08763) · [PDF](https://arxiv.org/pdf/2601.08763.pdf)  
**作者**：Zhiyuan Hu, Yucheng Wang, Yufei He, Jiaying Wu, Yilun Zhao, See-Kiong Ng, Cynthia Breazeal, Anh Tuan Luu, Hae Won Park, Bryan Hooi  

**一句话要点**：提出独特性感知强化学习，以解决大语言模型在复杂推理任务中的探索崩溃问题。

**关键词**：强化学习, 大语言模型, 探索崩溃, 解决方案多样性, 推理任务, 独特性奖励

## 3 点简述
- 核心问题：强化学习后训练大语言模型时，探索崩溃导致策略过早集中于少数主导推理模式，限制解决方案多样性。
- 方法要点：基于LLM的评判器聚类解决方案策略，按聚类大小反比加权策略优势，奖励罕见正确策略。
- 实验或效果：在数学、物理和医学推理基准上，提升pass@k和AUC@K，维持pass@1，增加解决方案多样性。

## 摘要（原文）

> Reinforcement learning (RL) has become a central paradigm for post-training large language models (LLMs), particularly for complex reasoning tasks, yet it often suffers from exploration collapse: policies prematurely concentrate on a small set of dominant reasoning patterns, improving pass@1 while limiting rollout-level diversity and gains in pass@k. We argue that this failure stems from regularizing local token behavior rather than diversity over sets of solutions. To address this, we propose Uniqueness-Aware Reinforcement Learning, a rollout-level objective that explicitly rewards correct solutions that exhibit rare high-level strategies. Our method uses an LLM-based judge to cluster rollouts for the same problem according to their high-level solution strategies, ignoring superficial variations, and reweights policy advantages inversely with cluster size. As a result, correct but novel strategies receive higher rewards than redundant ones. Across mathematics, physics, and medical reasoning benchmarks, our approach consistently improves pass@$k$ across large sampling budgets and increases the area under the pass@$k$ curve (AUC@$K$) without sacrificing pass@1, while sustaining exploration and uncovering more diverse solution strategies at scale.

