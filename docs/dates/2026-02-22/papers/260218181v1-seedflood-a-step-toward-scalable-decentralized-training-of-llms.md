---
layout: default
title: SeedFlood: A Step Toward Scalable Decentralized Training of LLMs
---

# SeedFlood: A Step Toward Scalable Decentralized Training of LLMs
**arXiv**：[2602.18181v1](https://arxiv.org/abs/2602.18181) · [PDF](https://arxiv.org/pdf/2602.18181.pdf)  
**作者**：Jihun Kim, Namhoon Lee  

**一句话要点**：提出SeedFlood方法以解决去中心化训练中通信开销随模型规模增长的问题

**关键词**：去中心化训练, 通信效率, 零阶优化, 大语言模型, 网络拓扑

## 3 点简述
- 核心问题：传统基于gossip的方法通信成本随模型大小增加，且网络跳数导致信息衰减，影响全局共识效率。
- 方法要点：利用零阶更新的种子可重构结构，使消息大小接近零，通过泛洪传播实现通信开销与模型规模无关。
- 实验或效果：在去中心化LLM微调实验中，SeedFlood在泛化性能和通信效率上优于基线，大规模设置下结果接近一阶方法。

## 摘要（原文）

> This work presents a new approach to decentralized training-SeedFlood-designed to scale for large models across complex network topologies and achieve global consensus with minimal communication overhead. Traditional gossip-based methods suffer from message communication costs that grow with model size, while information decay over network hops renders global consensus inefficient. SeedFlood departs from these practices by exploiting the seed-reconstructible structure of zeroth-order updates and effectively making the messages near-zero in size, allowing them to be flooded to every client in the network. This mechanism makes communication overhead negligible and independent of model size, removing the primary scalability bottleneck in decentralized training. Consequently, SeedFlood enables training in regimes previously considered impractical, such as billion-parameter models distributed across hundreds of clients. Our experiments on decentralized LLM fine-tuning demonstrate thatSeedFlood consistently outperforms gossip-based baselines in both generalization performance and communication efficiency, and even achieves results comparable to first-order methods in large scale settings.

