---
layout: default
title: Scaling Artificial Intelligence for Multi-Tumor Early Detection with More Reports, Fewer Masks
---

# Scaling Artificial Intelligence for Multi-Tumor Early Detection with More Reports, Fewer Masks
**arXiv**：[2510.14803v1](https://arxiv.org/abs/2510.14803) · [PDF](https://arxiv.org/pdf/2510.14803.pdf)  
**作者**：Pedro R. A. S. Bassi, Xinze Zhou, Wenxuan Li, Szymon Płotka, Jieneng Chen, Qi Chen, Zheren Zhu, Jakub Prządo, Ibrahim E. Hamacı, Sezgin Er, Yuhan Wang, Ashwin Kumar, Bjoern Menze, Jarosław B. Ćwikła, Yuyin Zhou, Akshay S. Chaudhari, Curtis P. Langlotz, Sergio Decherchi, Andrea Cavalli, Kang Wang, Yang Yang, Alan L. Yuille, Zongwei Zhou  

**一句话要点**：提出R-Super方法，利用医学报告训练AI进行多肿瘤早期检测，减少对肿瘤掩码的依赖。

**关键词**：肿瘤分割, 医学报告利用, AI可扩展训练, 多肿瘤检测, CT扫描分析

## 3 点简述
- 核心问题：早期肿瘤检测依赖昂贵的手动肿瘤掩码，限制了AI模型的可扩展性。
- 方法要点：使用医学报告描述训练AI模型，实现肿瘤分割，无需大量掩码。
- 实验或效果：在101,654份报告上训练，性能媲美723掩码模型，结合掩码提升敏感性和特异性。

## 摘要（原文）

> Early tumor detection save lives. Each year, more than 300 million computed
> tomography (CT) scans are performed worldwide, offering a vast opportunity for
> effective cancer screening. However, detecting small or early-stage tumors on
> these CT scans remains challenging, even for experts. Artificial intelligence
> (AI) models can assist by highlighting suspicious regions, but training such
> models typically requires extensive tumor masks--detailed, voxel-wise outlines
> of tumors manually drawn by radiologists. Drawing these masks is costly,
> requiring years of effort and millions of dollars. In contrast, nearly every CT
> scan in clinical practice is already accompanied by medical reports describing
> the tumor's size, number, appearance, and sometimes, pathology
> results--information that is rich, abundant, and often underutilized for AI
> training. We introduce R-Super, which trains AI to segment tumors that match
> their descriptions in medical reports. This approach scales AI training with
> large collections of readily available medical reports, substantially reducing
> the need for manually drawn tumor masks. When trained on 101,654 reports, AI
> models achieved performance comparable to those trained on 723 masks. Combining
> reports and masks further improved sensitivity by +13% and specificity by +8%,
> surpassing radiologists in detecting five of the seven tumor types. Notably,
> R-Super enabled segmentation of tumors in the spleen, gallbladder, prostate,
> bladder, uterus, and esophagus, for which no public masks or AI models
> previously existed. This study challenges the long-held belief that
> large-scale, labor-intensive tumor mask creation is indispensable, establishing
> a scalable and accessible path toward early detection across diverse tumor
> types.
>   We plan to release our trained models, code, and dataset at
> https://github.com/MrGiovanni/R-Super

