---
layout: default
title: SEP-YOLO: Fourier-Domain Feature Representation for Transparent Object Instance Segmentation
---

# SEP-YOLO: Fourier-Domain Feature Representation for Transparent Object Instance Segmentation
**arXiv**：[2603.02648v1](https://arxiv.org/abs/2603.02648) · [PDF](https://arxiv.org/pdf/2603.02648.pdf)  
**作者**：Fengming Zhang, Tao Yan, Jianchao Huang  

**一句话要点**：提出SEP-YOLO框架，通过频域特征增强解决透明物体实例分割难题

**关键词**：透明物体实例分割, 频域特征表示, 多尺度细化, YOLO框架, 数据集标注

## 3 点简述
- 透明物体因边界模糊、低对比度等特性，导致实例分割困难
- 方法结合频域细节增强模块和多尺度空间细化流，提升边界定位精度
- 在Trans10K和GVD数据集上实现SOTA性能，并提供高质量标注数据

## 摘要（原文）

> Transparent object instance segmentation presents significant challenges in computer vision, due to the inherent properties of transparent objects, including boundary blur, low contrast, and high dependence on background context. Existing methods often fail as they depend on strong appearance cues and clear boundaries. To address these limitations, we propose SEP-YOLO, a novel framework that integrates a dual-domain collaborative mechanism for transparent object instance segmentation. Our method incorporates a Frequency Domain Detail Enhancement Module, which separates and enhances weak highfrequency boundary components via learnable complex weights. We further design a multi-scale spatial refinement stream, which consists of a Content-Aware Alignment Neck and a Multi-scale Gated Refinement Block, to ensure precise feature alignment and boundary localization in deep semantic features. We also provide high-quality instance-level annotations for the Trans10K dataset, filling the critical data gap in transparent object instance segmentation. Extensive experiments on the Trans10K and GVD datasets show that SEP-YOLO achieves state-of-the-art (SOTA) performance.

