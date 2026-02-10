---
layout: default
title: Contextual Rollout Bandits for Reinforcement Learning with Verifiable Rewards
---

# Contextual Rollout Bandits for Reinforcement Learning with Verifiable Rewards
**arXiv**：[2602.08499v1](https://arxiv.org/abs/2602.08499) · [PDF](https://arxiv.org/pdf/2602.08499.pdf)  
**作者**：Xiaodong Lu, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Zhijun Chen, Yu Luo, Fuzhen Zhuang, Yikun Ban, Deqing Wang  

**一句话要点**：提出上下文滚动老虎机框架，以优化可验证奖励强化学习中的滚动调度问题。

**关键词**：可验证奖励强化学习, 上下文老虎机, 滚动调度, 样本效率, 数学推理, 策略优化

## 3 点简述
- 现有RLVR方法滚动使用无差别且短视，导致监督噪声大、样本效率低。
- 将滚动调度建模为上下文老虎机问题，自适应选择高价值滚动以提升性能。
- 在六个数学推理基准上验证了性能与训练效率的显著提升。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is an effective paradigm for improving the reasoning capabilities of large language models. However, existing RLVR methods utilize rollouts in an indiscriminate and short-horizon manner: responses of heterogeneous quality within each prompt are treated uniformly, and historical rollouts are discarded after a single use. This leads to noisy supervision, poor sample efficiency, and suboptimal policy updates. We address these issues by formulating rollout scheduling in RLVR as a contextual bandit problem and proposing a unified neural scheduling framework that adaptively selects high-value rollouts throughout training. Each rollout is treated as an arm whose reward is defined by the induced performance gain between consecutive optimization steps. The resulting scheduler supports both noise-aware intra-group selection and adaptive global reuse of historical rollouts within a single principled framework. We provide theoretical justification by deriving sublinear regret bounds and showing that enlarging the rollout buffer improves the achievable performance upper bound. Experiments on six mathematical reasoning benchmarks demonstrate consistent gains in performance and training efficiency across multiple RLVR optimization methods.

