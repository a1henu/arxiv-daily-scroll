---
layout: default
title: Beyond Code Contributions: How Network Position, Temporal Bursts, and Code Review Activities Shape Contributor Influence in Large-Scale Open Source Ecosystems
---

# Beyond Code Contributions: How Network Position, Temporal Bursts, and Code Review Activities Shape Contributor Influence in Large-Scale Open Source Ecosystems
**arXiv**：[2602.06426v1](https://arxiv.org/abs/2602.06426) · [PDF](https://arxiv.org/pdf/2602.06426.pdf)  
**作者**：S M Rakib Ul Karim, Wenyi Lu, Sean Goggins  

**一句话要点**：分析开源贡献者网络位置、时间爆发和代码审查活动如何影响影响力，基于图神经网络和时序网络分析。

**关键词**：开源贡献者网络, 图神经网络, 时序网络分析, 影响力分析, 社区健康指标, 结构完整性模拟

## 3 点简述
- 核心问题：开源贡献者网络中的影响力分布不均，少数贡献者控制大部分影响力，影响社区健康。
- 方法要点：使用GPU加速PageRank、中介中心性和自定义LSTM模型，识别五种贡献者角色并分析网络结构。
- 实验或效果：通过统计分析和结构完整性模拟，发现桥接贡献者对网络凝聚力有不成比例的影响，提供实证支持策略。

## 摘要（原文）

> Open source software (OSS) projects rely on complex networks of contributors whose interactions drive innovation and sustainability. This study presents a comprehensive analysis of OSS contributor networks using advanced graph neural networks and temporal network analysis on data spanning 25 years from the Cloud Native Computing Foundation ecosystem, encompassing sandbox, incubating, and graduated projects. Our analysis of thousands of contributors across hundreds of repositories reveals that OSS networks exhibit strong power-law distributions in influence, with the top 1\% of contributors controlling a substantial portion of network influence. Using GPU-accelerated PageRank, betweenness centrality, and custom LSTM models, we identify five distinct contributor roles: Core, Bridge, Connector, Regular, and Peripheral, each with unique network positions and structural importance. Statistical analysis reveals significant correlations between specific action types (commits, pull requests, issues) and contributor influence, with multiple regression models explaining substantial variance in influence metrics. Temporal analysis shows that network density, clustering coefficients, and modularity exhibit statistically significant temporal trends, with distinct regime changes coinciding with major project milestones. Structural integrity simulations show that Bridge contributors, despite representing a small fraction of the network, have a disproportionate impact on network cohesion when removed. Our findings provide empirical evidence for strategic contributor retention policies and offer actionable insights into community health metrics.

