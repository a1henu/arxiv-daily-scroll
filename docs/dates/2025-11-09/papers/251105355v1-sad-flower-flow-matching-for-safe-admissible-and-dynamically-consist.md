---
layout: default
title: SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning
---

# SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning
**arXiv**：[2511.05355v1](https://arxiv.org/abs/2511.05355) · [PDF](https://arxiv.org/pdf/2511.05355.pdf)  
**作者**：Tzu-Yuan Huang, Armin Lederer, Dai-Jie Wu, Xiaobing Dai, Sihua Zhang, Stefan Sosnowski, Shao-Hua Sun, Sandra Hirche  

**一句话要点**：提出SAD-Flower框架以解决流匹配规划中的安全、可接受和动态一致性问题

**关键词**：流匹配规划, 安全轨迹生成, 动态一致性, 虚拟控制输入, 非线性控制理论, 约束满足

## 3 点简述
- 流匹配规划缺乏状态和动作约束的正式保证，影响轨迹安全与可执行性
- 通过虚拟控制输入增强流，利用非线性控制理论提供正式约束和动态一致性保证
- 无需重新训练即可满足未见约束，实验显示在约束满足方面优于生成模型基线

## 摘要（原文）

> Flow matching (FM) has shown promising results in data-driven planning.
> However, it inherently lacks formal guarantees for ensuring state and action
> constraints, whose satisfaction is a fundamental and crucial requirement for
> the safety and admissibility of planned trajectories on various systems.
> Moreover, existing FM planners do not ensure the dynamical consistency, which
> potentially renders trajectories inexecutable. We address these shortcomings by
> proposing SAD-Flower, a novel framework for generating Safe, Admissible, and
> Dynamically consistent trajectories. Our approach relies on an augmentation of
> the flow with a virtual control input. Thereby, principled guidance can be
> derived using techniques from nonlinear control theory, providing formal
> guarantees for state constraints, action constraints, and dynamic consistency.
> Crucially, SAD-Flower operates without retraining, enabling test-time
> satisfaction of unseen constraints. Through extensive experiments across
> several tasks, we demonstrate that SAD-Flower outperforms various
> generative-model-based baselines in ensuring constraint satisfaction.

