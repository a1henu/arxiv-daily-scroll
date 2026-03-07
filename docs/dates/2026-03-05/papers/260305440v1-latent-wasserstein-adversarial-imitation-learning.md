---
layout: default
title: Latent Wasserstein Adversarial Imitation Learning
---

# Latent Wasserstein Adversarial Imitation Learning
**arXiv**：[2603.05440v1](https://arxiv.org/abs/2603.05440) · [PDF](https://arxiv.org/pdf/2603.05440.pdf)  
**作者**：Siqi Yang, Kai Yan, Alexander G. Schwing, Yu-Xiong Wang  

**一句话要点**：提出LWAIL框架，通过动态感知隐空间匹配状态分布，以少量状态演示实现模仿学习。

**关键词**：模仿学习, Wasserstein距离, 隐空间学习, 状态分布匹配, 对抗模仿学习

## 3 点简述
- 模仿学习传统方法需大量高质量演示和动作数据，这常不可得。
- LWAIL利用Wasserstein距离在动态感知隐空间匹配状态分布，提升策略对状态转移的理解。
- 在MuJoCo环境中，LWAIL优于先前方法，仅需一或几个状态演示即达专家水平。

## 摘要（原文）

> Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein distance computed in a dynamics-aware latent space. This dynamics-aware latent space differs from prior work and is obtained via a pre-training stage, where we train the Intention Conditioned Value Function (ICVF) to capture a dynamics-aware structure of the state space using a small set of randomly generated state-only data. We show that this enhances the policy's understanding of state transitions, enabling the learning process to use only one or a few state-only expert episodes to achieve expert-level performance. Through experiments on multiple MuJoCo environments, we demonstrate that our method outperforms prior Wasserstein-based IL methods and prior adversarial IL methods, achieving better results across various tasks.

