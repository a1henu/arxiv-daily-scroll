---
layout: default
title: Proximal Policy Optimization with Evolutionary Mutations
---

# Proximal Policy Optimization with Evolutionary Mutations
**arXiv**：[2601.14705v1](https://arxiv.org/abs/2601.14705) · [PDF](https://arxiv.org/pdf/2601.14705.pdf)  
**作者**：Casimir Czworkowski, Stephen Hornish, Alhassan S. Yasin  

**一句话要点**：提出POEM以解决PPO探索不足导致的早熟收敛问题

**关键词**：近端策略优化, 进化算法, 探索-利用权衡, KL散度, 自适应突变, 强化学习

## 3 点简述
- PPO算法因探索有限易早熟收敛，限制了性能提升。
- POEM通过监控KL散度，在策略停滞时自适应突变参数以增强探索。
- 在四个Gym环境中，POEM在三个任务上显著优于PPO，验证了进化原则的潜力。

## 摘要（原文）

> Proximal Policy Optimization (PPO) is a widely used reinforcement learning algorithm known for its stability and sample efficiency, but it often suffers from premature convergence due to limited exploration. In this paper, we propose POEM (Proximal Policy Optimization with Evolutionary Mutations), a novel modification to PPO that introduces an adaptive exploration mechanism inspired by evolutionary algorithms. POEM enhances policy diversity by monitoring the Kullback-Leibler (KL) divergence between the current policy and a moving average of previous policies. When policy changes become minimal, indicating stagnation, POEM triggers an adaptive mutation of policy parameters to promote exploration. We evaluate POEM on four OpenAI Gym environments: CarRacing, MountainCar, BipedalWalker, and LunarLander. Through extensive fine-tuning using Bayesian optimization techniques and statistical testing using Welch's t-test, we find that POEM significantly outperforms PPO on three of the four tasks (BipedalWalker: t=-2.0642, p=0.0495; CarRacing: t=-6.3987, p=0.0002; MountainCar: t=-6.2431, p<0.0001), while performance on LunarLander is not statistically significant (t=-1.8707, p=0.0778). Our results highlight the potential of integrating evolutionary principles into policy gradient methods to overcome exploration-exploitation tradeoffs.

