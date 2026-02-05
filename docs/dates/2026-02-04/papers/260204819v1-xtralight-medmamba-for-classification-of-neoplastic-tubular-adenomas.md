---
layout: default
title: XtraLight-MedMamba for Classification of Neoplastic Tubular Adenomas
---

# XtraLight-MedMamba for Classification of Neoplastic Tubular Adenomas
**arXiv**：[2602.04819v1](https://arxiv.org/abs/2602.04819) · [PDF](https://arxiv.org/pdf/2602.04819.pdf)  
**作者**：Aqsa Sultana, Rayan Afsar, Ahmed Rahu, Surendra P. Singh, Brian Shula, Brandon Combs, Derrick Forchetti, Vijayan K. Asari  

**一句话要点**：提出XtraLight-MedMamba以分类结直肠癌前病变管状腺瘤，实现高精度低参数模型。

**关键词**：结直肠癌前病变分类, 全切片图像分析, 状态空间模型, 轻量化深度学习, 注意力机制, 病理学人工智能

## 3 点简述
- 核心问题：结直肠癌前病变管状腺瘤的风险分层依赖主观病理评估，准确性受限。
- 方法要点：结合ConvNext浅层特征提取器与并行视觉Mamba，集成SCAB模块和FNO分类器，优化长短期依赖建模。
- 实验或效果：在约3.2万参数下，模型准确率达97.18%，F1分数0.9767，优于复杂架构。

## 摘要（原文）

> Accurate risk stratification of precancerous polyps during routine colonoscopy screenings is essential for lowering the risk of developing colorectal cancer (CRC). However, assessment of low-grade dysplasia remains limited by subjective histopathologic interpretation. Advancements in digital pathology and deep learning provide new opportunities to identify subtle and fine morphologic patterns associated with malignant progression that may be imperceptible to the human eye. In this work, we propose XtraLight-MedMamba, an ultra-lightweight state-space-based deep learning framework for classifying neoplastic tubular adenomas from whole-slide images (WSIs). The architecture is a blend of ConvNext based shallow feature extractor with parallel vision mamba to efficiently model both long- and short-range dependencies and image generalization. An integration of Spatial and Channel Attention Bridge (SCAB) module enhances multiscale feature extraction, while Fixed Non-Negative Orthogonal Classifier (FNOClassifier) enables substantial parameter reduction and improved generalization. The model was evaluated on a curated dataset acquired from patients with low-grade tubular adenomas, stratified into case and control cohorts based on subsequent CRC development. XtraLight-MedMamba achieved an accuracy of 97.18% and an F1-score of 0.9767 using approximately 32,000 parameters, outperforming transformer-based and conventional Mamba architectures with significantly higher model complexity.

