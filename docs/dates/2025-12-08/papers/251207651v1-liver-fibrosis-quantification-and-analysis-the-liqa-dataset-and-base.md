---
layout: default
title: Liver Fibrosis Quantification and Analysis: The LiQA Dataset and Baseline Method
---

# Liver Fibrosis Quantification and Analysis: The LiQA Dataset and Baseline Method
**arXiv**：[2512.07651v1](https://arxiv.org/abs/2512.07651) · [PDF](https://arxiv.org/pdf/2512.07651.pdf)  
**作者**：Yuanye Liu, Hanxiao Zhang, Nannan Shi, Yuxin Shi, Arif Mahmood, Murtaza Taj, Xiahai Zhuang  

**一句话要点**：提出LiQA数据集与基线方法，用于复杂临床条件下的肝纤维化量化分析

**关键词**：肝纤维化分期, 多模态MRI, 半监督学习, 多视图共识, 临床数据集

## 3 点简述
- 核心问题：肝纤维化准确分期对临床管理至关重要，需应对多中心、多模态MRI数据中的域偏移、缺失模态和空间错位等挑战。
- 方法要点：采用半监督学习框架结合外部数据进行稳健分割，并利用多视图共识与CAM正则化进行分期。
- 实验或效果：评估显示，利用多源数据和解剖约束显著提升了模型在临床环境中的鲁棒性。

## 摘要（原文）

> Liver fibrosis represents a significant global health burden, necessitating accurate staging for effective clinical management. This report introduces the LiQA (Liver Fibrosis Quantification and Analysis) dataset, established as part of the CARE 2024 challenge. Comprising $440$ patients with multi-phase, multi-center MRI scans, the dataset is curated to benchmark algorithms for Liver Segmentation (LiSeg) and Liver Fibrosis Staging (LiFS) under complex real-world conditions, including domain shifts, missing modalities, and spatial misalignment. We further describe the challenge's top-performing methodology, which integrates a semi-supervised learning framework with external data for robust segmentation, and utilizes a multi-view consensus approach with Class Activation Map (CAM)-based regularization for staging. Evaluation of this baseline demonstrates that leveraging multi-source data and anatomical constraints significantly enhances model robustness in clinical settings.

