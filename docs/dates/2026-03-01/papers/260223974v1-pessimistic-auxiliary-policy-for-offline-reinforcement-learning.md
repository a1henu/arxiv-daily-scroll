---
layout: default
title: Pessimistic Auxiliary Policy for Offline Reinforcement Learning
---

# Pessimistic Auxiliary Policy for Offline Reinforcement Learning
**arXiv**：[2602.23974v1](https://arxiv.org/abs/2602.23974) · [PDF](https://arxiv.org/pdf/2602.23974.pdf)  
**作者**：Fan Zhang, Baoru Huang, Xin Zhang  

**一句话要点**：提出悲观辅助策略以缓解离线强化学习中的误差累积问题

**关键词**：离线强化学习, 悲观策略, 误差累积, 置信下界, 分布外动作

## 3 点简述
- 离线强化学习中，分布外动作导致近似误差累积和过高估计
- 通过最大化Q函数置信下界构建悲观辅助策略，采样可靠动作
- 实验表明该策略能有效提升其他离线RL方法的性能

## 摘要（原文）

> Offline reinforcement learning aims to learn an agent from pre-collected datasets, avoiding unsafe and inefficient real-time interaction. However, inevitable access to out-ofdistribution actions during the learning process introduces approximation errors, causing the error accumulation and considerable overestimation. In this paper, we construct a new pessimistic auxiliary policy for sampling reliable actions. Specifically, we develop a pessimistic auxiliary strategy by maximizing the lower confidence bound of the Q-function. The pessimistic auxiliary strategy exhibits a relatively high value and low uncertainty in the vicinity of the learned policy, avoiding the learned policy sampling high-value actions with potentially high errors during the learning process. Less approximation error introduced by sampled action from pessimistic auxiliary strategy leads to the alleviation of error accumulation. Extensive experiments on offline reinforcement learning benchmarks reveal that utilizing the pessimistic auxiliary strategy can effectively improve the efficacy of other offline RL approaches.

