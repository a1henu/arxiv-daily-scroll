---
layout: default
title: Multi-Temporal Frames Projection for Dynamic Processes Fusion in Fluorescence Microscopy
---

# Multi-Temporal Frames Projection for Dynamic Processes Fusion in Fluorescence Microscopy
**arXiv**：[2601.10392v1](https://arxiv.org/abs/2601.10392) · [PDF](https://arxiv.org/pdf/2601.10392.pdf)  
**作者**：Hassan Eshkiki, Sarah Costa, Mostafa Mohammadpour, Farinaz Tanhaei, Christopher H. George, Fabio Caraffini  

**一句话要点**：提出多时态帧投影框架以融合荧光显微镜动态过程，提升图像质量与信息保留。

**关键词**：荧光显微镜, 多时态图像融合, 动态过程分析, 图像增强, 生物医学成像, 计算机视觉框架

## 3 点简述
- 核心问题：荧光显微镜记录受噪声、时间变异性和信号振荡影响，限制生物样本分析。
- 方法要点：结合可解释计算机视觉技术，将多时态帧融合为高质量单图像，保留原始生物内容。
- 实验或效果：在心脏细胞2D单层数据集上测试，细胞计数平均提升44%，优于先前方法。

## 摘要（原文）

> Fluorescence microscopy is widely employed for the analysis of living biological samples; however, the utility of the resulting recordings is frequently constrained by noise, temporal variability, and inconsistent visualisation of signals that oscillate over time. We present a unique computational framework that integrates information from multiple time-resolved frames into a single high-quality image, while preserving the underlying biological content of the original video. We evaluate the proposed method through an extensive number of configurations (n = 111) and on a challenging dataset comprising dynamic, heterogeneous, and morphologically complex 2D monolayers of cardiac cells. Results show that our framework, which consists of a combination of explainable techniques from different computer vision application fields, is capable of generating composite images that preserve and enhance the quality and information of individual microscopy frames, yielding 44% average increase in cell count compared to previous methods. The proposed pipeline is applicable to other imaging domains that require the fusion of multi-temporal image stacks into high-quality 2D images, thereby facilitating annotation and downstream segmentation.

