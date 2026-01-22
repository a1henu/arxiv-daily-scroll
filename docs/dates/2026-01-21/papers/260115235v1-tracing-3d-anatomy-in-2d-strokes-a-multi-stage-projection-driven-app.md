---
layout: default
title: Tracing 3D Anatomy in 2D Strokes: A Multi-Stage Projection Driven Approach to Cervical Spine Fracture Identification
---

# Tracing 3D Anatomy in 2D Strokes: A Multi-Stage Projection Driven Approach to Cervical Spine Fracture Identification
**arXiv**：[2601.15235v1](https://arxiv.org/abs/2601.15235) · [PDF](https://arxiv.org/pdf/2601.15235.pdf)  
**作者**：Fabi Nahian Madhurja, Rusab Sarmun, Muhammad E. H. Chowdhury, Adam Mushtak, Israa Al-Hashimi, Sohaib Bassam Zoghoul  

**一句话要点**：提出基于2D投影的多阶段方法，用于3D CT中颈椎骨折的自动识别。

**关键词**：医学影像分析, 3D CT分割, 2D投影优化, 骨折检测, 深度学习模型, 可解释性研究

## 3 点简述
- 核心问题：颈椎骨折检测需高效精准，传统3D分割计算复杂。
- 方法要点：通过优化2D投影定位脊椎，结合YOLOv8和DenseNet121-Unet进行分割与骨折分析。
- 实验或效果：3D mIoU达94.45%，Dice分数87.86%，骨折检测F1分数68.15%（椎骨级）和82.26%（患者级）。

## 摘要（原文）

> Cervical spine fractures are critical medical conditions requiring precise and efficient detection for effective clinical management. This study explores the viability of 2D projection-based vertebra segmentation for vertebra-level fracture detection in 3D CT volumes, presenting an end-to-end pipeline for automated analysis of cervical vertebrae (C1-C7). By approximating a 3D volume through optimized 2D axial, sagittal, and coronal projections, regions of interest are identified using the YOLOv8 model from all views and combined to approximate the 3D cervical spine area, achieving a 3D mIoU of 94.45 percent. This projection-based localization strategy reduces computational complexity compared to traditional 3D segmentation methods while maintaining high performance. It is followed by a DenseNet121-Unet-based multi-label segmentation leveraging variance- and energy-based projections, achieving a Dice score of 87.86 percent. Strategic approximation of 3D vertebral masks from these 2D segmentation masks enables the extraction of individual vertebra volumes. The volumes are analyzed for fractures using an ensemble of 2.5D Spatio-Sequential models incorporating both raw slices and projections per vertebra for complementary evaluation. This ensemble achieves vertebra-level and patient-level F1 scores of 68.15 and 82.26, and ROC-AUC scores of 91.62 and 83.04, respectively. We further validate our approach through an explainability study that provides saliency map visualizations highlighting anatomical regions relevant for diagnosis, and an interobserver variability analysis comparing our model's performance with expert radiologists, demonstrating competitive results.

