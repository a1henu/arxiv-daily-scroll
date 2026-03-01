---
layout: default
title: Monocular Open Vocabulary Occupancy Prediction for Indoor Scenes
---

# Monocular Open Vocabulary Occupancy Prediction for Indoor Scenes
**arXiv**：[2602.22667v1](https://arxiv.org/abs/2602.22667) · [PDF](https://arxiv.org/pdf/2602.22667.pdf)  
**作者**：Changqing Zhou, Yueru Luo, Han Zhang, Zeyu Jiang, Changhao Chen  

**一句话要点**：提出基于3D语言嵌入高斯和渐进温度衰减的单目开放词汇室内场景占用预测方法

**关键词**：单目视觉, 开放词汇占用预测, 室内场景理解, 3D语言嵌入高斯, 渐进温度衰减, 几何监督

## 3 点简述
- 核心问题：现有开放词汇占用预测方法在室内场景中因几何密集、布局复杂和语义细粒度而性能不佳
- 方法要点：采用仅二值占用标签的几何监督，通过不透明度感知泊松聚合稳定体积表示，并引入渐进温度衰减增强高斯-语言对齐
- 实验或效果：在Occ-ScanNet上，开放词汇设置下达到59.50 IoU和21.05 mIoU，超越现有方法

## 摘要（原文）

> Open-vocabulary 3D occupancy is vital for embodied agents, which need to understand complex indoor environments where semantic categories are abundant and evolve beyond fixed taxonomies. While recent work has explored open-vocabulary occupancy in outdoor driving scenarios, such methods transfer poorly indoors, where geometry is denser, layouts are more intricate, and semantics are far more fine-grained. To address these challenges, we adopt a geometry-only supervision paradigm that uses only binary occupancy labels (occupied vs free). Our framework builds upon 3D Language-Embedded Gaussians, which serve as a unified intermediate representation coupling fine-grained 3D geometry with a language-aligned semantic embedding. On the geometry side, we find that existing Gaussian-to-Occupancy operators fail to converge under such weak supervision, and we introduce an opacity-aware, Poisson-based approach that stabilizes volumetric aggregation. On the semantic side, direct alignment between rendered features and open-vocabulary segmentation features suffers from feature mixing; we therefore propose a Progressive Temperature Decay schedule that gradually sharpens opacities during splatting, strengthening Gaussian-language alignment. On Occ-ScanNet, our framework achieves 59.50 IoU and 21.05 mIoU in the open-vocabulary setting, surpassing all existing occupancy methods in IoU and outperforming prior open-vocabulary approaches by a large margin in mIoU. Code will be released at https://github.com/JuIvyy/LegoOcc.

