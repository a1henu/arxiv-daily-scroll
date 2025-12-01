---
layout: default
title: Cascaded Robust Rectification for Arbitrary Document Images
---

# Cascaded Robust Rectification for Arbitrary Document Images
**arXiv**：[2511.23150v1](https://arxiv.org/abs/2511.23150) · [PDF](https://arxiv.org/pdf/2511.23150.pdf)  
**作者**：Chaoyun Wang, Quanxin Huang, I-Chao Shen, Takeo Igarashi, Nanning Zheng, Caigui Jiang  

**一句话要点**：提出级联鲁棒校正框架以解决任意文档图像中的视角和物理变形问题

**关键词**：文档校正, 几何变形, 多阶段框架, 评估指标, 真实场景应用

## 3 点简述
- 核心问题：真实场景文档校正面临相机视角和物理变形的极端变化挑战
- 方法要点：采用多阶段框架，从粗到细逐步校正视角、几何和内容变形
- 实验或效果：在多个基准测试中实现最先进性能，AAD指标降低14.1%–34.7%

## 摘要（原文）

> Document rectification in real-world scenarios poses significant challenges due to extreme variations in camera perspectives and physical distortions. Driven by the insight that complex transformations can be decomposed and resolved progressively, we introduce a novel multi-stage framework that progressively reverses distinct distortion types in a coarse-to-fine manner. Specifically, our framework first performs a global affine transformation to correct perspective distortions arising from the camera's viewpoint, then rectifies geometric deformations resulting from physical paper curling and folding, and finally employs a content-aware iterative process to eliminate fine-grained content distortions. To address limitations in existing evaluation protocols, we also propose two enhanced metrics: layout-aligned OCR metrics (AED/ACER) for a stable assessment that decouples geometric rectification quality from the layout analysis errors of OCR engines, and masked AD/AAD (AD-M/AAD-M) tailored for accurately evaluating geometric distortions in documents with incomplete boundaries. Extensive experiments show that our method establishes new state-of-the-art performance on multiple challenging benchmarks, yielding a substantial reduction of 14.1\%--34.7\% in the AAD metric and demonstrating superior efficacy in real-world applications. The code will be publicly available at https://github.com/chaoyunwang/ArbDR.

