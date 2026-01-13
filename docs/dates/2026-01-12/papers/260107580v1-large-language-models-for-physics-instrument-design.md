---
layout: default
title: Large Language Models for Physics Instrument Design
---

# Large Language Models for Physics Instrument Design
**arXiv**：[2601.07580v1](https://arxiv.org/abs/2601.07580) · [PDF](https://arxiv.org/pdf/2601.07580.pdf)  
**作者**：Sara Zoccheddu, Shah Rukh Qasim, Patrick Owen, Nicola Serra  

**一句话要点**：研究大语言模型用于物理仪器设计，探索其作为元规划器与强化学习结合的潜力。

**关键词**：大语言模型, 物理仪器设计, 强化学习, 探测器配置, 元规划器, 自动化设计

## 3 点简述
- 核心问题：评估大语言模型在物理仪器设计中的性能，并与强化学习方法进行比较。
- 方法要点：仅通过提示，大语言模型基于任务约束和先验设计摘要生成完整探测器配置，使用相同模拟器和奖励函数评估。
- 实验或效果：大语言模型能生成有效、资源感知且物理有意义的配置，适合作为元规划器协调优化流程。

## 摘要（原文）

> We study the use of large language models (LLMs) for physics instrument design and compare their performance to reinforcement learning (RL). Using only prompting, LLMs are given task constraints and summaries of prior high-scoring designs and propose complete detector configurations, which we evaluate with the same simulators and reward functions used in RL-based optimization. Although RL yields stronger final designs, we find that modern LLMs consistently generate valid, resource-aware, and physically meaningful configurations that draw on broad pretrained knowledge of detector design principles and particle--matter interactions, despite having no task-specific training. Based on this result, as a first step toward hybrid design workflows, we explore pairing the LLMs with a dedicated trust region optimizer, serving as a precursor to future pipelines in which LLMs propose and structure design hypotheses while RL performs reward-driven optimization. Based on these experiments, we argue that LLMs are well suited as meta-planners: they can design and orchestrate RL-based optimization studies, define search strategies, and coordinate multiple interacting components within a unified workflow. In doing so, they point toward automated, closed-loop instrument design in which much of the human effort required to structure and supervise optimization can be reduced.

