---
layout: default
title: SFGFusion: Surface Fitting Guided 3D Object Detection with 4D Radar and Camera Fusion
---

# SFGFusion: Surface Fitting Guided 3D Object Detection with 4D Radar and Camera Fusion
**arXiv**：[2510.19215v1](https://arxiv.org/abs/2510.19215) · [PDF](https://arxiv.org/pdf/2510.19215.pdf)  
**作者**：Xiaozhi Li, Huijun Di, Jian Li, Feng Liu, Wei Liang  

**一句话要点**：提出SFGFusion通过表面拟合引导相机与4D雷达融合，提升自动驾驶3D物体检测性能。

**关键词**：3D物体检测, 多模态融合, 表面拟合, 4D雷达, 鸟瞰图, 自动驾驶

## 3 点简述
- 核心问题：4D雷达点云稀疏且分辨率低，限制物体几何表示和多模态融合。
- 方法要点：使用表面拟合模型估计物体参数，生成密集伪点云和统一BEV特征。
- 实验效果：在TJ4DRadSet和VoD基准上实现优越检测性能。

## 摘要（原文）

> 3D object detection is essential for autonomous driving. As an emerging
> sensor, 4D imaging radar offers advantages as low cost, long-range detection,
> and accurate velocity measurement, making it highly suitable for object
> detection. However, its sparse point clouds and low resolution limit object
> geometric representation and hinder multi-modal fusion. In this study, we
> introduce SFGFusion, a novel camera-4D imaging radar detection network guided
> by surface fitting. By estimating quadratic surface parameters of objects from
> image and radar data, the explicit surface fitting model enhances spatial
> representation and cross-modal interaction, enabling more reliable prediction
> of fine-grained dense depth. The predicted depth serves two purposes: 1) in an
> image branch to guide the transformation of image features from perspective
> view (PV) to a unified bird's-eye view (BEV) for multi-modal fusion, improving
> spatial mapping accuracy; and 2) in a surface pseudo-point branch to generate
> dense pseudo-point cloud, mitigating the radar point sparsity. The original
> radar point cloud is also encoded in a separate radar branch. These two point
> cloud branches adopt a pillar-based method and subsequently transform the
> features into the BEV space. Finally, a standard 2D backbone and detection head
> are used to predict object labels and bounding boxes from BEV features.
> Experimental results show that SFGFusion effectively fuses camera and 4D radar
> features, achieving superior performance on the TJ4DRadSet and view-of-delft
> (VoD) object detection benchmarks.

