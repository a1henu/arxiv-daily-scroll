---
layout: default
title: FreeOcc: Training-free Panoptic Occupancy Prediction via Foundation Models
---

# FreeOcc: Training-free Panoptic Occupancy Prediction via Foundation Models
**arXiv**：[2603.06166v1](https://arxiv.org/abs/2603.06166) · [PDF](https://arxiv.org/pdf/2603.06166.pdf)  
**作者**：Andrew Caunes, Thierry Chateau, Vincent Fremont  

**一句话要点**：提出FreeOcc训练免费全景占据预测方法，利用基础模型从多视图图像恢复语义与几何

**关键词**：全景占据预测, 基础模型, 训练免费方法, 多视图重建, 3D场景理解, 弱监督学习

## 3 点简述
- 问题：现有相机方法依赖昂贵3D监督或目标域训练，限制未知环境部署
- 方法：结合提示分割与重建基础模型，提取全景先验和3D点，通过过滤与融合生成占据
- 效果：在Occ3D-nuScenes上实现16.9 mIoU，作为伪标签生成器达21.1 RayIoU，超越弱监督基线

## 摘要（原文）

> Semantic and panoptic occupancy prediction for road scene analysis provides a dense 3D representation of the ego vehicle's surroundings. Current camera-only approaches typically rely on costly dense 3D supervision or require training models on data from the target domain, limiting deployment in unseen environments. We propose FreeOcc, a training-free pipeline that leverages pretrained foundation models to recover both semantics and geometry from multi-view images. FreeOcc extracts per-view panoptic priors with a promptable foundation segmentation model and prompt-to-taxonomy rules, and reconstructs metric 3D points with a reconstruction foundation model. Depth- and confidence- aware filtering lifts reliable labels into 3D, which are fused over time and voxelized with a deterministic refinement stack. For panoptic occupancy, instances are recovered by fitting and merging robust current-view 3D box candidates, enabling instance-aware occupancy without any learned 3D model. On Occ3D-nuScenes, FreeOcc achieves 16.9 mIoU and 16.5 RayIoU train-free, on par with state-of-the-art weakly supervised methods. When employed as a pseudo-label generation pipeline for training downstream models, it achieves 21.1 RayIoU, surpassing the previous state-of-the-art weakly supervised baseline. Furthermore, FreeOcc sets new baselines for both train-free and weakly supervised panoptic occupancy prediction, achieving 3.1 RayPQ and 3.9 RayPQ, respectively. These results highlight foundation-model-driven perception as a practical route to training-free 3D scene understanding.

