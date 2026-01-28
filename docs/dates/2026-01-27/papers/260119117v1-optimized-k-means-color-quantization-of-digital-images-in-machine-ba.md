---
layout: default
title: Optimized $k$-means color quantization of digital images in machine-based and human perception-based colorspaces
---

# Optimized $k$-means color quantization of digital images in machine-based and human perception-based colorspaces
**arXiv**：[2601.19117v1](https://arxiv.org/abs/2601.19117) · [PDF](https://arxiv.org/pdf/2601.19117.pdf)  
**作者**：Ranjan Maitra  

**一句话要点**：比较k-means颜色量化在机器与人类感知色彩空间中的性能，基于VIF评估量化图像质量

**关键词**：颜色量化, k-means算法, 色彩空间比较, 图像质量评估, 视觉信息保真度

## 3 点简述
- 研究k-means颜色量化在RGB、CIE-XYZ和CIE-LUV/HCL色彩空间中的性能差异
- 使用VIF指标评估148张多样化图像的量化质量，发现性能随色彩空间和量化级别变化
- 分析图像色调、色度和亮度分布，为不同色彩空间适用性提供细致特征描述

## 摘要（原文）

> Color quantization represents an image using a fraction of its original number of colors while only minimally losing its visual quality. The $k$-means algorithm is commonly used in this context, but has mostly been applied in the machine-based RGB colorspace composed of the three primary colors. However, some recent studies have indicated its improved performance in human perception-based colorspaces. We investigated the performance of $k$-means color quantization at four quantization levels in the RGB, CIE-XYZ, and CIE-LUV/CIE-HCL colorspaces, on 148 varied digital images spanning a wide range of scenes, subjects and settings. The Visual Information Fidelity (VIF) measure numerically assessed the quality of the quantized images, and showed that in about half of the cases, $k$-means color quantization is best in the RGB space, while at other times, and especially for higher quantization levels ($k$), the CIE-XYZ colorspace is where it usually does better. There are also some cases, especially at lower $k$, where the best performance is obtained in the CIE-LUV colorspace. Further analysis of the performances in terms of the distributions of the hue, chromaticity and luminance in an image presents a nuanced perspective and characterization of the images for which each colorspace is better for $k$-means color quantization.

