---
layout: default
title: WSI-INR: Implicit Neural Representations for Lesion Segmentation in Whole-Slide Images
---

# WSI-INR: Implicit Neural Representations for Lesion Segmentation in Whole-Slide Images
**arXiv**：[2603.03749v1](https://arxiv.org/abs/2603.03749) · [PDF](https://arxiv.org/pdf/2603.03749.pdf)  
**作者**：Yunheng Wu, Wenqi Huang, Liangyi Wang, Masahiro Oda, Yuichiro Hayashi, Daniel Rueckert, Kensaku Mori  

**一句话要点**：提出WSI-INR，基于隐式神经表示实现全切片图像中病灶的无碎片分割。

**关键词**：全切片图像分割, 隐式神经表示, 多分辨率哈希网格, 病灶分割, 计算病理学

## 3 点简述
- 现有方法将全切片图像分割为离散块，破坏空间连续性，导致分割碎片化。
- WSI-INR将图像建模为连续隐函数，直接映射坐标到语义特征，保持空间信息。
- 实验显示WSI-INR在分辨率变化下保持稳健性能，优于U-Net和TransUNet。

## 摘要（原文）

> Whole-slide images (WSIs) are fundamental for computational pathology, where accurate lesion segmentation is critical for clinical decision making. Existing methods partition WSIs into discrete patches, disrupting spatial continuity and treating multi-resolution views as independent samples, which leads to spatially fragmented segmentation and reduced robustness to resolution variations. To address the issues, we propose WSI-INR, a novel patch-free framework based on Implicit Neural Representations (INRs). WSI-INR models the WSI as a continuous implicit function mapping spatial coordinates directly to tissue semantics features, outputting segmentation results while preserving intrinsic spatial information across the entire slide. In the WSI-INR, we incorporate multi-resolution hash grid encoding to regard different resolution levels as varying sampling densities of the same continuous tissue, achieving a consistent feature representation across resolutions. In addition, by jointly training a shared INR decoder, WSI-INR can capture general priors across different cases. Experimental results showed that WSI-INR maintains robust segmentation performance across resolutions; at Base/4, our resolution-specific optimization improves Dice score by +26.11%, while U-Net and TransUNet decrease by 54.28% and 36.18%, respectively. Crucially, this work enables INRs to segment highly heterogeneous pathological lesions beyond structurally consistent anatomical tissues, offering a fresh perspective for pathological analysis.

