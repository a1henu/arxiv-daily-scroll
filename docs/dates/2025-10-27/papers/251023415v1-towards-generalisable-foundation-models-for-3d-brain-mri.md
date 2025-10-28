---
layout: default
title: Towards Generalisable Foundation Models for 3D Brain MRI
---

# Towards Generalisable Foundation Models for 3D Brain MRI
**arXiv**：[2510.23415v1](https://arxiv.org/abs/2510.23415) · [PDF](https://arxiv.org/pdf/2510.23415.pdf)  
**作者**：Moona Mazher, Geoff J. M. Parker, Daniel C. Alexander  

**一句话要点**：提出BrainFound基础模型以提升3D脑MRI的泛化性和诊断准确性

**关键词**：3D脑MRI, 自监督学习, 基础模型, 多模态输入, 疾病检测, 图像分割

## 3 点简述
- 核心问题：传统方法依赖单切片和大量标注，难以泛化到不同成像协议和临床场景。
- 方法要点：基于DINO-v2扩展，自监督学习3D脑解剖，支持单模态和多模态输入。
- 实验或效果：在标签稀缺和多对比度设置中优于现有方法，提高诊断准确性和减少标注依赖。

## 摘要（原文）

> Foundation models in artificial intelligence (AI) are transforming medical
> imaging by enabling general-purpose feature learning from large-scale,
> unlabeled datasets. In this work, we introduce BrainFound, a self-supervised
> foundation model for brain MRI, built by extending DINO-v2, a vision
> transformer originally designed for 2D natural images. BrainFound adapts
> DINO-v2 to model full 3D brain anatomy by incorporating volumetric information
> from sequential MRI slices, moving beyond conventional single-slice paradigms.
> It supports both single- and multimodal inputs, enabling a broad range of
> downstream tasks, including disease detection and image segmentation, while
> generalising across varied imaging protocols and clinical scenarios. We show
> that BrainFound consistently outperforms existing self-supervised pretraining
> strategies and supervised baselines, particularly in label-scarce and
> multi-contrast settings. By integrating information from diverse 3D MRI
> modalities (e.g., T1, T2, FLAIR), it enhances diagnostic accuracy and reduces
> dependency on extensive expert annotations. This flexibility makes BrainFound a
> scalable and practical solution for 3D neuroimaging pipelines, with significant
> potential for clinical deployment and research innovation.

