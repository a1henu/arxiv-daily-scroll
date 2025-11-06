---
layout: default
title: Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation
---

# Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation
**arXiv**：[2511.03163v1](https://arxiv.org/abs/2511.03163) · [PDF](https://arxiv.org/pdf/2511.03163.pdf)  
**作者**：Yun-Chen Lin, Jiayuan Huang, Hanyuan Zhang, Sergi Kavtaradze, Matthew J. Clarkson, Mobarak I. Hoque  

**一句话要点**：提出SRFT-GaLore方法以在深度引导下高效适应基础模型进行肝脏标志分割

**关键词**：肝脏标志分割, 基础模型适应, 低秩梯度投影, 深度引导融合, 腹腔镜手术, 跨数据集泛化

## 3 点简述
- 核心问题：医学影像中解剖结构分割在腹腔镜手术中因2D视频深度感知有限而困难
- 方法要点：使用SAM2和DA2编码器提取RGB与深度特征，SRFT-GaLore高效微调注意力层
- 实验或效果：在L3D数据集上Dice系数提升4.85%，平均对称表面距离降低11.78点

## 摘要（原文）

> Accurate detection and delineation of anatomical structures in medical
> imaging are critical for computer-assisted interventions, particularly in
> laparoscopic liver surgery where 2D video streams limit depth perception and
> complicate landmark localization. While recent works have leveraged monocular
> depth cues for enhanced landmark detection, challenges remain in fusing RGB and
> depth features and in efficiently adapting large-scale vision models to
> surgical domains. We propose a depth-guided liver landmark segmentation
> framework integrating semantic and geometric cues via vision foundation
> encoders. We employ Segment Anything Model V2 (SAM2) encoder to extract RGB
> features and Depth Anything V2 (DA2) encoder to extract depth-aware features.
> To efficiently adapt SAM2, we introduce SRFT-GaLore, a novel low-rank gradient
> projection method that replaces the computationally expensive SVD with a
> Subsampled Randomized Fourier Transform (SRFT). This enables efficient
> fine-tuning of high-dimensional attention layers without sacrificing
> representational power. A cross-attention fusion module further integrates RGB
> and depth cues. To assess cross-dataset generalization, we also construct a new
> Laparoscopic Liver Surgical Dataset (LLSD) as an external validation benchmark.
> On the public L3D dataset, our method achieves a 4.85% improvement in Dice
> Similarity Coefficient and a 11.78-point reduction in Average Symmetric Surface
> Distance compared to the D2GPLand. To further assess generalization capability,
> we evaluate our model on LLSD dataset. Our model maintains competitive
> performance and significantly outperforms SAM-based baselines, demonstrating
> strong cross-dataset robustness and adaptability to unseen surgical
> environments. These results demonstrate that our SRFT-GaLore-enhanced
> dual-encoder framework enables scalable and precise segmentation under
> real-time, depth-constrained surgical settings.

