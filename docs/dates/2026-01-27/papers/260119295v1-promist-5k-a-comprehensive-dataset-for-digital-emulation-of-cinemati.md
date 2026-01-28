---
layout: default
title: ProMist-5K: A Comprehensive Dataset for Digital Emulation of Cinematic Pro-Mist Filter Effects
---

# ProMist-5K: A Comprehensive Dataset for Digital Emulation of Cinematic Pro-Mist Filter Effects
**arXiv**：[2601.19295v1](https://arxiv.org/abs/2601.19295) · [PDF](https://arxiv.org/pdf/2601.19295.pdf)  
**作者**：Yingtie Lei, Zimeng Li, Chi-Man Pun, Wangyu Wu, Junke Yang, Xuhang Chen  

**一句话要点**：提出ProMist-5K数据集以支持数字模拟电影Pro-Mist滤镜效果

**关键词**：Pro-Mist滤镜模拟, 光扩散效果数据集, 电影风格图像转换, 物理启发建模, 高分辨率图像对

## 3 点简述
- 核心问题：Pro-Mist滤镜的光扩散效果难以数字再现，需高质量数据集支持模拟。
- 方法要点：基于物理启发流程构建20,000对高分辨率图像，覆盖不同密度和焦距配置。
- 实验或效果：数据集在不同训练设置中表现良好，能捕捉细微至强烈的电影风格外观。

## 摘要（原文）

> Pro-Mist filters are widely used in cinematography for their ability to create soft halation, lower contrast, and produce a distinctive, atmospheric style. These effects are difficult to reproduce digitally due to the complex behavior of light diffusion. We present ProMist-5K, a dataset designed to support cinematic style emulation. It is built using a physically inspired pipeline in a scene-referred linear space and includes 20,000 high-resolution image pairs across four configurations, covering two filter densities (1/2 and 1/8) and two focal lengths (20mm and 50mm). Unlike general style datasets, ProMist-5K focuses on realistic glow and highlight diffusion effects. Multiple blur layers and carefully tuned weighting are used to model the varying intensity and spread of optical diffusion. The dataset provides a consistent and controllable target domain that supports various image translation models and learning paradigms. Experiments show that the dataset works well across different training settings and helps capture both subtle and strong cinematic appearances. ProMist-5K offers a practical and physically grounded resource for film-inspired image transformation, bridging the gap between digital flexibility and traditional lens aesthetics. The dataset is available at https://www.kaggle.com/datasets/yingtielei/promist5k.

