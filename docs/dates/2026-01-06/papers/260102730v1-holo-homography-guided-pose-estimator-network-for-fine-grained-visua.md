---
layout: default
title: HOLO: Homography-Guided Pose Estimator Network for Fine-Grained Visual Localization on SD Maps
---

# HOLO: Homography-Guided Pose Estimator Network for Fine-Grained Visual Localization on SD Maps
**arXiv**：[2601.02730v1](https://arxiv.org/abs/2601.02730) · [PDF](https://arxiv.org/pdf/2601.02730.pdf)  
**作者**：Xuchang Zhong, Xu Cao, Jinke Feng, Hao Fang  

**一句话要点**：提出基于单应性引导的姿态估计网络，用于多视图图像与SD地图间的细粒度视觉定位。

**关键词**：视觉定位, 单应性学习, BEV语义推理, SD地图, 姿态估计, 自动驾驶

## 3 点简述
- 核心问题：现有回归方法忽略几何先验，导致训练效率低和定位精度受限。
- 方法要点：通过投影地面视图特征到BEV域并强制语义对齐，利用单应性约束引导特征融合和限制姿态输出。
- 实验或效果：在nuScenes数据集上显著优于现有方法，支持跨分辨率输入提升灵活性。

## 摘要（原文）

> Visual localization on standard-definition (SD) maps has emerged as a promising low-cost and scalable solution for autonomous driving. However, existing regression-based approaches often overlook inherent geometric priors, resulting in suboptimal training efficiency and limited localization accuracy. In this paper, we propose a novel homography-guided pose estimator network for fine-grained visual localization between multi-view images and standard-definition (SD) maps. We construct input pairs that satisfy a homography constraint by projecting ground-view features into the BEV domain and enforcing semantic alignment with map features. Then we leverage homography relationships to guide feature fusion and restrict the pose outputs to a valid feasible region, which significantly improves training efficiency and localization accuracy compared to prior methods relying on attention-based fusion and direct 3-DoF pose regression. To the best of our knowledge, this is the first work to unify BEV semantic reasoning with homography learning for image-to-map localization. Furthermore, by explicitly modeling homography transformations, the proposed framework naturally supports cross-resolution inputs, enhancing model flexibility. Extensive experiments on the nuScenes dataset demonstrate that our approach significantly outperforms existing state-of-the-art visual localization methods. Code and pretrained models will be publicly released to foster future research.

