---
layout: default
title: Bidirectional Cross-Perception for Open-Vocabulary Semantic Segmentation in Remote Sensing Imagery
---

# Bidirectional Cross-Perception for Open-Vocabulary Semantic Segmentation in Remote Sensing Imagery
**arXiv**：[2601.21159v1](https://arxiv.org/abs/2601.21159) · [PDF](https://arxiv.org/pdf/2601.21159.pdf)  
**作者**：Jianzheng Wang, Huan Ni  

**一句话要点**：提出SDCI框架以解决遥感图像开放词汇语义分割中的几何定位与语义预测难题。

**关键词**：开放词汇语义分割, 遥感图像分析, 跨模型注意力融合, 图扩散优化, 超像素结构, 免训练方法

## 3 点简述
- 针对高分辨率遥感图像密集对象与复杂边界，现有免训练方法难以满足需求。
- SDCI通过跨模型注意力融合与双向交叉图扩散优化双分支协同推理。
- 实验表明SDCI在多个基准上优于现有方法，并验证超像素结构在深度学习中的有效性。

## 摘要（原文）

> High-resolution remote sensing imagery is characterized by densely distributed land-cover objects and complex boundaries, which places higher demands on both geometric localization and semantic prediction. Existing training-free open-vocabulary semantic segmentation (OVSS) methods typically fuse CLIP and vision foundation models (VFMs) using "one-way injection" and "shallow post-processing" strategies, making it difficult to satisfy these requirements. To address this issue, we propose a spatial-regularization-aware dual-branch collaborative inference framework for training-free OVSS, termed SDCI. First, during feature encoding, SDCI introduces a cross-model attention fusion (CAF) module, which guides collaborative inference by injecting self-attention maps into each other. Second, we propose a bidirectional cross-graph diffusion refinement (BCDR) module that enhances the reliability of dual-branch segmentation scores through iterative random-walk diffusion. Finally, we incorporate low-level superpixel structures and develop a convex-optimization-based superpixel collaborative prediction (CSCP) mechanism to further refine object boundaries. Experiments on multiple remote sensing semantic segmentation benchmarks demonstrate that our method achieves better performance than existing approaches. Moreover, ablation studies further confirm that traditional object-based remote sensing image analysis methods leveraging superpixel structures remain effective within deep learning frameworks. Code: https://github.com/yu-ni1989/SDCI.

