---
layout: default
title: Diamond Maps: Efficient Reward Alignment via Stochastic Flow Maps
---

# Diamond Maps: Efficient Reward Alignment via Stochastic Flow Maps
**arXiv**：[2602.05993v1](https://arxiv.org/abs/2602.05993) · [PDF](https://arxiv.org/pdf/2602.05993.pdf)  
**作者**：Peter Holderrieth, Douglas Chen, Luca Eyring, Ishin Shah, Giri Anantharaman, Yutong He, Zeynep Akata, Tommi Jaakkola, Nicholas Matthew Boffi, Max Simchowitz  

**一句话要点**：提出Diamond Maps以在推理时高效对齐任意奖励，解决生成模型奖励对齐的挑战。

**关键词**：奖励对齐, 随机流图模型, 推理时适应, 蒸馏训练, 生成模型, 价值函数估计

## 3 点简述
- 核心问题：流和扩散模型在训练后适应偏好或约束时成本高且脆弱，奖励对齐困难。
- 方法要点：设计随机流图模型，将多步模拟摊销为单步采样，保留随机性以支持高效奖励对齐。
- 实验或效果：通过GLASS Flows蒸馏高效学习，在奖励对齐性能和可扩展性上优于现有方法。

## 摘要（原文）

> Flow and diffusion models produce high-quality samples, but adapting them to user preferences or constraints post-training remains costly and brittle, a challenge commonly called reward alignment. We argue that efficient reward alignment should be a property of the generative model itself, not an afterthought, and redesign the model for adaptability. We propose "Diamond Maps", stochastic flow map models that enable efficient and accurate alignment to arbitrary rewards at inference time. Diamond Maps amortize many simulation steps into a single-step sampler, like flow maps, while preserving the stochasticity required for optimal reward alignment. This design makes search, sequential Monte Carlo, and guidance scalable by enabling efficient and consistent estimation of the value function. Our experiments show that Diamond Maps can be learned efficiently via distillation from GLASS Flows, achieve stronger reward alignment performance, and scale better than existing methods. Our results point toward a practical route to generative models that can be rapidly adapted to arbitrary preferences and constraints at inference time.

