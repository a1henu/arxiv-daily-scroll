---
layout: default
title: RefineFormer3D: Efficient 3D Medical Image Segmentation via Adaptive Multi-Scale Transformer with Cross Attention Fusion
---

# RefineFormer3D: Efficient 3D Medical Image Segmentation via Adaptive Multi-Scale Transformer with Cross Attention Fusion
**arXiv**：[2602.16320v1](https://arxiv.org/abs/2602.16320) · [PDF](https://arxiv.org/pdf/2602.16320.pdf)  
**作者**：Kavyansh Tyagi, Vishwas Rathi, Puneet Goyal  

**一句话要点**：提出RefineFormer3D，通过自适应多尺度Transformer与交叉注意力融合，实现高效3D医学图像分割。

**关键词**：3D医学图像分割, 轻量级Transformer, 交叉注意力融合, 参数高效, 临床部署, 多尺度特征

## 3 点简述
- 核心问题：Transformer模型在3D医学图像分割中参数多、内存需求大，限制临床部署。
- 方法要点：集成GhostConv3D嵌入、MixFFN3D模块和交叉注意力融合解码器，以轻量级架构平衡精度与效率。
- 实验或效果：在ACDC和BraTS基准上达到93.44%和85.9%平均Dice分数，参数仅2.94M，推理快且内存需求低。

## 摘要（原文）

> Accurate and computationally efficient 3D medical image segmentation remains a critical challenge in clinical workflows. Transformer-based architectures often demonstrate superior global contextual modeling but at the expense of excessive parameter counts and memory demands, restricting their clinical deployment. We propose RefineFormer3D, a lightweight hierarchical transformer architecture that balances segmentation accuracy and computational efficiency for volumetric medical imaging. The architecture integrates three key components: (i) GhostConv3D-based patch embedding for efficient feature extraction with minimal redundancy, (ii) MixFFN3D module with low-rank projections and depthwise convolutions for parameter-efficient feature extraction, and (iii) a cross-attention fusion decoder enabling adaptive multi-scale skip connection integration. RefineFormer3D contains only 2.94M parameters, substantially fewer than contemporary transformer-based methods. Extensive experiments on ACDC and BraTS benchmarks demonstrate that RefineFormer3D achieves 93.44\% and 85.9\% average Dice scores respectively, outperforming or matching state-of-the-art methods while requiring significantly fewer parameters. Furthermore, the model achieves fast inference (8.35 ms per volume on GPU) with low memory requirements, supporting deployment in resource-constrained clinical environments. These results establish RefineFormer3D as an effective and scalable solution for practical 3D medical image segmentation.

