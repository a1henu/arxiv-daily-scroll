---
layout: default
title: SOMA-1M: A Large-Scale SAR-Optical Multi-resolution Alignment Dataset for Multi-Task Remote Sensing
---

# SOMA-1M: A Large-Scale SAR-Optical Multi-resolution Alignment Dataset for Multi-Task Remote Sensing
**arXiv**：[2602.05480v1](https://arxiv.org/abs/2602.05480) · [PDF](https://arxiv.org/pdf/2602.05480.pdf)  
**作者**：Peihao Wu, Yongxiang Yao, Yi Wan, Wenfei Zhang, Ruipeng Zhao, Jiayuan Li, Yongjun Zhang  

**一句话要点**：提出SOMA-1M数据集以解决遥感多模态对齐数据不足问题，支持多尺度基础模型训练。

**关键词**：遥感多模态对齐, 像素级图像匹配, 多尺度数据集, SAR-光学融合, 基础模型训练

## 3 点简述
- 现有遥感数据集存在分辨率单一、规模小、对齐精度低等问题，限制多模态模型发展。
- 构建包含130万对像素级对齐图像的数据集，覆盖全球多尺度，采用粗到精匹配框架确保精度。
- 在图像匹配等四项任务上建立评估基准，实验显示训练显著提升性能，匹配达到SOTA水平。

## 摘要（原文）

> Synthetic Aperture Radar (SAR) and optical imagery provide complementary strengths that constitute the critical foundation for transcending single-modality constraints and facilitating cross-modal collaborative processing and intelligent interpretation. However, existing benchmark datasets often suffer from limitations such as single spatial resolution, insufficient data scale, and low alignment accuracy, making them inadequate for supporting the training and generalization of multi-scale foundation models. To address these challenges, we introduce SOMA-1M (SAR-Optical Multi-resolution Alignment), a pixel-level precisely aligned dataset containing over 1.3 million pairs of georeferenced images with a specification of 512 x 512 pixels. This dataset integrates imagery from Sentinel-1, PIESAT-1, Capella Space, and Google Earth, achieving global multi-scale coverage from 0.5 m to 10 m. It encompasses 12 typical land cover categories, effectively ensuring scene diversity and complexity. To address multimodal projection deformation and massive data registration, we designed a rigorous coarse-to-fine image matching framework ensuring pixel-level alignment. Based on this dataset, we established comprehensive evaluation benchmarks for four hierarchical vision tasks, including image matching, image fusion, SAR-assisted cloud removal, and cross-modal translation, involving over 30 mainstream algorithms. Experimental results demonstrate that supervised training on SOMA-1M significantly enhances performance across all tasks. Notably, multimodal remote sensing image (MRSI) matching performance achieves current state-of-the-art (SOTA) levels. SOMA-1M serves as a foundational resource for robust multimodal algorithms and remote sensing foundation models. The dataset will be released publicly at: https://github.com/PeihaoWu/SOMA-1M.

