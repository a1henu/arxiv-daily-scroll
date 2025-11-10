---
layout: default
title: Decomposed Object Manipulation via Dual-Actor Policy
---

# Decomposed Object Manipulation via Dual-Actor Policy
**arXiv**：[2511.05129v1](https://arxiv.org/abs/2511.05129) · [PDF](https://arxiv.org/pdf/2511.05129.pdf)  
**作者**：Bin Fan, Jianjian Jiang, Zhuohao Li, Yixiang He, Xiaoming Wu, Yihan Yang, Shengbang Liu, Weishi Zheng  

**一句话要点**：提出双行动者策略以分解物体操作任务，提升机器人操作性能

**关键词**：物体操作, 双行动者策略, 可供性学习, 运动流, 机器人模拟, 多阶段任务

## 3 点简述
- 核心问题：现有方法用单一策略学习物体操作，忽略任务分阶段特性
- 方法要点：引入基于可供性和运动流的双行动者，分别优化接近与操作阶段
- 实验或效果：在模拟、基准和真实场景中平均优于SOTA方法5.55%至14.7%

## 摘要（原文）

> Object manipulation, which focuses on learning to perform tasks on similar
> parts across different types of objects, can be divided into an approaching
> stage and a manipulation stage. However, previous works often ignore this
> characteristic of the task and rely on a single policy to directly learn the
> whole process of object manipulation. To address this problem, we propose a
> novel Dual-Actor Policy, termed DAP, which explicitly considers different
> stages and leverages heterogeneous visual priors to enhance each stage.
> Specifically, we introduce an affordance-based actor to locate the functional
> part in the manipulation task, thereby improving the approaching process.
> Following this, we propose a motion flow-based actor to capture the movement of
> the component, facilitating the manipulation process. Finally, we introduce a
> decision maker to determine the current stage of DAP and select the
> corresponding actor. Moreover, existing object manipulation datasets contain
> few objects and lack the visual priors needed to support training. To address
> this, we construct a simulated dataset, the Dual-Prior Object Manipulation
> Dataset, which combines the two visual priors and includes seven tasks,
> including two challenging long-term, multi-stage tasks. Experimental results on
> our dataset, the RoboTwin benchmark and real-world scenarios illustrate that
> our method consistently outperforms the SOTA method by 5.55%, 14.7% and 10.4%
> on average respectively.

