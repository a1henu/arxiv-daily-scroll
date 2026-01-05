---
layout: default
title: IRPO: Scaling the Bradley-Terry Model via Reinforcement Learning
---

# IRPO: Scaling the Bradley-Terry Model via Reinforcement Learning
**arXiv**：[2601.00677v1](https://arxiv.org/abs/2601.00677) · [PDF](https://arxiv.org/pdf/2601.00677.pdf)  
**作者**：Haonan Song, Qingchen Xie, Huan Zhu, Feng Xiao, Luxi Xing, Fuzhen Li, Liu Kang, Feng Jiang, Zhiyong Zheng, Fan Yang  

**一句话要点**：提出IRPO框架，通过强化学习扩展Bradley-Terry模型以解决成对生成奖励模型的计算瓶颈。

**关键词**：生成奖励模型, 强化学习, Bradley-Terry模型, 计算效率, 点式评分, 策略优化

## 3 点简述
- 成对生成奖励模型在强化学习中存在O(n²)时间复杂度和额外计算开销的瓶颈。
- IRPO将Bradley-Terry模型融入GRPO，为每个响应生成点式评分，实现高效评估。
- 实验显示IRPO在多个基准上达到点式模型SOTA，性能媲美领先成对模型，并在后训练评估中显著超越。

## 摘要（原文）

> Generative Reward Models (GRMs) have attracted considerable research interest in reward modeling due to their interpretability, inference-time scalability, and potential for refinement through reinforcement learning (RL). However, widely used pairwise GRMs create a computational bottleneck when integrated with RL algorithms such as Group Relative Policy Optimization (GRPO). This bottleneck arises from two factors: (i) the O(n^2) time complexity of pairwise comparisons required to obtain relative scores, and (ii) the computational overhead of repeated sampling or additional chain-of-thought (CoT) reasoning to improve performance. To address the first factor, we propose Intergroup Relative Preference Optimization (IRPO), a novel RL framework that incorporates the well-established Bradley-Terry model into GRPO. By generating a pointwise score for each response, IRPO enables efficient evaluation of arbitrarily many candidates during RL training while preserving interpretability and fine-grained reward signals. Experimental results demonstrate that IRPO achieves state-of-the-art (SOTA) performance among pointwise GRMs across multiple benchmarks, with performance comparable to that of current leading pairwise GRMs. Furthermore, we show that IRPO significantly outperforms pairwise GRMs in post-training evaluations.

