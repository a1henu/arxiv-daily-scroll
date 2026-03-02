---
layout: default
title: Egocentric Visibility-Aware Human Pose Estimation
---

# Egocentric Visibility-Aware Human Pose Estimation
**arXiv**：[2602.23618v1](https://arxiv.org/abs/2602.23618) · [PDF](https://arxiv.org/pdf/2602.23618.pdf)  
**作者**：Peng Dai, Yu Zhang, Yiqiang Feng, Zhen Fan, Yang Zhang  

**一句话要点**：提出EvaPose方法以解决头戴设备中关键点不可见性对姿态估计的影响

**关键词**：头戴式姿态估计, 关键点可见性, 数据集构建, 可见性感知方法, VR/AR应用

## 3 点简述
- 核心问题：现有头戴式姿态估计数据集缺乏关键点可见性标注，方法忽视不可见性，影响准确度。
- 方法要点：构建Eva-3M数据集并标注可见性，提出EvaPose方法显式利用可见性信息提升估计精度。
- 实验或效果：实验验证可见性标签的价值，EvaPose在Eva-3M和EMHI数据集上达到最先进性能。

## 摘要（原文）

> Egocentric human pose estimation (HPE) using a head-mounted device is crucial for various VR and AR applications, but it faces significant challenges due to keypoint invisibility. Nevertheless, none of the existing egocentric HPE datasets provide keypoint visibility annotations, and the existing methods often overlook the invisibility problem, treating visible and invisible keypoints indiscriminately during estimation. As a result, their capacity to accurately predict visible keypoints is compromised. In this paper, we first present Eva-3M, a large-scale egocentric visibility-aware HPE dataset comprising over 3.0M frames, with 435K of them annotated with keypoint visibility labels. Additionally, we augment the existing EMHI dataset with keypoint visibility annotations to further facilitate the research in this direction. Furthermore, we propose EvaPose, a novel egocentric visibility-aware HPE method that explicitly incorporates visibility information to enhance pose estimation accuracy. Extensive experiments validate the significant value of ground-truth visibility labels in egocentric HPE settings, and demonstrate that our EvaPose achieves state-of-the-art performance in both Eva-3M and EMHI datasets.

