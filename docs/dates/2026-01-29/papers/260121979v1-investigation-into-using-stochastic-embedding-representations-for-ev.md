---
layout: default
title: Investigation into using stochastic embedding representations for evaluating the trustworthiness of the Fréchet Inception Distance
---

# Investigation into using stochastic embedding representations for evaluating the trustworthiness of the Fréchet Inception Distance
**arXiv**：[2601.21979v1](https://arxiv.org/abs/2601.21979) · [PDF](https://arxiv.org/pdf/2601.21979.pdf)  
**作者**：Ciaran Bench, Vivek Desai, Carlijn Roozemond, Ruben van Engen, Spencer A. Thomas  

**一句话要点**：提出使用蒙特卡洛dropout评估Fréchet Inception Distance在医学图像中的可信度

**关键词**：Fréchet Inception Distance, 蒙特卡洛dropout, 预测方差, 医学图像评估, 分布外检测, 特征嵌入

## 3 点简述
- 核心问题：FID基于自然图像预训练模型，在医学图像应用中可能无法有效捕捉图像特征差异，其可信度未知。
- 方法要点：利用蒙特卡洛dropout计算FID的预测方差，并补充估计特征嵌入模型潜在表示的预测方差。
- 实验或效果：预测方差大小与测试输入相对于训练数据的分布外程度相关，为FID可信度指标提供见解。

## 摘要（原文）

> Feature embeddings acquired from pretrained models are widely used in medical applications of deep learning to assess the characteristics of datasets; e.g. to determine the quality of synthetic, generated medical images. The Fréchet Inception Distance (FID) is one popular synthetic image quality metric that relies on the assumption that the characteristic features of the data can be detected and encoded by an InceptionV3 model pretrained on ImageNet1K (natural images). While it is widely known that this makes it less effective for applications involving medical images, the extent to which the metric fails to capture meaningful differences in image characteristics is not obviously known. Here, we use Monte Carlo dropout to compute the predictive variance in the FID as well as a supplemental estimate of the predictive variance in the feature embedding model's latent representations. We show that the magnitudes of the predictive variances considered exhibit varying degrees of correlation with the extent to which test inputs (ImageNet1K validation set augmented at various strengths, and other external datasets) are out-of-distribution relative to its training data, providing some insight into the effectiveness of their use as indicators of the trustworthiness of the FID.

