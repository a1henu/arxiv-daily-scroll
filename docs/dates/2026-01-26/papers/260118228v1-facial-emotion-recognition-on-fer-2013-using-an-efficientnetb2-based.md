---
layout: default
title: Facial Emotion Recognition on FER-2013 using an EfficientNetB2-Based Approach
---

# Facial Emotion Recognition on FER-2013 using an EfficientNetB2-Based Approach
**arXiv**：[2601.18228v1](https://arxiv.org/abs/2601.18228) · [PDF](https://arxiv.org/pdf/2601.18228.pdf)  
**作者**：Sahil Naik, Soham Bagayatkar, Pavankumar Singh  

**一句话要点**：提出基于EfficientNetB2的轻量级面部情绪识别方法，以解决FER-2013数据集中的噪声、类别不平衡和实时应用限制。

**关键词**：面部情绪识别, EfficientNetB2, 类别不平衡处理, 轻量级模型, 实时应用, FER-2013数据集

## 3 点简述
- 核心问题：FER-2013数据集存在图像质量低、光照变化、类别不平衡和噪声标签，导致面部情绪识别困难。
- 方法要点：使用EfficientNetB2轻量模型，结合两阶段训练、AdamW优化、标签平滑和剪裁类别权重，提升效率和鲁棒性。
- 实验或效果：在官方测试集上达到68.78%准确率，参数比VGG16基线少近十倍，适合实时和边缘应用。

## 摘要（原文）

> Detection of human emotions based on facial images in real-world scenarios is a difficult task due to low image quality, variations in lighting, pose changes, background distractions, small inter-class variations, noisy crowd-sourced labels, and severe class imbalance, as observed in the FER-2013 dataset of 48x48 grayscale images. Although recent approaches using large CNNs such as VGG and ResNet achieve reasonable accuracy, they are computationally expensive and memory-intensive, limiting their practicality for real-time applications. We address these challenges using a lightweight and efficient facial emotion recognition pipeline based on EfficientNetB2, trained using a two-stage warm-up and fine-tuning strategy. The model is enhanced with AdamW optimization, decoupled weight decay, label smoothing (epsilon = 0.06) to reduce annotation noise, and clipped class weights to mitigate class imbalance, along with dropout, mixed-precision training, and extensive real-time data augmentation. The model is trained using a stratified 87.5%/12.5% train-validation split while keeping the official test set intact, achieving a test accuracy of 68.78% with nearly ten times fewer parameters than VGG16-based baselines. Experimental results, including per-class metrics and learning dynamics, demonstrate stable training and strong generalization, making the proposed approach suitable for real-time and edge-based applications.

