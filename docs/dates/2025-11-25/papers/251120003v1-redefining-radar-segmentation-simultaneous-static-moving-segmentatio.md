---
layout: default
title: Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds
---

# Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds
**arXiv**：[2511.20003v1](https://arxiv.org/abs/2511.20003) · [PDF](https://arxiv.org/pdf/2511.20003.pdf)  
**作者**：Simin Zhu, Satish Ravindran, Alexander Yarovoy, Francesco Fioranelli  

**一句话要点**：提出神经网络方法，同时分割雷达点云中的静态与动态物体并估计自车运动。

**关键词**：雷达点云分割, 动静物体区分, 自车运动估计, 神经网络方法, 雷达感知任务

## 3 点简述
- 核心问题：雷达感知需区分物体动静，传统方法依赖类别标签，但动静区分更关键。
- 方法要点：使用MLP和RNN从原始点云直接提取特征，无需预处理步骤。
- 实验效果：在RadarScenes数据集上表现良好，验证双任务可行性。

## 摘要（原文）

> Conventional radar segmentation research has typically focused on learning category labels for different moving objects. Although fundamental differences between radar and optical sensors lead to differences in the reliability of predicting accurate and consistent category labels, a review of common radar perception tasks in automotive reveals that determining whether an object is moving or static is a prerequisite for most tasks. To fill this gap, this study proposes a neural network based solution that can simultaneously segment static and moving objects from radar point clouds. Furthermore, since the measured radial velocity of static objects is correlated with the motion of the radar, this approach can also estimate the instantaneous 2D velocity of the moving platform or vehicle (ego motion). However, despite performing dual tasks, the proposed method employs very simple yet effective building blocks for feature extraction: multi layer perceptrons (MLPs) and recurrent neural networks (RNNs). In addition to being the first of its kind in the literature, the proposed method also demonstrates the feasibility of extracting the information required for the dual task directly from unprocessed point clouds, without the need for cloud aggregation, Doppler compensation, motion compensation, or any other intermediate signal processing steps. To measure its performance, this study introduces a set of novel evaluation metrics and tests the proposed method using a challenging real world radar dataset, RadarScenes. The results show that the proposed method not only performs well on the dual tasks, but also has broad application potential in other radar perception tasks.

