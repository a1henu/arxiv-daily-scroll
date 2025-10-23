---
layout: default
title: Predicting before Reconstruction: A generative prior framework for MRI acceleration
---

# Predicting before Reconstruction: A generative prior framework for MRI acceleration
**arXiv**：[2510.19472v1](https://arxiv.org/abs/2510.19472) · [PDF](https://arxiv.org/pdf/2510.19472.pdf)  
**作者**：Juhyung Park, Rokgi Hong, Roh-Eul Yoo, Jaehyeon Koo, Se Young Chun, Seung Hong Choi, Jongho Lee  

**一句话要点**：提出生成先验框架以加速MRI，通过预测目标对比图像重构欠采样数据

**关键词**：MRI加速, 生成先验, 图像重构, 预测成像, 欠采样数据

## 3 点简述
- MRI采集时间长，限制临床吞吐量，需加速成像过程
- 使用生成模型预测目标对比图像，作为数据驱动先验重构欠采样数据
- 在多个数据集上评估，高加速因子下性能优于其他方法

## 摘要（原文）

> Recent advancements in artificial intelligence have created transformative
> capabilities in image synthesis and generation, enabling diverse research
> fields to innovate at revolutionary speed and spectrum. In this study, we
> leverage this generative power to introduce a new paradigm for accelerating
> Magnetic Resonance Imaging (MRI), introducing a shift from image reconstruction
> to proactive predictive imaging. Despite being a cornerstone of modern patient
> care, MRI's lengthy acquisition times limit clinical throughput. Our novel
> framework addresses this challenge by first predicting a target contrast image,
> which then serves as a data-driven prior for reconstructing highly
> under-sampled data. This informative prior is predicted by a generative model
> conditioned on diverse data sources, such as other contrast images, previously
> scanned images, acquisition parameters, patient information. We demonstrate
> this approach with two key applications: (1) reconstructing FLAIR images using
> predictions from T1w and/or T2w scans, and (2) reconstructing T1w images using
> predictions from previously acquired T1w scans. The framework was evaluated on
> internal and multiple public datasets (total 14,921 scans; 1,051,904 slices),
> including multi-channel k-space data, for a range of high acceleration factors
> (x4, x8 and x12). The results demonstrate that our prediction-prior
> reconstruction method significantly outperforms other approaches, including
> those with alternative or no prior information. Through this framework we
> introduce a fundamental shift from image reconstruction towards a new paradigm
> of predictive imaging.

