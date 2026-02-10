---
layout: default
title: A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents
---

# A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents
**arXiv**：[2602.08964v1](https://arxiv.org/abs/2602.08964) · [PDF](https://arxiv.org/pdf/2602.08964.pdf)  
**作者**：Raghu Arghal, Fade Chen, Niall Dalton, Evgenii Kortukov, Calum McNamara, Angelos Nalmpantis, Moksh Nirvaan, Gabriele Sarti, Mario Giulianelli  

**一句话要点**：提出结合行为评估与可解释性分析的框架，以评估语言模型代理在2D网格世界中的目标导向性。

**关键词**：目标导向性评估, 语言模型代理, 行为评估, 可解释性分析, 内部表示解码, 2D网格导航

## 3 点简述
- 核心问题：缺乏可靠方法将目标归因于代理系统，以解释和预测其行为。
- 方法要点：整合行为评估与基于可解释性的内部表示分析，评估代理的目标导向性。
- 实验或效果：在2D网格世界中，代理性能随任务难度扩展，内部表示编码空间地图并支持动作选择。

## 摘要（原文）

> Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating goal-directedness that integrates behavioural evaluation with interpretability-based analyses of models' internal representations. As a case study, we examine an LLM agent navigating a 2D grid world toward a goal state. Behaviourally, we evaluate the agent against an optimal policy across varying grid sizes, obstacle densities, and goal structures, finding that performance scales with task difficulty while remaining robust to difficulty-preserving transformations and complex goal structures. We then use probing methods to decode the agent's internal representations of the environment state and its multi-step action plans. We find that the LLM agent non-linearly encodes a coarse spatial map of the environment, preserving approximate task-relevant cues about its position and the goal location; that its actions are broadly consistent with these internal representations; and that reasoning reorganises them, shifting from broader environment structural cues toward information supporting immediate action selection. Our findings support the view that introspective examination is required beyond behavioural evaluations to characterise how agents represent and pursue their objectives.

