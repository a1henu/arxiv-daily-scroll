---
layout: default
title: Selection as Power: Constrained Reinforcement for Bounded Decision Authority
---

# Selection as Power: Constrained Reinforcement for Bounded Decision Authority
**arXiv**：[2603.02019v1](https://arxiv.org/abs/2603.02019) · [PDF](https://arxiv.org/pdf/2603.02019.pdf)  
**作者**：Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Díaz  

**一句话要点**：提出激励选择治理框架，通过约束强化学习在金融场景中维持有界选择权

**关键词**：约束强化学习, 选择治理, 金融监管, 投影约束, 有界选择权

## 3 点简述
- 核心问题：静态治理框架无法适应动态环境，无约束强化学习导致选择权过度集中
- 方法要点：引入投影约束将参数更新限制在治理定义的可行集内，防止超越预设边界
- 实验效果：在受监管金融场景中，该框架能保持选择多样性，避免确定性主导

## 摘要（原文）

> Selection as Power argued that upstream selection authority, rather than internal objective misalignment, constitutes a primary source of risk in high-stakes agentic systems. However, the original framework was static: governance constraints bounded selection power but did not adapt over time. In this work, we extend the framework to dynamic settings by introducing incentivized selection governance, where reinforcement updates are applied to scoring and reducer parameters under externally enforced sovereignty constraints.
>   We formalize selection as a constrained reinforcement process in which parameter updates are projected onto governance-defined feasible sets, preventing concentration beyond prescribed bounds. Across multiple regulated financial scenarios, unconstrained reinforcement consistently collapses into deterministic dominance under repeated feedback, especially at higher learning rates. In contrast, incentivized governance enables adaptive improvement while maintaining bounded selection concentration.
>   Projection-based constraints transform reinforcement from irreversible lock-in into controlled adaptation, with governance debt quantifying the tension between optimization pressure and authority bounds. These results demonstrate that learning dynamics can coexist with structural diversity when sovereignty constraints are enforced at every update step, offering a principled approach to integrating reinforcement into high-stakes agentic systems without surrendering bounded selection authority.

