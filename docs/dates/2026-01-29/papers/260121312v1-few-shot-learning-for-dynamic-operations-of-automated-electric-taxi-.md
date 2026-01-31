---
layout: default
title: Few-Shot Learning for Dynamic Operations of Automated Electric Taxi Fleets under Evolving Charging Infrastructure: A Meta-Deep Reinforcement Learning Approach
---

# Few-Shot Learning for Dynamic Operations of Automated Electric Taxi Fleets under Evolving Charging Infrastructure: A Meta-Deep Reinforcement Learning Approach
**arXiv**：[2601.21312v1](https://arxiv.org/abs/2601.21312) · [PDF](https://arxiv.org/pdf/2601.21312.pdf)  
**作者**：Xiaozhuang Li, Xindi Tang, Fang He  

**一句话要点**：提出GAT-PEARL元强化学习框架，以解决动态充电基础设施下自动电动出租车车队运营问题。

**关键词**：元强化学习, 图注意力网络, 概率嵌入, 自动电动出租车, 动态充电基础设施, 少样本学习

## 3 点简述
- 核心问题：现有研究假设静态充电网络，与真实动态环境存在差距，影响自动电动出租车车队管理效率。
- 方法要点：结合图注意力网络提取空间表示，使用概率嵌入强化学习实现快速适应充电网络变化，无需重新训练。
- 实验或效果：基于成都真实数据模拟，GAT-PEARL优于传统强化学习基线，在未见基础设施布局中泛化能力强，提升动态运营效率。

## 摘要（原文）

> With the rapid expansion of electric vehicles (EVs) and charging infrastructure, the effective management of Autonomous Electric Taxi (AET) fleets faces a critical challenge in environments with dynamic and uncertain charging availability. While most existing research assumes a static charging network, this simplification creates a significant gap between theoretical models and real-world operations. To bridge this gap, we propose GAT-PEARL, a novel meta-reinforcement learning framework that learns an adaptive operational policy. Our approach integrates a graph attention network (GAT) to effectively extract robust spatial representations under infrastructure layouts and model the complex spatiotemporal relationships of the urban environment, and employs probabilistic embeddings for actor-critic reinforcement learning (PEARL) to enable rapid, inference-based adaptation to changes in charging network layouts without retraining. Through extensive simulations on real-world data in Chengdu, China, we demonstrate that GAT-PEARL significantly outperforms conventional reinforcement learning baselines, showing superior generalization to unseen infrastructure layouts and achieving higher overall operational efficiency in dynamic settings.

