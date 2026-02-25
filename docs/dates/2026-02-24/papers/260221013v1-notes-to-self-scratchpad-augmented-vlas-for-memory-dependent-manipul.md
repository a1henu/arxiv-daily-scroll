---
layout: default
title: Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks
---

# Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks
**arXiv**：[2602.21013v1](https://arxiv.org/abs/2602.21013) · [PDF](https://arxiv.org/pdf/2602.21013.pdf)  
**作者**：Sanjay Haresh, Daniel Dijkman, Apratim Bhattacharyya, Roland Memisevic  

**一句话要点**：提出语言便签增强的视觉-语言-动作模型，以解决记忆依赖的灵巧操作任务问题。

**关键词**：视觉-语言-动作模型, 记忆增强, 灵巧操作, 非马尔可夫任务, 语言便签, 泛化性能

## 3 点简述
- 核心问题：现有视觉-语言-动作模型缺乏状态记忆，难以处理非马尔可夫性的长时程操作任务。
- 方法要点：通过集成语言便签，为模型提供空间和时间记忆，以记录任务信息和跟踪计划进度。
- 实验或效果：在ClevrSkills、MemoryBench和真实世界拾放任务中，该方法显著提升了泛化性能。

## 摘要（原文）

> Many dexterous manipulation tasks are non-markovian in nature, yet little attention has been paid to this fact in the recent upsurge of the vision-language-action (VLA) paradigm. Although they are successful in bringing internet-scale semantic understanding to robotics, existing VLAs are primarily "stateless" and struggle with memory-dependent long horizon tasks. In this work, we explore a way to impart both spatial and temporal memory to a VLA by incorporating a language scratchpad. The scratchpad makes it possible to memorize task-specific information, such as object positions, and it allows the model to keep track of a plan and progress towards subgoals within that plan. We evaluate this approach on a split of memory-dependent tasks from the ClevrSkills environment, on MemoryBench, as well as on a challenging real-world pick-and-place task. We show that incorporating a language scratchpad significantly improves generalization on these tasks for both non-recurrent and recurrent models.

