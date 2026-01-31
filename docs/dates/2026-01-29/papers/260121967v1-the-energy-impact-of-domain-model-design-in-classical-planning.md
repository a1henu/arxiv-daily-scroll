---
layout: default
title: The Energy Impact of Domain Model Design in Classical Planning
---

# The Energy Impact of Domain Model Design in Classical Planning
**arXiv**：[2601.21967v1](https://arxiv.org/abs/2601.21967) · [PDF](https://arxiv.org/pdf/2601.21967.pdf)  
**作者**：Ilche Georgievski, Serhat Tekin, Marco Aiello  

**一句话要点**：提出领域模型配置框架以分析经典规划中领域设计对能耗的影响

**关键词**：绿色AI, 经典规划, 领域模型设计, 能耗分析, 配置框架

## 3 点简述
- 核心问题：传统AI研究忽视能耗，经典规划领域模型设计对能源效率影响未知
- 方法要点：通过控制元素排序、动作元数和死端状态等特征，系统分析领域模型变体
- 实验或效果：在五个基准领域和五个规划器上测试，发现能耗与运行时间不总相关

## 摘要（原文）

> AI research has traditionally prioritised algorithmic performance, such as optimising accuracy in machine learning or runtime in automated planning. The emerging paradigm of Green AI challenges this by recognising energy consumption as a critical performance dimension. Despite the high computational demands of automated planning, its energy efficiency has received little attention. This gap is particularly salient given the modular planning structure, in which domain models are specified independently of algorithms. On the other hand, this separation also enables systematic analysis of energy usage through domain model design. We empirically investigate how domain model characteristics affect the energy consumption of classical planners. We introduce a domain model configuration framework that enables controlled variation of features, such as element ordering, action arity, and dead-end states. Using five benchmark domains and five state-of-the-art planners, we analyse energy and runtime impacts across 32 domain variants per benchmark. Results demonstrate that domain-level modifications produce measurable energy differences across planners, with energy consumption not always correlating with runtime.

