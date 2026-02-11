---
layout: default
title: Monocular Normal Estimation via Shading Sequence Estimation
---

# Monocular Normal Estimation via Shading Sequence Estimation
**arXiv**：[2602.09929v1](https://arxiv.org/abs/2602.09929) · [PDF](https://arxiv.org/pdf/2602.09929.pdf)  
**作者**：Zongrui Li, Xinhua Ma, Minghui Hu, Yunqing Zhao, Yingchen Yu, Qian Zheng, Chang Liu, Xudong Jiang, Song Bai  

**一句话要点**：提出RoSE方法，通过估计着色序列解决单目法线估计中的三维错位问题。

**关键词**：单目法线估计, 着色序列估计, 三维重建, 图像到视频生成, 合成数据集训练

## 3 点简述
- 核心问题：现有方法直接预测法线图易导致三维错位，几何细节与表面重建不匹配。
- 方法要点：将法线估计重构为着色序列估计，利用图像到视频生成模型预测序列，再转换为法线图。
- 实验或效果：在合成数据集MultiShade上训练，在真实世界基准数据集上达到最先进性能。

## 摘要（原文）

> Monocular normal estimation aims to estimate the normal map from a single RGB image of an object under arbitrary lights. Existing methods rely on deep models to directly predict normal maps. However, they often suffer from 3D misalignment: while the estimated normal maps may appear to have a correct appearance, the reconstructed surfaces often fail to align with the geometric details. We argue that this misalignment stems from the current paradigm: the model struggles to distinguish and reconstruct varying geometry represented in normal maps, as the differences in underlying geometry are reflected only through relatively subtle color variations. To address this issue, we propose a new paradigm that reformulates normal estimation as shading sequence estimation, where shading sequences are more sensitive to various geometric information. Building on this paradigm, we present RoSE, a method that leverages image-to-video generative models to predict shading sequences. The predicted shading sequences are then converted into normal maps by solving a simple ordinary least-squares problem. To enhance robustness and better handle complex objects, RoSE is trained on a synthetic dataset, MultiShade, with diverse shapes, materials, and light conditions. Experiments demonstrate that RoSE achieves state-of-the-art performance on real-world benchmark datasets for object-based monocular normal estimation.

