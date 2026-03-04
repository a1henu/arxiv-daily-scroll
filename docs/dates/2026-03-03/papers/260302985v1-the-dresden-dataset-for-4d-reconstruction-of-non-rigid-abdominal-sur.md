---
layout: default
title: The Dresden Dataset for 4D Reconstruction of Non-Rigid Abdominal Surgical Scenes
---

# The Dresden Dataset for 4D Reconstruction of Non-Rigid Abdominal Surgical Scenes
**arXiv**：[2603.02985v1](https://arxiv.org/abs/2603.02985) · [PDF](https://arxiv.org/pdf/2603.02985.pdf)  
**作者**：Reuben Docea, Rayan Younis, Yonghao Long, Maxime Fleury, Jinjing Xu, Chenyang Li, André Schulze, Ann Wierick, Johannes Bender, Micha Pfeiffer, Qi Dou, Martin Wagner, Stefanie Speidel  

**一句话要点**：提出D4D数据集以评估非刚性腹部手术场景的4D重建方法

**关键词**：非刚性重建, 手术场景数据集, 4D重建, 结构光几何, 内窥镜视频, SLAM基准

## 3 点简述
- 核心问题：缺乏高质量配对数据评估非刚性软组织在手术条件下的3D重建算法。
- 方法要点：使用猪尸体实验采集内窥镜视频和结构光几何数据，通过光学跟踪和手动对齐进行配准。
- 实验或效果：提供超过30万帧和369个点云，支持几何和光度评估，作为非刚性SLAM和深度估计的基准。

## 摘要（原文）

> The D4D Dataset provides paired endoscopic video and high-quality structured-light geometry for evaluating 3D reconstruction of deforming abdominal soft tissue in realistic surgical conditions. Data were acquired from six porcine cadaver sessions using a da Vinci Xi stereo endoscope and a Zivid structured-light camera, registered via optical tracking and manually curated iterative alignment methods. Three sequence types - whole deformations, incremental deformations, and moved-camera clips - probe algorithm robustness to non-rigid motion, deformation magnitude, and out-of-view updates. Each clip provides rectified stereo images, per-frame instrument masks, stereo depth, start/end structured-light point clouds, curated camera poses and camera intrinsics. In postprocessing, ICP and semi-automatic registration techniques are used to register data, and instrument masks are created. The dataset enables quantitative geometric evaluation in both visible and occluded regions, alongside photometric view-synthesis baselines. Comprising over 300,000 frames and 369 point clouds across 98 curated recordings, this resource can serve as a comprehensive benchmark for developing and evaluating non-rigid SLAM, 4D reconstruction, and depth estimation methods.

