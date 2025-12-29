---
layout: default
title: Balancing Accuracy and Efficiency: CNN Fusion Models for Diabetic Retinopathy Screening
---

# Balancing Accuracy and Efficiency: CNN Fusion Models for Diabetic Retinopathy Screening
**arXiv**：[2512.21861v1](https://arxiv.org/abs/2512.21861) · [PDF](https://arxiv.org/pdf/2512.21861.pdf)  
**作者**：Md Rafid Islam, Rafsan Jany, Akib Ahmed, Mohammad Ashrafuzzaman Khan  

**一句话要点**：提出CNN特征融合模型以提升糖尿病视网膜病变筛查的准确性与效率平衡。

**关键词**：糖尿病视网膜病变筛查, CNN特征融合, 二元分类, 眼底图像分析, 计算效率优化

## 3 点简述
- 核心问题：糖尿病视网膜病变筛查受限于专家资源不足和图像质量差异，需兼顾准确性与效率。
- 方法要点：通过特征级融合互补CNN骨干网络（如ResNet50、EfficientNet-B0、DenseNet121），构建二元分类模型。
- 实验或效果：在11,156张眼底图像上，EfficientNet-B0+DenseNet121融合模型表现最佳（准确率82.89%），平衡了计算成本与性能。

## 摘要（原文）

> Diabetic retinopathy (DR) remains a leading cause of preventable blindness, yet large-scale screening is constrained by limited specialist availability and variable image quality across devices and populations. This work investigates whether feature-level fusion of complementary convolutional neural network (CNN) backbones can deliver accurate and efficient binary DR screening on globally sourced fundus images. Using 11,156 images pooled from five public datasets (APTOS, EyePACS, IDRiD, Messidor, and ODIR), we frame DR detection as a binary classification task and compare three pretrained models (ResNet50, EfficientNet-B0, and DenseNet121) against pairwise and tri-fusion variants. Across five independent runs, fusion consistently outperforms single backbones. The EfficientNet-B0 + DenseNet121 (Eff+Den) fusion model achieves the best overall mean performance (accuracy: 82.89\%) with balanced class-wise F1-scores for normal (83.60\%) and diabetic (82.60\%) cases. While the tri-fusion is competitive, it incurs a substantially higher computational cost. Inference profiling highlights a practical trade-off: EfficientNet-B0 is the fastest (approximately 1.16 ms/image at batch size 1000), whereas the Eff+Den fusion offers a favorable accuracy--latency balance. These findings indicate that lightweight feature fusion can enhance generalization across heterogeneous datasets, supporting scalable binary DR screening workflows where both accuracy and throughput are critical.

