---
layout: default
title: VAAS: Vision-Attention Anomaly Scoring for Image Manipulation Detection in Digital Forensics
---

# VAAS: Vision-Attention Anomaly Scoring for Image Manipulation Detection in Digital Forensics
**arXiv**：[2512.15512v1](https://arxiv.org/abs/2512.15512) · [PDF](https://arxiv.org/pdf/2512.15512.pdf)  
**作者**：Opeyemi Bamigbade, Mark Scanlon, John Sheppard  

**一句话要点**：提出VAAS框架，结合视觉注意力与自一致性评分，用于数字取证中的图像篡改检测。

**关键词**：图像篡改检测, 数字取证, 视觉注意力, 异常评分, Vision Transformers, 自一致性

## 3 点简述
- 核心问题：AI生成图像难以被传统基于像素或压缩伪影的检测器识别，且缺乏篡改强度的量化指标。
- 方法要点：集成Vision Transformers的全局注意力异常估计与SegFormer嵌入的补丁级自一致性评分，提供连续可解释的异常分数。
- 实验或效果：在DF2023和CASIA v2.0数据集上实现竞争性F1和IoU性能，并通过注意力引导异常图增强视觉可解释性。

## 摘要（原文）

> Recent advances in AI-driven image generation have introduced new challenges for verifying the authenticity of digital evidence in forensic investigations. Modern generative models can produce visually consistent forgeries that evade traditional detectors based on pixel or compression artefacts. Most existing approaches also lack an explicit measure of anomaly intensity, which limits their ability to quantify the severity of manipulation. This paper introduces Vision-Attention Anomaly Scoring (VAAS), a novel dual-module framework that integrates global attention-based anomaly estimation using Vision Transformers (ViT) with patch-level self-consistency scoring derived from SegFormer embeddings. The hybrid formulation provides a continuous and interpretable anomaly score that reflects both the location and degree of manipulation. Evaluations on the DF2023 and CASIA v2.0 datasets demonstrate that VAAS achieves competitive F1 and IoU performance, while enhancing visual explainability through attention-guided anomaly maps. The framework bridges quantitative detection with human-understandable reasoning, supporting transparent and reliable image integrity assessment. The source code for all experiments and corresponding materials for reproducing the results are available open source.

