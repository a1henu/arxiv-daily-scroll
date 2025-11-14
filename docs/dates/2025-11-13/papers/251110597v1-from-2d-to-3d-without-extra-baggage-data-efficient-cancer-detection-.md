---
layout: default
title: From 2D to 3D Without Extra Baggage: Data-Efficient Cancer Detection in Digital Breast Tomosynthesis
---

# From 2D to 3D Without Extra Baggage: Data-Efficient Cancer Detection in Digital Breast Tomosynthesis
**arXiv**：[2511.10597v1](https://arxiv.org/abs/2511.10597) · [PDF](https://arxiv.org/pdf/2511.10597.pdf)  
**作者**：Yen Nhi Truong Vu, Dan Guo, Sripad Joshi, Harshit Kumar, Jason Su, Thomas Paul Matthews  

**一句话要点**：提出M&M-3D架构，在数据稀缺的DBT中实现高效3D推理，无需额外参数。

**关键词**：数字乳腺断层合成, 3D推理, 数据高效学习, 癌症检测, 参数免费架构

## 3 点简述
- 核心问题：DBT数据标注有限，现有方法丢弃体积信息或需复杂架构。
- 方法要点：通过修改M&M操作，学习3D特征与切片信息混合，实现参数免费3D推理。
- 实验或效果：在低数据下优于基线，分类和定位性能提升显著。

## 摘要（原文）

> Digital Breast Tomosynthesis (DBT) enhances finding visibility for breast cancer detection by providing volumetric information that reduces the impact of overlapping tissues; however, limited annotated data has constrained the development of deep learning models for DBT. To address data scarcity, existing methods attempt to reuse 2D full-field digital mammography (FFDM) models by either flattening DBT volumes or processing slices individually, thus discarding volumetric information. Alternatively, 3D reasoning approaches introduce complex architectures that require more DBT training data. Tackling these drawbacks, we propose M&M-3D, an architecture that enables learnable 3D reasoning while remaining parameter-free relative to its FFDM counterpart, M&M. M&M-3D constructs malignancy-guided 3D features, and 3D reasoning is learned through repeatedly mixing these 3D features with slice-level information. This is achieved by modifying operations in M&M without adding parameters, thus enabling direct weight transfer from FFDM. Extensive experiments show that M&M-3D surpasses 2D projection and 3D slice-based methods by 11-54% for localization and 3-10% for classification. Additionally, M&M-3D outperforms complex 3D reasoning variants by 20-47% for localization and 2-10% for classification in the low-data regime, while matching their performance in high-data regime. On the popular BCS-DBT benchmark, M&M-3D outperforms previous top baseline by 4% for classification and 10% for localization.

