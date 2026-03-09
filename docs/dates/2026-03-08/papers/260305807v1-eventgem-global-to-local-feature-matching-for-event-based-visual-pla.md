---
layout: default
title: EventGeM: Global-to-Local Feature Matching for Event-Based Visual Place Recognition
---

# EventGeM: Global-to-Local Feature Matching for Event-Based Visual Place Recognition
**arXiv**：[2603.05807v1](https://arxiv.org/abs/2603.05807) · [PDF](https://arxiv.org/pdf/2603.05807.pdf)  
**作者**：Adam D. Hines, Gokul B. Nair, Nicolás Marticorena, Michael Milford, Tobias Fischer  

**一句话要点**：提出EventGeM，通过全局到局部特征匹配实现基于事件的视觉地点识别

**关键词**：事件相机, 视觉地点识别, 特征匹配, 机器人导航, 实时定位

## 3 点简述
- 核心问题：事件相机在机器人导航中需高精度实时定位，现有方法性能有限
- 方法要点：结合ViT全局特征、MaxViT局部特征和深度估计进行多级匹配与重排序
- 实验或效果：在多个基准数据集上实现最先进性能，支持实时部署于机器人平台

## 摘要（原文）

> Dynamic vision sensors, also known as event cameras, are rapidly rising in popularity for robotic and computer vision tasks due to their sparse activation and high-temporal resolution. Event cameras have been used in robotic navigation and localization tasks where accurate positioning needs to occur on small and frequent time scales, or when energy concerns are paramount. In this work, we present EventGeM, a state-of-the-art global to local feature fusion pipeline for event-based Visual Place Recognition. We use a pre-trained vision transformer (ViT-S/16) backbone to obtain global feature patch for initial match predictions embeddings from event histogram images. Local feature keypoints were then detected using a pre-trained MaxViT backbone for 2D-homography based re-ranking with RANSAC. For additional re-ranking refinement, we subsequently used a pre-trained vision foundation model for depth estimation to compare structural similarity between references and queries. Our work performs state-of-the-art localization when compared to the best currently available event-based place recognition method across several benchmark datasets and lighting conditions all whilst being fully capable of running in real-time when deployed across a variety of compute architectures. We demonstrate the capability of EventGeM in a real-world deployment on a robotic platform for online localization using event streams directly from an event camera. Project page: https://eventgemvpr.github.io/

