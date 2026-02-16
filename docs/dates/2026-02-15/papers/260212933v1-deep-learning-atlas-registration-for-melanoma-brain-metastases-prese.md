---
layout: default
title: Deep-Learning Atlas Registration for Melanoma Brain Metastases: Preserving Pathology While Enabling Cohort-Level Analyses
---

# Deep-Learning Atlas Registration for Melanoma Brain Metastases: Preserving Pathology While Enabling Cohort-Level Analyses
**arXiv**：[2602.12933v1](https://arxiv.org/abs/2602.12933) · [PDF](https://arxiv.org/pdf/2602.12933.pdf)  
**作者**：Nanna E. Wielenberg, Ilinca Popp, Oliver Blanck, Lucas Zander, Jan C. Peeken, Stephanie E. Combs, Anca-Ligia Grosu, Dimos Baltas, Tobias Fechter  

**一句话要点**：提出基于深度学习的可变形配准框架，用于黑色素瘤脑转移的图谱对齐，无需病灶掩码即可保留病理组织。

**关键词**：深度学习配准, 脑转移瘤分析, 图谱对齐, 可变形配准, 多中心研究, 病理组织保留

## 3 点简述
- 核心问题：黑色素瘤脑转移空间异质性和解剖变异性阻碍多中心队列分析。
- 方法要点：使用前向模型相似性度量和体积保持正则化，处理转移瘤导致的解剖对应缺失。
- 实验或效果：在209名患者数据上实现高配准精度，确认转移瘤偏好位于灰白质交界处和皮层区域。

## 摘要（原文）

> Melanoma brain metastases (MBM) are common and spatially heterogeneous lesions, complicating cohort-level analyses due to anatomical variability and differing MRI protocols. We propose a fully differentiable, deep-learning-based deformable registration framework that aligns individual pathological brains to a common atlas while preserving metastatic tissue without requiring lesion masks or preprocessing.
>   Missing anatomical correspondences caused by metastases are handled through a forward-model similarity metric based on distance-transformed anatomical labels, combined with a volume-preserving regularization term to ensure deformation plausibility. Registration performance was evaluated using Dice coefficient (DSC), Hausdorff distance (HD), average symmetric surface distance (ASSD), and Jacobian-based measures. The method was applied to 209 MBM patients from three centres, enabling standardized mapping of metastases to anatomical, arterial, and perfusion atlases.
>   The framework achieved high registration accuracy across datasets (DSC 0.89-0.92, HD 6.79-7.60 mm, ASSD 0.63-0.77 mm) while preserving metastatic volumes. Spatial analysis demonstrated significant over-representation of MBM in the cerebral cortex and putamen, under-representation in white matter, and consistent localization near the gray-white matter junction. No arterial territory showed increased metastasis frequency after volume correction.
>   This approach enables robust atlas registration of pathological brain MRI without lesion masks and supports reproducible multi-centre analyses. Applied to MBM, it confirms and refines known spatial predilections, particularly preferential seeding near the gray-white matter junction and cortical regions. The publicly available implementation facilitates reproducible research and extension to other brain tumours and neurological pathologies.

