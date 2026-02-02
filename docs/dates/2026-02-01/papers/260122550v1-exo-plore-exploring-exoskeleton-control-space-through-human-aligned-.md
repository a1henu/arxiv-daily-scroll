---
layout: default
title: Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation
---

# Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation
**arXiv**：[2601.22550v1](https://arxiv.org/abs/2601.22550) · [PDF](https://arxiv.org/pdf/2601.22550.pdf)  
**作者**：Geonho Leem, Jaedong Lee, Jehee Lee, Seungmoon Song, Jungdam Won  

**一句话要点**：提出Exo-plore仿真框架，通过人机对齐模拟优化外骨骼控制，避免真实人体实验。

**关键词**：外骨骼控制, 神经力学模拟, 深度强化学习, 步态优化, 病理步态泛化

## 3 点简述
- 核心问题：外骨骼辅助优化需长时间人体实验，难以适用于行动不便者。
- 方法要点：结合神经力学模拟与深度强化学习，生成适应辅助力的真实步态数据。
- 实验或效果：优化结果可靠，可泛化至病理步态，辅助强度与病理严重度呈线性关系。

## 摘要（原文）

> Exoskeletons show great promise for enhancing mobility, but providing appropriate assistance remains challenging due to the complexity of human adaptation to external forces. Current state-of-the-art approaches for optimizing exoskeleton controllers require extensive human experiments in which participants must walk for hours, creating a paradox: those who could benefit most from exoskeleton assistance, such as individuals with mobility impairments, are rarely able to participate in such demanding procedures. We present Exo-plore, a simulation framework that combines neuromechanical simulation with deep reinforcement learning to optimize hip exoskeleton assistance without requiring real human experiments. Exo-plore can (1) generate realistic gait data that captures human adaptation to assistive forces, (2) produce reliable optimization results despite the stochastic nature of human gait, and (3) generalize to pathological gaits, showing strong linear relationships between pathology severity and optimal assistance.

