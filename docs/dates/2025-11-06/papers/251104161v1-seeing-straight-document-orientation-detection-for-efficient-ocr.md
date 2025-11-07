---
layout: default
title: Seeing Straight: Document Orientation Detection for Efficient OCR
---

# Seeing Straight: Document Orientation Detection for Efficient OCR
**arXiv**：[2511.04161v1](https://arxiv.org/abs/2511.04161) · [PDF](https://arxiv.org/pdf/2511.04161.pdf)  
**作者**：Suranjan Goswami, Abhinav Ravi, Raja Kolla, Ali Faraz, Shaharukh Khan, Akash, Chandra Khatri, Shubham Agarwal  

**一句话要点**：提出基于Phi-3.5-Vision的文档方向检测方法以提升OCR效率

**关键词**：文档方向检测, OCR增强, 旋转分类, Phi-3.5-Vision, 多语言基准, 图像预处理

## 3 点简述
- 核心问题：文档扫描或拍摄时方向错误影响OCR性能，需准确旋转校正。
- 方法要点：使用Phi-3.5-Vision视觉编码器，结合动态裁剪，微调用于4类旋转分类。
- 实验或效果：在ORB基准上准确率达96%和92%，显著提升开源和闭源OCR模型性能。

## 摘要（原文）

> Despite significant advances in document understanding, determining the
> correct orientation of scanned or photographed documents remains a critical
> pre-processing step in the real world settings. Accurate rotation correction is
> essential for enhancing the performance of downstream tasks such as Optical
> Character Recognition (OCR) where misalignment commonly arises due to user
> errors, particularly incorrect base orientations of the camera during capture.
> In this study, we first introduce OCR-Rotation-Bench (ORB), a new benchmark for
> evaluating OCR robustness to image rotations, comprising (i) ORB-En, built from
> rotation-transformed structured and free-form English OCR datasets, and (ii)
> ORB-Indic, a novel multilingual set spanning 11 Indic mid to low-resource
> languages. We also present a fast, robust and lightweight rotation
> classification pipeline built on the vision encoder of Phi-3.5-Vision model
> with dynamic image cropping, fine-tuned specifically for 4-class rotation task
> in a standalone fashion. Our method achieves near-perfect 96% and 92% accuracy
> on identifying the rotations respectively on both the datasets. Beyond
> classification, we demonstrate the critical role of our module in boosting OCR
> performance: closed-source (up to 14%) and open-weights models (up to 4x) in
> the simulated real-world setting.

