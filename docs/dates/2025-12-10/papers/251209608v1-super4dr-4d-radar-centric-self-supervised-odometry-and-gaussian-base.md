---
layout: default
title: Super4DR: 4D Radar-centric Self-supervised Odometry and Gaussian-based Map Optimization
---

# Super4DR: 4D Radar-centric Self-supervised Odometry and Gaussian-based Map Optimization
**arXiv**：[2512.09608v1](https://arxiv.org/abs/2512.09608) · [PDF](https://arxiv.org/pdf/2512.09608.pdf)  
**作者**：Zhiheng Li, Weihua Wang, Qiang Shen, Yichen Zhao, Zheng Fang  

**一句话要点**：提出Super4DR框架，以4D雷达为中心，通过自监督里程计和高斯地图优化解决恶劣环境下的SLAM问题。

**关键词**：4D雷达SLAM, 自监督里程计, 高斯地图优化, 恶劣环境感知, 多模态渲染

## 3 点简述
- 核心问题：4D雷达点云稀疏噪声导致里程计不准和地图结构模糊不完整。
- 方法要点：设计聚类感知里程计网络和自监督机制，结合3D高斯表示与雷达特定策略优化地图。
- 实验或效果：性能提升67%，接近监督里程计，缩小与LiDAR地图质量差距并支持多模态渲染。

## 摘要（原文）

> Conventional SLAM systems using visual or LiDAR data often struggle in poor lighting and severe weather. Although 4D radar is suited for such environments, its sparse and noisy point clouds hinder accurate odometry estimation, while the radar maps suffer from obscure and incomplete structures. Thus, we propose Super4DR, a 4D radar-centric framework for learning-based odometry estimation and gaussian-based map optimization. First, we design a cluster-aware odometry network that incorporates object-level cues from the clustered radar points for inter-frame matching, alongside a hierarchical self-supervision mechanism to overcome outliers through spatio-temporal consistency, knowledge transfer, and feature contrast. Second, we propose using 3D gaussians as an intermediate representation, coupled with a radar-specific growth strategy, selective separation, and multi-view regularization, to recover blurry map areas and those undetected based on image texture. Experiments show that Super4DR achieves a 67% performance gain over prior self-supervised methods, nearly matches supervised odometry, and narrows the map quality disparity with LiDAR while enabling multi-modal image rendering.

