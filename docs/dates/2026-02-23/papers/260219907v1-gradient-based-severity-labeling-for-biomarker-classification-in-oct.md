---
layout: default
title: Gradient based Severity Labeling for Biomarker Classification in OCT
---

# Gradient based Severity Labeling for Biomarker Classification in OCT
**arXiv**：[2602.19907v1](https://arxiv.org/abs/2602.19907) · [PDF](https://arxiv.org/pdf/2602.19907.pdf)  
**作者**：Kiran Kokilepersaud, Mohit Prabhushankar, Ghassan AlRegib, Stephanie Trejo Corona, Charles Wykoff  

**一句话要点**：提出基于梯度的疾病严重性标注方法，以改进OCT图像中生物标志物分类的对比学习。

**关键词**：医学图像分析, 对比学习, OCT扫描, 疾病严重性标注, 生物标志物分类, 梯度响应

## 3 点简述
- 核心问题：医学图像对比学习中，传统增强可能扭曲关键生物标志物区域，影响分类准确性。
- 方法要点：利用异常检测算法的梯度响应，为未标注OCT扫描生成疾病严重性标签，用于监督对比学习。
- 实验或效果：在糖尿病视网膜病变关键指标上，分类准确率比自监督基线提升高达6%。

## 摘要（原文）

> In this paper, we propose a novel selection strategy for contrastive learning for medical images. On natural images, contrastive learning uses augmentations to select positive and negative pairs for the contrastive loss. However, in the medical domain, arbitrary augmentations have the potential to distort small localized regions that contain the biomarkers we are interested in detecting. A more intuitive approach is to select samples with similar disease severity characteristics, since these samples are more likely to have similar structures related to the progression of a disease. To enable this, we introduce a method that generates disease severity labels for unlabeled OCT scans on the basis of gradient responses from an anomaly detection algorithm. These labels are used to train a supervised contrastive learning setup to improve biomarker classification accuracy by as much as 6% above self-supervised baselines for key indicators of Diabetic Retinopathy.

