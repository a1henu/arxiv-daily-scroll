---
layout: default
title: Evaluating the Impact of Weather-Induced Sensor Occlusion on BEVFusion for 3D Object Detection
---

# Evaluating the Impact of Weather-Induced Sensor Occlusion on BEVFusion for 3D Object Detection
**arXiv**：[2511.04347v1](https://arxiv.org/abs/2511.04347) · [PDF](https://arxiv.org/pdf/2511.04347.pdf)  
**作者**：Sanjay Kumar, Tim Brophy, Eoin Martino Grua, Ganesh Sistu, Valentina Donzella, Ciaran Eising  

**一句话要点**：评估天气致传感器遮挡对BEVFusion在3D物体检测中的影响

**关键词**：3D物体检测, BEV融合, 传感器遮挡, nuScenes数据集, 多模态集成, 环境鲁棒性

## 3 点简述
- 核心问题：传感器遮挡（如雾、霾）对BEV融合架构的3D检测精度影响未知。
- 方法要点：使用BEVFusion架构，分析相机和LiDAR在nuScenes数据集上的遮挡效应。
- 实验或效果：相机遮挡致mAP降41.3%，LiDAR遮挡降47.3%，融合时更依赖LiDAR。

## 摘要（原文）

> Accurate 3D object detection is essential for automated vehicles to navigate
> safely in complex real-world environments. Bird's Eye View (BEV)
> representations, which project multi-sensor data into a top-down spatial
> format, have emerged as a powerful approach for robust perception. Although
> BEV-based fusion architectures have demonstrated strong performance through
> multimodal integration, the effects of sensor occlusions, caused by
> environmental conditions such as fog, haze, or physical obstructions, on 3D
> detection accuracy remain underexplored. In this work, we investigate the
> impact of occlusions on both camera and Light Detection and Ranging (LiDAR)
> outputs using the BEVFusion architecture, evaluated on the nuScenes dataset.
> Detection performance is measured using mean Average Precision (mAP) and the
> nuScenes Detection Score (NDS). Our results show that moderate camera
> occlusions lead to a 41.3% drop in mAP (from 35.6% to 20.9%) when detection is
> based only on the camera. On the other hand, LiDAR sharply drops in performance
> only under heavy occlusion, with mAP falling by 47.3% (from 64.7% to 34.1%),
> with a severe impact on long-range detection. In fused settings, the effect
> depends on which sensor is occluded: occluding the camera leads to a minor 4.1%
> drop (from 68.5% to 65.7%), while occluding LiDAR results in a larger 26.8%
> drop (to 50.1%), revealing the model's stronger reliance on LiDAR for the task
> of 3D object detection. Our results highlight the need for future research into
> occlusion-aware evaluation methods and improved sensor fusion techniques that
> can maintain detection accuracy in the presence of partial sensor failure or
> degradation due to adverse environmental conditions.

