---
layout: default
title: AutoLugano: A Deep Learning Framework for Fully Automated Lymphoma Segmentation and Lugano Staging on FDG-PET/CT
---

# AutoLugano: A Deep Learning Framework for Fully Automated Lymphoma Segmentation and Lugano Staging on FDG-PET/CT
**arXiv**：[2512.07206v1](https://arxiv.org/abs/2512.07206) · [PDF](https://arxiv.org/pdf/2512.07206.pdf)  
**作者**：Boyang Pan, Zeyu Zhang, Hongyu Meng, Bin Cui, Yingying Zhang, Wenli Hou, Junhao Li, Langdi Zhong, Xiaoxiao Chen, Xiaoyu Xu, Changjin Zuo, Chao Cheng, Nan-Jie Gong  

**一句话要点**：提出AutoLugano框架，通过FDG-PET/CT扫描实现淋巴瘤自动分割与卢加诺分期

**关键词**：淋巴瘤分割, 卢加诺分期, FDG-PET/CT, 深度学习, 自动诊断, nnU-Net

## 3 点简述
- 核心问题：淋巴瘤诊断需从FDG-PET/CT扫描中自动分割病灶、定位解剖区域并完成卢加诺分期。
- 方法要点：系统包含三个模块：基于3D nnU-Net的病灶分割、基于图谱的解剖定位和自动分期转换。
- 实验或效果：在外部验证集上，区域受累检测准确率88.31%，治疗分层准确率85.07%，表现稳健。

## 摘要（原文）

> Purpose: To develop a fully automated deep learning system, AutoLugano, for end-to-end lymphoma classification by performing lesion segmentation, anatomical localization, and automated Lugano staging from baseline FDG-PET/CT scans. Methods: The AutoLugano system processes baseline FDG-PET/CT scans through three sequential modules:(1) Anatomy-Informed Lesion Segmentation, a 3D nnU-Net model, trained on multi-channel inputs, performs automated lesion detection (2) Atlas-based Anatomical Localization, which leverages the TotalSegmentator toolkit to map segmented lesions to 21 predefined lymph node regions using deterministic anatomical rules; and (3) Automated Lugano Staging, where the spatial distribution of involved regions is translated into Lugano stages and therapeutic groups (Limited vs. Advanced Stage).The system was trained on the public autoPET dataset (n=1,007) and externally validated on an independent cohort of 67 patients. Performance was assessed using accuracy, sensitivity, specificity, F1-scorefor regional involvement detection and staging agreement. Results: On the external validation set, the proposed model demonstrated robust performance, achieving an overall accuracy of 88.31%, sensitivity of 74.47%, Specificity of 94.21% and an F1-score of 80.80% for regional involvement detection,outperforming baseline models. Most notably, for the critical clinical task of therapeutic stratification (Limited vs. Advanced Stage), the system achieved a high accuracy of 85.07%, with a specificity of 90.48% and a sensitivity of 82.61%.Conclusion: AutoLugano represents the first fully automated, end-to-end pipeline that translates a single baseline FDG-PET/CT scan into a complete Lugano stage. This study demonstrates its strong potential to assist in initial staging, treatment stratification, and supporting clinical decision-making.

