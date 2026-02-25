---
layout: default
title: Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training
---

# Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training
**arXiv**：[2602.20532v1](https://arxiv.org/abs/2602.20532) · [PDF](https://arxiv.org/pdf/2602.20532.pdf)  
**作者**：Zhengyao Gu, Jonathan Light, Raul Astudillo, Ziyu Ye, Langzhou He, Henry Peng Zou, Wei Cheng, Santiago Paternain, Philip S. Yu, Yisong Yue  

**一句话要点**：提出Actor-Curator框架，通过策略改进多臂老虎机实现自适应课程学习，用于大规模语言模型强化学习后训练。

**关键词**：课程学习, 强化学习后训练, 多臂老虎机, 大规模语言模型, 自适应训练, 策略优化

## 3 点简述
- 核心问题：大规模基础模型强化学习后训练依赖异构数据集，课程学习面临挑战。
- 方法要点：设计神经策展人动态选择训练问题，基于在线随机镜像下降优化策略性能提升。
- 实验或效果：在多个推理基准上优于均匀采样和基线，提升训练稳定性和效率，速度最高达80%。

## 摘要（原文）

> Post-training large foundation models with reinforcement learning typically relies on massive and heterogeneous datasets, making effective curriculum learning both critical and challenging. In this work, we propose ACTOR-CURATOR, a scalable and fully automated curriculum learning framework for reinforcement learning post-training of large language models (LLMs). ACTOR-CURATOR learns a neural curator that dynamically selects training problems from large problem banks by directly optimizing for expected policy performance improvement. We formulate problem selection as a non-stationary stochastic bandit problem, derive a principled loss function based on online stochastic mirror descent, and establish regret guarantees under partial feedback. Empirically, ACTOR-CURATOR consistently outperforms uniform sampling and strong curriculum baselines across a wide range of challenging reasoning benchmarks, demonstrating improved training stability and efficiency. Notably, it achieves relative gains of 28.6% on AIME2024 and 30.5% on ARC-1D over the strongest baseline and up to 80% speedup. These results suggest that ACTOR-CURATOR is a powerful and practical approach for scalable LLM post-training.

