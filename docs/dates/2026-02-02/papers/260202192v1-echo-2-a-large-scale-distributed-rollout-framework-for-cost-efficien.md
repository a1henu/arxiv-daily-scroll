---
layout: default
title: ECHO-2: A Large Scale Distributed Rollout Framework for Cost-efficient Reinforcement Learning
---

# ECHO-2: A Large Scale Distributed Rollout Framework for Cost-efficient Reinforcement Learning
**arXiv**：[2602.02192v1](https://arxiv.org/abs/2602.02192) · [PDF](https://arxiv.org/pdf/2602.02192.pdf)  
**作者**：Jie Xiao, Meng Chen, Qingnan Ren, Song Jingwei, Jiaqi Huang, Yangshen Deng, Chris Tong, Wanyi Chen, Suli Wang, Ziqian Bi, Shuo Lu, Yiqun Duan, Lynn Ai, Eric Yang, Bill Shi  

**一句话要点**：提出ECHO-2分布式强化学习框架，以解决后训练中远程推理与策略传播延迟的成本效率问题。

**关键词**：强化学习后训练, 分布式rollout框架, 成本效率优化, 策略传播延迟, 广域网协调, 异构工作器激活

## 3 点简述
- 核心问题：分布式强化学习后训练中，远程推理资源协调与策略传播延迟影响成本效率。
- 方法要点：结合集中学习与分布式rollout，通过重叠生成、传播和训练，控制策略陈旧性参数。
- 实验或效果：在真实广域网带宽下，对4B和8B模型进行GRPO后训练，显著提升成本效率，保持奖励可比性。

## 摘要（原文）

> Reinforcement learning (RL) is a critical stage in post-training large language models (LLMs), involving repeated interaction between rollout generation, reward evaluation, and centralized learning. Distributing rollout execution offers opportunities to leverage more cost-efficient inference resources, but introduces challenges in wide-area coordination and policy dissemination. We present ECHO-2, a distributed RL framework for post-training with remote inference workers and non-negligible dissemination latency. ECHO-2 combines centralized learning with distributed rollouts and treats bounded policy staleness as a user-controlled parameter, enabling rollout generation, dissemination, and training to overlap. We introduce an overlap-based capacity model that relates training time, dissemination latency, and rollout throughput, yielding a practical provisioning rule for sustaining learner utilization. To mitigate dissemination bottlenecks and lower cost, ECHO-2 employs peer-assisted pipelined broadcast and cost-aware activation of heterogeneous workers. Experiments on GRPO post-training of 4B and 8B models under real wide-area bandwidth regimes show that ECHO-2 significantly improves cost efficiency while preserving RL reward comparable to strong baselines.

