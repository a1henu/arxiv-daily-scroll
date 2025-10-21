---
layout: default
title: MambaX-Net: Dual-Input Mamba-Enhanced Cross-Attention Network for Longitudinal MRI Segmentation
---

# MambaX-Net: Dual-Input Mamba-Enhanced Cross-Attention Network for Longitudinal MRI Segmentation
**arXiv**：[2510.17529v1](https://arxiv.org/abs/2510.17529) · [PDF](https://arxiv.org/pdf/2510.17529.pdf)  
**作者**：Yovin Yahathugoda, Davide Prezzi, Piyalitt Ittichaiwong, Vicky Goh, Sebastien Ourselin, Michela Antonelli  

**一句话要点**：提出MambaX-Net以解决纵向MRI前列腺分割中多时间点与标注稀缺问题

**关键词**：纵向MRI分割, Mamba增强交叉注意力, 半监督学习, 前列腺癌监测, 3D分割架构

## 3 点简述
- 核心问题：纵向主动监测中多时间点MRI分割因标注稀缺难以微调现有模型
- 方法要点：集成Mamba块与交叉注意力，利用前一时间点MRI和分割掩码
- 实验或效果：在纵向数据集上优于U-Net和Transformer模型，提升分割精度

## 摘要（原文）

> Active Surveillance (AS) is a treatment option for managing low and
> intermediate-risk prostate cancer (PCa), aiming to avoid overtreatment while
> monitoring disease progression through serial MRI and clinical follow-up.
> Accurate prostate segmentation is an important preliminary step for automating
> this process, enabling automated detection and diagnosis of PCa. However,
> existing deep-learning segmentation models are often trained on
> single-time-point and expertly annotated datasets, making them unsuitable for
> longitudinal AS analysis, where multiple time points and a scarcity of expert
> labels hinder their effective fine-tuning. To address these challenges, we
> propose MambaX-Net, a novel semi-supervised, dual-scan 3D segmentation
> architecture that computes the segmentation for time point t by leveraging the
> MRI and the corresponding segmentation mask from the previous time point. We
> introduce two new components: (i) a Mamba-enhanced Cross-Attention Module,
> which integrates the Mamba block into cross attention to efficiently capture
> temporal evolution and long-range spatial dependencies, and (ii) a Shape
> Extractor Module that encodes the previous segmentation mask into a latent
> anatomical representation for refined zone delination. Moreover, we introduce a
> semi-supervised self-training strategy that leverages pseudo-labels generated
> from a pre-trained nnU-Net, enabling effective learning without expert
> annotations. MambaX-Net was evaluated on a longitudinal AS dataset, and results
> showed that it significantly outperforms state-of-the-art U-Net and
> Transformer-based models, achieving superior prostate zone segmentation even
> when trained on limited and noisy data.

