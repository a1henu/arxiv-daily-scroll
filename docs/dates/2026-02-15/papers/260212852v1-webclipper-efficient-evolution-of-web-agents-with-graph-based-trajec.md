---
layout: default
title: WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning
---

# WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning
**arXiv**：[2602.12852v1](https://arxiv.org/abs/2602.12852) · [PDF](https://arxiv.org/pdf/2602.12852.pdf)  
**作者**：Junjie Wang, Zequn Xie, Dan Yang, Jie Feng, Yue Shen, Duolin Sun, Meixiu Long, Yihan Jiao, Zhehao Tan, Jian Wang, Peng Wei, Jinjie Gu  

**一句话要点**：提出WebClipper框架，通过基于图的轨迹剪枝优化网络代理的搜索效率

**关键词**：网络代理, 轨迹剪枝, 图优化, 搜索效率, 工具调用, F-AE评分

## 3 点简述
- 核心问题：现有网络代理存在长工具调用轨迹、循环推理和无效分支探索，导致搜索效率低下
- 方法要点：将搜索过程建模为状态图，通过最小必要有向无环图挖掘进行轨迹剪枝，保留关键推理
- 实验或效果：剪枝后训练使工具调用轮数减少约20%，同时提升准确性，并引入F-AE评分平衡性能与效率

## 摘要（原文）

> Deep Research systems based on web agents have shown strong potential in solving complex information-seeking tasks, yet their search efficiency remains underexplored. We observe that many state-of-the-art open-source web agents rely on long tool-call trajectories with cyclic reasoning loops and exploration of unproductive branches. To address this, we propose WebClipper, a framework that compresses web agent trajectories via graph-based pruning. Concretely, we model the agent's search process as a state graph and cast trajectory optimization as a minimum-necessary Directed Acyclic Graph (DAG) mining problem, yielding pruned trajectories that preserve essential reasoning while eliminating redundant steps. Continued training on these refined trajectories enables the agent to evolve toward more efficient search patterns and reduces tool-call rounds by about 20% while improving accuracy. Furthermore, we introduce a new metric called F-AE Score to measure the model's overall performance in balancing accuracy and efficiency. Experiments demonstrate that WebClipper compresses tool-call rounds under excellent performance, providing practical insight into balancing effectiveness and efficiency in web agent design.

