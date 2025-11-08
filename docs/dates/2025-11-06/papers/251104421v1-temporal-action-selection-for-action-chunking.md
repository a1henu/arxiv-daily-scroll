---
layout: default
title: Temporal Action Selection for Action Chunking
---

# Temporal Action Selection for Action Chunking
**arXiv**：[2511.04421v1](https://arxiv.org/abs/2511.04421) · [PDF](https://arxiv.org/pdf/2511.04421.pdf)  
**作者**：Yueyang Weng, Xiaopeng Zhang, Yongjin Mu, Yingcong Zhu, Yanjie Li, Qi Liu  

**一句话要点**：提出时序动作选择器以优化动作分块中的反应性与决策一致性

**关键词**：动作分块, 时序动作选择, 强化学习, 机器人控制, 决策优化

## 3 点简述
- 动作分块降低决策频率，导致反应性不足，难以适应噪声和动态环境变化。
- TAS缓存多步预测动作块，通过轻量选择器网络动态选择最优动作。
- 实验显示TAS显著提升成功率，结合残差RL增强训练效率和性能。

## 摘要（原文）

> Action chunking is a widely adopted approach in Learning from Demonstration
> (LfD). By modeling multi-step action chunks rather than single-step actions,
> action chunking significantly enhances modeling capabilities for human expert
> policies. However, the reduced decision frequency restricts the utilization of
> recent observations, degrading reactivity - particularly evident in the
> inadequate adaptation to sensor noise and dynamic environmental changes.
> Existing efforts to address this issue have primarily resorted to trading off
> reactivity against decision consistency, without achieving both. To address
> this limitation, we propose a novel algorithm, Temporal Action Selector (TAS),
> which caches predicted action chunks from multiple timesteps and dynamically
> selects the optimal action through a lightweight selector network. TAS achieves
> balanced optimization across three critical dimensions: reactivity, decision
> consistency, and motion coherence. Experiments across multiple tasks with
> diverse base policies show that TAS significantly improves success rates -
> yielding an absolute gain of up to 73.3%. Furthermore, integrating TAS as a
> base policy with residual reinforcement learning (RL) substantially enhances
> training efficiency and elevates the performance plateau. Experiments in both
> simulation and physical robots confirm the method's efficacy.

