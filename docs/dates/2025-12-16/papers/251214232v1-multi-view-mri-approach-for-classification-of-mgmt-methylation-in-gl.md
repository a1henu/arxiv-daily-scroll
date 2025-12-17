---
layout: default
title: Multi-View MRI Approach for Classification of MGMT Methylation in Glioblastoma Patients
---

# Multi-View MRI Approach for Classification of MGMT Methylation in Glioblastoma Patients
**arXiv**：[2512.14232v1](https://arxiv.org/abs/2512.14232) · [PDF](https://arxiv.org/pdf/2512.14232.pdf)  
**作者**：Rawan Alyahya, Asrar Alruwayqi, Atheer Alqarni, Asma Alkhaldi, Metab Alkubeyyer, Xin Gao, Mona Alshahrani  

**一句话要点**：提出多视图MRI方法，利用深度学习检测胶质母细胞瘤MGMT甲基化状态

**关键词**：胶质母细胞瘤, MGMT甲基化, 多视图MRI, 深度学习, 放射基因组学, 非侵入性诊断

## 3 点简述
- 核心问题：MGMT启动子甲基化影响化疗效果，当前依赖侵入性活检，需非侵入性检测方法。
- 方法要点：采用多视图MRI和深度学习，考虑视图间空间关系，避免复杂3D模型，引入新肿瘤切片提取技术。
- 实验或效果：通过对比先进模型验证方法有效性，分享可复现流程，提升诊断工具透明度与鲁棒性。

## 摘要（原文）

> The presence of MGMT promoter methylation significantly affects how well chemotherapy works for patients with Glioblastoma Multiforme (GBM). Currently, confirmation of MGMT promoter methylation relies on invasive brain tumor tissue biopsies. In this study, we explore radiogenomics techniques, a promising approach in precision medicine, to identify genetic markers from medical images. Using MRI scans and deep learning models, we propose a new multi-view approach that considers spatial relationships between MRI views to detect MGMT methylation status. Importantly, our method extracts information from all three views without using a complicated 3D deep learning model, avoiding issues associated with high parameter count, slow convergence, and substantial memory demands. We also introduce a new technique for tumor slice extraction and show its superiority over existing methods based on multiple evaluation metrics. By comparing our approach to state-of-the-art models, we demonstrate the efficacy of our method. Furthermore, we share a reproducible pipeline of published models, encouraging transparency and the development of robust diagnostic tools. Our study highlights the potential of non-invasive methods for identifying MGMT promoter methylation and contributes to advancing precision medicine in GBM treatment.

