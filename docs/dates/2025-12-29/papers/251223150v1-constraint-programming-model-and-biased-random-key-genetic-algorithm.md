---
layout: default
title: Constraint programming model and biased random-key genetic algorithm for the single-machine coupled task scheduling problem with exact delays to minimize the makespan
---

# Constraint programming model and biased random-key genetic algorithm for the single-machine coupled task scheduling problem with exact delays to minimize the makespan
**arXiv**：[2512.23150v1](https://arxiv.org/abs/2512.23150) · [PDF](https://arxiv.org/pdf/2512.23150.pdf)  
**作者**：Vítor A. Barbosa, Rafael A. Melo  

**一句话要点**：提出约束编程模型与偏置随机密钥遗传算法，以最小化完工时间，解决单机精确延迟耦合任务调度问题。

**关键词**：单机调度, 耦合任务, 精确延迟, 约束编程, 偏置随机密钥遗传算法, 完工时间最小化

## 3 点简述
- 核心问题：单机精确延迟耦合任务调度，任务间有固定延迟，目标最小化完工时间，属于强NP难问题。
- 方法要点：结合约束编程建模与偏置随机密钥遗传算法，后者包含高效解码器、周期性重启、抖动和局部搜索组件。
- 实验或效果：算法在100个作业实例上高效探索解空间，在短时间限制下优于CP模型，长时间多线程下CP模型达到90.56%实例当前最优解。

## 摘要（原文）

> We consider the strongly NP-hard single-machine coupled task scheduling problem with exact delays to minimize the makespan. In this problem, a set of jobs has to be scheduled, each composed of two tasks interspersed by an exact delay. Given that no preemption is allowed, the goal consists of minimizing the completion time of the last scheduled task. We model the problem using constraint programming (CP) and propose a biased random-key genetic algorithm (BRKGA). Our CP model applies well-established global constraints. Our BRKGA combines some successful components in the literature: an initial solution generator, periodical restarts and shakes, and a local search algorithm. Furthermore, the BRKGA's decoder is focused on efficiency rather than optimality, which accelerates the solution space exploration. Computational experiments on a benchmark set containing instances with up to 100 jobs (200 tasks) indicate that the proposed BRKGA can efficiently explore the problem solution space, providing high-quality approximate solutions within low computational times. It can also provide better solutions than the CP model under the same computational settings, i.e., three minutes of time limit and a single thread. The CP model, when offered a longer running time of 3600 seconds and multiple threads, significantly improved the results, reaching the current best-known solution for 90.56% of these instances. Finally, our experiments highlight the importance of the shake and local search components in the BRKGA, whose combination significantly improves the results of a standard BRKGA.

