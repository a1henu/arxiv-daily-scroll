---
layout: default
title: DExTeR: Weakly Semi-Supervised Object Detection with Class and Instance Experts for Medical Imaging
---

# DExTeR: Weakly Semi-Supervised Object Detection with Class and Instance Experts for Medical Imaging
**arXiv**：[2601.13954v1](https://arxiv.org/abs/2601.13954) · [PDF](https://arxiv.org/pdf/2601.13954.pdf)  
**作者**：Adrien Meyer, Didier Mutter, Nicolas Padoy  

**一句话要点**：提出DExTeR，一种基于Transformer的点到框回归器，用于医学影像中的弱半监督目标检测。

**关键词**：弱半监督目标检测, 医学影像分析, Transformer模型, 点到框回归, 注意力机制, 混合专家

## 3 点简述
- 核心问题：医学影像中目标检测依赖昂贵边界框标注，且存在重叠解剖、尺寸多变等挑战，阻碍准确框推断。
- 方法要点：基于Point-DETR，引入类引导可变形注意力以捕获类特定特征，并采用CLICK-MoE解耦类和实例表示以减少混淆。
- 实验或效果：在三个医学数据集上实现最先进性能，显示能降低标注成本并保持高检测精度。

## 摘要（原文）

> Detecting anatomical landmarks in medical imaging is essential for diagnosis and intervention guidance. However, object detection models rely on costly bounding box annotations, limiting scalability. Weakly Semi-Supervised Object Detection (WSSOD) with point annotations proposes annotating each instance with a single point, minimizing annotation time while preserving localization signals. A Point-to-Box teacher model, trained on a small box-labeled subset, converts these point annotations into pseudo-box labels to train a student detector. Yet, medical imagery presents unique challenges, including overlapping anatomy, variable object sizes, and elusive structures, which hinder accurate bounding box inference. To overcome these challenges, we introduce DExTeR (DETR with Experts), a transformer-based Point-to-Box regressor tailored for medical imaging. Built upon Point-DETR, DExTeR encodes single-point annotations as object queries, refining feature extraction with the proposed class-guided deformable attention, which guides attention sampling using point coordinates and class labels to capture class-specific characteristics. To improve discrimination in complex structures, it introduces CLICK-MoE (CLass, Instance, and Common Knowledge Mixture of Experts), decoupling class and instance representations to reduce confusion among adjacent or overlapping instances. Finally, we implement a multi-point training strategy which promotes prediction consistency across different point placements, improving robustness to annotation variability. DExTeR achieves state-of-the-art performance across three datasets spanning different medical domains (endoscopy, chest X-rays, and endoscopic ultrasound) highlighting its potential to reduce annotation costs while maintaining high detection accuracy.

