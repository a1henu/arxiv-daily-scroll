---
layout: default
title: GDPR-Compliant Person Recognition in Industrial Environments Using MEMS-LiDAR and Hybrid Data
---

# GDPR-Compliant Person Recognition in Industrial Environments Using MEMS-LiDAR and Hybrid Data
**arXiv**：[2602.01764v1](https://arxiv.org/abs/2602.01764) · [PDF](https://arxiv.org/pdf/2602.01764.pdf)  
**作者**：Dennis Basile, Dennis Sprute, Helene Dörksen, Holger Flatt  

**一句话要点**：提出基于MEMS-LiDAR与混合数据的GDPR合规人员识别方法，用于工业环境

**关键词**：MEMS-LiDAR, GDPR合规, 人员识别, 混合数据, 工业安全, 合成数据增强

## 3 点简述
- 核心问题：工业室内安全需可靠检测未授权人员，传统视觉方法易受光照影响且违反隐私法规。
- 方法要点：使用MEMS-LiDAR捕获匿名3D点云，结合CARLA模拟生成合成数据增强训练集。
- 实验或效果：混合数据使平均精度提升44个百分点，手动标注工作量减少50%。

## 摘要（原文）

> The reliable detection of unauthorized individuals in safety-critical industrial indoor spaces is crucial to avoid plant shutdowns, property damage, and personal hazards. Conventional vision-based methods that use deep-learning approaches for person recognition provide image information but are sensitive to lighting and visibility conditions and often violate privacy regulations, such as the General Data Protection Regulation (GDPR) in the European Union. Typically, detection systems based on deep learning require annotated data for training. Collecting and annotating such data, however, is highly time-consuming and due to manual treatments not necessarily error free. Therefore, this paper presents a privacy-compliant approach based on Micro-Electro-Mechanical Systems LiDAR (MEMS-LiDAR), which exclusively captures anonymized 3D point clouds and avoids personal identification features. To compensate for the large amount of time required to record real LiDAR data and for post-processing and annotation, real recordings are augmented with synthetically generated scenes from the CARLA simulation framework. The results demonstrate that the hybrid data improves the average precision by 44 percentage points compared to a model trained exclusively with real data while reducing the manual annotation effort by 50 %. Thus, the proposed approach provides a scalable, cost-efficient alternative to purely real-data-based methods and systematically shows how synthetic LiDAR data can combine high performance in person detection with GDPR compliance in an industrial environment.

