---
layout: default
title: Zero-shot Structure Learning and Planning for Autonomous Robot Navigation using Active Inference
---

# Zero-shot Structure Learning and Planning for Autonomous Robot Navigation using Active Inference
**arXiv**：[2510.09574v1](https://arxiv.org/abs/2510.09574) · [PDF](https://arxiv.org/pdf/2510.09574.pdf)  
**作者**：Daria de tinguy, Tim Verbelen, Emilio Gamba, Bart Dhoedt  

**一句话要点**：提出AIMAPP框架以解决未知环境中机器人自主导航问题

**关键词**：自主导航, 主动推理, 拓扑建图, 零样本学习, 机器人规划

## 3 点简述
- 核心问题：未知环境中机器人需同时探索、定位和规划，无预定义地图或训练
- 方法要点：基于主动推理，统一建图、定位和决策，使用拓扑推理和预期自由能量最小化
- 实验或效果：在真实和模拟环境中展示鲁棒性能，适应观测模糊和环境变化

## 摘要（原文）

> Autonomous navigation in unfamiliar environments requires robots to
> simultaneously explore, localise, and plan under uncertainty, without relying
> on predefined maps or extensive training. We present a biologically inspired,
> Active Inference-based framework, Active Inference MAPping and Planning
> (AIMAPP). This model unifies mapping, localisation, and decision-making within
> a single generative model. Inspired by hippocampal navigation, it uses
> topological reasoning, place-cell encoding, and episodic memory to guide
> behaviour. The agent builds and updates a sparse topological map online, learns
> state transitions dynamically, and plans actions by minimising Expected Free
> Energy. This allows it to balance goal-directed and exploratory behaviours. We
> implemented a ROS-compatible navigation system that is sensor and
> robot-agnostic, capable of integrating with diverse hardware configurations. It
> operates in a fully self-supervised manner, is resilient to drift, and supports
> both exploration and goal-directed navigation without any pre-training. We
> demonstrate robust performance in large-scale real and simulated environments
> against state-of-the-art planning models, highlighting the system's
> adaptability to ambiguous observations, environmental changes, and sensor
> noise. The model offers a biologically inspired, modular solution to scalable,
> self-supervised navigation in unstructured settings. AIMAPP is available at
> https://github.com/decide-ugent/AIMAPP.

