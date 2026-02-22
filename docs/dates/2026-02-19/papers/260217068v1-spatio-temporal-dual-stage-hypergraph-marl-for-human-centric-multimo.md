---
layout: default
title: Spatio-temporal dual-stage hypergraph MARL for human-centric multimodal corridor traffic signal control
---

# Spatio-temporal dual-stage hypergraph MARL for human-centric multimodal corridor traffic signal control
**arXiv**：[2602.17068v1](https://arxiv.org/abs/2602.17068) · [PDF](https://arxiv.org/pdf/2602.17068.pdf)  
**作者**：Xiaocai Zhang, Neema Nassir, Milad Haghani  

**一句话要点**：提出STDSH-MARL框架，通过双阶段超图注意力机制优化多模态走廊交通信号控制

**关键词**：多智能体强化学习, 交通信号控制, 超图注意力, 时空依赖建模, 多模态出行, 公共交通优先

## 3 点简述
- 核心问题：走廊网络中交通信号控制需兼顾多模态出行者，特别是公共交通优先，而非仅关注车辆性能。
- 方法要点：采用集中训练分散执行的多智能体强化学习，引入双阶段超图注意力建模时空依赖，并设计混合离散动作空间。
- 实验或效果：在五种交通场景下测试，STDSH-MARL提升多模态性能，优于基线方法，消融研究确认时空超边是关键因素。

## 摘要（原文）

> Human-centric traffic signal control in corridor networks must increasingly account for multimodal travelers, particularly high-occupancy public transportation, rather than focusing solely on vehicle-centric performance. This paper proposes STDSH-MARL (Spatio-Temporal Dual-Stage Hypergraph based Multi-Agent Reinforcement Learning), a scalable multi-agent deep reinforcement learning framework that follows a centralized training and decentralized execution paradigm. The proposed method captures spatio-temporal dependencies through a novel dual-stage hypergraph attention mechanism that models interactions across both spatial and temporal hyperedges. In addition, a hybrid discrete action space is introduced to jointly determine the next signal phase configuration and its corresponding green duration, enabling more adaptive signal timing decisions. Experiments conducted on a corridor network under five traffic scenarios demonstrate that STDSH-MARL consistently improves multimodal performance and provides clear benefits for public transportation priority. Compared with state-of-the-art baseline methods, the proposed approach achieves superior overall performance. Further ablation studies confirm the contribution of each component of STDSH-MARL, with temporal hyperedges identified as the most influential factor driving the observed performance gains.

