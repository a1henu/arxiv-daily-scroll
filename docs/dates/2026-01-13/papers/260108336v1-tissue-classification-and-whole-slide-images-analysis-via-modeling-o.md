---
layout: default
title: Tissue Classification and Whole-Slide Images Analysis via Modeling of the Tumor Microenvironment and Biological Pathways
---

# Tissue Classification and Whole-Slide Images Analysis via Modeling of the Tumor Microenvironment and Biological Pathways
**arXiv**：[2601.08336v1](https://arxiv.org/abs/2601.08336) · [PDF](https://arxiv.org/pdf/2601.08336.pdf)  
**作者**：Junzhuo Liu, Xuemei Du, Daniel Reisenbuchler, Ye Chen, Markus Eckstein, Christian Matek, Friedrich Feuerhake, Dorit Merhof  

**一句话要点**：提出BioMorphNet以整合组织形态与空间基因表达，支持组织分类与差异基因分析。

**关键词**：全切片图像分析, 空间转录组学, 多模态网络, 肿瘤微环境建模, 生物路径分析, 组织分类

## 3 点简述
- 核心问题：现有方法忽视空间转录组学与补丁级应用，限制肿瘤微环境建模。
- 方法要点：构建图模型关联补丁，基于临床路径与可学习模块桥接形态与基因数据。
- 实验或效果：在三种癌症数据集上分类指标平均提升2.67%至6.29%，支持肿瘤定位与生物标志物发现。

## 摘要（原文）

> Automatic integration of whole slide images (WSIs) and gene expression profiles has demonstrated substantial potential in precision clinical diagnosis and cancer progression studies. However, most existing studies focus on individual gene sequences and slide level classification tasks, with limited attention to spatial transcriptomics and patch level applications. To address this limitation, we propose a multimodal network, BioMorphNet, which automatically integrates tissue morphological features and spatial gene expression to support tissue classification and differential gene analysis. For considering morphological features, BioMorphNet constructs a graph to model the relationships between target patches and their neighbors, and adjusts the response strength based on morphological and molecular level similarity, to better characterize the tumor microenvironment. In terms of multimodal interactions, BioMorphNet derives clinical pathway features from spatial transcriptomic data based on a predefined pathway database, serving as a bridge between tissue morphology and gene expression. In addition, a novel learnable pathway module is designed to automatically simulate the biological pathway formation process, providing a complementary representation to existing clinical pathways. Compared with the latest morphology gene multimodal methods, BioMorphNet's average classification metrics improve by 2.67%, 5.48%, and 6.29% for prostate cancer, colorectal cancer, and breast cancer datasets, respectively. BioMorphNet not only classifies tissue categories within WSIs accurately to support tumor localization, but also analyzes differential gene expression between tissue categories based on prediction confidence, contributing to the discovery of potential tumor biomarkers.

