---
layout: default
title: Pandar128 dataset for lane line detection
---

# Pandar128 dataset for lane line detection
**arXiv**：[2511.07084v1](https://arxiv.org/abs/2511.07084) · [PDF](https://arxiv.org/pdf/2511.07084.pdf)  
**作者**：Filip Beránek, Václav Diviš, Ivan Gruber  

**一句话要点**：提出Pandar128数据集和SimpleLidarLane方法以提升LiDAR车道线检测性能

**关键词**：LiDAR车道线检测, BEV分割, 多传感器数据集, 轻量级方法, 标准化评估

## 3 点简述
- 核心问题：缺乏大规模LiDAR车道线检测数据集和标准化评估方法。
- 方法要点：引入128光束LiDAR数据集，并开发轻量级BEV分割与聚类基线方法。
- 实验或效果：方法在雨、稀疏点云等挑战条件下表现强劲，支持投影和融合任务。

## 摘要（原文）

> We present Pandar128, the largest public dataset for lane line detection
> using a 128-beam LiDAR. It contains over 52,000 camera frames and 34,000 LiDAR
> scans, captured in diverse real-world conditions in Germany. The dataset
> includes full sensor calibration (intrinsics, extrinsics) and synchronized
> odometry, supporting tasks such as projection, fusion, and temporal modeling.
>   To complement the dataset, we also introduce SimpleLidarLane, a light-weight
> baseline method for lane line reconstruction that combines BEV segmentation,
> clustering, and polyline fitting. Despite its simplicity, our method achieves
> strong performance under challenging various conditions (e.g., rain, sparse
> returns), showing that modular pipelines paired with high-quality data and
> principled evaluation can compete with more complex approaches.
>   Furthermore, to address the lack of standardized evaluation, we propose a
> novel polyline-based metric - Interpolation-Aware Matching F1 (IAM-F1) - that
> employs interpolation-aware lateral matching in BEV space.
>   All data and code are publicly released to support reproducibility in
> LiDAR-based lane detection.

