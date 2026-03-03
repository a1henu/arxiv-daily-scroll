---
layout: default
title: A Resource-Rational Principle for Modeling Visual Attention Control
---

# A Resource-Rational Principle for Modeling Visual Attention Control
**arXiv**：[2603.02056v1](https://arxiv.org/abs/2603.02056) · [PDF](https://arxiv.org/pdf/2603.02056.pdf)  
**作者**：Yunpeng Bai  

**一句话要点**：提出资源理性框架，以模拟视觉注意作为约束下的序列决策过程，应用于人机交互设计。

**关键词**：视觉注意建模, 资源理性框架, 序列决策过程, 部分可观测马尔可夫决策过程, 人机交互设计, 仿真验证

## 3 点简述
- 核心问题：现有视觉注意模型多为描述性、任务特定或难以解释，缺乏统一计算理论。
- 方法要点：基于部分可观测马尔可夫决策过程，将视觉任务形式化为有界最优控制问题，模拟注视和注意切换行为。
- 实验或效果：在文本阅读和行走阅读等仿真环境中验证，重现经典效应，解释理解与安全权衡，生成新预测。

## 摘要（原文）

> Understanding how people allocate visual attention is central to Human-Computer Interaction (HCI), yet existing computational models of attention are often either descriptive, task-specific, or difficult to interpret. My dissertation develops a resource-rational, simulation-based framework for modeling visual attention as a sequential decision-making process under perceptual, memory, and time constraints. I formalize visual tasks, such as reading and multitasking, as bounded-optimal control problems using Partially Observable Markov Decision Processes, enabling eye-movement behaviors such as fixation and attention switching to emerge from rational adaptation rather than being hand-coded or purely data-driven. These models are instantiated in simulation environments spanning traditional text reading and reading-while-walking with smart glasses, where they reproduce classic empirical effects, explain observed trade-offs between comprehension and safety, and generate novel predictions under time pressure and interface variation. Collectively, this work contributes a unified computational account of visual attention, offering new tools for theory-driven and resource-efficient HCI design.

