---
layout: default
title: GeoTeacher: Geometry-Guided Semi-Supervised 3D Object Detection
---

# GeoTeacher: Geometry-Guided Semi-Supervised 3D Object Detection
**arXiv**：[2512.23147v1](https://arxiv.org/abs/2512.23147) · [PDF](https://arxiv.org/pdf/2512.23147.pdf)  
**作者**：Jingyu Li, Xiaolong Zhao, Zhe Liu, Wenxiao Wu, Li Zhang  

**一句话要点**：提出GeoTeacher以增强半监督3D目标检测中几何关系捕获能力

**关键词**：半监督3D目标检测, 几何关系监督, 数据增强, 关键点检测, 体素处理, 距离衰减机制

## 3 点简述
- 核心问题：现有方法在有限标注数据下对目标几何敏感度低，影响感知与定位能力。
- 方法要点：设计基于关键点的几何关系监督模块和体素级数据增强策略，结合距离衰减机制。
- 实验或效果：在ONCE和Waymo数据集上实现新SOTA，可与其他SS3D方法结合提升性能。

## 摘要（原文）

> Semi-supervised 3D object detection, aiming to explore unlabeled data for boosting 3D object detectors, has emerged as an active research area in recent years. Some previous methods have shown substantial improvements by either employing heterogeneous teacher models to provide high-quality pseudo labels or enforcing feature-perspective consistency between the teacher and student networks. However, these methods overlook the fact that the model usually tends to exhibit low sensitivity to object geometries with limited labeled data, making it difficult to capture geometric information, which is crucial for enhancing the student model's ability in object perception and localization. In this paper, we propose GeoTeacher to enhance the student model's ability to capture geometric relations of objects with limited training data, especially unlabeled data. We design a keypoint-based geometric relation supervision module that transfers the teacher model's knowledge of object geometry to the student, thereby improving the student's capability in understanding geometric relations. Furthermore, we introduce a voxel-wise data augmentation strategy that increases the diversity of object geometries, thereby further improving the student model's ability to comprehend geometric structures. To preserve the integrity of distant objects during augmentation, we incorporate a distance-decay mechanism into this strategy. Moreover, GeoTeacher can be combined with different SS3D methods to further improve their performance. Extensive experiments on the ONCE and Waymo datasets indicate the effectiveness and generalization of our method and we achieve the new state-of-the-art results. Code will be available at https://github.com/SII-Whaleice/GeoTeacher

