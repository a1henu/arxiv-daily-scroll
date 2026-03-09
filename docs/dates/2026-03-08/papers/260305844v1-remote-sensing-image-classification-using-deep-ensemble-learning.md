---
layout: default
title: Remote Sensing Image Classification Using Deep Ensemble Learning
---

# Remote Sensing Image Classification Using Deep Ensemble Learning
**arXiv**：[2603.05844v1](https://arxiv.org/abs/2603.05844) · [PDF](https://arxiv.org/pdf/2603.05844.pdf)  
**作者**：Niful Islam, Md. Rayhan Ahmed, Nur Mohammad Fahad, Salekul Islam, A. K. M. Muzahidul Islam, Saddam Mukta, Swakkhar Shatabda  

**一句话要点**：提出融合CNN与ViT的集成模型以提升遥感图像分类精度

**关键词**：遥感图像分类, 深度集成学习, CNN-ViT融合, 特征冗余, 自注意力机制, 计算效率

## 3 点简述
- 核心问题：CNN擅长局部特征但全局信息不足，ViT补充长程依赖，但简单融合导致冗余特征瓶颈。
- 方法要点：训练四个独立融合模型，集成CNN与ViT骨干，在预测阶段组合输出以克服瓶颈。
- 实验或效果：在UC Merced、RSSCN7和MSRSI数据集上分别达到98.10%、94.46%和95.45%准确率，优于现有方法。

## 摘要（原文）

> Remote sensing imagery plays a crucial role in many applications and requires accurate computerized classification techniques. Reliable classification is essential for transforming raw imagery into structured and usable information. While Convolutional Neural Networks (CNNs) are mostly used for image classification, they excel at local feature extraction, but struggle to capture global contextual information. Vision Transformers (ViTs) address this limitation through self attention mechanisms that model long-range dependencies. Integrating CNNs and ViTs, therefore, leads to better performance than standalone architectures. However, the use of additional CNN and ViT components does not lead to further performance improvement and instead introduces a bottleneck caused by redundant feature representations. In this research, we propose a fusion model that combines the strengths of CNNs and ViTs for remote sensing image classification. To overcome the performance bottleneck, the proposed approach trains four independent fusion models that integrate CNN and ViT backbones and combine their outputs at the final prediction stage through ensembling. The proposed method achieves accuracy rates of 98.10 percent, 94.46 percent, and 95.45 percent on the UC Merced, RSSCN7, and MSRSI datasets, respectively. These results outperform competing architectures and highlight the effectiveness of the proposed solution, particularly due to its efficient use of computational resources during training.

