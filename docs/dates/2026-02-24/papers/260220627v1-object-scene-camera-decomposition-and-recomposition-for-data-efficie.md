---
layout: default
title: Object-Scene-Camera Decomposition and Recomposition for Data-Efficient Monocular 3D Object Detection
---

# Object-Scene-Camera Decomposition and Recomposition for Data-Efficient Monocular 3D Object Detection
**arXiv**：[2602.20627v1](https://arxiv.org/abs/2602.20627) · [PDF](https://arxiv.org/pdf/2602.20627.pdf)  
**作者**：Zhaonian Kuang, Rui Ding, Meng Yang, Xinhu Zheng, Gang Hua  

**一句话要点**：提出对象-场景-相机分解与重组方案以提升单目3D目标检测的数据效率

**关键词**：单目3D目标检测, 数据增强, 分解与重组, 稀疏监督, 点云渲染

## 3 点简述
- 核心问题：训练数据中对象、场景和相机姿态紧密耦合，导致数据多样性不足和过拟合。
- 方法要点：在线分解训练图像为纹理化3D对象点模型和背景场景，并重组为新图像以覆盖全组合。
- 实验或效果：应用于五种代表性模型，在KITTI和Waymo数据集上验证，支持全监督和稀疏监督设置。

## 摘要（原文）

> Monocular 3D object detection (M3OD) is intrinsically ill-posed, hence training a high-performance deep learning based M3OD model requires a humongous amount of labeled data with complicated visual variation from diverse scenes, variety of objects and camera poses.However, we observe that, due to strong human bias, the three independent entities, i.e., object, scene, and camera pose, are always tightly entangled when an image is captured to construct training data. More specifically, specific 3D objects are always captured in particular scenes with fixed camera poses, and hence lacks necessary diversity. Such tight entanglement induces the challenging issues of insufficient utilization and overfitting to uniform training data. To mitigate this, we propose an online object-scene-camera decomposition and recomposition data manipulation scheme to more efficiently exploit the training data. We first fully decompose training images into textured 3D object point models and background scenes in an efficient computation and storage manner. We then continuously recompose new training images in each epoch by inserting the 3D objects into the freespace of the background scenes, and rendering them with perturbed camera poses from textured 3D point representation. In this way, the refreshed training data in all epochs can cover the full spectrum of independent object, scene, and camera pose combinations. This scheme can serve as a plug-and-play component to boost M3OD models, working flexibly with both fully and sparsely supervised settings. In the sparsely-supervised setting, objects closest to the ego-camera for all instances are sparsely annotated. We then can flexibly increase the annotated objects to control annotation cost. For validation, our method is widely applied to five representative M3OD models and evaluated on both the KITTI and the more complicated Waymo datasets.

