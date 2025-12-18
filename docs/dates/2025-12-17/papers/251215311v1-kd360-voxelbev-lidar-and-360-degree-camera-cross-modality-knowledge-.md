---
layout: default
title: KD360-VoxelBEV: LiDAR and 360-degree Camera Cross Modality Knowledge Distillation for Bird's-Eye-View Segmentation
---

# KD360-VoxelBEV: LiDAR and 360-degree Camera Cross Modality Knowledge Distillation for Bird's-Eye-View Segmentation
**arXiv**：[2512.15311v1](https://arxiv.org/abs/2512.15311) · [PDF](https://arxiv.org/pdf/2512.15311.pdf)  
**作者**：Wenke E, Yixin Sun, Jiaxu Liu, Hubert P. H. Shum, Amir Atapour-Abarghouei, Toby P. Breckon  

**一句话要点**：提出跨模态知识蒸馏框架，用于单全景相机鸟瞰图分割，降低传感器复杂度。

**关键词**：鸟瞰图分割, 跨模态知识蒸馏, 全景相机, LiDAR融合, 体素对齐变换器, 自动驾驶

## 3 点简述
- 核心问题：单全景相机鸟瞰图分割性能受限，需提升精度与效率。
- 方法要点：融合LiDAR多通道表示与体素对齐视图变换器，通过教师网络蒸馏至学生网络。
- 实验或效果：在Dur360BEV数据集上，教师网络IoU提升25.6%，学生网络IoU增益8.5%，推理速度达31.2 FPS。

## 摘要（原文）

> We present the first cross-modality distillation framework specifically tailored for single-panoramic-camera Bird's-Eye-View (BEV) segmentation. Our approach leverages a novel LiDAR image representation fused from range, intensity and ambient channels, together with a voxel-aligned view transformer that preserves spatial fidelity while enabling efficient BEV processing. During training, a high-capacity LiDAR and camera fusion Teacher network extracts both rich spatial and semantic features for cross-modality knowledge distillation into a lightweight Student network that relies solely on a single 360-degree panoramic camera image. Extensive experiments on the Dur360BEV dataset demonstrate that our teacher model significantly outperforms existing camera-based BEV segmentation methods, achieving a 25.6\% IoU improvement. Meanwhile, the distilled Student network attains competitive performance with an 8.5\% IoU gain and state-of-the-art inference speed of 31.2 FPS. Moreover, evaluations on KITTI-360 (two fisheye cameras) confirm that our distillation framework generalises to diverse camera setups, underscoring its feasibility and robustness. This approach reduces sensor complexity and deployment costs while providing a practical solution for efficient, low-cost BEV segmentation in real-world autonomous driving.

