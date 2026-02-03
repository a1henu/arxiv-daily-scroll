---
layout: default
title: Toxicity Assessment in Preclinical Histopathology via Class-Aware Mahalanobis Distance for Known and Novel Anomalies
---

# Toxicity Assessment in Preclinical Histopathology via Class-Aware Mahalanobis Distance for Known and Novel Anomalies
**arXiv**：[2602.02124v1](https://arxiv.org/abs/2602.02124) · [PDF](https://arxiv.org/pdf/2602.02124.pdf)  
**作者**：Olga Graf, Dhrupal Patel, Peter Groß, Charlotte Lempp, Matthias Hein, Fabian Heinemann  

**一句话要点**：提出基于类感知马氏距离的AI框架，用于毒理学组织病理学中已知与未知异常的检测

**关键词**：组织病理学, 异常检测, Vision Transformer, 马氏距离, 毒理学, 全切片图像

## 3 点简述
- 核心问题：药物诱导毒性是临床前开发失败主因，组织病理学评估依赖专家，形成大规模筛查瓶颈。
- 方法要点：使用DINOv2预训练Vision Transformer，通过LoRA微调进行组织分割，并基于类感知马氏距离检测异常。
- 实验或效果：在鼠肝全切片图像上，仅0.16%病理组织误判为健康，0.35%健康组织误判为病理，能准确检测罕见异常。

## 摘要（原文）

> Drug-induced toxicity remains a leading cause of failure in preclinical development and early clinical trials. Detecting adverse effects at an early stage is critical to reduce attrition and accelerate the development of safe medicines. Histopathological evaluation remains the gold standard for toxicity assessment, but it relies heavily on expert pathologists, creating a bottleneck for large-scale screening. To address this challenge, we introduce an AI-based anomaly detection framework for histopathological whole-slide images (WSIs) in rodent livers from toxicology studies. The system identifies healthy tissue and known pathologies (anomalies) for which training data is available. In addition, it can detect rare pathologies without training data as out-of-distribution (OOD) findings. We generate a novel dataset of pixelwise annotations of healthy tissue and known pathologies and use this data to fine-tune a pre-trained Vision Transformer (DINOv2) via Low-Rank Adaptation (LoRA) in order to do tissue segmentation. Finally, we extract features for OOD detection using the Mahalanobis distance. To better account for class-dependent variability in histological data, we propose the use of class-specific thresholds. We optimize the thresholds using the mean of the false negative and false positive rates, resulting in only 0.16\% of pathological tissue classified as healthy and 0.35\% of healthy tissue classified as pathological. Applied to mouse liver WSIs with known toxicological findings, the framework accurately detects anomalies, including rare OOD morphologies. This work demonstrates the potential of AI-driven histopathology to support preclinical workflows, reduce late-stage failures, and improve efficiency in drug development.

