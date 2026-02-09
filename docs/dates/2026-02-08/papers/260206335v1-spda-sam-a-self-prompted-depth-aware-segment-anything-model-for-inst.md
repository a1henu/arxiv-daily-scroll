---
layout: default
title: SPDA-SAM: A Self-prompted Depth-Aware Segment Anything Model for Instance Segmentation
---

# SPDA-SAM: A Self-prompted Depth-Aware Segment Anything Model for Instance Segmentation
**arXiv**：[2602.06335v1](https://arxiv.org/abs/2602.06335) · [PDF](https://arxiv.org/pdf/2602.06335.pdf)  
**作者**：Yihan Shang, Wei Wang, Chao Huang, Xinghui Dong  

**一句话要点**：提出SPDA-SAM，通过自提示与深度感知解决实例分割中手动提示依赖与空间信息缺失问题。

**关键词**：实例分割, 自提示学习, 深度感知, RGB-D融合, 语义空间提示, 粗到细特征融合

## 3 点简述
- 核心问题：SAM依赖手动提示质量，RGB图像缺乏深度信息，影响空间感知与边界分割。
- 方法要点：设计语义-空间自提示模块提取提示，引入粗到细RGB-D融合模块融合深度信息。
- 实验或效果：在12个数据集上优于现有方法，自提示与深度融合补偿空间信息损失。

## 摘要（原文）

> Recently, Segment Anything Model (SAM) has demonstrated strong generalizability in various instance segmentation tasks. However, its performance is severely dependent on the quality of manual prompts. In addition, the RGB images that instance segmentation methods normally use inherently lack depth information. As a result, the ability of these methods to perceive spatial structures and delineate object boundaries is hindered. To address these challenges, we propose a Self-prompted Depth-Aware SAM (SPDA-SAM) for instance segmentation. Specifically, we design a Semantic-Spatial Self-prompt Module (SSSPM) which extracts the semantic and spatial prompts from the image encoder and the mask decoder of SAM, respectively. Furthermore, we introduce a Coarse-to-Fine RGB-D Fusion Module (C2FFM), in which the features extracted from a monocular RGB image and the depth map estimated from it are fused. In particular, the structural information in the depth map is used to provide coarse-grained guidance to feature fusion, while local variations in depth are encoded in order to fuse fine-grained feature representations. To our knowledge, SAM has not been explored in such self-prompted and depth-aware manners. Experimental results demonstrate that our SPDA-SAM outperforms its state-of-the-art counterparts across twelve different data sets. These promising results should be due to the guidance of the self-prompts and the compensation for the spatial information loss by the coarse-to-fine RGB-D fusion operation.

