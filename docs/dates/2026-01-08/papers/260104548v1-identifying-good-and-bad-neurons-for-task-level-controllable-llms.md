---
layout: default
title: Identifying Good and Bad Neurons for Task-Level Controllable LLMs
---

# Identifying Good and Bad Neurons for Task-Level Controllable LLMs
**arXiv**：[2601.04548v1](https://arxiv.org/abs/2601.04548) · [PDF](https://arxiv.org/pdf/2601.04548.pdf)  
**作者**：Wenjie Li, Guansong Pang, Hezhe Qiao, Debin Gao, David Lo  

**一句话要点**：提出NeuronLLM框架，基于功能拮抗原理识别大语言模型中的好与坏神经元，以解决任务级可控性问题。

**关键词**：大语言模型理解, 神经元识别, 功能拮抗, 对比学习, 任务级可控性, 偶然行为缓解

## 3 点简述
- 核心问题：现有方法难以识别任务中多能力协同的神经元，且忽略抑制性角色和偶然行为误导。
- 方法要点：采用功能拮抗原理，通过对比学习建模好与坏神经元，并利用增强问题集缓解偶然行为。
- 实验或效果：在不同规模和家族的大语言模型上，在四个NLP任务中优于现有方法，揭示功能组织新见解。

## 摘要（原文）

> Large Language Models have demonstrated remarkable capabilities on multiple-choice question answering benchmarks, but the complex mechanisms underlying their large-scale neurons remain opaque, posing significant challenges for understanding and steering LLMs. While recent studies made progress on identifying responsible neurons for certain abilities, these ability-specific methods are infeasible for task-focused scenarios requiring coordinated use of multiple abilities. Moreover, these approaches focus only on supportive neurons that correlate positively with task completion, while neglecting neurons with other roles-such as inhibitive roles-and misled neuron attribution due to fortuitous behaviors in LLMs (i.e., correctly answer the questions by chance rather than genuine understanding). To address these challenges, we propose NeuronLLM, a novel task-level LLM understanding framework that adopts the biological principle of functional antagonism for LLM neuron identification. The key insight is that task performance is jointly determined by neurons with two opposing roles: good neurons that facilitate task completion and bad neurons that inhibit it. NeuronLLM achieves a holistic modeling of neurons via contrastive learning of good and bad neurons, while leveraging augmented question sets to mitigate the fortuitous behaviors in LLMs. Comprehensive experiments on LLMs of different sizes and families show the superiority of NeuronLLM over existing methods in four NLP tasks, providing new insights into LLM functional organization.

