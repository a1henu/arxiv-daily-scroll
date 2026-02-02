---
layout: default
title: Diachronic Stereo Matching for Multi-Date Satellite Imagery
---

# Diachronic Stereo Matching for Multi-Date Satellite Imagery
**arXiv**：[2601.22808v1](https://arxiv.org/abs/2601.22808) · [PDF](https://arxiv.org/pdf/2601.22808.pdf)  
**作者**：Elías Masquil, Luca Savant Aira, Roger Marí, Thibaud Ehret, Pablo Musé, Gabriele Facciolo  

**一句话要点**：提出历时立体匹配方法，解决卫星图像因时间间隔长导致重建失败的问题。

**关键词**：历时立体匹配, 卫星图像重建, 深度网络微调, 多日期遥感, 单目深度先验, 三维几何恢复

## 3 点简述
- 核心问题：卫星图像采集时间相隔数月时，季节、光照和阴影变化违反标准立体假设，使现有重建方法失效。
- 方法要点：基于预训练的MonSter模型，利用单目深度先验，在包含历时图像对的数据集上进行微调。
- 实验或效果：在WorldView-3图像上测试，本方法在同步和历时设置下均优于传统流程和未适配的深度模型。

## 摘要（原文）

> Recent advances in image-based satellite 3D reconstruction have progressed along two complementary directions. On one hand, multi-date approaches using NeRF or Gaussian-splatting jointly model appearance and geometry across many acquisitions, achieving accurate reconstructions on opportunistic imagery with numerous observations. On the other hand, classical stereoscopic reconstruction pipelines deliver robust and scalable results for simultaneous or quasi-simultaneous image pairs. However, when the two images are captured months apart, strong seasonal, illumination, and shadow changes violate standard stereoscopic assumptions, causing existing pipelines to fail. This work presents the first Diachronic Stereo Matching method for satellite imagery, enabling reliable 3D reconstruction from temporally distant pairs. Two advances make this possible: (1) fine-tuning a state-of-the-art deep stereo network that leverages monocular depth priors, and (2) exposing it to a dataset specifically curated to include a diverse set of diachronic image pairs. In particular, we start from a pretrained MonSter model, trained initially on a mix of synthetic and real datasets such as SceneFlow and KITTI, and fine-tune it on a set of stereo pairs derived from the DFC2019 remote sensing challenge. This dataset contains both synchronic and diachronic pairs under diverse seasonal and illumination conditions. Experiments on multi-date WorldView-3 imagery demonstrate that our approach consistently surpasses classical pipelines and unadapted deep stereo models on both synchronic and diachronic settings. Fine-tuning on temporally diverse images, together with monocular priors, proves essential for enabling 3D reconstruction from previously incompatible acquisition dates. Left image (winter) Right image (autumn) DSM geometry Ours (1.23 m) Zero-shot (3.99 m) LiDAR GT Figure 1. Output geometry for a winter-autumn image pair from Omaha (OMA 331 test scene). Our method recovers accurate geometry despite the diachronic nature of the pair, exhibiting strong appearance changes, which cause existing zero-shot methods to fail. Missing values due to perspective shown in black.  Mean altitude error in parentheses; lower is better.

