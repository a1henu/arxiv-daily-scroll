---
layout: default
title: SparScene: Efficient Traffic Scene Representation via Sparse Graph Learning for Large-Scale Trajectory Generation
---

# SparScene: Efficient Traffic Scene Representation via Sparse Graph Learning for Large-Scale Trajectory Generation
**arXiv**：[2512.21133v1](https://arxiv.org/abs/2512.21133) · [PDF](https://arxiv.org/pdf/2512.21133.pdf)  
**作者**：Xiaoyu Mo, Jintian Ge, Zifan Wang, Chen Lv, Karl Henrik Johansson  

**一句话要点**：提出SparScene稀疏图学习框架，以高效表示大规模交通场景并生成轨迹

**关键词**：稀疏图学习, 交通场景表示, 轨迹生成, 多智能体交互, 自动驾驶

## 3 点简述
- 核心问题：现有方法使用密集图结构建模交通交互，导致计算冗余和效率低下，难以扩展至复杂场景
- 方法要点：基于车道图拓扑构建稀疏连接，采用轻量图编码器高效聚合智能体与地图、智能体间的交互
- 实验效果：在Waymo数据集上实现竞争性性能，可高效处理数千智能体和车道，推理时间短且内存占用低

## 摘要（原文）

> Multi-agent trajectory generation is a core problem for autonomous driving and intelligent transportation systems. However, efficiently modeling the dynamic interactions between numerous road users and infrastructures in complex scenes remains an open problem. Existing methods typically employ distance-based or fully connected dense graph structures to capture interaction information, which not only introduces a large number of redundant edges but also requires complex and heavily parameterized networks for encoding, thereby resulting in low training and inference efficiency, limiting scalability to large and complex traffic scenes. To overcome the limitations of existing methods, we propose SparScene, a sparse graph learning framework designed for efficient and scalable traffic scene representation. Instead of relying on distance thresholds, SparScene leverages the lane graph topology to construct structure-aware sparse connections between agents and lanes, enabling efficient yet informative scene graph representation. SparScene adopts a lightweight graph encoder that efficiently aggregates agent-map and agent-agent interactions, yielding compact scene representations with substantially improved efficiency and scalability. On the motion prediction benchmark of the Waymo Open Motion Dataset (WOMD), SparScene achieves competitive performance with remarkable efficiency. It generates trajectories for more than 200 agents in a scene within 5 ms and scales to more than 5,000 agents and 17,000 lanes with merely 54 ms of inference time with a GPU memory of 2.9 GB, highlighting its superior scalability for large-scale traffic scenes.

