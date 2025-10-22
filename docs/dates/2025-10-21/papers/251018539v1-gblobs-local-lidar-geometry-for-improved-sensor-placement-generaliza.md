---
layout: default
title: GBlobs: Local LiDAR Geometry for Improved Sensor Placement Generalization
---

# GBlobs: Local LiDAR Geometry for Improved Sensor Placement Generalization
**arXiv**：[2510.18539v1](https://arxiv.org/abs/2510.18539) · [PDF](https://arxiv.org/pdf/2510.18539.pdf)  
**作者**：Dušan Malić, Christian Fruhwirth-Reisinger, Alexander Prutsch, Wei Lin, Samuel Schulter, Horst Possegger  

**一句话要点**：提出GBlobs局部特征描述符以解决LiDAR传感器放置变化下的3D物体检测泛化问题

**关键词**：3D物体检测, LiDAR点云, 特征描述符, 传感器泛化, 几何捷径问题

## 3 点简述
- 核心问题：传统LiDAR检测器依赖绝对坐标导致位置偏见，泛化能力差于不同传感器配置
- 方法要点：使用GBlobs作为局部点云特征，迫使网络学习以物体为中心的鲁棒表示
- 实验或效果：在RoboSense 2025挑战中实现顶尖性能，显著提升跨传感器放置的泛化能力

## 摘要（原文）

> This technical report outlines the top-ranking solution for RoboSense 2025:
> Track 3, achieving state-of-the-art performance on 3D object detection under
> various sensor placements. Our submission utilizes GBlobs, a local point cloud
> feature descriptor specifically designed to enhance model generalization across
> diverse LiDAR configurations. Current LiDAR-based 3D detectors often suffer
> from a \enquote{geometric shortcut} when trained on conventional global
> features (\ie, absolute Cartesian coordinates). This introduces a position bias
> that causes models to primarily rely on absolute object position rather than
> distinguishing shape and appearance characteristics. Although effective for
> in-domain data, this shortcut severely limits generalization when encountering
> different point distributions, such as those resulting from varying sensor
> placements. By using GBlobs as network input features, we effectively
> circumvent this geometric shortcut, compelling the network to learn robust,
> object-centric representations. This approach significantly enhances the
> model's ability to generalize, resulting in the exceptional performance
> demonstrated in this challenge.

