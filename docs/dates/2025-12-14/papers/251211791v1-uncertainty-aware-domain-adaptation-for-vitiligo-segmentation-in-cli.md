---
layout: default
title: Uncertainty-Aware Domain Adaptation for Vitiligo Segmentation in Clinical Photographs
---

# Uncertainty-Aware Domain Adaptation for Vitiligo Segmentation in Clinical Photographs
**arXiv**：[2512.11791v1](https://arxiv.org/abs/2512.11791) · [PDF](https://arxiv.org/pdf/2512.11791.pdf)  
**作者**：Wentao Jiang, Vamsi Varra, Caitlin Perez-Stable, Harrison Zhu, Meredith Apicella, Nicole Nyamongo  

**一句话要点**：提出不确定性感知域适应框架，用于临床照片中白癜风分割，以提升量化准确性和可靠性。

**关键词**：医学图像分割, 域适应, 不确定性估计, 高频特征提取, 临床照片分析, 白癜风量化

## 3 点简述
- 核心问题：临床照片中白癜风区域分割受背景噪声和纹理细微变化影响，需高精度量化以监测治疗反应。
- 方法要点：结合域适应预训练、高频谱门控模块和双任务损失，增强模型对细微纹理的捕捉并抑制噪声。
- 实验或效果：在专家标注数据集上验证，Dice分数达85.05%，边界误差显著降低，优于CNN和Transformer基线，提供不确定性地图增强临床信任。

## 摘要（原文）

> Accurately quantifying vitiligo extent in routine clinical photographs is crucial for longitudinal monitoring of treatment response. We propose a trustworthy, frequency-aware segmentation framework built on three synergistic pillars: (1) a data-efficient training strategy combining domain-adaptive pre-training on the ISIC 2019 dataset with an ROI-constrained dual-task loss to suppress background noise; (2) an architectural refinement via a ConvNeXt V2-based encoder enhanced with a novel High-Frequency Spectral Gating (HFSG) module and stem-skip connections to capture subtle textures; and (3) a clinical trust mechanism employing K-fold ensemble and Test-Time Augmentation (TTA) to generate pixel-wise uncertainty maps. Extensive validation on an expert-annotated clinical cohort demonstrates superior performance, achieving a Dice score of 85.05% and significantly reducing boundary error (95% Hausdorff Distance improved from 44.79 px to 29.95 px), consistently outperforming strong CNN (ResNet-50 and UNet++) and Transformer (MiT-B5) baselines. Notably, our framework demonstrates high reliability with zero catastrophic failures and provides interpretable entropy maps to identify ambiguous regions for clinician review. Our approach suggests that the proposed framework establishes a robust and reliable standard for automated vitiligo assessment.

