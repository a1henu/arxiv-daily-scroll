---
layout: default
title: DressWild: Feed-Forward Pose-Agnostic Garment Sewing Pattern Generation from In-the-Wild Images
---

# DressWild: Feed-Forward Pose-Agnostic Garment Sewing Pattern Generation from In-the-Wild Images
**arXiv**：[2602.16502v1](https://arxiv.org/abs/2602.16502) · [PDF](https://arxiv.org/pdf/2602.16502.pdf)  
**作者**：Zeng Tao, Ying Jiang, Yunuo Chen, Tianyi Xie, Huamin Wang, Yingnian Wu, Yin Yang, Abishek Sampath Kumar, Kenji Tashiro, Chenfanfu Jiang  

**一句话要点**：提出DressWild以从单张野外图像生成可编辑的服装缝纫图案和3D模型

**关键词**：服装建模, 缝纫图案生成, 3D重建, 视觉语言模型, 物理模拟, 虚拟试穿

## 3 点简述
- 核心问题：现有前馈方法难以处理多样姿态和视角，优化方法计算成本高且不易扩展。
- 方法要点：利用视觉语言模型归一化姿态，提取3D感知特征，通过Transformer编码器预测缝纫图案参数。
- 实验或效果：无需多视图输入或迭代优化，能鲁棒恢复多样缝纫图案和3D服装，支持物理模拟和虚拟试穿。

## 摘要（原文）

> Recent advances in garment pattern generation have shown promising progress. However, existing feed-forward methods struggle with diverse poses and viewpoints, while optimization-based approaches are computationally expensive and difficult to scale. This paper focuses on sewing pattern generation for garment modeling and fabrication applications that demand editable, separable, and simulation-ready garments. We propose DressWild, a novel feed-forward pipeline that reconstructs physics-consistent 2D sewing patterns and the corresponding 3D garments from a single in-the-wild image. Given an input image, our method leverages vision-language models (VLMs) to normalize pose variations at the image level, then extract pose-aware, 3D-informed garment features. These features are fused through a transformer-based encoder and subsequently used to predict sewing pattern parameters, which can be directly applied to physical simulation, texture synthesis, and multi-layer virtual try-on. Extensive experiments demonstrate that our approach robustly recovers diverse sewing patterns and the corresponding 3D garments from in-the-wild images without requiring multi-view inputs or iterative optimization, offering an efficient and scalable solution for realistic garment simulation and animation.

