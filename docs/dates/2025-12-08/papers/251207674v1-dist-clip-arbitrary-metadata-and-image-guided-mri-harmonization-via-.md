---
layout: default
title: DIST-CLIP: Arbitrary Metadata and Image Guided MRI Harmonization via Disentangled Anatomy-Contrast Representations
---

# DIST-CLIP: Arbitrary Metadata and Image Guided MRI Harmonization via Disentangled Anatomy-Contrast Representations
**arXiv**：[2512.07674v1](https://arxiv.org/abs/2512.07674) · [PDF](https://arxiv.org/pdf/2512.07674.pdf)  
**作者**：Mehmet Yigit Avci, Pedro Borges, Virginia Fernandez, Paul Wright, Mehmet Yigitsoy, Sebastien Ourselin, Jorge Cardoso  

**一句话要点**：提出DIST-CLIP框架，通过解耦解剖-对比表示实现任意元数据和图像引导的MRI数据协调

**关键词**：MRI数据协调, 解耦表示, CLIP引导, 自适应风格转移, 医学图像分析

## 3 点简述
- 核心问题：MRI数据因扫描仪和协议差异导致异质性，现有方法依赖目标图像或简单标签，难以处理真实临床环境。
- 方法要点：使用预训练CLIP编码器提取对比表示，通过自适应风格转移模块整合到解剖内容中，支持图像或DICOM元数据引导。
- 实验或效果：在真实临床数据集上评估，相比先进方法在风格转换保真度和解剖保留方面表现显著提升。

## 摘要（原文）

> Deep learning holds immense promise for transforming medical image analysis, yet its clinical generalization remains profoundly limited. A major barrier is data heterogeneity. This is particularly true in Magnetic Resonance Imaging, where scanner hardware differences, diverse acquisition protocols, and varying sequence parameters introduce substantial domain shifts that obscure underlying biological signals. Data harmonization methods aim to reduce these instrumental and acquisition variability, but existing approaches remain insufficient. When applied to imaging data, image-based harmonization approaches are often restricted by the need for target images, while existing text-guided methods rely on simplistic labels that fail to capture complex acquisition details or are typically restricted to datasets with limited variability, failing to capture the heterogeneity of real-world clinical environments. To address these limitations, we propose DIST-CLIP (Disentangled Style Transfer with CLIP Guidance), a unified framework for MRI harmonization that flexibly uses either target images or DICOM metadata for guidance. Our framework explicitly disentangles anatomical content from image contrast, with the contrast representations being extracted using pre-trained CLIP encoders. These contrast embeddings are then integrated into the anatomical content via a novel Adaptive Style Transfer module. We trained and evaluated DIST-CLIP on diverse real-world clinical datasets, and showed significant improvements in performance when compared against state-of-the-art methods in both style translation fidelity and anatomical preservation, offering a flexible solution for style transfer and standardizing MRI data. Our code and weights will be made publicly available upon publication.

