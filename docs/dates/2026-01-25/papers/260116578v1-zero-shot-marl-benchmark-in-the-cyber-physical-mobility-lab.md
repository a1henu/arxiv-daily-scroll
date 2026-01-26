---
layout: default
title: Zero-Shot MARL Benchmark in the Cyber-Physical Mobility Lab
---

# Zero-Shot MARL Benchmark in the Cyber-Physical Mobility Lab
**arXiv**：[2601.16578v1](https://arxiv.org/abs/2601.16578) · [PDF](https://arxiv.org/pdf/2601.16578.pdf)  
**作者**：Julius Beerwerth, Jianye Xu, Simon Schäfer, Fynn Belderink, Bassam Alrifaee  

**一句话要点**：提出可复现基准以评估多智能体强化学习在网联自动驾驶车辆中的零次模拟到真实迁移

**关键词**：多智能体强化学习, 模拟到真实迁移, 网联自动驾驶车辆, 零次学习, 数字孪生, 可复现基准

## 3 点简述
- 核心问题：评估多智能体强化学习策略在网联自动驾驶车辆中的模拟到真实迁移性能，面临架构差异和环境真实度差距的挑战。
- 方法要点：基于网联物理移动实验室，集成仿真、高保真数字孪生和物理测试平台，支持结构化零次评估。
- 实验或效果：部署SigmaRL训练的策略，揭示性能下降源于仿真与硬件控制栈的架构差异及环境真实度提升导致的模拟到真实差距。

## 摘要（原文）

> We present a reproducible benchmark for evaluating sim-to-real transfer of Multi-Agent Reinforcement Learning (MARL) policies for Connected and Automated Vehicles (CAVs). The platform, based on the Cyber-Physical Mobility Lab (CPM Lab) [1], integrates simulation, a high-fidelity digital twin, and a physical testbed, enabling structured zero-shot evaluation of MARL motion-planning policies. We demonstrate its use by deploying a SigmaRL-trained policy [2] across all three domains, revealing two complementary sources of performance degradation: architectural differences between simulation and hardware control stacks, and the sim-to-real gap induced by increasing environmental realism. The open-source setup enables systematic analysis of sim-to-real challenges in MARL under realistic, reproducible conditions.

