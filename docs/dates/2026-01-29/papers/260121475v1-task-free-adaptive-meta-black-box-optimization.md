---
layout: default
title: Task-free Adaptive Meta Black-box Optimization
---

# Task-free Adaptive Meta Black-box Optimization
**arXiv**：[2601.21475v1](https://arxiv.org/abs/2601.21475) · [PDF](https://arxiv.org/pdf/2601.21475.pdf)  
**作者**：Chao Wang, Licheng Jiao, Lingling Li, Jiaxuan Zhao, Guanchun Wang, Fang Liu, Shuyuan Yang  

**一句话要点**：提出自适应元黑盒优化模型ABOM，实现无任务依赖的零样本优化

**关键词**：黑盒优化, 元学习, 自适应参数, 进化算法, 零样本优化

## 3 点简述
- 核心问题：现有元黑盒优化方法依赖大量手工训练任务，难以适应未知任务分布
- 方法要点：引入闭环自适应参数学习机制，利用目标任务数据在线更新进化算子
- 实验或效果：在合成基准和无人机路径规划中实现竞争性能，无需手工训练任务

## 摘要（原文）

> Handcrafted optimizers become prohibitively inefficient for complex black-box optimization (BBO) tasks. MetaBBO addresses this challenge by meta-learning to automatically configure optimizers for low-level BBO tasks, thereby eliminating heuristic dependencies. However, existing methods typically require extensive handcrafted training tasks to learn meta-strategies that generalize to target tasks, which poses a critical limitation for realistic applications with unknown task distributions. To overcome the issue, we propose the Adaptive meta Black-box Optimization Model (ABOM), which performs online parameter adaptation using solely optimization data from the target task, obviating the need for predefined task distributions. Unlike conventional metaBBO frameworks that decouple meta-training and optimization phases, ABOM introduces a closed-loop adaptive parameter learning mechanism, where parameterized evolutionary operators continuously self-update by leveraging generated populations during optimization. This paradigm shift enables zero-shot optimization: ABOM achieves competitive performance on synthetic BBO benchmarks and realistic unmanned aerial vehicle path planning problems without any handcrafted training tasks. Visualization studies reveal that parameterized evolutionary operators exhibit statistically significant search patterns, including natural selection and genetic recombination.

