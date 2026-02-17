---
layout: default
title: Removing Planner Bias in Goal Recognition Through Multi-Plan Dataset Generation
---

# Removing Planner Bias in Goal Recognition Through Multi-Plan Dataset Generation
**arXiv**：[2602.14691v1](https://arxiv.org/abs/2602.14691) · [PDF](https://arxiv.org/pdf/2602.14691.pdf)  
**作者**：Mustafa F. Abdelwahed, Felipe Meneguzzi Kin Max Piamolini Gusmao, Joan Espasa  

**一句话要点**：提出基于top-k规划的多计划数据集生成方法，以消除目标识别中的规划器偏差。

**关键词**：目标识别, 规划器偏差, 多计划生成, top-k规划, 版本覆盖分数, 低可观测性

## 3 点简述
- 现有目标识别数据集存在由启发式前向搜索规划器引入的系统性偏差，影响评估。
- 使用top-k规划为同一目标生成多个不同计划，构建无偏基准并引入版本覆盖分数度量。
- 实验表明，在低可观测性下，当前最先进目标识别器的鲁棒性显著下降。

## 摘要（原文）

> Autonomous agents require some form of goal and plan recognition to interact in multiagent settings. Unfortunately, all existing goal recognition datasets suffer from a systematical bias induced by the planning systems that generated them, namely heuristic-based forward search. This means that existing datasets lack enough challenge for more realistic scenarios (e.g., agents using different planners), which impacts the evaluation of goal recognisers with respect to using different planners for the same goal. In this paper, we propose a new method that uses top-k planning to generate multiple, different, plans for the same goal hypothesis, yielding benchmarks that mitigate the bias found in the current dataset. This allows us to introduce a new metric called Version Coverage Score (VCS) to measure the resilience of the goal recogniser when inferring a goal based on different sets of plans. Our results show that the resilience of the current state-of-the-art goal recogniser degrades substantially under low observability settings.

