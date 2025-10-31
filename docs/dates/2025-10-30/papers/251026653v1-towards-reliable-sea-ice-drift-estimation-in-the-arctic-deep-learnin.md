---
layout: default
title: Towards Reliable Sea Ice Drift Estimation in the Arctic Deep Learning Optical Flow on RADARSAT-2
---

# Towards Reliable Sea Ice Drift Estimation in the Arctic Deep Learning Optical Flow on RADARSAT-2
**arXiv**：[2510.26653v1](https://arxiv.org/abs/2510.26653) · [PDF](https://arxiv.org/pdf/2510.26653.pdf)  
**作者**：Daniela Martin, Joseph Gallego  

**一句话要点**：提出深度学习光流方法以估计北极海冰漂移，基于RADARSAT-2影像

**关键词**：海冰漂移估计, 深度学习光流, RADARSAT-2影像, 北极遥感, 运动估计, 卫星图像分析

## 3 点简述
- 核心问题：传统光流方法在复杂场景下精度受限，海冰漂移估计对北极导航和气候研究至关重要。
- 方法要点：首次大规模评估48种深度学习光流模型，应用于SAR卫星影像，实现像素级运动估计。
- 实验或效果：模型达到亚公里级精度，捕获区域漂移模式，优于经典方法，提供连续漂移场。

## 摘要（原文）

> Accurate estimation of sea ice drift is critical for Arctic navigation,
> climate research, and operational forecasting. While optical flow, a computer
> vision technique for estimating pixel wise motion between consecutive images,
> has advanced rapidly in computer vision, its applicability to geophysical
> problems and to satellite SAR imagery remains underexplored. Classical optical
> flow methods rely on mathematical models and strong assumptions about motion,
> which limit their accuracy in complex scenarios. Recent deep learning based
> approaches have substantially improved performance and are now the standard in
> computer vision, motivating their application to sea ice drift estimation. We
> present the first large scale benchmark of 48 deep learning optical flow models
> on RADARSAT 2 ScanSAR sea ice imagery, evaluated with endpoint error (EPE) and
> Fl all metrics against GNSS tracked buoys. Several models achieve sub kilometer
> accuracy (EPE 6 to 8 pixels, 300 to 400 m), a small error relative to the
> spatial scales of sea ice motion and typical navigation requirements in the
> Arctic. Our results demonstrate that the models are capable of capturing
> consistent regional drift patterns and that recent deep learning based optical
> flow methods, which have substantially improved motion estimation accuracy
> compared to classical methods, can be effectively transferred to polar remote
> sensing. Optical flow produces spatially continuous drift fields, providing
> motion estimates for every image pixel rather than at sparse buoy locations,
> offering new opportunities for navigation and climate modeling.

