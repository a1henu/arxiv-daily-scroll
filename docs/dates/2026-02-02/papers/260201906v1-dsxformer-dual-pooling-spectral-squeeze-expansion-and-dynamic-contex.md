---
layout: default
title: DSXFormer: Dual-Pooling Spectral Squeeze-Expansion and Dynamic Context Attention Transformer for Hyperspectral Image Classification
---

# DSXFormer: Dual-Pooling Spectral Squeeze-Expansion and Dynamic Context Attention Transformer for Hyperspectral Image Classification
**arXiv**：[2602.01906v1](https://arxiv.org/abs/2602.01906) · [PDF](https://arxiv.org/pdf/2602.01906.pdf)  
**作者**：Farhan Ullah, Irfan Ullah, Khalil Khan, Giovanni Pau, JaKeoung Koo  

**一句话要点**：提出DSXFormer，通过双池化谱压缩扩展和动态上下文注意力解决高光谱图像分类中的谱判别性和计算效率问题。

**关键词**：高光谱图像分类, Transformer模型, 谱特征增强, 动态注意力机制, 计算效率优化

## 3 点简述
- 核心问题：高光谱图像分类面临高谱维、复杂谱空相关和有限标注样本的挑战。
- 方法要点：引入DSX块增强谱判别性，结合DCA机制动态捕获局部谱空关系以降低计算开销。
- 实验或效果：在四个基准数据集上优于现有方法，最高准确率达99.95%。

## 摘要（原文）

> Hyperspectral image classification (HSIC) is a challenging task due to high spectral dimensionality, complex spectral-spatial correlations, and limited labeled training samples. Although transformer-based models have shown strong potential for HSIC, existing approaches often struggle to achieve sufficient spectral discriminability while maintaining computational efficiency. To address these limitations, we propose a novel DSXFormer, a novel dual-pooling spectral squeeze-expansion transformer with Dynamic Context Attention for HSIC. The proposed DSXFormer introduces a Dual-Pooling Spectral Squeeze-Expansion (DSX) block, which exploits complementary global average and max pooling to adaptively recalibrate spectral feature channels, thereby enhancing spectral discriminability and inter-band dependency modeling. In addition, DSXFormer incorporates a Dynamic Context Attention (DCA) mechanism within a window-based transformer architecture to dynamically capture local spectral-spatial relationships while significantly reducing computational overhead. The joint integration of spectral dual-pooling squeeze-expansion and DCA enables DSXFormer to achieve an effective balance between spectral emphasis and spatial contextual representation. Furthermore, patch extraction, embedding, and patch merging strategies are employed to facilitate efficient multi-scale feature learning. Extensive experiments conducted on four widely used hyperspectral benchmark datasets, including Salinas (SA), Indian Pines (IP), Pavia University (PU), and Kennedy Space Center (KSC), demonstrate that DSXFormer consistently outperforms state-of-the-art methods, achieving classification accuracies of 99.95%, 98.91%, 99.85%, and 98.52%, respectively.

