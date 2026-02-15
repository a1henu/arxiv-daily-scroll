---
layout: default
title: Efficient Segment Anything with Depth-Aware Fusion and Limited Training Data
---

# Efficient Segment Anything with Depth-Aware Fusion and Limited Training Data
**arXiv**：[2602.11804v1](https://arxiv.org/abs/2602.11804) · [PDF](https://arxiv.org/pdf/2602.11804.pdf)  
**作者**：Yiming Zhou, Xuenjie Xie, Panfeng Li, Albrecht Kunz, Ahmad Osman, Xavier Maldague  

**一句话要点**：提出轻量级RGB-D融合框架，通过深度先验增强EfficientViT-SAM，在少量数据下提升分割精度。

**关键词**：轻量级分割模型, RGB-D融合, 深度先验, 少量数据训练, EfficientViT-SAM

## 3 点简述
- 核心问题：SAM依赖大规模RGB数据训练，计算成本高且缺乏几何信息。
- 方法要点：使用预训练深度估计器生成深度图，通过专用编码器与RGB特征中层级融合。
- 实验或效果：仅用11.2k样本训练，精度超越EfficientViT-SAM，验证深度先验的有效性。

## 摘要（原文）

> Segment Anything Models (SAM) achieve impressive universal segmentation performance but require massive datasets (e.g., 11M images) and rely solely on RGB inputs. Recent efficient variants reduce computation but still depend on large-scale training. We propose a lightweight RGB-D fusion framework that augments EfficientViT-SAM with monocular depth priors. Depth maps are generated with a pretrained estimator and fused mid-level with RGB features through a dedicated depth encoder. Trained on only 11.2k samples (less than 0.1\% of SA-1B), our method achieves higher accuracy than EfficientViT-SAM, showing that depth cues provide strong geometric priors for segmentation.

