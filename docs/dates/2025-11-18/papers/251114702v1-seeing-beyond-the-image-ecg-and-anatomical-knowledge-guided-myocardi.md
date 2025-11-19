---
layout: default
title: Seeing Beyond the Image: ECG and Anatomical Knowledge-Guided Myocardial Scar Segmentation from Late Gadolinium-Enhanced Images
---

# Seeing Beyond the Image: ECG and Anatomical Knowledge-Guided Myocardial Scar Segmentation from Late Gadolinium-Enhanced Images
**arXiv**：[2511.14702v1](https://arxiv.org/abs/2511.14702) · [PDF](https://arxiv.org/pdf/2511.14702.pdf)  
**作者**：Farheen Ramzan, Yusuf Kiberu, Nikesh Jathanna, Meryem Jabrane, Vicente Grau, Shahnaz Jamil-Copley, Richard H. Clayton, Chen, Chen  

**一句话要点**：提出多模态框架整合ECG与解剖先验，提升LGE-MRI心肌瘢痕分割精度

**关键词**：心肌瘢痕分割, 多模态融合, ECG引导, 解剖先验, 时间感知特征融合, LGE-MRI

## 3 点简述
- 核心问题：LGE-MRI心肌瘢痕分割因对比度变化和伪影而困难。
- 方法要点：融合ECG电生理信息和AHA-17解剖图谱，引入时间感知特征融合机制。
- 实验效果：在临床数据集上Dice分数从0.6149提升至0.8463，精度和灵敏度高。

## 摘要（原文）

> Accurate segmentation of myocardial scar from late gadolinium enhanced (LGE) cardiac MRI is essential for evaluating tissue viability, yet remains challenging due to variable contrast and imaging artifacts. Electrocardiogram (ECG) signals provide complementary physiological information, as conduction abnormalities can help localize or suggest scarred myocardial regions. In this work, we propose a novel multimodal framework that integrates ECG-derived electrophysiological information with anatomical priors from the AHA-17 atlas for physiologically consistent LGE-based scar segmentation. As ECGs and LGE-MRIs are not acquired simultaneously, we introduce a Temporal Aware Feature Fusion (TAFF) mechanism that dynamically weights and fuses features based on their acquisition time difference. Our method was evaluated on a clinical dataset and achieved substantial gains over the state-of-the-art image-only baseline (nnU-Net), increasing the average Dice score for scars from 0.6149 to 0.8463 and achieving high performance in both precision (0.9115) and sensitivity (0.9043). These results show that integrating physiological and anatomical knowledge allows the model to "see beyond the image", setting a new direction for robust and physiologically grounded cardiac scar segmentation.

