---
layout: default
title: APC-RL: Exceeding Data-Driven Behavior Priors with Adaptive Policy Composition
---

# APC-RL: Exceeding Data-Driven Behavior Priors with Adaptive Policy Composition
**arXiv**：[2601.19452v1](https://arxiv.org/abs/2601.19452) · [PDF](https://arxiv.org/pdf/2601.19452.pdf)  
**作者**：Finn Rietz, Pedro Zuidberg dos Martires, Johannes Andreas Stork  

**一句话要点**：提出自适应策略组合以解决演示数据稀疏、次优或错配时强化学习性能下降问题

**关键词**：自适应策略组合, 归一化流先验, 演示数据集成, 强化学习加速, 错配鲁棒性

## 3 点简述
- 核心问题：现有方法假设演示数据最优且与任务对齐，但实际中演示常稀疏、次优或错配，导致性能下降
- 方法要点：自适应组合多个归一化流先验，估计先验适用性并用于探索，必要时绕过错配先验以优化奖励
- 实验或效果：在多样基准测试中加速对齐演示学习，在严重错配下保持鲁棒，利用次优演示引导探索避免性能下降

## 摘要（原文）

> Incorporating demonstration data into reinforcement learning (RL) can greatly accelerate learning, but existing approaches often assume demonstrations are optimal and fully aligned with the target task. In practice, demonstrations are frequently sparse, suboptimal, or misaligned, which can degrade performance when these demonstrations are integrated into RL. We propose Adaptive Policy Composition (APC), a hierarchical model that adaptively composes multiple data-driven Normalizing Flow (NF) priors. Instead of enforcing strict adherence to the priors, APC estimates each prior's applicability to the target task while leveraging them for exploration. Moreover, APC either refines useful priors, or sidesteps misaligned ones when necessary to optimize downstream reward. Across diverse benchmarks, APC accelerates learning when demonstrations are aligned, remains robust under severe misalignment, and leverages suboptimal demonstrations to bootstrap exploration while avoiding performance degradation caused by overly strict adherence to suboptimal demonstrations.

