---
layout: default
title: HandMCM: Multi-modal Point Cloud-based Correspondence State Space Model for 3D Hand Pose Estimation
---

# HandMCM: Multi-modal Point Cloud-based Correspondence State Space Model for 3D Hand Pose Estimation
**arXiv**：[2602.01586v1](https://arxiv.org/abs/2602.01586) · [PDF](https://arxiv.org/pdf/2602.01586.pdf)  
**作者**：Wencan Cheng, Gim Hee Lee  

**一句话要点**：提出HandMCM，基于状态空间模型增强多模态点云对应性，以解决3D手部姿态估计中的遮挡挑战。

**关键词**：3D手部姿态估计, 状态空间模型, 多模态特征, 点云对应性, 遮挡处理

## 3 点简述
- 核心问题：手部自遮挡和物体交互遮挡导致3D手部关键点定位困难。
- 方法要点：结合局部信息注入/过滤和对应性建模，利用状态空间模型学习动态关键点拓扑。
- 实验或效果：在三个基准数据集上显著优于现有方法，尤其在严重遮挡场景中表现突出。

## 摘要（原文）

> 3D hand pose estimation that involves accurate estimation of 3D human hand keypoint locations is crucial for many human-computer interaction applications such as augmented reality. However, this task poses significant challenges due to self-occlusion of the hands and occlusions caused by interactions with objects. In this paper, we propose HandMCM to address these challenges. Our HandMCM is a novel method based on the powerful state space model (Mamba). By incorporating modules for local information injection/filtering and correspondence modeling, the proposed correspondence Mamba effectively learns the highly dynamic kinematic topology of keypoints across various occlusion scenarios. Moreover, by integrating multi-modal image features, we enhance the robustness and representational capacity of the input, leading to more accurate hand pose estimation. Empirical evaluations on three benchmark datasets demonstrate that our model significantly outperforms current state-of-the-art methods, particularly in challenging scenarios involving severe occlusions. These results highlight the potential of our approach to advance the accuracy and reliability of 3D hand pose estimation in practical applications.

