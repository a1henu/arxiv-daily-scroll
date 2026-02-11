---
layout: default
title: Semi-supervised Liver Segmentation and Patch-based Fibrosis Staging with Registration-aided Multi-parametric MRI
---

# Semi-supervised Liver Segmentation and Patch-based Fibrosis Staging with Registration-aided Multi-parametric MRI
**arXiv**：[2602.09686v1](https://arxiv.org/abs/2602.09686) · [PDF](https://arxiv.org/pdf/2602.09686.pdf)  
**作者**：Boya Wang, Ruizhe Li, Chao Chen, Xin Chen  

**一句话要点**：提出半监督肝脏分割与基于patch的纤维化分期框架，以解决多参数MRI中标注有限和域偏移问题。

**关键词**：肝脏分割, 纤维化分期, 半监督学习, 多参数MRI, 域偏移处理, patch分类

## 3 点简述
- 核心问题：肝脏纤维化临床需求高，但多参数MRI数据标注少、模态差异大，导致分割和分期困难。
- 方法要点：采用半监督学习结合图像分割与配准，利用有标签和无标签数据处理域偏移；分期阶段使用基于patch的分类实现可视化。
- 实验或效果：在独立测试集上评估，涵盖ID和OOD病例，支持三通道和七通道MRI，代码已开源。

## 摘要（原文）

> Liver fibrosis poses a substantial challenge in clinical practice, emphasizing the necessity for precise liver segmentation and accurate disease staging. Based on the CARE Liver 2025 Track 4 Challenge, this study introduces a multi-task deep learning framework developed for liver segmentation (LiSeg) and liver fibrosis staging (LiFS) using multiparametric MRI. The LiSeg phase addresses the challenge of limited annotated images and the complexities of multi-parametric MRI data by employing a semi-supervised learning model that integrates image segmentation and registration. By leveraging both labeled and unlabeled data, the model overcomes the difficulties introduced by domain shifts and variations across modalities. In the LiFS phase, we employed a patchbased method which allows the visualization of liver fibrosis stages based on the classification outputs. Our approach effectively handles multimodality imaging data, limited labels, and domain shifts. The proposed method has been tested by the challenge organizer on an independent test set that includes in-distribution (ID) and out-of-distribution (OOD) cases using three-channel MRIs (T1, T2, DWI) and seven-channel MRIs (T1, T2, DWI, GED1-GED4). The code is freely available. Github link: https://github.com/mileywang3061/Care-Liver

