---
layout: default
title: Beer-Lambert Autoencoder for Unsupervised Stain Representation Learning and Deconvolution in Multi-immunohistochemical Brightfield Histology Images
---

# Beer-Lambert Autoencoder for Unsupervised Stain Representation Learning and Deconvolution in Multi-immunohistochemical Brightfield Histology Images
**arXiv**：[2601.11336v1](https://arxiv.org/abs/2601.11336) · [PDF](https://arxiv.org/pdf/2601.11336.pdf)  
**作者**：Mark Eastwood, Thomas McKee, Zedong Hu, Sabine Tejpar, Fayyaz Minhas  

**一句话要点**：提出Beer-Lambert自编码器，用于多免疫组化亮场组织学图像的无监督染色表示学习与解卷积。

**关键词**：染色解卷积, 无监督学习, 免疫组化图像, Beer-Lambert模型, 多染色分析

## 3 点简述
- 核心问题：多免疫组化（mIHC）中超过3种染色剂时，传统Beer-Lambert解卷积方法不稳定且欠定。
- 方法要点：采用紧凑U-Net编码器和可微分Beer-Lambert解码器，无监督学习染色矩阵和浓度图。
- 实验或效果：在含5种染色的结直肠mIHC数据集上，实现优异RGB重建并减少通道间渗漏。

## 摘要（原文）

> Separating the contributions of individual chromogenic stains in RGB histology whole slide images (WSIs) is essential for stain normalization, quantitative assessment of marker expression, and cell-level readouts in immunohistochemistry (IHC). Classical Beer-Lambert (BL) color deconvolution is well-established for two- or three-stain settings, but becomes under-determined and unstable for multiplex IHC (mIHC) with K>3 chromogens. We present a simple, data-driven encoder-decoder architecture that learns cohort-specific stain characteristics for mIHC RGB WSIs and yields crisp, well-separated per-stain concentration maps. The encoder is a compact U-Net that predicts K nonnegative concentration channels; the decoder is a differentiable BL forward model with a learnable stain matrix initialized from typical chromogen hues. Training is unsupervised with a perceptual reconstruction objective augmented by loss terms that discourage unnecessary stain mixing. On a colorectal mIHC panel comprising 5 stains (H, CDX2, MUC2, MUC5, CD8) we show excellent RGB reconstruction, and significantly reduced inter-channel bleed-through compared with matrix-based deconvolution. Code and model are available at https://github.com/measty/StainQuant.git.

