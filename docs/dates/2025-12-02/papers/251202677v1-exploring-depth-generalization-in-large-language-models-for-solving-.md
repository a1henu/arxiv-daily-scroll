---
layout: default
title: Exploring Depth Generalization in Large Language Models for Solving Recursive Logic Tasks
---

# Exploring Depth Generalization in Large Language Models for Solving Recursive Logic Tasks
**arXiv**：[2512.02677v1](https://arxiv.org/abs/2512.02677) · [PDF](https://arxiv.org/pdf/2512.02677.pdf)  
**作者**：Zhiyuan He  

**一句话要点**：提出循环定位替换管道以解决大语言模型在递归逻辑任务中的深度泛化问题

**关键词**：深度泛化, 递归推理, Transformer架构, 循环定位替换, 逻辑任务, 栈式行为

## 3 点简述
- 核心问题：标准Transformer架构在递归深度超出训练范围时性能快速下降，源于无法维持栈式行为。
- 方法要点：开发循环定位替换管道，使用定位器和替换器分解递归问题为可管理子组件。
- 实验或效果：在布尔代数、递归算术和命题逻辑中评估，有效缓解分布外递归深度下的性能衰减。

## 摘要（原文）

> Large language models have demonstrated remarkable capabilities across many tasks, yet face significant challenges when dealing with recursive reasoning problems, those requiring the resolution of nested hierarchical structures. While prior research has extensively studied length generalization (a model's ability to handle longer sequences than seen during training), we investigate a distinct and underexplored limitation: depth generalization. Here, depth refers to the number of nested levels in a hierarchical problem, such as the layers of parentheses in a mathematical expression or the nesting of logical clauses in a Boolean formula. Our work reveals that standard transformer architectures struggle with problems involving deeper recursion than encountered during training, even when they perform well on longer but non-nested sequences. This limitation stems from their inability to maintain stack-like behavior, the capacity to track and resolve multiple levels of nested dependencies. Through systematic analysis, we demonstrate how this architectural constraint leads to rapid performance decay as the depth of the recursion increases. To address this challenge, we develop a novel looped locate-and-replace pipeline that decomposes recursive problems into manageable subcomponents. The approach employs two specialized models: a locator that identifies solvable subexpressions and a replacer that evaluates these components while preserving the overall structure. We evaluated this method in three carefully designed domains: Boolean algebra, recursive arithmetic, and propositional logic, each with a controllable depth of recursion. We show that our method effectively alleviates the performance decay when tested on out-of-distribution recursion depth.

