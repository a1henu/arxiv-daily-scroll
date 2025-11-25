---
layout: default
title: Zero-shot segmentation of skin tumors in whole-slide images with vision-language foundation models
---

# Zero-shot segmentation of skin tumors in whole-slide images with vision-language foundation models
**arXiv**：[2511.18978v1](https://arxiv.org/abs/2511.18978) · [PDF](https://arxiv.org/pdf/2511.18978.pdf)  
**作者**：Santiago Moreno, Pablo Meseguer, Rocío del Amor, Valery Naranjo  

**一句话要点**：提出ZEUS零样本视觉语言分割框架，用于全切片图像中的皮肤肿瘤分割。

**关键词**：零样本分割, 视觉语言模型, 全切片图像, 皮肤肿瘤, 文本提示集成, 组织病理学

## 3 点简述
- 皮肤肿瘤活检注释困难，因形态多变、良恶性区分细微。
- 方法使用文本提示集成和冻结VLM编码器，生成高分辨率分割掩码。
- 在内部数据集上表现竞争性，评估提示设计、领域偏移和机构变异性影响。

## 摘要（原文）

> Accurate annotation of cutaneous neoplasm biopsies represents a major challenge due to their wide morphological variability, overlapping histological patterns, and the subtle distinctions between benign and malignant lesions. Vision-language foundation models (VLMs), pre-trained on paired image-text corpora, learn joint representations that bridge visual features and diagnostic terminology, enabling zero-shot localization and classification of tissue regions without pixel-level labels. However, most existing VLM applications in histopathology remain limited to slide-level tasks or rely on coarse interactive prompts, and they struggle to produce fine-grained segmentations across gigapixel whole-slide images (WSIs). In this work, we introduce a zero-shot visual-language segmentation pipeline for whole-slide images (ZEUS), a fully automated, zero-shot segmentation framework that leverages class-specific textual prompt ensembles and frozen VLM encoders to generate high-resolution tumor masks in WSIs. By partitioning each WSI into overlapping patches, extracting visual embeddings, and computing cosine similarities against text prompts, we generate a final segmentation mask. We demonstrate competitive performance on two in-house datasets, primary spindle cell neoplasms and cutaneous metastases, highlighting the influence of prompt design, domain shifts, and institutional variability in VLMs for histopathology. ZEUS markedly reduces annotation burden while offering scalable, explainable tumor delineation for downstream diagnostic workflows.

