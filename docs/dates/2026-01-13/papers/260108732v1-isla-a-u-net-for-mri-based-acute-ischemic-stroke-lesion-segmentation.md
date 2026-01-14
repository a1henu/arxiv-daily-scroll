---
layout: default
title: ISLA: A U-Net for MRI-based acute ischemic stroke lesion segmentation with deep supervision, attention, domain adaptation, and ensemble learning
---

# ISLA: A U-Net for MRI-based acute ischemic stroke lesion segmentation with deep supervision, attention, domain adaptation, and ensemble learning
**arXiv**：[2601.08732v1](https://arxiv.org/abs/2601.08732) · [PDF](https://arxiv.org/pdf/2601.08732.pdf)  
**作者**：Vincent Roca, Martin Bretzner, Hilde Henon, Laurent Puy, Grégory Kuchcinski, Renaud Lopes  

**一句话要点**：提出ISLA模型，用于MRI急性缺血性卒中病灶分割，结合深度监督、注意力机制和域适应提升性能。

**关键词**：急性缺血性卒中分割, U-Net架构, 深度监督, 注意力机制, 域适应, MRI影像分析

## 3 点简述
- 核心问题：急性缺血性卒中病灶在MRI中的准确分割对诊断至关重要，现有方法配置不明确且代码不公开。
- 方法要点：基于U-Net框架，系统优化损失函数、卷积架构、深度监督和注意力机制，并探索无监督域适应。
- 实验或效果：在超过1500名参与者的多中心数据上训练，外部测试集上优于两种先进方法，代码和模型将公开。

## 摘要（原文）

> Accurate delineation of acute ischemic stroke lesions in MRI is a key component of stroke diagnosis and management. In recent years, deep learning models have been successfully applied to the automatic segmentation of such lesions. While most proposed architectures are based on the U-Net framework, they primarily differ in their choice of loss functions and in the use of deep supervision, residual connections, and attention mechanisms. Moreover, many implementations are not publicly available, and the optimal configuration for acute ischemic stroke (AIS) lesion segmentation remains unclear. In this work, we introduce ISLA (Ischemic Stroke Lesion Analyzer), a new deep learning model for AIS lesion segmentation from diffusion MRI, trained on three multicenter databases totaling more than 1500 AIS participants. Through systematic optimization of the loss function, convolutional architecture, deep supervision, and attention mechanisms, we developed a robust segmentation framework. We further investigated unsupervised domain adaptation to improve generalization to an external clinical dataset. ISLA outperformed two state-of-the-art approaches for AIS lesion segmentation on an external test set. Codes and trained models will be made publicly available to facilitate reuse and reproducibility.

