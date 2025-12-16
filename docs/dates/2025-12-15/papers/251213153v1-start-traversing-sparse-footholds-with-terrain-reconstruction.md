---
layout: default
title: START: Traversing Sparse Footholds with Terrain Reconstruction
---

# START: Traversing Sparse Footholds with Terrain Reconstruction
**arXiv**：[2512.13153v1](https://arxiv.org/abs/2512.13153) · [PDF](https://arxiv.org/pdf/2512.13153.pdf)  
**作者**：Ruiqi Yu, Qianshi Wang, Hongyi Li, Zheng Jun, Zhicheng Wang, Jun Wu, Qiuguo Zhu  

**一句话要点**：提出START单阶段学习框架，实现四足机器人在稀疏立足点地形上的敏捷稳定运动。

**关键词**：四足机器人运动控制, 稀疏立足点地形, 单阶段学习框架, 地形重建, 零样本迁移, 机载视觉感知

## 3 点简述
- 核心问题：现有方法在稀疏立足点地形上存在泛化性差、感知噪声大或几何信息缺失，导致运动效率低和步态僵硬。
- 方法要点：仅利用低成本机载视觉和本体感知，精确重建局部地形高度图，提供显式中间表示以支持环境理解和立足点评估。
- 实验或效果：在多样化真实场景中实现零样本迁移，展示出优越的适应性、精确立足点放置和鲁棒运动能力。

## 摘要（原文）

> Traversing terrains with sparse footholds like legged animals presents a promising yet challenging task for quadruped robots, as it requires precise environmental perception and agile control to secure safe foot placement while maintaining dynamic stability. Model-based hierarchical controllers excel in laboratory settings, but suffer from limited generalization and overly conservative behaviors. End-to-end learning-based approaches unlock greater flexibility and adaptability, but existing state-of-the-art methods either rely on heightmaps that introduce noise and complex, costly pipelines, or implicitly infer terrain features from egocentric depth images, often missing accurate critical geometric cues and leading to inefficient learning and rigid gaits. To overcome these limitations, we propose START, a single-stage learning framework that enables agile, stable locomotion on highly sparse and randomized footholds. START leverages only low-cost onboard vision and proprioception to accurately reconstruct local terrain heightmap, providing an explicit intermediate representation to convey essential features relevant to sparse foothold regions. This supports comprehensive environmental understanding and precise terrain assessment, reducing exploration cost and accelerating skill acquisition. Experimental results demonstrate that START achieves zero-shot transfer across diverse real-world scenarios, showcasing superior adaptability, precise foothold placement, and robust locomotion.

