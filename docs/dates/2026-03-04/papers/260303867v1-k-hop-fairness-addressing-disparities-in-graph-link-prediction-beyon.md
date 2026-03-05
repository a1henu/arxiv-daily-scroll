---
layout: default
title: k-hop Fairness: Addressing Disparities in Graph Link Prediction Beyond First-Order Neighborhoods
---

# k-hop Fairness: Addressing Disparities in Graph Link Prediction Beyond First-Order Neighborhoods
**arXiv**：[2603.03867v1](https://arxiv.org/abs/2603.03867) · [PDF](https://arxiv.org/pdf/2603.03867.pdf)  
**作者**：Lilian Marey, Tiphaine Viard, Charlotte Laclau  

**一句话要点**：提出k-hop公平性以解决图链接预测中超越一阶邻域的结构偏差问题

**关键词**：图链接预测, 公平性学习, 结构偏差, k-hop公平性, 后处理策略

## 3 点简述
- 核心问题：现有公平链接预测方法仅关注节点间敏感属性差异，忽略组内结构偏差。
- 方法要点：引入k-hop公平性概念，基于节点距离评估和缓解预测与结构偏差。
- 实验或效果：实验显示模型在不同k-hop重现偏差，后处理方法优于现有基线。

## 摘要（原文）

> Link prediction (LP) plays a central role in graph-based applications, particularly in social recommendation. However, real-world graphs often reflect structural biases, most notably homophily, the tendency of nodes with similar attributes to connect. While this property can improve predictive performance, it also risks reinforcing existing social disparities. In response, fairness-aware LP methods have emerged, often seeking to mitigate these effects by promoting inter-group connections, that is, links between nodes with differing sensitive attributes (e.g., gender), following the principle of dyadic fairness. However, dyadic fairness overlooks potential disparities within the sensitive groups themselves. To overcome this issue, we propose $k$-hop fairness, a structural notion of fairness for LP, that assesses disparities conditioned on the distance between nodes in the graph. We formalize this notion through predictive fairness and structural bias metrics, and propose pre- and post-processing mitigation strategies. Experiments across standard LP benchmarks reveal: (1) a strong tendency of models to reproduce structural biases at different $k$-hops; (2) interdependence between structural biases at different hops when rewiring graphs; and (3) that our post-processing method achieves favorable $k$-hop performance-fairness trade-offs compared to existing fair LP baselines.

