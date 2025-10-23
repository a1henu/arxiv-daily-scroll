---
layout: default
title: SEA: Semantic Map Prediction for Active Exploration of Uncertain Areas
---

# SEA: Semantic Map Prediction for Active Exploration of Uncertain Areas
**arXiv**：[2510.19766v1](https://arxiv.org/abs/2510.19766) · [PDF](https://arxiv.org/pdf/2510.19766.pdf)  
**作者**：Hongyu Ding, Xinyue Liang, Yudong Fang, You Wu, Jieqi Shi, Jing Huo, Wenbin Li, Jing Wu, Yu-Kun Lai, Yang Gao  

**一句话要点**：提出SEA方法，通过语义地图预测和强化学习策略提升机器人主动探索效率

**关键词**：机器人探索, 语义地图预测, 强化学习, 迭代预测框架, 主动探索策略

## 3 点简述
- 核心问题：现有学习型方法依赖单步路径点预测，缺乏长期环境理解，导致探索效率低。
- 方法要点：采用迭代预测-探索框架，预测缺失地图区域，并基于预测与实际地图差异指导探索。
- 实验效果：在相同时间限制下，显著优于现有方法，实现更高的全局地图覆盖率。

## 摘要（原文）

> In this paper, we propose SEA, a novel approach for active robot exploration
> through semantic map prediction and a reinforcement learning-based hierarchical
> exploration policy. Unlike existing learning-based methods that rely on
> one-step waypoint prediction, our approach enhances the agent's long-term
> environmental understanding to facilitate more efficient exploration. We
> propose an iterative prediction-exploration framework that explicitly predicts
> the missing areas of the map based on current observations. The difference
> between the actual accumulated map and the predicted global map is then used to
> guide exploration. Additionally, we design a novel reward mechanism that
> leverages reinforcement learning to update the long-term exploration
> strategies, enabling us to construct an accurate semantic map within limited
> steps. Experimental results demonstrate that our method significantly
> outperforms state-of-the-art exploration strategies, achieving superior
> coverage ares of the global map within the same time constraints.

