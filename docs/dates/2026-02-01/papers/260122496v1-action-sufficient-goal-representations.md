---
layout: default
title: Action-Sufficient Goal Representations
---

# Action-Sufficient Goal Representations
**arXiv**：[2601.22496v1](https://arxiv.org/abs/2601.22496) · [PDF](https://arxiv.org/pdf/2601.22496.pdf)  
**作者**：Jinu Hyeon, Woobin Park, Hongjoon Ahn, Taesup Moon  

**一句话要点**：提出动作充分性目标表示框架，以解决离线目标条件强化学习中层次策略的控制失效问题。

**关键词**：离线强化学习, 目标条件强化学习, 层次策略, 目标表示, 动作充分性, 信息论框架

## 3 点简述
- 核心问题：现有目标表示基于价值估计，可能无法区分需不同动作的目标状态，导致控制失败。
- 方法要点：引入信息论框架定义动作充分性，证明其优于价值充分性，并利用低层策略训练自然诱导此类表示。
- 实验或效果：在离散环境中验证动作充分性与控制成功强相关，且基于演员的表示优于价值估计表示。

## 摘要（原文）

> Hierarchical policies in offline goal-conditioned reinforcement learning (GCRL) addresses long-horizon tasks by decomposing control into high-level subgoal planning and low-level action execution. A critical design choice in such architectures is the goal representation-the compressed encoding of goals that serves as the interface between these levels. Existing approaches commonly derive goal representations while learning value functions, implicitly assuming that preserving information sufficient for value estimation is adequate for optimal control. We show that this assumption can fail, even when the value estimation is exact, as such representations may collapse goal states that need to be differentiated for action learning. To address this, we introduce an information-theoretic framework that defines action sufficiency, a condition on goal representations necessary for optimal action selection. We prove that value sufficiency does not imply action sufficiency and empirically verify that the latter is more strongly associated with control success in a discrete environment. We further demonstrate that standard log-loss training of low-level policies naturally induces action-sufficient representations. Our experimental results a popular benchmark demonstrate that our actor-derived representations consistently outperform representations learned via value estimation.

