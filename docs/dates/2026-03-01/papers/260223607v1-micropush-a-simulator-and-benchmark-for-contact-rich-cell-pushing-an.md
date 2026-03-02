---
layout: default
title: MicroPush: A Simulator and Benchmark for Contact-Rich Cell Pushing and Assembly with a Magnetic Rolling Microrobot
---

# MicroPush: A Simulator and Benchmark for Contact-Rich Cell Pushing and Assembly with a Magnetic Rolling Microrobot
**arXiv**：[2602.23607v1](https://arxiv.org/abs/2602.23607) · [PDF](https://arxiv.org/pdf/2602.23607.pdf)  
**作者**：Yanda Yang, Sambeeta Das  

**一句话要点**：提出MicroPush模拟器与基准套件，用于磁滚动微机器人在接触密集场景下的细胞推动与组装研究。

**关键词**：磁滚动微机器人, 微流体模拟, 接触密集操作, 细胞推动, 基准测试, 自主规划控制

## 3 点简述
- 核心问题：磁滚动微机器人在微流体环境中实现接触密集行为的自主性难以可重复开发和评估。
- 方法要点：结合过阻尼交互模型、接触感知粘滑效应和轻量近场阻尼，提供模块化规划-控制栈。
- 实验或效果：通过基准协议报告成功率、时间和跟踪指标，控制器稳定性在流动干扰下主导性能。

## 摘要（原文）

> Magnetic rolling microrobots enable gentle manipulation in confined microfluidic environments, yet autonomy for contact-rich behaviors such as cell pushing and multi-target assembly remains difficult to develop and evaluate reproducibly. We present MicroPush, an open-source simulator and benchmark suite for magnetic rolling microrobots in cluttered 2D scenes. MicroPush combines an overdamped interaction model with contact-aware stick--slip effects, lightweight near-field damping, optional Poiseuille background flow, and a calibrated mapping from actuation frequency to free-space rolling speed. On top of the simulator core, we provide a modular planning--control stack with a two-phase strategy for contact establishment and goal-directed pushing, together with a deterministic benchmark protocol with fixed tasks, staged execution, and unified CSV logging for single-object transport and hexagonal assembly. We report success, time, and tracking metrics, and an actuation-variation measure $E_{Δω}$. Results show that controller stability dominates performance under flow disturbances, while planner choice can influence command smoothness over long-horizon sequences via waypoint progression. MicroPush enables reproducible comparison and ablation of planning, control, and learning methods for microscale contact-rich micromanipulation.

