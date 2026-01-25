---
layout: default
title: Enhanced LULC Segmentation via Lightweight Model Refinements on ALOS-2 SAR Data
---

# Enhanced LULC Segmentation via Lightweight Model Refinements on ALOS-2 SAR Data
**arXiv**：[2601.15705v1](https://arxiv.org/abs/2601.15705) · [PDF](https://arxiv.org/pdf/2601.15705.pdf)  
**作者**：Ali Caglayan, Nevrez Imamoglu, Toru Kouyama  

**一句话要点**：提出三种轻量级改进以增强ALOS-2 SAR数据上的LULC语义分割性能

**关键词**：SAR语义分割, 轻量级模型改进, 长尾分布处理, ALOS-2数据, 水检测任务, 自监督预训练

## 3 点简述
- 核心问题：SAR密集预测中的边界平滑、细长结构遗漏和长尾标签下稀有类退化
- 方法要点：引入高分辨率特征注入、渐进细化上采样头和α尺度因子调整损失函数
- 实验或效果：在日本全国ALOS-2 LULC基准上实现一致改进，尤其提升稀有类和水检测性能

## 摘要（原文）

> This work focuses on national-scale land-use/land-cover (LULC) semantic segmentation using ALOS-2 single-polarization (HH) SAR data over Japan, together with a companion binary water detection task. Building on SAR-W-MixMAE self-supervised pretraining [1], we address common SAR dense-prediction failure modes, boundary over-smoothing, missed thin/slender structures, and rare-class degradation under long-tailed labels, without increasing pipeline complexity. We introduce three lightweight refinements: (i) injecting high-resolution features into multi-scale decoding, (ii) a progressive refine-up head that alternates convolutional refinement and stepwise upsampling, and (iii) an $α$-scale factor that tempers class reweighting within a focal+dice objective. The resulting model yields consistent improvements on the Japan-wide ALOS-2 LULC benchmark, particularly for under-represented classes, and improves water detection across standard evaluation metrics.

