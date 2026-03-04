---
layout: default
title: ATD: Improved Transformer with Adaptive Token Dictionary for Image Restoration
---

# ATD: Improved Transformer with Adaptive Token Dictionary for Image Restoration
**arXiv**：[2603.02581v1](https://arxiv.org/abs/2603.02581) · [PDF](https://arxiv.org/pdf/2603.02581.pdf)  
**作者**：Leheng Zhang, Wei Long, Yawei Li, Xingyu Zhou, Xiaorui Zhao, Shuhang Gu  

**一句话要点**：提出自适应令牌字典ATD，以线性复杂度实现全局依赖建模，用于图像恢复任务。

**关键词**：图像恢复, Transformer架构, 自适应令牌字典, 全局依赖建模, 线性复杂度, 多尺度处理

## 3 点简述
- 核心问题：Transformer在图像恢复中因自注意力二次复杂度，常限制于局部窗口，导致感受野有限和性能次优。
- 方法要点：引入可学习令牌字典总结图像先验，通过令牌字典交叉注意力TDCA增强特征，并利用类别信息分组特征以改进融合。
- 实验或效果：ATD及其变体在超分辨率等任务上达到SOTA，多尺度ATD-U扩展至去噪和JPEG伪影去除，实验验证优越性。

## 摘要（原文）

> Recently, Transformers have gained significant popularity in image restoration tasks such as image super-resolution and denoising, owing to their superior performance. However, balancing performance and computational burden remains a long-standing problem for transformer-based architectures. Due to the quadratic complexity of self-attention, existing methods often restrict attention to local windows, resulting in limited receptive field and suboptimal performance. To address this issue, we propose Adaptive Token Dictionary (ATD), a novel transformer-based architecture for image restoration that enables global dependency modeling with linear complexity relative to image size. The ATD model incorporates a learnable token dictionary, which summarizes external image priors (i.e., typical image structures) during the training process. To utilize this information, we introduce a token dictionary cross-attention (TDCA) mechanism that enhances the input features via interaction with the learned dictionary. Furthermore, we exploit the category information embedded in the TDCA attention maps to group input features into multiple categories, each representing a cluster of similar features across the image and serving as an attention group. We also integrate the learned category information into the feed-forward network to further improve feature fusion. ATD and its lightweight version ATD-light, achieve state-of-the-art performance on multiple image super-resolution benchmarks. Moreover, we develop ATD-U, a multi-scale variant of ATD, to address other image restoration tasks, including image denoising and JPEG compression artifacts removal. Extensive experiments demonstrate the superiority of out proposed models, both quantitatively and qualitatively.

