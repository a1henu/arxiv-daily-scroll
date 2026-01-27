---
layout: default
title: RouteMoA: Dynamic Routing without Pre-Inference Boosts Efficient Mixture-of-Agents
---

# RouteMoA: Dynamic Routing without Pre-Inference Boosts Efficient Mixture-of-Agents
**arXiv**：[2601.18130v1](https://arxiv.org/abs/2601.18130) · [PDF](https://arxiv.org/pdf/2601.18130.pdf)  
**作者**：Jize Wang, Han Wu, Zhiyuan You, Yiming Song, Yijun Wang, Zifei Shan, Yining Li, Songyang Zhang, Xinyi Le, Cailian Chen, Xinping Guan, Dacheng Tao  

**一句话要点**：提出RouteMoA框架，通过动态路由解决混合代理中成本与延迟高的问题。

**关键词**：混合代理, 动态路由, 轻量级评分, 模型选择, 成本优化, 延迟降低

## 3 点简述
- 核心问题：混合代理的密集拓扑导致高成本和延迟，现有方法需全模型推理后筛选。
- 方法要点：使用轻量级评分器预筛选候选模型，结合混合评估器进行后验修正，无需额外推理。
- 实验或效果：在大规模模型池中，成本降低89.8%，延迟减少63.6%，优于现有方法。

## 摘要（原文）

> Mixture-of-Agents (MoA) improves LLM performance through layered collaboration, but its dense topology raises costs and latency. Existing methods employ LLM judges to filter responses, yet still require all models to perform inference before judging, failing to cut costs effectively. They also lack model selection criteria and struggle with large model pools, where full inference is costly and can exceed context limits. To address this, we propose RouteMoA, an efficient mixture-of-agents framework with dynamic routing. It employs a lightweight scorer to perform initial screening by predicting coarse-grained performance from the query, narrowing candidates to a high-potential subset without inference. A mixture of judges then refines these scores through lightweight self- and cross-assessment based on existing model outputs, providing posterior correction without additional inference. Finally, a model ranking mechanism selects models by balancing performance, cost, and latency. RouteMoA outperforms MoA across varying tasks and model pool sizes, reducing cost by 89.8% and latency by 63.6% in the large-scale model pool.

