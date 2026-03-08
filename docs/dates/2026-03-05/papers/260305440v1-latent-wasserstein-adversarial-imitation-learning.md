---
layout: default
title: Latent Wasserstein Adversarial Imitation Learning
---

# Latent Wasserstein Adversarial Imitation Learning
**arXiv**：[2603.05440v1](https://arxiv.org/abs/2603.05440) · [PDF](https://arxiv.org/pdf/2603.05440.pdf)  
**作者**：Siqi Yang, Kai Yan, Alexander G. Schwing, Yu-Xiong Wang  

**一句话要点**：提出LWAIL以解决模仿学习中仅需少量状态演示的问题

**关键词**：模仿学习, Wasserstein距离, 潜在空间, 状态分布匹配, 动态感知, 对抗学习

## 3 点简述
- 核心问题：传统模仿学习需大量高质量演示和动作数据，现实中常不可得。
- 方法要点：基于Wasserstein距离，在动态感知潜在空间中进行状态分布匹配，通过预训练ICVF捕获状态空间结构。
- 实验或效果：在MuJoCo环境中，仅用一至几个状态演示即达专家水平，优于先前方法。

## 摘要（原文）

> Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein distance computed in a dynamics-aware latent space. This dynamics-aware latent space differs from prior work and is obtained via a pre-training stage, where we train the Intention Conditioned Value Function (ICVF) to capture a dynamics-aware structure of the state space using a small set of randomly generated state-only data. We show that this enhances the policy's understanding of state transitions, enabling the learning process to use only one or a few state-only expert episodes to achieve expert-level performance. Through experiments on multiple MuJoCo environments, we demonstrate that our method outperforms prior Wasserstein-based IL methods and prior adversarial IL methods, achieving better results across various tasks.

