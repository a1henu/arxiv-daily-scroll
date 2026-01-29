---
layout: default
title: Bridging the Applicator Gap with Data-Doping:Dual-Domain Learning for Precise Bladder Segmentation in CT-Guided Brachytherapy
---

# Bridging the Applicator Gap with Data-Doping:Dual-Domain Learning for Precise Bladder Segmentation in CT-Guided Brachytherapy
**arXiv**：[2601.20302v1](https://arxiv.org/abs/2601.20302) · [PDF](https://arxiv.org/pdf/2601.20302.pdf)  
**作者**：Suresh Das, Siladittya Manna, Sayantari Ghosh  

**一句话要点**：提出双域学习策略，结合无与有施源器CT数据，提升膀胱分割在协变量偏移下的鲁棒性。

**关键词**：医学图像分割, 协变量偏移, 双域学习, 近距离放疗, 膀胱分割, 数据掺杂

## 3 点简述
- 核心问题：CT引导近距离放疗中，有施源器图像稀缺且存在解剖变形和伪影，导致分割模型性能下降。
- 方法要点：通过数据掺杂，将少量有施源器数据融入无施源器训练集，实现双域学习以增强模型适应性。
- 实验或效果：仅掺杂10-30%有施源器数据，即可达到与全有施源器数据训练相当的分割性能，Dice系数最高0.94。

## 摘要（原文）

> Performance degradation due to covariate shift remains a major challenge for deep learning models in medical image segmentation. An open question is whether samples from a shifted distribution can effectively support learning when combined with limited target domain data. We investigate this problem in the context of bladder segmentation in CT guided gynecological brachytherapy, a critical task for accurate dose optimization and organ at risk sparing. While CT scans without brachytherapy applicators (no applicator: NA) are widely available, scans with applicators inserted (with applicator: WA) are scarce and exhibit substantial anatomical deformation and imaging artifacts, making automated segmentation particularly difficult.
>   We propose a dual domain learning strategy that integrates NA and WA CT data to improve robustness and generalizability under covariate shift. Using a curated assorted dataset, we show that NA data alone fail to capture the anatomical and artifact related characteristics of WA images. However, introducing a modest proportion of WA data into a predominantly NA training set leads to significant performance improvements. Through systematic experiments across axial, coronal, and sagittal planes using multiple deep learning architectures, we demonstrate that doping only 10 to 30 percent WA data achieves segmentation performance comparable to models trained exclusively on WA data.
>   The proposed approach attains Dice similarity coefficients of up to 0.94 and Intersection over Union scores of up to 0.92, indicating effective domain adaptation and improved clinical reliability. This study highlights the value of integrating anatomically similar but distribution shifted datasets to overcome data scarcity and enhance deep learning based segmentation for brachytherapy treatment planning.

