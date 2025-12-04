---
layout: default
title: CSMapping: Scalable Crowdsourced Semantic Mapping and Topology Inference for Autonomous Driving
---

# CSMapping: Scalable Crowdsourced Semantic Mapping and Topology Inference for Autonomous Driving
**arXiv**：[2512.03510v1](https://arxiv.org/abs/2512.03510) · [PDF](https://arxiv.org/pdf/2512.03510.pdf)  
**作者**：Zhijian Qiao, Zehuan Yu, Tong Li, Chih-Chung Chou, Wenchao Ding, Shaojie Shen  

**一句话要点**：提出CSMapping系统，通过生成先验和优化方法实现可扩展的众包语义地图与拓扑推断，用于自动驾驶

**关键词**：众包语义地图, 潜在扩散模型, 拓扑推断, 自动驾驶地图构建, 约束优化, 轨迹聚类

## 3 点简述
- 核心问题：低成本传感器噪声限制众包地图质量随数据量提升，需鲁棒方法处理噪声和未观测区域
- 方法要点：结合潜在扩散模型学习地图结构先验，通过约束优化在潜在空间生成准确语义地图；使用聚类和运动学细化提取拓扑道路中心线
- 实验或效果：在公开和专有数据集上实现最先进的语义和拓扑映射性能，展示可扩展性和鲁棒性

## 摘要（原文）

> Crowdsourcing enables scalable autonomous driving map construction, but low-cost sensor noise hinders quality from improving with data volume. We propose CSMapping, a system that produces accurate semantic maps and topological road centerlines whose quality consistently increases with more crowdsourced data. For semantic mapping, we train a latent diffusion model on HD maps (optionally conditioned on SD maps) to learn a generative prior of real-world map structure, without requiring paired crowdsourced/HD-map supervision. This prior is incorporated via constrained MAP optimization in latent space, ensuring robustness to severe noise and plausible completion in unobserved areas. Initialization uses a robust vectorized mapping module followed by diffusion inversion; optimization employs efficient Gaussian-basis reparameterization, projected gradient descent zobracket multi-start, and latent-space factor-graph for global consistency. For topological mapping, we apply confidence-weighted k-medoids clustering and kinematic refinement to trajectories, yielding smooth, human-like centerlines robust to trajectory variation. Experiments on nuScenes, Argoverse 2, and a large proprietary dataset achieve state-of-the-art semantic and topological mapping performance, with thorough ablation and scalability studies.

