---
layout: default
title: Iterative Compositional Data Generation for Robot Control
---

# Iterative Compositional Data Generation for Robot Control
**arXiv**：[2512.10891v1](https://arxiv.org/abs/2512.10891) · [PDF](https://arxiv.org/pdf/2512.10891.pdf)  
**作者**：Anh-Quan Pham, Marcel Hussing, Shubhankar P. Patankar, Dani S. Bassett, Jorge Mendez-Mendez, Eric Eaton  

**一句话要点**：提出语义组合扩散变换器，以解决机器人控制中组合任务数据生成与泛化问题。

**关键词**：机器人控制, 数据生成, 扩散模型, 组合学习, 零样本泛化, 离线强化学习

## 3 点简述
- 核心问题：机器人操作数据收集成本高，现有生成模型难以泛化到未见任务组合。
- 方法要点：通过因子化组件和注意力学习交互，实现零样本高质量过渡生成。
- 实验或效果：迭代自改进提升零样本性能，解决几乎所有保留任务，学习表示呈现组合结构。

## 摘要（原文）

> Collecting robotic manipulation data is expensive, making it impractical to acquire demonstrations for the combinatorially large space of tasks that arise in multi-object, multi-robot, and multi-environment settings. While recent generative models can synthesize useful data for individual tasks, they do not exploit the compositional structure of robotic domains and struggle to generalize to unseen task combinations. We propose a semantic compositional diffusion transformer that factorizes transitions into robot-, object-, obstacle-, and objective-specific components and learns their interactions through attention. Once trained on a limited subset of tasks, we show that our model can zero-shot generate high-quality transitions from which we can learn control policies for unseen task combinations. Then, we introduce an iterative self-improvement procedure in which synthetic data is validated via offline reinforcement learning and incorporated into subsequent training rounds. Our approach substantially improves zero-shot performance over monolithic and hard-coded compositional baselines, ultimately solving nearly all held-out tasks and demonstrating the emergence of meaningful compositional structure in the learned representations.

