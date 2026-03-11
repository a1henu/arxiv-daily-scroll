---
layout: default
title: Transformer-Based Multi-Region Segmentation and Radiomic Analysis of HR-pQCT Imaging
---

# Transformer-Based Multi-Region Segmentation and Radiomic Analysis of HR-pQCT Imaging
**arXiv**：[2603.09137v1](https://arxiv.org/abs/2603.09137) · [PDF](https://arxiv.org/pdf/2603.09137.pdf)  
**作者**：Mohseu Rashid Subah, Mohammed Abdul Gani Zilani, Thomas L. Nickolas, Matthew R. Allen, Stuart J. Warden, Rachel K. Surowiec  

**一句话要点**：提出基于Transformer的多区域分割与影像组学分析框架，用于HR-pQCT成像的骨质疏松分类。

**关键词**：骨质疏松分类, HR-pQCT成像, Transformer分割, 多区域分析, 影像组学特征

## 3 点简述
- 骨质疏松诊断依赖DXA，但忽略骨微结构和软组织，HR-pQCT数据利用不足。
- 采用SegFormer模型自动分割胫骨、腓骨的皮质骨、松质骨及软组织，平均F1分数达95.36%。
- 从各区域提取影像组学特征，训练分类器，软组织特征在图像和患者层面均优于骨特征。

## 摘要（原文）

> Osteoporosis is a skeletal disease typically diagnosed using dual-energy X-ray absorptiometry (DXA), which quantifies areal bone mineral density but overlooks bone microarchitecture and surrounding soft tissues. High-resolution peripheral quantitative computed tomography (HR-pQCT) enables three-dimensional microstructural imaging with minimal radiation. However, current analysis pipelines largely focus on mineralized bone compartments, leaving much of the acquired image data underutilized. We introduce a fully automated framework for binary osteoporosis classification using radiomics features extracted from anatomically segmented HR-pQCT images. To our knowledge, this work is the first to leverage a transformer-based segmentation architecture, i.e., the SegFormer, for fully automated multi-region HR-pQCT analysis. The SegFormer model simultaneously delineated the cortical and trabecular bone of the tibia and fibula along with surrounding soft tissues and achieved a mean F1 score of 95.36%. Soft tissues were further subdivided into skin, myotendinous, and adipose regions through post-processing. From each region, 939 radiomic features were extracted and dimensionally reduced to train six machine learning classifiers on an independent dataset comprising 20,496 images from 122 HR-pQCT scans. The best image level performance was achieved using myotendinous tissue features, yielding an accuracy of 80.08% and an area under the receiver operating characteristic curve (AUROC) of 0.85, outperforming bone-based models. At the patient level, replacing standard biological, DXA, and HR-pQCT parameters with soft tissue radiomics improved AUROC from 0.792 to 0.875. These findings demonstrate that automated, multi-region HR-pQCT segmentation enables the extraction of clinically informative signals beyond bone alone, highlighting the importance of integrated tissue assessment for osteoporosis detection.

