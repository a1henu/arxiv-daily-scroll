---
layout: default
title: HABIT: Human Action Benchmark for Interactive Traffic in CARLA
---

# HABIT: Human Action Benchmark for Interactive Traffic in CARLA
**arXiv**：[2511.19109v1](https://arxiv.org/abs/2511.19109) · [PDF](https://arxiv.org/pdf/2511.19109.pdf)  
**作者**：Mohan Ramesh, Mark Azer, Fabian B. Flohr  

**一句话要点**：提出HABIT基准以解决自动驾驶模拟中人类行为真实性问题

**关键词**：自动驾驶模拟, 人类行为基准, 运动重定向, 安全评估, CARLA集成

## 3 点简述
- 核心问题：现有自动驾驶模拟缺乏真实多样的人类行为，影响系统安全评估。
- 方法要点：集成真实人类运动数据到CARLA，通过模块化运动重定向管道。
- 实验或效果：评估显示先进AD代理在HABIT中碰撞率高达7.43次/公里，暴露隐藏弱点。

## 摘要（原文）

> Current autonomous driving (AD) simulations are critically limited by their inadequate representation of realistic and diverse human behavior, which is essential for ensuring safety and reliability. Existing benchmarks often simplify pedestrian interactions, failing to capture complex, dynamic intentions and varied responses critical for robust system deployment. To overcome this, we introduce HABIT (Human Action Benchmark for Interactive Traffic), a high-fidelity simulation benchmark. HABIT integrates real-world human motion, sourced from mocap and videos, into CARLA (Car Learning to Act, a full autonomous driving simulator) via a modular, extensible, and physically consistent motion retargeting pipeline. From an initial pool of approximately 30,000 retargeted motions, we curate 4,730 traffic-compatible pedestrian motions, standardized in SMPL format for physically consistent trajectories. HABIT seamlessly integrates with CARLA's Leaderboard, enabling automated scenario generation and rigorous agent evaluation. Our safety metrics, including Abbreviated Injury Scale (AIS) and False Positive Braking Rate (FPBR), reveal critical failure modes in state-of-the-art AD agents missed by prior evaluations. Evaluating three state-of-the-art autonomous driving agents, InterFuser, TransFuser, and BEVDriver, demonstrates how HABIT exposes planner weaknesses that remain hidden in scripted simulations. Despite achieving close or equal to zero collisions per kilometer on the CARLA Leaderboard, the autonomous agents perform notably worse on HABIT, with up to 7.43 collisions/km and a 12.94% AIS 3+ injury risk, and they brake unnecessarily in up to 33% of cases. All components are publicly released to support reproducible, pedestrian-aware AI research.

