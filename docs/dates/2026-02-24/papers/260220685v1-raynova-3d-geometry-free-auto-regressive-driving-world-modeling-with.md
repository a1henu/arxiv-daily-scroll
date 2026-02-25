---
layout: default
title: RAYNOVA: 3D-Geometry-Free Auto-Regressive Driving World Modeling with Unified Spatio-Temporal Representation
---

# RAYNOVA: 3D-Geometry-Free Auto-Regressive Driving World Modeling with Unified Spatio-Temporal Representation
**arXiv**：[2602.20685v1](https://arxiv.org/abs/2602.20685) · [PDF](https://arxiv.org/pdf/2602.20685.pdf)  
**作者**：Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  

**一句话要点**：提出RAYNOVA以解决自动驾驶世界建模中时空关联分离的问题，采用几何无关的自回归框架。

**关键词**：自动驾驶世界建模, 自回归框架, 时空表示, 多视角视频生成, 几何无关建模

## 3 点简述
- 核心问题：现有方法分别处理时空关联，依赖强3D几何先验，限制泛化能力。
- 方法要点：基于相对Plücker射线位置编码构建各向同性时空表示，支持双因果自回归和全局注意力。
- 实验或效果：在nuScenes上实现多视角视频生成SOTA，泛化至新视角和相机配置，无需显式3D表示。

## 摘要（原文）

> World foundation models aim to simulate the evolution of the real world with physically plausible behavior. Unlike prior methods that handle spatial and temporal correlations separately, we propose RAYNOVA, a geometry-free world model that employs a dual-causal autoregressive framework. It follows both scale-wise and temporal topological orders in the autoregressive process, and leverages global attention for unified 4D spatio-temporal reasoning. Different from existing works that impose strong 3D geometric priors, RAYNOVA constructs an isotropic spatio-temporal representation across views, frames, and scales based on relative Plücker-ray positional encoding, enabling robust generalization to diverse camera setups and ego motions. We further introduce a recurrent training paradigm to alleviate distribution drift in long-horizon video generation. RAYNOVA achieves state-of-the-art multi-view video generation results on nuScenes, while offering higher throughput and strong controllability under diverse input conditions, generalizing to novel views and camera configurations without explicit 3D scene representation. Our code will be released at http://yichen928.github.io/raynova.

