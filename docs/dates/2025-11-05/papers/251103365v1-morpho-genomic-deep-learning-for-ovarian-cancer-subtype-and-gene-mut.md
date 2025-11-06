---
layout: default
title: Morpho-Genomic Deep Learning for Ovarian Cancer Subtype and Gene Mutation Prediction from Histopathology
---

# Morpho-Genomic Deep Learning for Ovarian Cancer Subtype and Gene Mutation Prediction from Histopathology
**arXiv**：[2511.03365v1](https://arxiv.org/abs/2511.03365) · [PDF](https://arxiv.org/pdf/2511.03365.pdf)  
**作者**：Gabriela Fernandes  

**一句话要点**：提出融合形态组学与深度学习的管道，从卵巢癌病理图像预测亚型和基因突变

**关键词**：卵巢癌亚型分类, 基因突变预测, 深度学习融合模型, 病理图像分析, 核形态测量

## 3 点简述
- 卵巢癌因晚期诊断和异质性高而致死率高，现有方法难以揭示关键基因组变异
- 开发ResNet-50与Vision Transformer融合模型，整合核形态测量和图像特征
- 在TCGA数据集上，亚型分类准确率84.2%，基因突变推断AUC达0.73-0.82

## 摘要（原文）

> Ovarian cancer remains one of the most lethal gynecological malignancies,
> largely due to late diagnosis and extensive heterogeneity across subtypes.
> Current diagnostic methods are limited in their ability to reveal underlying
> genomic variations essential for precision oncology. This study introduces a
> novel hybrid deep learning pipeline that integrates quantitative nuclear
> morphometry with deep convolutional image features to perform ovarian cancer
> subtype classification and gene mutation inference directly from Hematoxylin
> and Eosin (H&E) histopathological images. Using $\sim45,000$ image patches
> sourced from The Cancer Genome Atlas (TCGA) and public datasets, a fusion model
> combining a ResNet-50 Convolutional Neural Network (CNN) encoder and a Vision
> Transformer (ViT) was developed. This model successfully captured both local
> morphological texture and global tissue context. The pipeline achieved a robust
> overall subtype classification accuracy of $84.2\%$ (Macro AUC of $0.87 \pm
> 0.03$). Crucially, the model demonstrated the capacity for gene mutation
> inference with moderate-to-high accuracy: $AUC_{TP53} = 0.82 \pm 0.02$,
> $AUC_{BRCA1} = 0.76 \pm 0.04$, and $AUC_{ARID1A} = 0.73 \pm 0.05$. Feature
> importance analysis established direct quantitative links, revealing that
> nuclear solidity and eccentricity were the dominant predictors for TP53
> mutation. These findings validate that quantifiable histological phenotypes
> encode measurable genomic signals, paving the way for cost-effective, precision
> histopathology in ovarian cancer triage and diagnosis.

