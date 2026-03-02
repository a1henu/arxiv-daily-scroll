---
layout: default
title: A multimodal slice discovery framework for systematic failure detection and explanation in medical image classification
---

# A multimodal slice discovery framework for systematic failure detection and explanation in medical image classification
**arXiv**：[2602.24183v1](https://arxiv.org/abs/2602.24183) · [PDF](https://arxiv.org/pdf/2602.24183.pdf)  
**作者**：Yixuan Liu, Kanwal K. Bhatia, Ahmed E. Fetit  

**一句话要点**：提出多模态切片发现框架，用于医学图像分类中的系统性故障检测与解释

**关键词**：医学图像分类, 多模态表示, 切片发现, 故障检测, 审计框架, 解释生成

## 3 点简述
- 核心问题：现有医学图像分类器审计方法依赖单模态特征或元数据，解释性有限且难以发现隐藏系统性故障。
- 方法要点：扩展切片发现方法至多模态表示，实现自动化审计框架，专门针对医学应用。
- 实验或效果：在MIMIC-CXR-JPG数据集上验证，展示框架在故障发现和解释生成方面的强能力，多模态信息提升审计全面性。

## 摘要（原文）

> Despite advances in machine learning-based medical image classifiers, the safety and reliability of these systems remain major concerns in practical settings. Existing auditing approaches mainly rely on unimodal features or metadata-based subgroup analyses, which are limited in interpretability and often fail to capture hidden systematic failures. To address these limitations, we introduce the first automated auditing framework that extends slice discovery methods to multimodal representations specifically for medical applications. Comprehensive experiments were conducted under common failure scenarios using the MIMIC-CXR-JPG dataset, demonstrating the framework's strong capability in both failure discovery and explanation generation. Our results also show that multimodal information generally allows more comprehensive and effective auditing of classifiers, while unimodal variants beyond image-only inputs exhibit strong potential in scenarios where resources are constrained.

