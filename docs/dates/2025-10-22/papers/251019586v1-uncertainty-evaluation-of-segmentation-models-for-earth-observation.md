---
layout: default
title: Uncertainty evaluation of segmentation models for Earth observation
---

# Uncertainty evaluation of segmentation models for Earth observation
**arXiv**：[2510.19586v1](https://arxiv.org/abs/2510.19586) · [PDF](https://arxiv.org/pdf/2510.19586.pdf)  
**作者**：Melanie Rey, Andriy Mnih, Maxim Neumann, Matt Overlan, Drew Purves  

**一句话要点**：评估遥感图像分割模型的不确定性方法，以识别预测错误和噪声区域

**关键词**：语义分割, 不确定性估计, 遥感图像, 基准测试, 预测错误识别

## 3 点简述
- 核心问题：语义分割不确定性估计在遥感应用中面临可扩展性和逐像素估计挑战
- 方法要点：基准测试多种模型如随机分割网络和集成方法，结合不同架构和不确定性指标
- 实验或效果：在PASTIS和ForTy数据集上评估不确定性度量识别错误和噪声的能力

## 摘要（原文）

> This paper investigates methods for estimating uncertainty in semantic
> segmentation predictions derived from satellite imagery. Estimating uncertainty
> for segmentation presents unique challenges compared to standard image
> classification, requiring scalable methods producing per-pixel estimates. While
> most research on this topic has focused on scene understanding or medical
> imaging, this work benchmarks existing methods specifically for remote sensing
> and Earth observation applications. Our evaluation focuses on the practical
> utility of uncertainty measures, testing their ability to identify prediction
> errors and noise-corrupted input image regions. Experiments are conducted on
> two remote sensing datasets, PASTIS and ForTy, selected for their differences
> in scale, geographic coverage, and label confidence. We perform an extensive
> evaluation featuring several models, such as Stochastic Segmentation Networks
> and ensembles, in combination with a number of neural architectures and
> uncertainty metrics. We make a number of practical recommendations based on our
> findings.

