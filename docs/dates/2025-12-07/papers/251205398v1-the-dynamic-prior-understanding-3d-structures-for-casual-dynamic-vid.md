---
layout: default
title: The Dynamic Prior: Understanding 3D Structures for Casual Dynamic Videos
---

# The Dynamic Prior: Understanding 3D Structures for Casual Dynamic Videos
**arXiv**：[2512.05398v1](https://arxiv.org/abs/2512.05398) · [PDF](https://arxiv.org/pdf/2512.05398.pdf)  
**作者**：Zhuoyuan Wu, Xurui Yang, Jiahui Huang, Yue Wang, Jun Gao  

**一句话要点**：提出Dynamic Prior以利用视觉语言模型和SAM2提升动态视频中的3D结构理解

**关键词**：动态视频理解, 3D结构重建, 视觉语言模型, 运动分割, 相机姿态优化, 深度估计

## 3 点简述
- 核心问题：动态物体干扰传统方法对相机姿态和3D几何的估计，现有学习法依赖大规模数据集导致分割不准确。
- 方法要点：结合视觉语言模型的推理能力和SAM2的精细分割，无需任务特定训练即可识别动态物体。
- 实验或效果：在合成和真实视频上验证，动态分割性能领先，并显著提升3D结构理解的准确性和鲁棒性。

## 摘要（原文）

> Estimating accurate camera poses, 3D scene geometry, and object motion from in-the-wild videos is a long-standing challenge for classical structure from motion pipelines due to the presence of dynamic objects. Recent learning-based methods attempt to overcome this challenge by training motion estimators to filter dynamic objects and focus on the static background. However, their performance is largely limited by the availability of large-scale motion segmentation datasets, resulting in inaccurate segmentation and, therefore, inferior structural 3D understanding. In this work, we introduce the Dynamic Prior (\ourmodel) to robustly identify dynamic objects without task-specific training, leveraging the powerful reasoning capabilities of Vision-Language Models (VLMs) and the fine-grained spatial segmentation capacity of SAM2. \ourmodel can be seamlessly integrated into state-of-the-art pipelines for camera pose optimization, depth reconstruction, and 4D trajectory estimation. Extensive experiments on both synthetic and real-world videos demonstrate that \ourmodel not only achieves state-of-the-art performance on motion segmentation, but also significantly improves accuracy and robustness for structural 3D understanding.

