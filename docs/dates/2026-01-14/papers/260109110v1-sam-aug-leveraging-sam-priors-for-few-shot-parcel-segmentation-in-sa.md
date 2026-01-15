---
layout: default
title: SAM-Aug: Leveraging SAM Priors for Few-Shot Parcel Segmentation in Satellite Time Series
---

# SAM-Aug: Leveraging SAM Priors for Few-Shot Parcel Segmentation in Satellite Time Series
**arXiv**：[2601.09110v1](https://arxiv.org/abs/2601.09110) · [PDF](https://arxiv.org/pdf/2601.09110.pdf)  
**作者**：Kai Hu, Yaozu Feng, Vladimir Lysenko, Ya Guo Member, Huayi Wu  

**一句话要点**：提出SAM-Aug框架，利用SAM几何感知先验提升卫星时序图像少样本地块分割性能

**关键词**：少样本分割, 卫星时序图像, SAM先验, 无监督正则化, 土地覆盖制图

## 3 点简述
- 核心问题：卫星时序图像少样本语义分割在标注稀缺区域面临性能下降挑战
- 方法要点：构建无云合成图像，无监督应用SAM生成几何感知掩码先验，通过RegionSmoothLoss整合训练
- 实验或效果：在PASTIS-R基准上，5%标注设置下平均测试mIoU达36.21%，相对提升6.89%

## 摘要（原文）

> Few-shot semantic segmentation of time-series remote sensing images remains a critical challenge, particularly in regions where labeled data is scarce or costly to obtain. While state-of-the-art models perform well under full supervision, their performance degrades significantly under limited labeling, limiting their real-world applicability. In this work, we propose SAM-Aug, a new annotation-efficient framework that leverages the geometry-aware segmentation capability of the Segment Anything Model (SAM) to improve few-shot land cover mapping. Our approach constructs cloud-free composite images from temporal sequences and applies SAM in a fully unsupervised manner to generate geometry-aware mask priors. These priors are then integrated into training through a proposed loss function called RegionSmoothLoss, which enforces prediction consistency within each SAM-derived region across temporal frames, effectively regularizing the model to respect semantically coherent structures. Extensive experiments on the PASTIS-R benchmark under a 5 percent labeled setting demonstrate the effectiveness and robustness of SAM-Aug. Averaged over three random seeds (42, 2025, 4090), our method achieves a mean test mIoU of 36.21 percent, outperforming the state-of-the-art baseline by +2.33 percentage points, a relative improvement of 6.89 percent. Notably, on the most favorable split (seed=42), SAM-Aug reaches a test mIoU of 40.28 percent, representing an 11.2 percent relative gain with no additional labeled data. The consistent improvement across all seeds confirms the generalization power of leveraging foundation model priors under annotation scarcity. Our results highlight that vision models like SAM can serve as useful regularizers in few-shot remote sensing learning, offering a scalable and plug-and-play solution for land cover monitoring without requiring manual annotations or model fine-tuning.

