---
layout: default
title: Blockchain-Enabled Routing for Zero-Trust Low-Altitude Intelligent Networks
---

# Blockchain-Enabled Routing for Zero-Trust Low-Altitude Intelligent Networks
**arXiv**：[2602.23667v1](https://arxiv.org/abs/2602.23667) · [PDF](https://arxiv.org/pdf/2602.23667.pdf)  
**作者**：Ziye Jia, Sijie He, Ligang Yuan, Fuhui Zhou, Qihui Wu, Zhu Han, Dusit Niyato  

**一句话要点**：提出基于区块链和零信任架构的路由算法，以优化低空智能网络的安全与性能。

**关键词**：低空智能网络, 零信任架构, 区块链路由, 多智能体强化学习, 无人机安全, 端到端延迟优化

## 3 点简述
- 核心问题：低空智能网络中无人机的高移动性和分布式拓扑易受安全威胁，影响路由稳定性和数据传输性能。
- 方法要点：采用零信任架构结合软件定义边界和区块链技术管理身份与移动性，并设计多智能体深度强化学习算法优化端到端延迟和传输成功率。
- 实验或效果：仿真结果显示，相比基准方法，平均端到端延迟降低59%，传输成功率提升29%，并能更快识别低信任无人机。

## 摘要（原文）

> Due to the scalability and portability, low-altitude intelligent networks (LAINs) are essential in various fields such as surveillance and disaster rescue. However, in LAINs, unmanned aerial vehicles (UAVs) are characterized by the distributed topology and high mobility, thus vulnerable to security threats, which may degrade routing performances for data transmissions. Hence, how to ensure the routing stability and security of LAINs is challenging. In this paper, we focus on the routing with multiple UAV clusters in LAINs. To minimize the damage caused by potential threats, we present the zero-trust architecture with the software-defined perimeter and blockchain techniques to manage the identify and mobility of UAVs. Besides, we formulate the routing problem to optimize the end-to-end (E2E) delay and transmission success ratio (TSR) simultaneously, which is an integer nonlinear programming problem and intractable to solve. Therefore, we reformulate the problem into a decentralized partially observable Markov decision process. We design the multi-agent double deep Q-network-based routing algorithms to solve the problem, empowered by the soft-hierarchical experience replay buffer and prioritized experience replay mechanisms. Finally, extensive simulations are conducted and the numerical results demonstrate that the proposed framework reduces the average E2E delay by 59\% and improves the TSR by 29\% on average compared to benchmarks, while simultaneously enabling faster and more robust identification of low-trust UAVs.

