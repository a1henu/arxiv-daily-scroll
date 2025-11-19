---
layout: default
title: A Neural Field-Based Approach for View Computation & Data Exploration in 3D Urban Environments
---

# A Neural Field-Based Approach for View Computation & Data Exploration in 3D Urban Environments
**arXiv**：[2511.14742v1](https://arxiv.org/abs/2511.14742) · [PDF](https://arxiv.org/pdf/2511.14742.pdf)  
**作者**：Stefan Cobeli, Kazi Shahrukh Omar, Rodrigo Valença, Nivan Ferreira, Fabio Miranda  

**一句话要点**：提出基于神经场的视图计算方法，以解决3D城市环境数据探索中的遮挡和效率问题。

**关键词**：神经场表示, 3D城市探索, 视图计算, 遮挡避免, 隐式查询

## 3 点简述
- 核心问题：3D城市环境几何复杂，遮挡严重，手动调整视角效率低下。
- 方法要点：使用神经场构建隐式表示，支持快速视图评估和反查询。
- 实验或效果：验证了在可见性、日照和视觉影响分析中的有效性。

## 摘要（原文）

> Despite the growing availability of 3D urban datasets, extracting insights remains challenging due to computational bottlenecks and the complexity of interacting with data. In fact, the intricate geometry of 3D urban environments results in high degrees of occlusion and requires extensive manual viewpoint adjustments that make large-scale exploration inefficient. To address this, we propose a view-based approach for 3D data exploration, where a vector field encodes views from the environment. To support this approach, we introduce a neural field-based method that constructs an efficient implicit representation of 3D environments. This representation enables both faster direct queries, which consist of the computation of view assessment indices, and inverse queries, which help avoid occlusion and facilitate the search for views that match desired data patterns. Our approach supports key urban analysis tasks such as visibility assessments, solar exposure evaluation, and assessing the visual impact of new developments. We validate our method through quantitative experiments, case studies informed by real-world urban challenges, and feedback from domain experts. Results show its effectiveness in finding desirable viewpoints, analyzing building facade visibility, and evaluating views from outdoor spaces. Code and data are publicly available at https://urbantk.org/neural-3d.

