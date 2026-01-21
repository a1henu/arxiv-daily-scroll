---
layout: default
title: KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning
---

# KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning
**arXiv**：[2601.14232v1](https://arxiv.org/abs/2601.14232) · [PDF](https://arxiv.org/pdf/2601.14232.pdf)  
**作者**：Egor Cherepanov, Daniil Zelezetsky, Alexey K. Kovalev, Aleksandr I. Panov  

**一句话要点**：提出KAGE-Bench基准以评估强化学习在已知视觉轴下的泛化能力

**关键词**：强化学习, 视觉泛化, 基准评估, 像素策略, JAX实现, 分布偏移

## 3 点简述
- 核心问题：像素强化学习代理在视觉分布偏移下易失败，现有基准混杂多种偏移，阻碍系统分析。
- 方法要点：引入KAGE-Env环境，将观察过程分解为独立可控视觉轴，保持底层控制问题固定，提供视觉泛化的清晰抽象。
- 实验或效果：基于PPO-CNN基线，在六个已知轴套件上观察到轴依赖性失败，背景和光度偏移常导致性能崩溃，而代理外观偏移相对温和。

## 摘要（原文）

> Pixel-based reinforcement learning agents often fail under purely visual distribution shift even when latent dynamics and rewards are unchanged, but existing benchmarks entangle multiple sources of shift and hinder systematic analysis. We introduce KAGE-Env, a JAX-native 2D platformer that factorizes the observation process into independently controllable visual axes while keeping the underlying control problem fixed. By construction, varying a visual axis affects performance only through the induced state-conditional action distribution of a pixel policy, providing a clean abstraction for visual generalization. Building on this environment, we define KAGE-Bench, a benchmark of six known-axis suites comprising 34 train-evaluation configuration pairs that isolate individual visual shifts. Using a standard PPO-CNN baseline, we observe strong axis-dependent failures, with background and photometric shifts often collapsing success, while agent-appearance shifts are comparatively benign. Several shifts preserve forward motion while breaking task completion, showing that return alone can obscure generalization failures. Finally, the fully vectorized JAX implementation enables up to 33M environment steps per second on a single GPU, enabling fast and reproducible sweeps over visual factors. Code: https://avanturist322.github.io/KAGEBench/.

