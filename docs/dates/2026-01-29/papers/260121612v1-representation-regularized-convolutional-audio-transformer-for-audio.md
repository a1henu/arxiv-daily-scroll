---
layout: default
title: Representation-Regularized Convolutional Audio Transformer for Audio Understanding
---

# Representation-Regularized Convolutional Audio Transformer for Audio Understanding
**arXiv**：[2601.21612v1](https://arxiv.org/abs/2601.21612) · [PDF](https://arxiv.org/pdf/2601.21612.pdf)  
**作者**：Bing Han, Chushu Zhou, Yifan Yang, Wei Wang, Chenda Li, Wangyou Zhang, Yanmin Qian  

**一句话要点**：提出卷积音频变换器以解决音频理解中多粒度建模和训练效率低的问题。

**关键词**：音频理解, 自监督学习, 多粒度建模, 表示正则化, 卷积音频变换器, 训练效率

## 3 点简述
- 现有自监督学习方法在音频理解中通常仅处理单一粒度，难以捕捉复杂音频信号的多样结构。
- CAT框架引入多分辨率块以聚合不同粒度的信息，并采用表示正则化目标提升训练效率。
- 实验显示CAT在AudioSet 20k数据集上性能优异，收敛速度比现有方法快5倍。

## 摘要（原文）

> Bootstrap-based Self-Supervised Learning (SSL) has achieved remarkable progress in audio understanding. However, existing methods typically operate at a single level of granularity, limiting their ability to model the diverse temporal and spectral structures inherent in complex audio signals. Furthermore, bootstrapping representations from scratch is computationally expensive, often requiring extensive training to converge. In this work, we propose the Convolutional Audio Transformer (CAT), a unified framework designed to address these challenges. First, to capture hierarchical audio features, CAT incorporates a Multi-resolution Block that aggregates information across varying granularities. Second, to enhance training efficiency, we introduce a Representation Regularization objective. Drawing inspiration from generative modeling, this auxiliary task guides the student model by aligning its predictions with high-quality semantic representations from frozen, pre-trained external encoders. Experimental results demonstrate that CAT significantly outperforms baselines on audio understanding benchmarks. Notably, it achieves competitive performance on the AudioSet 20k dataset with 5 times faster convergence than existing methods. Codes and checkpoints will be released soon at https://github.com/realzhouchushu/CAT.

