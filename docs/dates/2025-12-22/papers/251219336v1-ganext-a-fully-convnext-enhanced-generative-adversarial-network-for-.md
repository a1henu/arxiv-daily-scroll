---
layout: default
title: GANeXt: A Fully ConvNeXt-Enhanced Generative Adversarial Network for MRI- and CBCT-to-CT Synthesis
---

# GANeXt: A Fully ConvNeXt-Enhanced Generative Adversarial Network for MRI- and CBCT-to-CT Synthesis
**arXiv**：[2512.19336v1](https://arxiv.org/abs/2512.19336) · [PDF](https://arxiv.org/pdf/2512.19336.pdf)  
**作者**：Siyuan Mei, Yan Xia, Fuxin Fan  

**一句话要点**：提出GANeXt，一种基于ConvNeXt的生成对抗网络，用于MRI和CBCT到CT的合成，以支持自适应放疗规划。

**关键词**：医学图像合成, 生成对抗网络, ConvNeXt, 自适应放疗, 3D图像处理

## 3 点简述
- 核心问题：从MRI和CBCT合成CT，以在自适应放疗中提供准确的解剖表示。
- 方法要点：使用3D ConvNeXt块构建U形生成器，结合多种损失函数和条件PatchGAN判别器。
- 实验或效果：通过联合训练，在3000和1000轮次后选择模型，采用滑动窗口和平均折叠进行推理。

## 摘要（原文）

> The synthesis of computed tomography (CT) from magnetic resonance imaging (MRI) and cone-beam CT (CBCT) plays a critical role in clinical treatment planning by enabling accurate anatomical representation in adaptive radiotherapy. In this work, we propose GANeXt, a 3D patch-based, fully ConvNeXt-powered generative adversarial network for unified CT synthesis across different modalities and anatomical regions. Specifically, GANeXt employs an efficient U-shaped generator constructed from stacked 3D ConvNeXt blocks with compact convolution kernels, while the discriminator adopts a conditional PatchGAN. To improve synthesis quality, we incorporate a combination of loss functions, including mean absolute error (MAE), perceptual loss, segmentation-based masked MAE, and adversarial loss and a combination of Dice loss and cross-entropy for multi-head segmentation discriminator. For both tasks, training is performed with a batch size of 8 using two separate AdamW optimizers for the generator and discriminator, each equipped with a warmup and cosine decay scheduler, with learning rates of $5\times10^{-4}$ and $1\times10^{-3}$, respectively. Data preprocessing includes deformable registration, foreground cropping, percentile normalization for the input modality, and linear normalization of the CT to the range $[-1024, 1000]$. Data augmentation involves random zooming within $(0.8, 1.3)$ (for MRI-to-CT only), fixed-size cropping to $32\times160\times192$ for MRI-to-CT and $32\times128\times128$ for CBCT-to-CT, and random flipping. During inference, we apply a sliding-window approach with $0.8$ overlap and average folding to reconstruct the full-size sCT, followed by inversion of the CT normalization. After joint training on all regions without any fine-tuning, the final models are selected at the end of 3000 epochs for MRI-to-CT and 1000 epochs for CBCT-to-CT using the full training dataset.

