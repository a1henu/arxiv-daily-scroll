---
layout: default
title: A Cautionary Tale of Self-Supervised Learning for Imaging Biomarkers: Alzheimer's Disease Case Study
---

# A Cautionary Tale of Self-Supervised Learning for Imaging Biomarkers: Alzheimer's Disease Case Study
**arXiv**：[2601.16467v1](https://arxiv.org/abs/2601.16467) · [PDF](https://arxiv.org/pdf/2601.16467.pdf)  
**作者**：Maxwell Reynolds, Chaitanya Srinivasan, Vijay Cherupally, Michael Leone, Ke Yu, Li Sun, Tigmanshu Chaudhary, Andreas Pfenning, Kayhan Batmanghelich  

**一句话要点**：提出R-NCE自监督学习框架，整合辅助特征以提升阿尔茨海默病成像生物标志物性能。

**关键词**：自监督学习, 阿尔茨海默病, 成像生物标志物, 脑年龄差, 基因组关联研究, 结构MRI

## 3 点简述
- 核心问题：自监督学习在阿尔茨海默病成像生物标志物发现中表现不佳，需改进。
- 方法要点：R-NCE结合FreeSurfer特征，最大化增强不变信息，优化生物标志物提取。
- 实验或效果：R-NCE在疾病分类和预测任务中优于传统特征和现有自监督方法。

## 摘要（原文）

> Discovery of sensitive and biologically grounded biomarkers is essential for early detection and monitoring of Alzheimer's disease (AD). Structural MRI is widely available but typically relies on hand-crafted features such as cortical thickness or volume. We ask whether self-supervised learning (SSL) can uncover more powerful biomarkers from the same data. Existing SSL methods underperform FreeSurfer-derived features in disease classification, conversion prediction, and amyloid status prediction. We introduce Residual Noise Contrastive Estimation (R-NCE), a new SSL framework that integrates auxiliary FreeSurfer features while maximizing additional augmentation-invariant information. R-NCE outperforms traditional features and existing SSL methods across multiple benchmarks, including AD conversion prediction. To assess biological relevance, we derive Brain Age Gap (BAG) measures and perform genome-wide association studies. R-NCE-BAG shows high heritability and associations with MAPT and IRAG1, with enrichment in astrocytes and oligodendrocytes, indicating sensitivity to neurodegenerative and cerebrovascular processes.

