---
layout: default
title: 3D Reconstruction from Transient Measurements with Time-Resolved Transformer
---

# 3D Reconstruction from Transient Measurements with Time-Resolved Transformer
**arXiv**：[2510.09205v1](https://arxiv.org/abs/2510.09205) · [PDF](https://arxiv.org/pdf/2510.09205.pdf)  
**作者**：Yue Li, Shida Sun, Yu Hong, Feihu Xu, Zhiwei Xiong  
**一句话要点**：提出时间分辨Transformer以提升光子高效成像中的3D重建性能
**关键词**：3D重建, 瞬态测量, 时间分辨Transformer, 非视距成像, 光子高效成像

## 3 点简述
- 核心问题：光子高效成像中传感器量子效率低、噪声高，导致3D重建困难。
- 方法要点：设计时空自注意力和交叉注意力，提取局部与全局特征，增强表示能力。
- 实验或效果：在合成和真实数据上显著优于现有方法，贡献新数据集和代码。

## 摘要（原文）

> Transient measurements, captured by the timeresolved systems, are widely
> employed in photon-efficient reconstruction tasks, including line-of-sight
> (LOS) and non-line-of-sight (NLOS) imaging. However, challenges persist in
> their 3D reconstruction due to the low quantum efficiency of sensors and the
> high noise levels, particularly for long-range or complex scenes. To boost the
> 3D reconstruction performance in photon-efficient imaging, we propose a generic
> Time-Resolved Transformer (TRT) architecture. Different from existing
> transformers designed for high-dimensional data, TRT has two elaborate
> attention designs tailored for the spatio-temporal transient measurements.
> Specifically, the spatio-temporal self-attention encoders explore both local
> and global correlations within transient data by splitting or downsampling
> input features into different scales. Then, the spatio-temporal cross attention
> decoders integrate the local and global features in the token space, resulting
> in deep features with high representation capabilities. Building on TRT, we
> develop two task-specific embodiments: TRT-LOS for LOS imaging and TRT-NLOS for
> NLOS imaging. Extensive experiments demonstrate that both embodiments
> significantly outperform existing methods on synthetic data and real-world data
> captured by different imaging systems. In addition, we contribute a
> large-scale, high-resolution synthetic LOS dataset with various noise levels
> and capture a set of real-world NLOS measurements using a custom-built imaging
> system, enhancing the data diversity in this field. Code and datasets are
> available at https://github.com/Depth2World/TRT.

