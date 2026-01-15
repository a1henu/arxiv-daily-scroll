---
layout: default
title: SRT: Accelerating Reinforcement Learning via Speculative Rollout with Tree-Structured Cache
---

# SRT: Accelerating Reinforcement Learning via Speculative Rollout with Tree-Structured Cache
**arXiv**：[2601.09083v1](https://arxiv.org/abs/2601.09083) · [PDF](https://arxiv.org/pdf/2601.09083.pdf)  
**作者**：Chi-Chih Chang, Siqi Zhu, Zhichen Zeng, Haibin Lin, Jiaxuan You, Mohamed S. Abdelfattah, Ziheng Jiang, Xuehai Qian  

**一句话要点**：提出SRT方法，通过树结构缓存加速语言模型强化学习，不牺牲分布正确性。

**关键词**：强化学习加速, 推测解码, 树结构缓存, 语言模型训练, 在线更新

## 3 点简述
- 核心问题：强化学习中rollout生成慢，影响训练效率。
- 方法要点：利用历史rollout相似性，构建每提示树缓存进行推测解码。
- 实验或效果：集成标准RL流程，降低延迟和推理成本，加速达2.08倍。

## 摘要（原文）

> We present Speculative Rollout with Tree-Structured Cache (SRT), a simple, model-free approach to accelerate on-policy reinforcement learning (RL) for language models without sacrificing distributional correctness. SRT exploits the empirical similarity of rollouts for the same prompt across training steps by storing previously generated continuations in a per-prompt tree-structured cache. During generation, the current policy uses this tree as the draft model for performing speculative decoding. To keep the cache fresh and improve draft model quality, SRT updates trees online from ongoing rollouts and proactively performs run-ahead generation during idle GPU bubbles. Integrated into standard RL pipelines (\textit{e.g.}, PPO, GRPO and DAPO) and multi-turn settings, SRT consistently reduces generation and step latency and lowers per-token inference cost, achieving up to 2.08x wall-clock time speedup during rollout.

