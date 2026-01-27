---
layout: default
title: Generative Diffusion Augmentation with Quantum-Enhanced Discrimination for Medical Image Diagnosis
---

# Generative Diffusion Augmentation with Quantum-Enhanced Discrimination for Medical Image Diagnosis
**arXiv**：[2601.18556v1](https://arxiv.org/abs/2601.18556) · [PDF](https://arxiv.org/pdf/2601.18556.pdf)  
**作者**：Jingsong Xia, Siqi Wang  

**一句话要点**：提出SDA-QEC框架，通过简化扩散增强与量子增强分类解决医学图像分类中的类别不平衡问题。

**关键词**：医学图像分类, 类别不平衡, 扩散增强, 量子增强, 冠状动脉造影, MobileNetV2

## 3 点简述
- 核心问题：医学图像数据集存在严重类别不平衡，导致模型偏向多数类，降低少数类召回率，增加临床误诊风险。
- 方法要点：结合轻量级扩散增强生成高质量少数类合成样本，并在MobileNetV2中嵌入量子特征层，通过希尔伯特空间高维映射提升判别能力。
- 实验或效果：在冠状动脉造影图像分类中，SDA-QEC达到98.33%准确率、98.78% AUC和98.33% F1分数，优于经典基线模型，实现高敏感性与特异性平衡。

## 摘要（原文）

> In biomedical engineering, artificial intelligence has become a pivotal tool for enhancing medical diagnostics, particularly in medical image classification tasks such as detecting pneumonia from chest X-rays and breast cancer screening. However, real-world medical datasets frequently exhibit severe class imbalance, where positive samples substantially outnumber negative samples, leading to biased models with low recall rates for minority classes. This imbalance not only compromises diagnostic accuracy but also poses clinical misdiagnosis risks. To address this challenge, we propose SDA-QEC (Simplified Diffusion Augmentation with Quantum-Enhanced Classification), an innovative framework that integrates simplified diffusion-based data augmentation with quantum-enhanced feature discrimination. Our approach employs a lightweight diffusion augmentor to generate high-quality synthetic samples for minority classes, rebalancing the training distribution. Subsequently, a quantum feature layer embedded within MobileNetV2 architecture enhances the model's discriminative capability through high-dimensional feature mapping in Hilbert space. Comprehensive experiments on coronary angiography image classification demonstrate that SDA-QEC achieves 98.33% accuracy, 98.78% AUC, and 98.33% F1-score, significantly outperforming classical baselines including ResNet18, MobileNetV2, DenseNet121, and VGG16. Notably, our framework simultaneously attains 98.33% sensitivity and 98.33% specificity, achieving a balanced performance critical for clinical deployment. The proposed method validates the feasibility of integrating generative augmentation with quantum-enhanced modeling in real-world medical imaging tasks, offering a novel research pathway for developing highly reliable medical AI systems in small-sample, highly imbalanced, and high-risk diagnostic scenarios.

