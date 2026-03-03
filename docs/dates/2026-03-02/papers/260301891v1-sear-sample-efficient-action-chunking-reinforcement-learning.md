---
layout: default
title: SEAR: Sample Efficient Action Chunking Reinforcement Learning
---

# SEAR: Sample Efficient Action Chunking Reinforcement Learning
**arXiv**：[2603.01891v1](https://arxiv.org/abs/2603.01891) · [PDF](https://arxiv.org/pdf/2603.01891.pdf)  
**作者**：C. F. Maximilian Nagy, Onur Celik, Emiliyan Gospodinov, Florian Seligmann, Weiran Liao, Aryan Kaushik, Gerhard Neumann  

**一句话要点**：提出SEAR算法以解决在线强化学习中动作分块的数据效率问题

**关键词**：动作分块强化学习, 在线强化学习, 数据效率, 滚动时域控制, 长时程任务

## 3 点简述
- 动作分块在长时程强化学习中可提升探索和价值估计，但增加学习难度，现有方法在纯在线设置中表现不佳。
- SEAR利用动作块的时间结构，采用滚动时域策略，结合不同块大小的优势，实现高效在线学习。
- 在Metaworld基准测试中，SEAR优于现有在线强化学习方法，支持块大小达20的训练。

## 摘要（原文）

> Action chunking can improve exploration and value estimation in long horizon reinforcement learning, but makes learning substantially harder since the critic must evaluate action sequences rather than single actions, greatly increasing approximation and data efficiency challenges. As a result, existing action chunking methods, primarily designed for the offline and offline-to-online settings, have not achieved strong performance in purely online reinforcement learning. We introduce SEAR, an off policy online reinforcement learning algorithm for action chunking. It exploits the temporal structure of action chunks and operates with a receding horizon, effectively combining the benefits of small and large chunk sizes. SEAR outperforms state of the art online reinforcement learning methods on Metaworld, training with chunk sizes up to 20.

