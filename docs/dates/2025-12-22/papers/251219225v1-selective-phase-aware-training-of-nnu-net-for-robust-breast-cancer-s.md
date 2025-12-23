---
layout: default
title: Selective Phase-Aware Training of nnU-Net for Robust Breast Cancer Segmentation in Multi-Center DCE-MRI
---

# Selective Phase-Aware Training of nnU-Net for Robust Breast Cancer Segmentation in Multi-Center DCE-MRI
**arXiv**：[2512.19225v1](https://arxiv.org/abs/2512.19225) · [PDF](https://arxiv.org/pdf/2512.19225.pdf)  
**作者**：Beyza Zayim, Aissiou Ikram, Boukhiar Naima  

**一句话要点**：提出选择性相位感知训练框架以增强nnU-Net在多中心DCE-MRI乳腺癌分割中的鲁棒性

**关键词**：乳腺癌分割, DCE-MRI, nnU-Net, 选择性训练, 多中心数据, 图像质量

## 3 点简述
- 核心问题：多中心DCE-MRI数据质量差异影响乳腺癌分割性能，缺乏标准化基准。
- 方法要点：基于nnU-Net，采用选择性训练策略，分析图像质量和中心变异性，优先使用高质量早期相位数据。
- 实验或效果：在DUKE、NACT等数据集上验证，高质量数据训练提升分割稳定性，低质量数据（如ISPY）损害性能。

## 摘要（原文）

> Breast cancer remains the most common cancer among women and is a leading cause of female mortality. Dynamic contrast-enhanced MRI (DCE-MRI) is a powerful imaging tool for evaluating breast tumors, yet the field lacks a standardized benchmark for analyzing treatment responses and guiding personalized care. We participated in the MAMA-MIA Challenge's Primary Tumor Segmentation task and this work presents a proposed selective, phase-aware training framework for the nnU-Net architecture, emphasizing quality-focused data selection to strengthen model robustness and generalization. We employed the No New Net (nnU-Net) framework with a selective training strategy that systematically analyzed the impact of image quality and center-specific variability on segmentation performance. Controlled experiments on the DUKE, NACT, ISPY1, and ISPY2 datasets revealed that including ISPY scans with motion artifacts and reduced contrast impaired segmentation performance, even with advanced preprocessing, such as contrast-limited adaptive histogram equalization (CLAHE). In contrast, training on DUKE and NACT data, which exhibited clearer contrast and fewer motion artifacts despite varying resolutions, with early phase images (0000-0002) provided more stable training conditions. Our results demonstrate the importance of phase-sensitive and quality-aware training strategies in achieving reliable segmentation performance in heterogeneous clinical datasets, highlighting the limitations of the expansion of naive datasets and motivating the need for future automation of quality-based data selection strategies.

