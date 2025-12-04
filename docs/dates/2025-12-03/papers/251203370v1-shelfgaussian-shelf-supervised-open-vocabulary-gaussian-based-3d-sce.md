---
layout: default
title: ShelfGaussian: Shelf-Supervised Open-Vocabulary Gaussian-based 3D Scene Understanding
---

# ShelfGaussian: Shelf-Supervised Open-Vocabulary Gaussian-based 3D Scene Understanding
**arXiv**：[2512.03370v1](https://arxiv.org/abs/2512.03370) · [PDF](https://arxiv.org/pdf/2512.03370.pdf)  
**作者**：Lingjun Zhao, Yandong Luo, James Hay, Lu Gan  

**一句话要点**：提出ShelfGaussian，利用现成视觉基础模型监督，实现开放词汇多模态高斯3D场景理解。

**关键词**：开放词汇3D场景理解, 高斯表示学习, 多模态融合, 现成模型监督, 零样本语义占据预测, 无人地面车辆应用

## 3 点简述
- 现有高斯方法在3D场景理解中面临封闭语义监督或纯2D自监督的局限性，导致渲染能力缺失或几何退化。
- 引入多模态高斯变换器，使高斯能从多传感器模态查询特征，并结合现成监督学习范式在2D和3D层面联合优化。
- 在Occ3D-nuScenes上实现零样本语义占据预测的先进性能，并在无人地面车辆上评估野外场景表现。

## 摘要（原文）

> We introduce ShelfGaussian, an open-vocabulary multi-modal Gaussian-based 3D scene understanding framework supervised by off-the-shelf vision foundation models (VFMs). Gaussian-based methods have demonstrated superior performance and computational efficiency across a wide range of scene understanding tasks. However, existing methods either model objects as closed-set semantic Gaussians supervised by annotated 3D labels, neglecting their rendering ability, or learn open-set Gaussian representations via purely 2D self-supervision, leading to degraded geometry and limited to camera-only settings. To fully exploit the potential of Gaussians, we propose a Multi-Modal Gaussian Transformer that enables Gaussians to query features from diverse sensor modalities, and a Shelf-Supervised Learning Paradigm that efficiently optimizes Gaussians with VFM features jointly at 2D image and 3D scene levels. We evaluate ShelfGaussian on various perception and planning tasks. Experiments on Occ3D-nuScenes demonstrate its state-of-the-art zero-shot semantic occupancy prediction performance. ShelfGaussian is further evaluated on an unmanned ground vehicle (UGV) to assess its in the-wild performance across diverse urban scenarios. Project website: https://lunarlab-gatech.github.io/ShelfGaussian/.

