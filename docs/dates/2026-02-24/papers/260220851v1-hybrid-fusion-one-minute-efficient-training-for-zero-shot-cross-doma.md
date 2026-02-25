---
layout: default
title: Hybrid Fusion: One-Minute Efficient Training for Zero-Shot Cross-Domain Image Fusion
---

# Hybrid Fusion: One-Minute Efficient Training for Zero-Shot Cross-Domain Image Fusion
**arXiv**：[2602.20851v1](https://arxiv.org/abs/2602.20851) · [PDF](https://arxiv.org/pdf/2602.20851.pdf)  
**作者**：Ran Zhang, Xuanhua He, Liu Liu  

**一句话要点**：提出混合融合框架，通过可学习U-Net引导固定拉普拉斯金字塔，实现一分钟高效训练与零样本跨域图像融合。

**关键词**：图像融合, 高效训练, 零样本学习, 拉普拉斯金字塔, 跨域泛化, 全分辨率训练

## 3 点简述
- 传统图像融合方法快速但适应性差，深度学习方法性能优但训练效率低，存在训练-推理差距。
- 方法核心为可学习U-Net生成动态引导图，指导固定拉普拉斯金字塔融合核，实现全分辨率高效训练。
- 实验显示，在RTX 4090上约一分钟达到SOTA可比性能，零样本泛化能力强，适用于红外-可见光到医学成像。

## 摘要（原文）

> Image fusion seeks to integrate complementary information from multiple sources into a single, superior image. While traditional methods are fast, they lack adaptability and performance. Conversely, deep learning approaches achieve state-of-the-art (SOTA) results but suffer from critical inefficiencies: their reliance on slow, resource-intensive, patch-based training introduces a significant gap with full-resolution inference. We propose a novel hybrid framework that resolves this trade-off. Our method utilizes a learnable U-Net to generate a dynamic guidance map that directs a classic, fixed Laplacian pyramid fusion kernel. This decoupling of policy learning from pixel synthesis enables remarkably efficient full-resolution training, eliminating the train-inference gap. Consequently, our model achieves SOTA-comparable performance in about one minute on a RTX 4090 or two minutes on a consumer laptop GPU from scratch without any external model and demonstrates powerful zero-shot generalization across diverse tasks, from infrared-visible to medical imaging. By design, the fused output is linearly constructed solely from source information, ensuring high faithfulness for critical applications. The codes are available at https://github.com/Zirconium233/HybridFusion

