---
layout: default
title: NV3D: Leveraging Spatial Shape Through Normal Vector-based 3D Object Detection
---

# NV3D: Leveraging Spatial Shape Through Normal Vector-based 3D Object Detection
**arXiv**：[2510.11632v1](https://arxiv.org/abs/2510.11632) · [PDF](https://arxiv.org/pdf/2510.11632.pdf)  
**作者**：Krittin Chaowakarn, Paramin Sangwongngam, Nang Htet Htet Aung, Chalie Charoenlarpnopparut  

**一句话要点**：提出NV3D模型，利用法向量增强3D物体检测，适用于自动驾驶场景。

**关键词**：3D物体检测, 法向量特征, 体素采样, 自动驾驶, KITTI数据集

## 3 点简述
- 核心问题：多模态方法特征对齐困难，局部特征提取在复杂3D检测中过于简化。
- 方法要点：基于KNN和PCA计算体素法向量，采用密度和FOV感知采样减少数据。
- 实验效果：在KITTI数据集上，mAP优于基线，采样后性能保持且数据减少55%。

## 摘要（原文）

> Recent studies in 3D object detection for autonomous vehicles aim to enrich
> features through the utilization of multi-modal setups or the extraction of
> local patterns within LiDAR point clouds. However, multi-modal methods face
> significant challenges in feature alignment, and gaining features locally can
> be oversimplified for complex 3D object detection tasks. In this paper, we
> propose a novel model, NV3D, which utilizes local features acquired from voxel
> neighbors, as normal vectors computed per voxel basis using K-nearest neighbors
> (KNN) and principal component analysis (PCA). This informative feature enables
> NV3D to determine the relationship between the surface and pertinent target
> entities, including cars, pedestrians, or cyclists. During the normal vector
> extraction process, NV3D offers two distinct sampling strategies: normal vector
> density-based sampling and FOV-aware bin-based sampling, allowing elimination
> of up to 55% of data while maintaining performance. In addition, we applied
> element-wise attention fusion, which accepts voxel features as the query and
> value and normal vector features as the key, similar to the attention
> mechanism. Our method is trained on the KITTI dataset and has demonstrated
> superior performance in car and cyclist detection owing to their spatial
> shapes. In the validation set, NV3D without sampling achieves 86.60% and 80.18%
> mean Average Precision (mAP), greater than the baseline Voxel R-CNN by 2.61%
> and 4.23% mAP, respectively. With both samplings, NV3D achieves 85.54% mAP in
> car detection, exceeding the baseline by 1.56% mAP, despite roughly 55% of
> voxels being filtered out.

