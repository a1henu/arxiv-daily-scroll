---
layout: default
title: Towards 3D Object-Centric Feature Learning for Semantic Scene Completion
---

# Towards 3D Object-Centric Feature Learning for Semantic Scene Completion
**arXiv**：[2511.13031v1](https://arxiv.org/abs/2511.13031) · [PDF](https://arxiv.org/pdf/2511.13031.pdf)  
**作者**：Weihua Wang, Yubo Cui, Xiangru Lin, Zhiheng Li, Zheng Fang  

**一句话要点**：提出Ocean对象中心框架以解决语义场景完成中的细粒度细节缺失问题

**关键词**：语义场景完成, 对象中心学习, 3D特征聚合, 注意力机制, BEV空间优化

## 3 点简述
- 核心问题：现有方法忽视对象级细节，导致语义和几何模糊，尤其在复杂环境中
- 方法要点：使用MobileSAM提取实例掩码，结合3D语义组注意力和全局相似性引导注意力
- 实验或效果：在SemanticKITTI和SSCBench-KITTI360基准上达到SOTA，mIoU分别为17.40和20.28

## 摘要（原文）

> Vision-based 3D Semantic Scene Completion (SSC) has received growing attention due to its potential in autonomous driving. While most existing approaches follow an ego-centric paradigm by aggregating and diffusing features over the entire scene, they often overlook fine-grained object-level details, leading to semantic and geometric ambiguities, especially in complex environments. To address this limitation, we propose Ocean, an object-centric prediction framework that decomposes the scene into individual object instances to enable more accurate semantic occupancy prediction. Specifically, we first employ a lightweight segmentation model, MobileSAM, to extract instance masks from the input image. Then, we introduce a 3D Semantic Group Attention module that leverages linear attention to aggregate object-centric features in 3D space. To handle segmentation errors and missing instances, we further design a Global Similarity-Guided Attention module that leverages segmentation features for global interaction. Finally, we propose an Instance-aware Local Diffusion module that improves instance features through a generative process and subsequently refines the scene representation in the BEV space. Extensive experiments on the SemanticKITTI and SSCBench-KITTI360 benchmarks demonstrate that Ocean achieves state-of-the-art performance, with mIoU scores of 17.40 and 20.28, respectively.

