---
layout: default
title: DCAU-Net: Differential Cross Attention and Channel-Spatial Feature Fusion for Medical Image Segmentation
---

# DCAU-Net: Differential Cross Attention and Channel-Spatial Feature Fusion for Medical Image Segmentation
**arXiv**：[2603.09530v1](https://arxiv.org/abs/2603.09530) · [PDF](https://arxiv.org/pdf/2603.09530.pdf)  
**作者**：Yanxin Li, Hui Wan, Libin Lan  

**一句话要点**：提出DCAU-Net，通过差分交叉注意力和通道-空间特征融合解决医学图像分割中的全局建模与细节整合问题。

**关键词**：医学图像分割, 差分交叉注意力, 通道-空间特征融合, Transformer优化, 特征融合策略, 计算复杂度降低

## 3 点简述
- 核心问题：Transformer自注意力计算复杂度高且易关注无关区域，传统融合策略无法自适应整合语义与空间细节。
- 方法要点：设计差分交叉注意力以突出判别结构并降低计算复杂度，引入通道-空间特征融合策略自适应校准特征。
- 实验或效果：在公开基准测试中实现竞争性性能，提升分割准确性和鲁棒性。

## 摘要（原文）

> Accurate medical image segmentation requires effective modeling of both long-range dependencies and fine-grained boundary details. While transformers mitigate the issue of insufficient semantic information arising from the limited receptive field inherent in convolutional neural networks, they introduce new challenges: standard self-attention incurs quadratic computational complexity and often assigns non-negligible attention weights to irrelevant regions, diluting focus on discriminative structures and ultimately compromising segmentation accuracy. Existing attention variants, although effective in reducing computational complexity, fail to suppress redundant computation and inadvertently impair global context modeling. Furthermore, conventional fusion strategies in encoder-decoder architectures, typically based on simple concatenation or summation, can not adaptively integrate high-level semantic information with low-level spatial details. To address these limitations, we propose DCAU-Net, a novel yet efficient segmentation framework with two key ideas. First, a new Differential Cross Attention (DCA) is designed to compute the difference between two independent softmax attention maps to adaptively highlight discriminative structures. By replacing pixel-wise key and value tokens with window-level summary tokens, DCA dramatically reduces computational complexity without sacrificing precision. Second, a Channel-Spatial Feature Fusion (CSFF) strategy is introduced to adaptively recalibrate features from skip connections and up-sampling paths through using sequential channel and spatial attention, effectively suppressing redundant information and amplifying salient cues. Experiments on two public benchmarks demonstrate that DCAU-Net achieves competitive performance with enhanced segmentation accuracy and robustness.

