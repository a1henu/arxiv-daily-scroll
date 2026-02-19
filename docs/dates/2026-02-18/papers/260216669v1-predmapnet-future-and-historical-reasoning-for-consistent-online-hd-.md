---
layout: default
title: PredMapNet: Future and Historical Reasoning for Consistent Online HD Vectorized Map Construction
---

# PredMapNet: Future and Historical Reasoning for Consistent Online HD Vectorized Map Construction
**arXiv**：[2602.16669v1](https://arxiv.org/abs/2602.16669) · [PDF](https://arxiv.org/pdf/2602.16669.pdf)  
**作者**：Bo Lang, Nirav Savaliya, Zhihao Zheng, Jinglun Feng, Zheng-Hang Yeh, Mooi Choo Chuah  

**一句话要点**：提出PredMapNet框架，通过联合跟踪与预测解决在线高精地图构建的时序不一致问题。

**关键词**：高精地图构建, 时序一致性, 地图实例跟踪, 短期预测, 自动驾驶感知

## 3 点简述
- 核心问题：现有查询方法因随机初始化和隐式时序建模导致地图构建的时序不一致和不稳定。
- 方法要点：引入语义感知查询生成器、历史栅格化地图记忆、历史地图引导模块和短期未来引导模块，实现显式历史先验和未来预测。
- 实验或效果：在nuScenes和Argoverse2数据集上超越现有方法，展示高效性能。

## 摘要（原文）

> High-definition (HD) maps are crucial to autonomous driving, providing structured representations of road elements to support navigation and planning. However, existing query-based methods often employ random query initialization and depend on implicit temporal modeling, which lead to temporal inconsistencies and instabilities during the construction of a global map. To overcome these challenges, we introduce a novel end-to-end framework for consistent online HD vectorized map construction, which jointly performs map instance tracking and short-term prediction. First, we propose a Semantic-Aware Query Generator that initializes queries with spatially aligned semantic masks to capture scene-level context globally. Next, we design a History Rasterized Map Memory to store fine-grained instance-level maps for each tracked instance, enabling explicit historical priors. A History-Map Guidance Module then integrates rasterized map information into track queries, improving temporal continuity. Finally, we propose a Short-Term Future Guidance module to forecast the immediate motion of map instances based on the stored history trajectories. These predicted future locations serve as hints for tracked instances to further avoid implausible predictions and keep temporal consistency. Extensive experiments on the nuScenes and Argoverse2 datasets demonstrate that our proposed method outperforms state-of-the-art (SOTA) methods with good efficiency.

