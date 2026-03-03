---
layout: default
title: Learning to Read Where to Look: Disease-Aware Vision-Language Pretraining for 3D CT
---

# Learning to Read Where to Look: Disease-Aware Vision-Language Pretraining for 3D CT
**arXiv**：[2603.02026v1](https://arxiv.org/abs/2603.02026) · [PDF](https://arxiv.org/pdf/2603.02026.pdf)  
**作者**：Simon Ging, Philipp Arnold, Sebastian Walter, Hani Alnahas, Hannah Bast, Elmar Kotter, Jiancheng Yang, Behzad Bozorgtabar, Thomas Brox  

**一句话要点**：提出疾病感知的3D CT视觉语言预训练模型，结合对比学习和疾病监督，提升检索、分类与扫描内定位性能。

**关键词**：3D CT视觉语言模型, 对比学习预训练, 疾病监督, 扫描内定位, 文本到图像检索, 医学影像分析

## 3 点简述
- 核心问题：现有3D CT视觉语言模型依赖有限公共数据，仅提供粗粒度全局监督，缺乏精确的文本-图像对齐。
- 方法要点：在98k报告-体积对上进行SigLIP风格对比预训练，结合疾病监督和自动挖掘的片段-切片对，引入扫描内片段定位任务。
- 实验或效果：在CT-RATE上实现文本到图像检索R@10 31.5，疾病分类AUC 83.8，扫描内定位误差降至36.3 mm，模型统一支持检索、分类和定位。

## 摘要（原文）

> Recent 3D CT vision-language models align volumes with reports via contrastive pretraining, but typically rely on limited public data and provide only coarse global supervision. We train a 3D CT vision-language model on 98k report-volume pairs (50k patients) collected at a single hospital, combined with public datasets, using SigLIP-style contrastive pretraining together with prompt-based disease supervision in the shared vision-text embedding space. On CT-RATE, our model achieves state-of-the-art text-to-image retrieval (R@10 31.5 vs. 22.2) and competitive disease classification (AUC 83.8 vs. 83.8), with consistent results on Rad-ChestCT (AUC 77.0 vs. 77.3). We further observe that radiologists routinely reference specific images within their reports (e.g., ``series X, image Y''), linking textual descriptions to precise axial locations. We automatically mine 262k such snippet-slice pairs and introduce the task of intra-scan snippet localization -- predicting the axial depth referred to by a text snippet -- reducing mean absolute error to 36.3 mm at 12 mm feature resolution, compared with 67.0 mm for the best baseline. Adding this localization objective leaves retrieval and classification broadly unchanged within confidence bounds, yielding a single unified model for retrieval, classification, and intra-scan grounding.

