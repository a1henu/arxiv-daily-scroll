---
layout: default
title: DVGT: Driving Visual Geometry Transformer
---

# DVGT: Driving Visual Geometry Transformer
**arXiv**：[2512.16919v1](https://arxiv.org/abs/2512.16919) · [PDF](https://arxiv.org/pdf/2512.16919.pdf)  
**作者**：Sicheng Zuo, Zixun Xie, Wenzhao Zheng, Shaoqing Xu, Fang Li, Shengyin Jiang, Long Chen, Zhi-Xin Yang, Jiwen Lu  

**一句话要点**：提出DVGT以从无位姿多视角图像序列重建全局密集3D点云地图，适应自动驾驶场景。

**关键词**：自动驾驶, 3D重建, 视觉Transformer, 多视角几何, 无位姿估计

## 3 点简述
- 核心问题：自动驾驶中缺乏适应不同场景和相机配置的密集几何感知模型。
- 方法要点：使用DINO提取特征，通过交替注意力机制推断跨图像几何关系，无需显式3D先验。
- 实验或效果：在混合数据集上训练，显著优于现有模型，直接预测度量尺度几何。

## 摘要（原文）

> Perceiving and reconstructing 3D scene geometry from visual inputs is crucial for autonomous driving. However, there still lacks a driving-targeted dense geometry perception model that can adapt to different scenarios and camera configurations. To bridge this gap, we propose a Driving Visual Geometry Transformer (DVGT), which reconstructs a global dense 3D point map from a sequence of unposed multi-view visual inputs. We first extract visual features for each image using a DINO backbone, and employ alternating intra-view local attention, cross-view spatial attention, and cross-frame temporal attention to infer geometric relations across images. We then use multiple heads to decode a global point map in the ego coordinate of the first frame and the ego poses for each frame. Unlike conventional methods that rely on precise camera parameters, DVGT is free of explicit 3D geometric priors, enabling flexible processing of arbitrary camera configurations. DVGT directly predicts metric-scaled geometry from image sequences, eliminating the need for post-alignment with external sensors. Trained on a large mixture of driving datasets including nuScenes, OpenScene, Waymo, KITTI, and DDAD, DVGT significantly outperforms existing models on various scenarios. Code is available at https://github.com/wzzheng/DVGT.

