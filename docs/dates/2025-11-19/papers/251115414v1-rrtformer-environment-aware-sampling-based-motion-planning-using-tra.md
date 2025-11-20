---
layout: default
title: RRT*former: Environment-Aware Sampling-Based Motion Planning using Transformer
---

# RRT*former: Environment-Aware Sampling-Based Motion Planning using Transformer
**arXiv**：[2511.15414v1](https://arxiv.org/abs/2511.15414) · [PDF](https://arxiv.org/pdf/2511.15414.pdf)  
**作者**：Mingyang Feng, Shaoyuan Li, Xiang Yin  

**一句话要点**：提出RRT*former以在复杂动态环境中改进机器人路径规划

**关键词**：路径规划, 采样算法, Transformer网络, 机器人导航, 动态环境

## 3 点简述
- 核心问题：采样路径规划忽略环境信息和历史样本，影响最优性和效率。
- 方法要点：将Transformer与RRT*结合，利用环境和样本信息指导采样。
- 实验效果：相比RRT*等算法，路径最优性和采样效率显著提升。

## 摘要（原文）

> We investigate the sampling-based optimal path planning problem for robotics in complex and dynamic environments. Most existing sampling-based algorithms neglect environmental information or the information from previous samples. Yet, these pieces of information are highly informative, as leveraging them can provide better heuristics when sampling the next state. In this paper, we propose a novel sampling-based planning algorithm, called \emph{RRT*former}, which integrates the standard RRT* algorithm with a Transformer network in a novel way. Specifically, the Transformer is used to extract features from the environment and leverage information from previous samples to better guide the sampling process. Our extensive experiments demonstrate that, compared to existing sampling-based approaches such as RRT*, Neural RRT*, and their variants, our algorithm achieves considerable improvements in both the optimality of the path and sampling efficiency. The code for our implementation is available on https://github.com/fengmingyang666/RRTformer.

