---
layout: default
title: MobileOcc: A Human-Aware Semantic Occupancy Dataset for Mobile Robots
---

# MobileOcc: A Human-Aware Semantic Occupancy Dataset for Mobile Robots
**arXiv**：[2511.16949v1](https://arxiv.org/abs/2511.16949) · [PDF](https://arxiv.org/pdf/2511.16949.pdf)  
**作者**：Junseo Kim, Guido Dumont, Xinyu Gao, Gang Chen, Holger Caesar, Javier Alonso-Mora  

**一句话要点**：提出MobileOcc数据集以解决移动机器人在拥挤环境中语义占用感知不足的问题

**关键词**：语义占用感知, 移动机器人, 人体几何重建, LiDAR优化, 基准数据集, 3D人体姿态估计

## 3 点简述
- 核心问题：密集3D语义占用感知在移动机器人领域研究不足，尤其在行人密集环境
- 方法要点：结合静态对象标注和新型网格优化框架，从2D图像重建可变形人体几何
- 实验或效果：建立占用和行人速度预测基准，并在3D人体姿态估计中验证鲁棒性

## 摘要（原文）

> Dense 3D semantic occupancy perception is critical for mobile robots operating in pedestrian-rich environments, yet it remains underexplored compared to its application in autonomous driving. To address this gap, we present MobileOcc, a semantic occupancy dataset for mobile robots operating in crowded human environments. Our dataset is built using an annotation pipeline that incorporates static object occupancy annotations and a novel mesh optimization framework explicitly designed for human occupancy modeling. It reconstructs deformable human geometry from 2D images and subsequently refines and optimizes it using associated LiDAR point data. Using MobileOcc, we establish benchmarks for two tasks, i) Occupancy prediction and ii) Pedestrian velocity prediction, using different methods including monocular, stereo, and panoptic occupancy, with metrics and baseline implementations for reproducible comparison. Beyond occupancy prediction, we further assess our annotation method on 3D human pose estimation datasets. Results demonstrate that our method exhibits robust performance across different datasets.

