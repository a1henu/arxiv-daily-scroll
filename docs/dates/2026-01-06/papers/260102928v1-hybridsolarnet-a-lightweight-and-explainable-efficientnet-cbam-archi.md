---
layout: default
title: HybridSolarNet: A Lightweight and Explainable EfficientNet-CBAM Architecture for Real-Time Solar Panel Fault Detection
---

# HybridSolarNet: A Lightweight and Explainable EfficientNet-CBAM Architecture for Real-Time Solar Panel Fault Detection
**arXiv**：[2601.02928v1](https://arxiv.org/abs/2601.02928) · [PDF](https://arxiv.org/pdf/2601.02928.pdf)  
**作者**：Md. Asif Hossain, G M Mota-Tahrin Tayef, Nabil Subhan  

**一句话要点**：提出HybridSolarNet，一种轻量可解释的EfficientNet-CBAM架构，用于实时太阳能电池板故障检测。

**关键词**：太阳能电池板故障检测, 轻量神经网络, 注意力机制, 边缘计算, 无人机监控, 可解释性分析

## 3 点简述
- 针对太阳能电池板人工检测成本高、易出错的问题，提出基于无人机监控的自动化解决方案。
- 结合EfficientNet-B0与CBAM，引入焦点损失和余弦退火，提升模型精度和鲁棒性。
- 在Kaggle数据集上实现92.37%平均准确率，存储仅16.3MB，推理速度54.9 FPS，适用于实时边缘计算。

## 摘要（原文）

> Manual inspections for solar panel systems are a tedious, costly, and error-prone task, making it desirable for Unmanned Aerial Vehicle (UAV) based monitoring. Though deep learning models have excellent fault detection capabilities, almost all methods either are too large and heavy for edge computing devices or involve biased estimation of accuracy due to ineffective learning techniques. We propose a new solar panel fault detection model called HybridSolarNet. It integrates EfficientNet-B0 with Convolutional Block Attention Module (CBAM). We implemented it on the Kaggle Solar Panel Images competition dataset with a tight split-before-augmentation protocol. It avoids leakage in accuracy estimation. We introduced focal loss and cosine annealing. Ablation analysis validates that accuracy boosts due to added benefits from CBAM (+1.53%) and that there are benefits from recognition of classes with imbalanced samples via focal loss. Overall average accuracy on 5-fold stratified cross-validation experiments on the given competition dataset topped 92.37% +/- 0.41 and an F1-score of 0.9226 +/- 0.39 compared to baselines like VGG19, requiring merely 16.3 MB storage, i.e., 32 times less. Its inference speed measured at 54.9 FPS with GPU support makes it a successful candidate for real-time UAV implementation. Moreover, visualization obtained from Grad-CAM illustrates that HybridSolarNet focuses on actual locations instead of irrelevant ones.

