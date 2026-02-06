---
layout: default
title: Automatic Cognitive Task Generation for In-Situ Evaluation of Embodied Agents
---

# Automatic Cognitive Task Generation for In-Situ Evaluation of Embodied Agents
**arXiv**：[2602.05249v1](https://arxiv.org/abs/2602.05249) · [PDF](https://arxiv.org/pdf/2602.05249.pdf)  
**作者**：Xinyi He, Ying Yang, Chuanjian Fu, Sihan Guo, Songchun Zhu, Lifeng Fan, Zhenliang Zhang, Yujia Peng  

**一句话要点**：提出动态原位任务生成方法TEA，以解决未知3D环境中具身智能体评估的缺乏场景特异性和数据污染问题。

**关键词**：具身智能体评估, 动态任务生成, 原位评估, 3D环境交互, 认知任务建模, 任务图表示

## 3 点简述
- 核心问题：现有基准测试存在数据污染和缺乏场景特异性，无法有效评估具身智能体在未知环境中的能力。
- 方法要点：基于人类认知，通过结构化图表示定义任务，构建交互-演化两阶段系统，实现任务执行与生成的闭环。
- 实验或效果：在10个未知场景中自动生成87,876个任务，经人工验证物理合理且覆盖日常认知能力，揭示SOTA模型在感知和交互方面的不足。

## 摘要（原文）

> As general intelligent agents are poised for widespread deployment in diverse households, evaluation tailored to each unique unseen 3D environment has become a critical prerequisite. However, existing benchmarks suffer from severe data contamination and a lack of scene specificity, inadequate for assessing agent capabilities in unseen settings. To address this, we propose a dynamic in-situ task generation method for unseen environments inspired by human cognition. We define tasks through a structured graph representation and construct a two-stage interaction-evolution task generation system for embodied agents (TEA). In the interaction stage, the agent actively interacts with the environment, creating a loop between task execution and generation that allows for continuous task generation. In the evolution stage, task graph modeling allows us to recombine and reuse existing tasks to generate new ones without external data. Experiments across 10 unseen scenes demonstrate that TEA automatically generated 87,876 tasks in two cycles, which human verification confirmed to be physically reasonable and encompassing essential daily cognitive capabilities. Benchmarking SOTA models against humans on our in-situ tasks reveals that models, despite excelling on public benchmarks, perform surprisingly poorly on basic perception tasks, severely lack 3D interaction awareness and show high sensitivity to task types in reasoning. These sobering findings highlight the necessity of in-situ evaluation before deploying agents into real-world human environments.

