---
layout: default
title: Scaling Online Distributionally Robust Reinforcement Learning: Sample-Efficient Guarantees with General Function Approximation
---

# Scaling Online Distributionally Robust Reinforcement Learning: Sample-Efficient Guarantees with General Function Approximation
**arXiv**：[2512.18957v1](https://arxiv.org/abs/2512.18957) · [PDF](https://arxiv.org/pdf/2512.18957.pdf)  
**作者**：Debamita Ghosh, George K. Atia, Yue Wang  

**一句话要点**：提出在线分布鲁棒强化学习算法，通过通用函数逼近解决环境失配问题。

**关键词**：分布鲁棒强化学习, 在线学习, 通用函数逼近, 样本效率, 环境失配, 理论保证

## 3 点简述
- 核心问题：强化学习在训练与部署环境失配时性能下降，现有方法依赖先验知识且难以扩展。
- 方法要点：设计在线算法，无需生成模型或离线数据，通过环境交互学习鲁棒策略，支持高维任务。
- 实验或效果：理论分析证明在总变差不确定性集下具有近优次线性遗憾界，样本高效。

## 摘要（原文）

> The deployment of reinforcement learning (RL) agents in real-world applications is often hindered by performance degradation caused by mismatches between training and deployment environments. Distributionally robust RL (DR-RL) addresses this issue by optimizing worst-case performance over an uncertainty set of transition dynamics. However, existing work typically relies on substantial prior knowledge-such as access to a generative model or a large offline dataset-and largely focuses on tabular methods that do not scale to complex domains. We overcome these limitations by proposing an online DR-RL algorithm with general function approximation that learns an optimal robust policy purely through interaction with the environment, without requiring prior models or offline data, enabling deployment in high-dimensional tasks. We further provide a theoretical analysis establishing a near-optimal sublinear regret bound under a total variation uncertainty set, demonstrating the sample efficiency and effectiveness of our method.

