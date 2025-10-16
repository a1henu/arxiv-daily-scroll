---
layout: default
title: DP-TTA: Test-time Adaptation for Transient Electromagnetic Signal Denoising via Dictionary-driven Prior Regularization
---

# DP-TTA: Test-time Adaptation for Transient Electromagnetic Signal Denoising via Dictionary-driven Prior Regularization
**arXiv**：[2510.13160v1](https://arxiv.org/abs/2510.13160) · [PDF](https://arxiv.org/pdf/2510.13160.pdf)  
**作者**：Meng Yang, Kecheng Chen, Wei Luo, Xianjie Chen, Yong Jia, Mingyue Wang, Fanqiang Lin  

**一句话要点**：提出DP-TTA方法，通过字典驱动先验正则化提升瞬变电磁信号去噪的测试时适应性

**关键词**：瞬变电磁信号去噪, 测试时适应, 字典学习, 先验正则化, 自监督学习

## 3 点简述
- 核心问题：瞬变电磁信号在不同地理区域噪声特性差异大，导致预训练模型泛化性能下降
- 方法要点：利用信号固有物理特性构建字典先验，指导模型在测试时通过自监督损失动态调整参数
- 实验或效果：在多种场景下，该方法优于现有瞬变电磁去噪和测试时适应方法

## 摘要（原文）

> Transient Electromagnetic (TEM) method is widely used in various geophysical
> applications, providing valuable insights into subsurface properties. However,
> time-domain TEM signals are often submerged in various types of noise. While
> recent deep learning-based denoising models have shown strong performance,
> these models are mostly trained on simulated or single real-world scenario
> data, overlooking the significant differences in noise characteristics from
> different geographical regions. Intuitively, models trained in one environment
> often struggle to perform well in new settings due to differences in geological
> conditions, equipment, and external interference, leading to reduced denoising
> performance. To this end, we propose the Dictionary-driven Prior Regularization
> Test-time Adaptation (DP-TTA). Our key insight is that TEM signals possess
> intrinsic physical characteristics, such as exponential decay and smoothness,
> which remain consistent across different regions regardless of external
> conditions. These intrinsic characteristics serve as ideal prior knowledge for
> guiding the TTA strategy, which helps the pre-trained model dynamically adjust
> parameters by utilizing self-supervised losses, improving denoising performance
> in new scenarios. To implement this, we customized a network, named DTEMDNet.
> Specifically, we first use dictionary learning to encode these intrinsic
> characteristics as a dictionary-driven prior, which is integrated into the
> model during training. At the testing stage, this prior guides the model to
> adapt dynamically to new environments by minimizing self-supervised losses
> derived from the dictionary-driven consistency and the signal one-order
> variation. Extensive experimental results demonstrate that the proposed method
> achieves much better performance than existing TEM denoising methods and TTA
> methods.

