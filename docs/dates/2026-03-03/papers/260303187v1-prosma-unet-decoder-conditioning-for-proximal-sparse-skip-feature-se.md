---
layout: default
title: ProSMA-UNet: Decoder Conditioning for Proximal-Sparse Skip Feature Selection
---

# ProSMA-UNet: Decoder Conditioning for Proximal-Sparse Skip Feature Selection
**arXiv**：[2603.03187v1](https://arxiv.org/abs/2603.03187) · [PDF](https://arxiv.org/pdf/2603.03187.pdf)  
**作者**：Chun-Wun Cheng, Yanqi Cheng, Peiyuan Jing, Guang Yang, Carola-Bibiane Schönlieb, Angelica I. Aviles-Rivero  

**一句话要点**：提出ProSMA-UNet，通过解码器条件化稀疏特征选择解决医学图像分割中跳跃连接传播噪声的问题。

**关键词**：医学图像分割, U-Net架构, 稀疏特征选择, 解码器条件化, 多尺度注意力, 3D分割

## 3 点简述
- 核心问题：U-Net跳跃连接传播低层纹理和噪声，影响低对比度医学图像分割精度。
- 方法要点：使用多尺度兼容性场和ℓ1近端算子实现稀疏特征选择，结合解码器条件化通道门控。
- 实验或效果：在2D和3D基准测试中达到先进性能，3D分割任务提升约20%。

## 摘要（原文）

> Medical image segmentation commonly relies on U-shaped encoder-decoder architectures such as U-Net, where skip connections preserve fine spatial detail by injecting high-resolution encoder features into the decoder. However, these skip pathways also propagate low-level textures, background clutter, and acquisition noise, allowing irrelevant information to bypass deeper semantic filtering -- an issue that is particularly detrimental in low-contrast clinical imaging. Although attention gates have been introduced to address this limitation, they typically produce dense sigmoid masks that softly reweight features rather than explicitly removing irrelevant activations. We propose ProSMA-UNet (Proximal-Sparse Multi-Scale Attention U-Net), which reformulates skip gating as a decoder-conditioned sparse feature selection problem. ProSMA constructs a multi-scale compatibility field using lightweight depthwise dilated convolutions to capture relevance across local and contextual scales, then enforces explicit sparsity via an $\ell_1$ proximal operator with learnable per-channel thresholds, yielding a closed-form soft-thresholding gate that can remove noisy responses. To further suppress semantically irrelevant channels, ProSMA incorporates decoder-conditioned channel gating driven by global decoder context. Extensive experiments on challenging 2D and 3D benchmarks demonstrate state-of-the-art performance, with particularly large gains ($\approx20$\%) on difficult 3D segmentation tasks. Project page: https://math-ml-x.github.io/ProSMA-UNet/

