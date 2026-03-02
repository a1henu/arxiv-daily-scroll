---
layout: default
title: Revisiting Integration of Image and Metadata for DICOM Series Classification: Cross-Attention and Dictionary Learning
---

# Revisiting Integration of Image and Metadata for DICOM Series Classification: Cross-Attention and Dictionary Learning
**arXiv**：[2602.23833v1](https://arxiv.org/abs/2602.23833) · [PDF](https://arxiv.org/pdf/2602.23833.pdf)  
**作者**：Tuan Truong, Melanie Dohmen, Sara Lorio, Matthias Lenga  

**一句话要点**：提出基于交叉注意力和字典学习的多模态框架，以解决DICOM序列分类中的图像与元数据融合挑战。

**关键词**：DICOM序列分类, 多模态融合, 交叉注意力, 字典学习, 医学图像分析, 元数据处理

## 3 点简述
- 核心问题：DICOM序列分类面临图像内容异质、序列长度可变及元数据缺失或不一致等挑战。
- 方法要点：采用双向跨模态注意力融合图像与元数据，并设计稀疏感知的元数据编码器，无需插补处理缺失值。
- 实验或效果：在公开和内部数据集上评估，方法优于仅图像、仅元数据及多模态基线，提升鲁棒性和泛化能力。

## 摘要（原文）

> Automated identification of DICOM image series is essential for large-scale medical image analysis, quality control, protocol harmonization, and reliable downstream processing. However, DICOM series classification remains challenging due to heterogeneous slice content, variable series length, and entirely missing, incomplete or inconsistent DICOM metadata. We propose an end-to-end multimodal framework for DICOM series classification that jointly models image content and acquisition metadata while explicitly accounting for all these challenges. (i) Images and metadata are encoded with modality-aware modules and fused using a bi-directional cross-modal attention mechanism. (ii) Metadata is processed by a sparse, missingness-aware encoder based on learnable feature dictionaries and value-conditioned modulation. By design, the approach does not require any form of imputation. (iii) Variability in series length and image data dimensions is handled via a 2.5D visual encoder and attention operating on equidistantly sampled slices. We evaluate the proposed approach on the publicly available Duke Liver MRI dataset and a large multi-institutional in-house cohort, assessing both in-domain performance and out-of-domain generalization. Across all evaluation settings, the proposed method consistently outperforms relevant image only, metadata-only and multimodal 2D/3D baselines. The results demonstrate that explicitly modeling metadata sparsity and cross-modal interactions improves robustness for DICOM series classification.

