---
layout: default
title: RoboHiMan: A Hierarchical Evaluation Paradigm for Compositional Generalization in Long-Horizon Manipulation
---

# RoboHiMan: A Hierarchical Evaluation Paradigm for Compositional Generalization in Long-Horizon Manipulation
**arXiv**：[2510.13149v1](https://arxiv.org/abs/2510.13149) · [PDF](https://arxiv.org/pdf/2510.13149.pdf)  
**作者**：Yangtao Chen, Zixuan Chen, Nga Teng Chan, Junting Chen, Junhui Yin, Jieqi Shi, Yang Gao, Yong-Lu Li, Jing Huo  

**一句话要点**：提出RoboHiMan分层评估范式以解决长视野操作中的组合泛化问题

**关键词**：长视野操作, 组合泛化, 分层评估, 机器人技能, 基准测试, 扰动鲁棒性

## 3 点简述
- 核心问题：现有方法在复杂扰动下组合技能泛化能力不足，缺乏系统性评估。
- 方法要点：引入HiMan-Bench基准和三种评估范式，分析分层架构瓶颈。
- 实验或效果：实验揭示模型能力差距，为真实世界长视野操作提供方向。

## 摘要（原文）

> Enabling robots to flexibly schedule and compose learned skills for novel
> long-horizon manipulation under diverse perturbations remains a core challenge.
> Early explorations with end-to-end VLA models show limited success, as these
> models struggle to generalize beyond the training distribution. Hierarchical
> approaches, where high-level planners generate subgoals for low-level policies,
> bring certain improvements but still suffer under complex perturbations,
> revealing limited capability in skill composition. However, existing benchmarks
> primarily emphasize task completion in long-horizon settings, offering little
> insight into compositional generalization, robustness, and the interplay
> between planning and execution. To systematically investigate these gaps, we
> propose RoboHiMan, a hierarchical evaluation paradigm for compositional
> generalization in long-horizon manipulation. RoboHiMan introduces HiMan-Bench,
> a benchmark of atomic and compositional tasks under diverse perturbations,
> supported by a multi-level training dataset for analyzing progressive data
> scaling, and proposes three evaluation paradigms (vanilla, decoupled, coupled)
> that probe the necessity of skill composition and reveal bottlenecks in
> hierarchical architectures. Experiments highlight clear capability gaps across
> representative models and architectures, pointing to directions for advancing
> models better suited to real-world long-horizon manipulation tasks. Videos and
> open-source code can be found on our project website:
> https://chenyt31.github.io/robo-himan.github.io/.

