---
layout: default
title: Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation
---

# Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation
**arXiv**：[2603.06374v1](https://arxiv.org/abs/2603.06374) · [PDF](https://arxiv.org/pdf/2603.06374.pdf)  
**作者**：Jonas Ernst, Wolfgang Boettcher, Lukas Hoyer, Jan Eric Lenssen, Bernt Schiele  

**一句话要点**：提出Rewis3d框架，利用3D重建改进2D图像的弱监督语义分割

**关键词**：弱监督语义分割, 3D重建, 师生架构, 稀疏标注, 几何监督

## 3 点简述
- 核心问题：密集像素级标注成本高，稀疏标注存在性能差距
- 方法要点：利用3D重建作为辅助监督信号，通过师生架构增强语义一致性
- 实验或效果：在稀疏监督下实现SOTA，性能提升2-7%，无需额外标注

## 摘要（原文）

> We present Rewis3d, a framework that leverages recent advances in feed-forward 3D reconstruction to significantly improve weakly supervised semantic segmentation on 2D images. Obtaining dense, pixel-level annotations remains a costly bottleneck for training segmentation models. Alleviating this issue, sparse annotations offer an efficient weakly-supervised alternative. However, they still incur a performance gap. To address this, we introduce a novel approach that leverages 3D scene reconstruction as an auxiliary supervisory signal. Our key insight is that 3D geometric structure recovered from 2D videos provides strong cues that can propagate sparse annotations across entire scenes. Specifically, a dual student-teacher architecture enforces semantic consistency between 2D images and reconstructed 3D point clouds, using state-of-the-art feed-forward reconstruction to generate reliable geometric supervision. Extensive experiments demonstrate that Rewis3d achieves state-of-the-art performance in sparse supervision, outperforming existing approaches by 2-7% without requiring additional labels or inference overhead.

