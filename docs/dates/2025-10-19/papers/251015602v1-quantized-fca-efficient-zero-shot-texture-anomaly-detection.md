---
layout: default
title: Quantized FCA: Efficient Zero-Shot Texture Anomaly Detection
---

# Quantized FCA: Efficient Zero-Shot Texture Anomaly Detection
**arXiv**：[2510.15602v1](https://arxiv.org/abs/2510.15602) · [PDF](https://arxiv.org/pdf/2510.15602.pdf)  
**作者**：Andrei-Timotei Ardelean, Patrick Rückbeil, Tim Weyrich  

**一句话要点**：提出量化FCA方法以实时检测纹理异常

**关键词**：纹理异常检测, 零样本学习, 量化算法, 实时系统, 特征对应分析

## 3 点简述
- 核心问题：现有纹理异常检测方法运行时间过长，难以实际部署。
- 方法要点：采用量化特征对应分析，通过直方图比较实现10倍加速。
- 实验或效果：在精度损失极小下，速度显著提升，优于现有方法。

## 摘要（原文）

> Zero-shot anomaly localization is a rising field in computer vision research,
> with important progress in recent years. This work focuses on the problem of
> detecting and localizing anomalies in textures, where anomalies can be defined
> as the regions that deviate from the overall statistics, violating the
> stationarity assumption. The main limitation of existing methods is their high
> running time, making them impractical for deployment in real-world scenarios,
> such as assembly line monitoring. We propose a real-time method, named QFCA,
> which implements a quantized version of the feature correspondence analysis
> (FCA) algorithm. By carefully adapting the patch statistics comparison to work
> on histograms of quantized values, we obtain a 10x speedup with little to no
> loss in accuracy. Moreover, we introduce a feature preprocessing step based on
> principal component analysis, which enhances the contrast between normal and
> anomalous features, improving the detection precision on complex textures. Our
> method is thoroughly evaluated against prior art, comparing favorably with
> existing methods. Project page:
> https://reality.tf.fau.de/pub/ardelean2025quantized.html

