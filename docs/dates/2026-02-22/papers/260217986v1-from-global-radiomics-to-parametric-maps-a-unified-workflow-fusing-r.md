---
layout: default
title: From Global Radiomics to Parametric Maps: A Unified Workflow Fusing Radiomics and Deep Learning for PDAC Detection
---

# From Global Radiomics to Parametric Maps: A Unified Workflow Fusing Radiomics and Deep Learning for PDAC Detection
**arXiv**：[2602.17986v1](https://arxiv.org/abs/2602.17986) · [PDF](https://arxiv.org/pdf/2602.17986.pdf)  
**作者**：Zengtian Deng, Yimeng He, Yu Shi, Lixia Wang, Touseef Ahmad Qureshi, Xiuzhen Huang, Debiao Li  

**一句话要点**：提出融合全局与体素级放射组学的统一框架，用于胰腺导管腺癌检测。

**关键词**：放射组学, 深度学习, 胰腺导管腺癌检测, 参数图融合, nnUNet增强, 医学影像分析

## 3 点简述
- 现有方法多仅利用全局放射组学特征，忽略空间分辨的放射组学参数图的互补价值。
- 框架先选择判别性放射组学特征，再在全局和体素级别注入增强的nnUNet中。
- 在PANORAMA数据集上AUC达0.96，外部验证AUC达0.95，优于基线模型。

## 摘要（原文）

> Radiomics and deep learning both offer powerful tools for quantitative medical imaging, but most existing fusion approaches only leverage global radiomic features and overlook the complementary value of spatially resolved radiomic parametric maps. We propose a unified framework that first selects discriminative radiomic features and then injects them into a radiomics-enhanced nnUNet at both the global and voxel levels for pancreatic ductal adenocarcinoma (PDAC) detection. On the PANORAMA dataset, our method achieved AUC = 0.96 and AP = 0.84 in cross-validation. On an external in-house cohort, it achieved AUC = 0.95 and AP = 0.78, outperforming the baseline nnUNet; it also ranked second in the PANORAMA Grand Challenge. This demonstrates that handcrafted radiomics, when injected at both global and voxel levels, provide complementary signals to deep learning models for PDAC detection. Our code can be found at https://github.com/briandzt/dl-pdac-radiomics-global-n-paramaps

