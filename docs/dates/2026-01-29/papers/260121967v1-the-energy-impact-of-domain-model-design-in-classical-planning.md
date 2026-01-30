---
layout: default
title: The Energy Impact of Domain Model Design in Classical Planning
---

# The Energy Impact of Domain Model Design in Classical Planning
**arXiv**：[2601.21967v1](https://arxiv.org/abs/2601.21967) · [PDF](https://arxiv.org/pdf/2601.21967.pdf)  
**作者**：Ilche Georgievski, Serhat Tekin, Marco Aiello  

**一句话要点**：提出领域模型配置框架以分析经典规划中领域设计对能耗的影响

**关键词**：绿色AI, 经典规划, 领域模型设计, 能耗分析, 自动规划, 能源效率

## 3 点简述
- 核心问题：自动规划研究忽视能耗，领域模型设计对能源效率的影响未知
- 方法要点：通过控制领域特征如元素排序和动作元数，系统评估能耗差异
- 实验或效果：在五个基准领域和规划器上，领域修改导致可测量的能耗变化，能耗与运行时间不总相关

## 摘要（原文）

> AI research has traditionally prioritised algorithmic performance, such as optimising accuracy in machine learning or runtime in automated planning. The emerging paradigm of Green AI challenges this by recognising energy consumption as a critical performance dimension. Despite the high computational demands of automated planning, its energy efficiency has received little attention. This gap is particularly salient given the modular planning structure, in which domain models are specified independently of algorithms. On the other hand, this separation also enables systematic analysis of energy usage through domain model design. We empirically investigate how domain model characteristics affect the energy consumption of classical planners. We introduce a domain model configuration framework that enables controlled variation of features, such as element ordering, action arity, and dead-end states. Using five benchmark domains and five state-of-the-art planners, we analyse energy and runtime impacts across 32 domain variants per benchmark. Results demonstrate that domain-level modifications produce measurable energy differences across planners, with energy consumption not always correlating with runtime.

