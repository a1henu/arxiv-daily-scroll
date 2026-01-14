---
layout: default
title: Structure Detection for Contextual Reinforcement Learning
---

# Structure Detection for Contextual Reinforcement Learning
**arXiv**：[2601.08120v1](https://arxiv.org/abs/2601.08120) · [PDF](https://arxiv.org/pdf/2601.08120.pdf)  
**作者**：Tianyue Zhou, Jung-Hoon Cho, Cathy Wu  

**一句话要点**：提出SD-MBTL框架，通过在线结构检测指导源任务选择以优化上下文强化学习性能。

**关键词**：上下文强化学习, 结构检测, 模型迁移学习, 多任务学习, 高斯过程, 连续控制

## 3 点简述
- 核心问题：上下文强化学习中传统方法存在计算成本高或负迁移问题，需适应不同CMDP结构。
- 方法要点：SD-MBTL动态识别CMDP泛化结构，如Mountain结构，并自适应切换基于高斯过程或聚类的算法。
- 实验或效果：在合成数据和多个基准测试中，M/GP-MBTL比先前最佳方法提升12.49%的聚合指标。

## 摘要（原文）

> Contextual Reinforcement Learning (CRL) tackles the problem of solving a set of related Contextual Markov Decision Processes (CMDPs) that vary across different context variables. Traditional approaches--independent training and multi-task learning--struggle with either excessive computational costs or negative transfer. A recently proposed multi-policy approach, Model-Based Transfer Learning (MBTL), has demonstrated effectiveness by strategically selecting a few tasks to train and zero-shot transfer. However, CMDPs encompass a wide range of problems, exhibiting structural properties that vary from problem to problem. As such, different task selection strategies are suitable for different CMDPs. In this work, we introduce Structure Detection MBTL (SD-MBTL), a generic framework that dynamically identifies the underlying generalization structure of CMDP and selects an appropriate MBTL algorithm. For instance, we observe Mountain structure in which generalization performance degrades from the training performance of the target task as the context difference increases. We thus propose M/GP-MBTL, which detects the structure and adaptively switches between a Gaussian Process-based approach and a clustering-based approach. Extensive experiments on synthetic data and CRL benchmarks--covering continuous control, traffic control, and agricultural management--show that M/GP-MBTL surpasses the strongest prior method by 12.49% on the aggregated metric. These results highlight the promise of online structure detection for guiding source task selection in complex CRL environments.

