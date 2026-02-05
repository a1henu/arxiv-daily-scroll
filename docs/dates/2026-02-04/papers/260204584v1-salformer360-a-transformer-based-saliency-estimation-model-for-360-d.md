---
layout: default
title: SalFormer360: a transformer-based saliency estimation model for 360-degree videos
---

# SalFormer360: a transformer-based saliency estimation model for 360-degree videos
**arXiv**：[2602.04584v1](https://arxiv.org/abs/2602.04584) · [PDF](https://arxiv.org/pdf/2602.04584.pdf)  
**作者**：Mahmoud Z. A. Wahba, Francesco Barbato, Sara Baldoni, Federica Battisti  

**一句话要点**：提出SalFormer360，基于Transformer架构的360度视频显著性估计模型

**关键词**：360度视频, 显著性估计, Transformer架构, 视口预测, 沉浸式内容优化

## 3 点简述
- 核心问题：360度视频的显著性估计，用于视口预测和沉浸式内容优化。
- 方法要点：结合SegFormer编码器和自定义解码器，并引入视点中心偏置以提升准确性。
- 实验或效果：在三个基准数据集上优于现有方法，Pearson相关系数提升最高达18.6%。

## 摘要（原文）

> Saliency estimation has received growing attention in recent years due to its importance in a wide range of applications. In the context of 360-degree video, it has been particularly valuable for tasks such as viewport prediction and immersive content optimization. In this paper, we propose SalFormer360, a novel saliency estimation model for 360-degree videos built on a transformer-based architecture. Our approach is based on the combination of an existing encoder architecture, SegFormer, and a custom decoder. The SegFormer model was originally developed for 2D segmentation tasks, and it has been fine-tuned to adapt it to 360-degree content. To further enhance prediction accuracy in our model, we incorporated Viewing Center Bias to reflect user attention in 360-degree environments. Extensive experiments on the three largest benchmark datasets for saliency estimation demonstrate that SalFormer360 outperforms existing state-of-the-art methods. In terms of Pearson Correlation Coefficient, our model achieves 8.4% higher performance on Sport360, 2.5% on PVS-HM, and 18.6% on VR-EyeTracking compared to previous state-of-the-art.

