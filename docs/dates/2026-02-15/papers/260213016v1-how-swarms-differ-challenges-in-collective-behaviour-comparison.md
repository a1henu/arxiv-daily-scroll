---
layout: default
title: How Swarms Differ: Challenges in Collective Behaviour Comparison
---

# How Swarms Differ: Challenges in Collective Behaviour Comparison
**arXiv**：[2602.13016v1](https://arxiv.org/abs/2602.13016) · [PDF](https://arxiv.org/pdf/2602.13016.pdf)  
**作者**：André Fialho Jesus, Jonas Kuckling  

**一句话要点**：评估特征集与相似度度量在群体行为比较中的稳健性，并提出自组织映射方法识别难区分行为区域。

**关键词**：群体行为比较, 特征集稳健性, 相似度度量, 自组织映射, 群体机器人

## 3 点简述
- 核心问题：群体行为需数值特征表达，但现有特征集常针对特定上下文，缺乏稳健性评估。
- 方法要点：选取先前群体机器人工作中的特征集和相似度度量，分析其组合对区分相似行为的影响。
- 实验或效果：发现特征集与相似度度量的交互影响区分能力，并基于自组织映射识别特征空间中难区分行为区域。

## 摘要（原文）

> Collective behaviours often need to be expressed through numerical features, e.g., for classification or imitation learning. This problem is often addressed by proposing an ad-hoc feature set for a particular swarm behaviour context, usually without further consideration of the solution's resilience outside of the conceived context. Yet, the development of automatic methods to design swarm behaviours is dependent on the ability to measure quantitatively the similarity of swarm behaviours. Hence, we investigate the impact of feature sets for collective behaviours. We select swarm feature sets and similarity measures from prior swarm robotics works, which mainly considered a narrow behavioural context and assess their robustness. We demonstrate that the interplay of feature set and similarity measure makes some combinations more suitable to distinguish groups of similar behaviours. We also propose a self-organised map-based approach to identify regions of the feature space where behaviours cannot be easily distinguished.

