---
layout: default
title: Adaptive Frequency Domain Alignment Network for Medical image segmentation
---

# Adaptive Frequency Domain Alignment Network for Medical image segmentation
**arXiv**：[2512.16393v1](https://arxiv.org/abs/2512.16393) · [PDF](https://arxiv.org/pdf/2512.16393.pdf)  
**作者**：Zhanwei Li, Liang Li, Jiawan Zhang  

**一句话要点**：提出自适应频域对齐网络以解决医学图像分割中的数据稀缺问题

**关键词**：医学图像分割, 域适应, 频域对齐, 对抗学习, 特征融合

## 3 点简述
- 核心问题：医学图像分割中高质量标注数据稀缺，影响模型准确性
- 方法要点：通过频域特征对齐、源-目标频域融合和空间-频域集成实现跨域知识迁移
- 实验或效果：在VITILIGO2025数据集上IoU达90.9%，DRIVE基准上IoU为82.6%，超越现有方法

## 摘要（原文）

> High-quality annotated data plays a crucial role in achieving accurate segmentation. However, such data for medical image segmentation are often scarce due to the time-consuming and labor-intensive nature of manual annotation. To address this challenge, we propose the Adaptive Frequency Domain Alignment Network (AFDAN)--a novel domain adaptation framework designed to align features in the frequency domain and alleviate data scarcity. AFDAN integrates three core components to enable robust cross-domain knowledge transfer: an Adversarial Domain Learning Module that transfers features from the source to the target domain; a Source-Target Frequency Fusion Module that blends frequency representations across domains; and a Spatial-Frequency Integration Module that combines both frequency and spatial features to further enhance segmentation accuracy across domains. Extensive experiments demonstrate the effectiveness of AFDAN: it achieves an Intersection over Union (IoU) of 90.9% for vitiligo segmentation in the newly constructed VITILIGO2025 dataset and a competitive IoU of 82.6% on the retinal vessel segmentation benchmark DRIVE, surpassing existing state-of-the-art approaches.

