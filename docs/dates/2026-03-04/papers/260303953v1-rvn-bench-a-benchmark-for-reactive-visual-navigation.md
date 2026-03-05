---
layout: default
title: RVN-Bench: A Benchmark for Reactive Visual Navigation
---

# RVN-Bench: A Benchmark for Reactive Visual Navigation
**arXiv**：[2603.03953v1](https://arxiv.org/abs/2603.03953) · [PDF](https://arxiv.org/pdf/2603.03953.pdf)  
**作者**：Jaewon Lee, Jaeseok Heo, Gunmin Lee, Howoong Jun, Jeongwoo Oh, Songhwai Oh  

**一句话要点**：提出RVN-Bench基准以解决室内视觉导航中碰撞忽略和场景不匹配问题

**关键词**：视觉导航, 碰撞感知, 室内机器人, 基准测试, 强化学习, 仿真环境

## 3 点简述
- 现有基准常忽略碰撞或适用于户外，不适用于室内安全视觉导航
- 基于Habitat 2.0和HM3D场景，提供碰撞感知任务、评估指标和标准化工具
- 实验表明训练策略能泛化到未见环境，验证基准的有效性和标准化价值

## 摘要（原文）

> Safe visual navigation is critical for indoor mobile robots operating in cluttered environments. Existing benchmarks, however, often neglect collisions or are designed for outdoor scenarios, making them unsuitable for indoor visual navigation. To address this limitation, we introduce the reactive visual navigation benchmark (RVN-Bench), a collision-aware benchmark for indoor mobile robots. In RVN-Bench, an agent must reach sequential goal positions in previously unseen environments using only visual observations and no prior map, while avoiding collisions. Built on the Habitat 2.0 simulator and leveraging high-fidelity HM3D scenes, RVN-Bench provides large-scale, diverse indoor environments, defines a collision-aware navigation task and evaluation metrics, and offers tools for standardized training and benchmarking. RVN-Bench supports both online and offline learning by offering an environment for online reinforcement learning, a trajectory image dataset generator, and tools for producing negative trajectory image datasets that capture collision events. Experiments show that policies trained on RVN-Bench generalize effectively to unseen environments, demonstrating its value as a standardized benchmark for safe and robust visual navigation. Code and additional materials are available at: https://rvn-bench.github.io/.

