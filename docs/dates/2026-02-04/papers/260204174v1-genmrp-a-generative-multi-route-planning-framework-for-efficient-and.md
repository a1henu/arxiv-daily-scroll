---
layout: default
title: GenMRP: A Generative Multi-Route Planning Framework for Efficient and Personalized Real-Time Industrial Navigation
---

# GenMRP: A Generative Multi-Route Planning Framework for Efficient and Personalized Real-Time Industrial Navigation
**arXiv**：[2602.04174v1](https://arxiv.org/abs/2602.04174) · [PDF](https://arxiv.org/pdf/2602.04174.pdf)  
**作者**：Chengzhang Wang, Chao Chen, Jun Tao, Tengfei Liu, He Bai, Song Wang, Longfei Xu, Kaikui Liu, Xiangxiang Chu  

**一句话要点**：提出GenMRP生成式多路线规划框架，以解决工业导航中效率与个性化平衡问题。

**关键词**：多路线规划, 生成式方法, 工业导航, 实时系统, 个性化路由

## 3 点简述
- 现有方法在工业导航中面临效率与个性化不足的挑战，如预计算法缺乏多样性，生成方法效率低。
- GenMRP采用骨架-毛细血管法构建子网络，结合校正提升迭代生成路线，平衡质量与多样性。
- 实验显示GenMRP在离线与在线环境中高效且性能领先，已部署于实际导航应用。

## 摘要（原文）

> Existing industrial-scale navigation applications contend with massive road networks, typically employing two main categories of approaches for route planning. The first relies on precomputed road costs for optimal routing and heuristic algorithms for generating alternatives, while the second, generative methods, has recently gained significant attention. However, the former struggles with personalization and route diversity, while the latter fails to meet the efficiency requirements of large-scale real-time scenarios. To address these limitations, we propose GenMRP, a generative framework for multi-route planning. To ensure generation efficiency, GenMRP first introduces a skeleton-to-capillary approach that dynamically constructs a relevant sub-network significantly smaller than the full road network. Within this sub-network, routes are generated iteratively. The first iteration identifies the optimal route, while the subsequent ones generate alternatives that balance quality and diversity using the newly proposed correctional boosting approach. Each iteration incorporates road features, user historical sequences, and previously generated routes into a Link Cost Model to update road costs, followed by route generation using the Dijkstra algorithm. Extensive experiments show that GenMRP achieves state-of-the-art performance with high efficiency in both offline and online environments. To facilitate further research, we have publicly released the training and evaluation dataset. GenMRP has been fully deployed in a real-world navigation app, demonstrating its effectiveness and benefits.

