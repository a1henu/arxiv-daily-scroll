---
layout: default
title: Precomputing Multi-Agent Path Replanning using Temporal Flexibility: A Case Study on the Dutch Railway Network
---

# Precomputing Multi-Agent Path Replanning using Temporal Flexibility: A Case Study on the Dutch Railway Network
**arXiv**：[2601.04884v1](https://arxiv.org/abs/2601.04884) · [PDF](https://arxiv.org/pdf/2601.04884.pdf)  
**作者**：Issa Hanou, Eric Kemmeren, Devin Wild Thomas, Mathijs de Weerdt  

**一句话要点**：提出FlexSIPP算法，利用时间灵活性预计算多智能体路径重规划，应用于荷兰铁路网络案例。

**关键词**：多智能体路径规划, 时间灵活性, 预计算算法, 铁路网络调度, 重规划优化

## 3 点简述
- 核心问题：多智能体执行中单个智能体延迟易引发冲突，传统重规划方法效率低或不可行。
- 方法要点：通过跟踪其他智能体的时间灵活性，预计算延迟智能体的所有可能计划，避免级联延迟。
- 实验或效果：在荷兰铁路网络案例中验证，FlexSIPP能提供有效解决方案，适应现实调整，计算时间合理。

## 摘要（原文）

> Executing a multi-agent plan can be challenging when an agent is delayed, because this typically creates conflicts with other agents. So, we need to quickly find a new safe plan. Replanning only the delayed agent often does not result in an efficient plan, and sometimes cannot even yield a feasible plan. On the other hand, replanning other agents may lead to a cascade of changes and delays. We show how to efficiently replan by tracking and using the temporal flexibility of other agents while avoiding cascading delays. This flexibility is the maximum delay an agent can take without changing the order of or further delaying more agents. Our algorithm, FlexSIPP, precomputes all possible plans for the delayed agent, also returning the changes for the other agents, for any single-agent delay within the given scenario. We demonstrate our method in a real-world case study of replanning trains in the densely-used Dutch railway network. Our experiments show that FlexSIPP provides effective solutions, relevant to real-world adjustments, and within a reasonable timeframe.

