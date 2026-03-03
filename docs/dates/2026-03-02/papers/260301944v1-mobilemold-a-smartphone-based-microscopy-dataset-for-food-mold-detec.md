---
layout: default
title: MobileMold: A Smartphone-Based Microscopy Dataset for Food Mold Detection
---

# MobileMold: A Smartphone-Based Microscopy Dataset for Food Mold Detection
**arXiv**：[2603.01944v1](https://arxiv.org/abs/2603.01944) · [PDF](https://arxiv.org/pdf/2603.01944.pdf)  
**作者**：Dinh Nam Pham, Leonard Prokisch, Bennet Meyer, Jonas Thumbs  

**一句话要点**：提出MobileMold数据集以支持基于智能手机显微镜的食品霉菌检测与分类研究

**关键词**：智能手机显微镜, 食品霉菌检测, 多任务学习, 数据集构建, 模型可解释性

## 3 点简述
- 核心问题：智能手机显微镜图像中食品霉菌检测与分类，提升食品安全的可及性。
- 方法要点：构建包含4941张图像的数据集，涵盖多种食品、设备和条件，并建立多任务基线模型。
- 实验或效果：在预训练模型上实现高精度（准确率0.9954），并通过显著性图增强模型可解释性。

## 摘要（原文）

> Smartphone clip-on microscopes turn everyday devices into low-cost, portable imaging systems that can even reveal fungal structures at the microscopic level, enabling mold inspection beyond unaided visual checks. In this paper, we introduce MobileMold, an open smartphone-based microscopy dataset for food mold detection and food classification. MobileMold contains 4,941 handheld microscopy images spanning 11 food types, 4 smartphones, 3 microscopes, and diverse real-world conditions. Beyond the dataset release, we establish baselines for (i) mold detection and (ii) food-type classification, including a multi-task setting that predicts both attributes. Across multiple pretrained deep learning architectures and augmentation strategies, we obtain near-ceiling performance (accuracy = 0.9954, F1 = 0.9954, MCC = 0.9907), validating the utility of our dataset for detecting food spoilage. To increase transparency, we complement our evaluation with saliency-based visual explanations highlighting mold regions associated with the model's predictions. MobileMold aims to contribute to research on accessible food-safety sensing, mobile imaging, and exploring the potential of smartphones enhanced with attachments.

