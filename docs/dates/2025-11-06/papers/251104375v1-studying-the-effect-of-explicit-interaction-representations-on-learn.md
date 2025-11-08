---
layout: default
title: Studying the Effect of Explicit Interaction Representations on Learning Scene-level Distributions of Human Trajectories
---

# Studying the Effect of Explicit Interaction Representations on Learning Scene-level Distributions of Human Trajectories
**arXiv**：[2511.04375v1](https://arxiv.org/abs/2511.04375) · [PDF](https://arxiv.org/pdf/2511.04375.pdf)  
**作者**：Anna Mészáros, Javier Alonso-Mora, Jens Kober  

**一句话要点**：研究显式交互表示对学习场景级人类轨迹分布的影响

**关键词**：人类轨迹预测, 交互表示, 场景级分布, 自主车辆决策, 神经网络建模

## 3 点简述
- 核心问题：如何最佳表示智能体间交互以学习场景级联合分布。
- 方法要点：比较隐式和显式交互表示在同一网络结构中的效果。
- 实验或效果：显式交互（如路口优先通过）常提升性能，隐式学习可能有害。

## 摘要（原文）

> Effectively capturing the joint distribution of all agents in a scene is
> relevant for predicting the true evolution of the scene and in turn providing
> more accurate information to the decision processes of autonomous vehicles.
> While new models have been developed for this purpose in recent years, it
> remains unclear how to best represent the joint distributions particularly from
> the perspective of the interactions between agents. Thus far there is no clear
> consensus on how best to represent interactions between agents; whether they
> should be learned implicitly from data by neural networks, or explicitly
> modeled using the spatial and temporal relations that are more grounded in
> human decision-making. This paper aims to study various means of describing
> interactions within the same network structure and their effect on the final
> learned joint distributions. Our findings show that more often than not, simply
> allowing a network to establish interactive connections between agents based on
> data has a detrimental effect on performance. Instead, having well defined
> interactions (such as which agent of an agent pair passes first at an
> intersection) can often bring about a clear boost in performance.

