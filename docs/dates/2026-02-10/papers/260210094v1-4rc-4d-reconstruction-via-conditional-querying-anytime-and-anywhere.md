---
layout: default
title: 4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere
---

# 4RC: 4D Reconstruction via Conditional Querying Anytime and Anywhere
**arXiv**：[2602.10094v1](https://arxiv.org/abs/2602.10094) · [PDF](https://arxiv.org/pdf/2602.10094.pdf)  
**作者**：Yihang Luo, Shangchen Zhou, Yushi Lan, Xingang Pan, Chen Change Loy  

**一句话要点**：提出4RC框架，通过条件查询实现单目视频的4D重建，统一捕获几何与运动动态。

**关键词**：4D重建, 单目视频, Transformer编码, 条件查询, 几何与运动联合建模

## 3 点简述
- 核心问题：现有方法常解耦运动与几何或仅生成稀疏轨迹，难以捕获密集4D属性。
- 方法要点：采用编码一次、任意查询范式，通过Transformer编码视频，条件解码器高效查询几何与运动。
- 实验或效果：在多种4D重建任务中优于先前方法，验证了框架的有效性。

## 摘要（原文）

> We present 4RC, a unified feed-forward framework for 4D reconstruction from monocular videos. Unlike existing approaches that typically decouple motion from geometry or produce limited 4D attributes such as sparse trajectories or two-view scene flow, 4RC learns a holistic 4D representation that jointly captures dense scene geometry and motion dynamics. At its core, 4RC introduces a novel encode-once, query-anywhere and anytime paradigm: a transformer backbone encodes the entire video into a compact spatio-temporal latent space, from which a conditional decoder can efficiently query 3D geometry and motion for any query frame at any target timestamp. To facilitate learning, we represent per-view 4D attributes in a minimally factorized form by decomposing them into base geometry and time-dependent relative motion. Extensive experiments demonstrate that 4RC outperforms prior and concurrent methods across a wide range of 4D reconstruction tasks.

