---
layout: default
title: Morphology-Aware Prognostic model for Five-Year Survival Prediction in Colorectal Cancer from H&E Whole Slide Images
---

# Morphology-Aware Prognostic model for Five-Year Survival Prediction in Colorectal Cancer from H&E Whole Slide Images
**arXiv**：[2510.14800v1](https://arxiv.org/abs/2510.14800) · [PDF](https://arxiv.org/pdf/2510.14800.pdf)  
**作者**：Usama Sajjad, Abdul Rehman Akbar, Ziyu Su, Deborah Knight, Wendy L. Frankel, Metin N. Gurcan, Wei Chen, Muhammad Khalid Khan Niazi  

**一句话要点**：提出PRISM模型以预测结直肠癌五年生存率，整合形态学连续变异性

**关键词**：结直肠癌预后预测, 形态学整合模型, 全切片图像分析, 生存分析, AI可解释性

## 3 点简述
- 核心问题：现有基础模型忽视器官特异性形态模式，影响结直肠癌预后预测准确性。
- 方法要点：开发PRISM模型，通过连续变异性谱表征形态多样性，模拟渐进演化过程。
- 实验或效果：在424患者数据上训练，AUC达0.70，准确率68.37%，优于现有方法。

## 摘要（原文）

> Colorectal cancer (CRC) remains the third most prevalent malignancy globally,
> with approximately 154,000 new cases and 54,000 projected deaths anticipated
> for 2025. The recent advancement of foundation models in computational
> pathology has been largely propelled by task agnostic methodologies that can
> overlook organ-specific crucial morphological patterns that represent distinct
> biological processes that can fundamentally influence tumor behavior,
> therapeutic response, and patient outcomes. The aim of this study is to develop
> a novel, interpretable AI model, PRISM (Prognostic Representation of Integrated
> Spatial Morphology), that incorporates a continuous variability spectrum within
> each distinct morphology to characterize phenotypic diversity and reflecting
> the principle that malignant transformation occurs through incremental
> evolutionary processes rather than abrupt phenotypic shifts. PRISM is trained
> on 8.74 million histological images extracted from surgical resection specimens
> of 424 patients with stage III CRC. PRISM achieved superior prognostic
> performance for five-year OS (AUC = 0.70 +- 0.04; accuracy = 68.37% +- 4.75%;
> HR = 3.34, 95% CI = 2.28-4.90; p < 0.0001), outperforming existing CRC-specific
> methods by 15% and AI foundation models by ~23% accuracy. It showed
> sex-agnostic robustness (AUC delta = 0.02; accuracy delta = 0.15%) and stable
> performance across clinicopathological subgroups, with minimal accuracy
> fluctuation (delta = 1.44%) between 5FU/LV and CPT-11/5FU/LV regimens,
> replicating the Alliance cohort finding of no survival difference between
> treatments.

