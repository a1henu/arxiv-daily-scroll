---
layout: default
title: Bridging Dynamics Gaps via Diffusion Schrödinger Bridge for Cross-Domain Reinforcement Learning
---

# Bridging Dynamics Gaps via Diffusion Schrödinger Bridge for Cross-Domain Reinforcement Learning
**arXiv**：[2602.23737v1](https://arxiv.org/abs/2602.23737) · [PDF](https://arxiv.org/pdf/2602.23737.pdf)  
**作者**：Hanping Zhang, Yuhong Guo  

**一句话要点**：提出BDGxRL框架，利用扩散薛定谔桥对齐动态差异以解决跨域强化学习问题。

**关键词**：跨域强化学习, 扩散薛定谔桥, 动态对齐, 离线演示, 奖励调制, 策略迁移

## 3 点简述
- 核心问题：跨域强化学习中源域与目标域动态差异导致策略迁移困难，缺乏目标域交互和奖励监督。
- 方法要点：使用扩散薛定谔桥对齐源域转移与目标域离线演示动态，引入基于状态转移的奖励调制机制。
- 实验或效果：在MuJoCo跨域基准测试中优于现有方法，展示在动态转移下的强适应性。

## 摘要（原文）

> Cross-domain reinforcement learning (RL) aims to learn transferable policies under dynamics shifts between source and target domains. A key challenge lies in the lack of target-domain environment interaction and reward supervision, which prevents direct policy learning. To address this challenge, we propose Bridging Dynamics Gaps for Cross-Domain Reinforcement Learning (BDGxRL), a novel framework that leverages Diffusion Schrödinger Bridge (DSB) to align source transitions with target-domain dynamics encoded in offline demonstrations. Moreover, we introduce a reward modulation mechanism that estimates rewards based on state transitions, applying to DSB-aligned samples to ensure consistency between rewards and target-domain dynamics. BDGxRL performs target-oriented policy learning entirely within the source domain, without access to the target environment or its rewards. Experiments on MuJoCo cross-domain benchmarks demonstrate that BDGxRL outperforms state-of-the-art baselines and shows strong adaptability under transition dynamics shifts.

