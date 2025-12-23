---
layout: default
title: Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation
---

# Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation
**arXiv**：[2512.19088v1](https://arxiv.org/abs/2512.19088) · [PDF](https://arxiv.org/pdf/2512.19088.pdf)  
**作者**：Khanh Nguyen, Dasith de Silva Edirimuni, Ghulam Mubashar Hassan, Ajmal Mian  

**一句话要点**：提出基于2D检测器引导的3D实例分割方法，以高效检索点云场景中的罕见物体。

**关键词**：3D实例分割, 开放词汇检测, 点云检索, 罕见物体泛化, 实时处理

## 3 点简述
- 核心问题：现有方法依赖SAM和CLIP导致计算开销大，且对罕见物体泛化能力不足。
- 方法要点：利用2D开放词汇检测器引导从RGB图像生成3D实例掩码，继承其识别新物体的能力。
- 实验或效果：实现快速准确检索，减少推理时间，代码已开源。

## 摘要（原文）

> Locating and retrieving objects from scene-level point clouds is a challenging problem with broad applications in robotics and augmented reality. This task is commonly formulated as open-vocabulary 3D instance segmentation. Although recent methods demonstrate strong performance, they depend heavily on SAM and CLIP to generate and classify 3D instance masks from images accompanying the point cloud, leading to substantial computational overhead and slow processing that limit their deployment in real-world settings. Open-YOLO 3D alleviates this issue by using a real-time 2D detector to classify class-agnostic masks produced directly from the point cloud by a pretrained 3D segmenter, eliminating the need for SAM and CLIP and significantly reducing inference time. However, Open-YOLO 3D often fails to generalize to object categories that appear infrequently in the 3D training data. In this paper, we propose a method that generates 3D instance masks for novel objects from RGB images guided by a 2D open-vocabulary detector. Our approach inherits the 2D detector's ability to recognize novel objects while maintaining efficient classification, enabling fast and accurate retrieval of rare instances from open-ended text queries. Our code will be made available at https://github.com/ndkhanh360/BoxOVIS.

