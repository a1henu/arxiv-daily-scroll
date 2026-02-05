---
layout: default
title: Evolving Afferent Architectures: Biologically-inspired Models for Damage-Avoidance Learning
---

# Evolving Afferent Architectures: Biologically-inspired Models for Damage-Avoidance Learning
**arXiv**：[2602.04807v1](https://arxiv.org/abs/2602.04807) · [PDF](https://arxiv.org/pdf/2602.04807.pdf)  
**作者**：Wolfgang Maass, Sabine Janzen, Prajvi Saxena, Sach Mukherjee  

**一句话要点**：提出传入学习框架，通过进化优化传入感知架构，以支持生物力学数字孪生中的损伤避免学习。

**关键词**：传入学习, 损伤避免学习, 进化优化, 生物力学数字孪生, 强化学习, 归纳偏置

## 3 点简述
- 核心问题：如何设计自适应内部风险信号，以在长期生物力学数字孪生中实现高效损伤避免学习。
- 方法要点：采用两层架构，外层进化优化传入感知架构，内层强化学习训练策略，提供归纳偏置。
- 实验或效果：基于CAT的进化架构比人工基线效率更高、年龄鲁棒性更强，高风险动作减少23%。

## 摘要（原文）

> We introduce Afferent Learning, a framework that produces Computational Afferent Traces (CATs) as adaptive, internal risk signals for damage-avoidance learning. Inspired by biological systems, the framework uses a two-level architecture: evolutionary optimization (outer loop) discovers afferent sensing architectures that enable effective policy learning, while reinforcement learning (inner loop) trains damage-avoidance policies using these signals. This formalizes afferent sensing as providing an inductive bias for efficient learning: architectures are selected based on their ability to enable effective learning (rather than directly minimizing damage). We provide theoretical convergence guarantees under smoothness and bounded-noise assumptions. We illustrate the general approach in the challenging context of biomechanical digital twins operating over long time horizons (multiple decades of the life-course). Here, we find that CAT-based evolved architectures achieve significantly higher efficiency and better age-robustness than hand-designed baselines, enabling policies that exhibit age-dependent behavioral adaptation (23% reduction in high-risk actions). Ablation studies validate CAT signals, evolution, and predictive discrepancy as essential. We release code and data for reproducibility.

