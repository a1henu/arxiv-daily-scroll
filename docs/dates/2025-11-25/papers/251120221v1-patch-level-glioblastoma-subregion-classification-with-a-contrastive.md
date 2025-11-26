---
layout: default
title: Patch-Level Glioblastoma Subregion Classification with a Contrastive Learning-Based Encoder
---

# Patch-Level Glioblastoma Subregion Classification with a Contrastive Learning-Based Encoder
**arXiv**：[2511.20221v1](https://arxiv.org/abs/2511.20221) · [PDF](https://arxiv.org/pdf/2511.20221.pdf)  
**作者**：Juexin Zhang, Qifeng Zhong, Ying Weng, Ke Chen  

**一句话要点**：提出基于对比学习的ViT编码器，用于胶质母细胞瘤病理图像子区域分类

**关键词**：胶质母细胞瘤分类, 对比学习, Vision Transformer, 病理图像分析, BraTS挑战赛

## 3 点简述
- 胶质母细胞瘤分子和病理异质性高，诊断和患者分层困难
- 方法基于预训练ViT编码器微调，结合分类头进行图像分析
- 在BraTS-Path 2025挑战赛中，验证集MCC为0.7064，测试集MCC为0.6509

## 摘要（原文）

> The significant molecular and pathological heterogeneity of glioblastoma, an aggressive brain tumor, complicates diagnosis and patient stratification. While traditional histopathological assessment remains the standard, deep learning offers a promising path toward objective and automated analysis of whole slide images. For the BraTS-Path 2025 Challenge, we developed a method that fine-tunes a pre-trained Vision Transformer (ViT) encoder with a dedicated classification head on the official training dataset. Our model's performance on the online validation set, evaluated via the Synapse platform, yielded a Matthews Correlation Coefficient (MCC) of 0.7064 and an F1-score of 0.7676. On the final test set, the model achieved an MCC of 0.6509 and an F1-score of 0.5330, which secured our team second place in the BraTS-Pathology 2025 Challenge. Our results establish a solid baseline for ViT-based histopathological analysis, and future efforts will focus on bridging the performance gap observed on the unseen validation data.

