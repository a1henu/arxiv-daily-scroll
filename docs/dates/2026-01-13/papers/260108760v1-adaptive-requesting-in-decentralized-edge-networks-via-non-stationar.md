---
layout: default
title: Adaptive Requesting in Decentralized Edge Networks via Non-Stationary Bandits
---

# Adaptive Requesting in Decentralized Edge Networks via Non-Stationary Bandits
**arXiv**：[2601.08760v1](https://arxiv.org/abs/2601.08760) · [PDF](https://arxiv.org/pdf/2601.08760.pdf)  
**作者**：Yi Zhuang, Kun Yang, Xingran Chen  

**一句话要点**：提出AGING BANDIT WITH ADAPTIVE RESET算法以优化去中心化边缘网络中时间敏感客户端的信息新鲜度

**关键词**：去中心化边缘网络, 信息新鲜度优化, 非平稳多臂老虎机, 自适应算法, 协作请求

## 3 点简述
- 研究去中心化协作请求问题，优化边缘网络中客户端的信息新鲜度，建模为非平稳多臂老虎机
- 提出结合自适应窗口和周期性监控的算法，跟踪奖励分布变化，理论证明近优性能
- 通过仿真验证理论结果，算法在非平稳和部分可观测环境下有效

## 摘要（原文）

> We study a decentralized collaborative requesting problem that aims to optimize the information freshness of time-sensitive clients in edge networks consisting of multiple clients, access nodes (ANs), and servers. Clients request content through ANs acting as gateways, without observing AN states or the actions of other clients. We define the reward as the age of information reduction resulting from a client's selection of an AN, and formulate the problem as a non-stationary multi-armed bandit. In this decentralized and partially observable setting, the resulting reward process is history-dependent and coupled across clients, and exhibits both abrupt and gradual changes in expected rewards, rendering classical bandit-based approaches ineffective. To address these challenges, we propose the AGING BANDIT WITH ADAPTIVE RESET algorithm, which combines adaptive windowing with periodic monitoring to track evolving reward distributions. We establish theoretical performance guarantees showing that the proposed algorithm achieves near-optimal performance, and we validate the theoretical results through simulations.

