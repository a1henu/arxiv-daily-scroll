---
layout: default
title: GrandTour: A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation
---

# GrandTour: A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation
**arXiv**：[2602.18164v1](https://arxiv.org/abs/2602.18164) · [PDF](https://arxiv.org/pdf/2602.18164.pdf)  
**作者**：Jonas Frey, Turcan Tuna, Frank Fu, Katharine Patterson, Tianao Xu, Maurice Fallon, Cesar Cadena, Marco Hutter  

**一句话要点**：提出GrandTour数据集以解决野外环境下腿式机器人多模态感知与状态估计的数据缺失问题

**关键词**：腿式机器人数据集, 多模态感知, 状态估计, SLAM, 传感器融合, 野外环境

## 3 点简述
- 核心问题：缺乏大规模公开腿式机器人数据集，难以开发和评估复杂环境下的算法
- 方法要点：使用ANYmal-D四足机器人搭载多模态传感器，在多样户外和室内环境中采集同步数据
- 实验或效果：提供高精度地面真值轨迹，支持SLAM、状态估计和多模态学习研究

## 摘要（原文）

> Accurate state estimation and multi-modal perception are prerequisites for autonomous legged robots in complex, large-scale environments. To date, no large-scale public legged-robot dataset captures the real-world conditions needed to develop and benchmark algorithms for legged-robot state estimation, perception, and navigation. To address this, we introduce the GrandTour dataset, a multi-modal legged-robotics dataset collected across challenging outdoor and indoor environments, featuring an ANYbotics ANYmal-D quadruped equipped with the \boxi multi-modal sensor payload. GrandTour spans a broad range of environments and operational scenarios across distinct test sites, ranging from alpine scenery and forests to demolished buildings and urban areas, and covers a wide variation in scale, complexity, illumination, and weather conditions. The dataset provides time-synchronized sensor data from spinning LiDARs, multiple RGB cameras with complementary characteristics, proprioceptive sensors, and stereo depth cameras. Moreover, it includes high-precision ground-truth trajectories from satellite-based RTK-GNSS and a Leica Geosystems total station. This dataset supports research in SLAM, high-precision state estimation, and multi-modal learning, enabling rigorous evaluation and development of new approaches to sensor fusion in legged robotic systems. With its extensive scope, GrandTour represents the largest open-access legged-robotics dataset to date. The dataset is available at https://grand-tour.leggedrobotics.com, on HuggingFace (ROS-independent), and in ROS formats, along with tools and demo resources.

