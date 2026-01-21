---
layout: default
title: Reinforcement Learning for Opportunistic Routing in Software-Defined LEO-Terrestrial Systems
---

# Reinforcement Learning for Opportunistic Routing in Software-Defined LEO-Terrestrial Systems
**arXiv**：[2601.13662v1](https://arxiv.org/abs/2601.13662) · [PDF](https://arxiv.org/pdf/2601.13662.pdf)  
**作者**：Sivaram Krishnan, Zhouyou Gu, Jihong Park, Sung-Min Oh, Jinho Choi  

**一句话要点**：提出基于强化学习的机遇路由方法，以优化软件定义LEO-地面系统中的数据传输延迟。

**关键词**：机遇路由, 强化学习, 软件定义网络, 低地球轨道卫星, 数据传输延迟, 队列优化

## 3 点简述
- 核心问题：大规模LEO卫星网络在时变拓扑和间歇网关可见性下，需智能路由策略以降低数据传输延迟。
- 方法要点：利用GEO-SDN控制器全局控制，采用机遇路由和残差强化学习框架，优化数据包转发至可用地面网关。
- 实验或效果：多日轨道数据仿真显示，相比经典背压等算法，显著减少队列长度，提升传输性能。

## 摘要（原文）

> The proliferation of large-scale low Earth orbit (LEO) satellite constellations is driving the need for intelligent routing strategies that can effectively deliver data to terrestrial networks under rapidly time-varying topologies and intermittent gateway visibility. Leveraging the global control capabilities of a geostationary (GEO)-resident software-defined networking (SDN) controller, we introduce opportunistic routing, which aims to minimize delivery delay by forwarding packets to any currently available ground gateways rather than fixed destinations. This makes it a promising approach for achieving low-latency and robust data delivery in highly dynamic LEO networks. Specifically, we formulate a constrained stochastic optimization problem and employ a residual reinforcement learning framework to optimize opportunistic routing for reducing transmission delay. Simulation results over multiple days of orbital data demonstrate that our method achieves significant improvements in queue length reduction compared to classical backpressure and other well-known queueing algorithms.

