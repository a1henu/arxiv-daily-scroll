---
layout: default
title: Exponential capacity scaling of classical GANs compared to hybrid latent style-based quantum GANs
---

# Exponential capacity scaling of classical GANs compared to hybrid latent style-based quantum GANs
**arXiv**：[2601.05036v1](https://arxiv.org/abs/2601.05036) · [PDF](https://arxiv.org/pdf/2601.05036.pdf)  
**作者**：Milan Liepelt, Julien Baglio  

**一句话要点**：提出混合潜在风格量子生成对抗网络，在SAT4图像生成中实现指数级容量缩放优势

**关键词**：量子生成对抗网络, 混合潜在风格架构, 指数容量缩放, SAT4图像生成, 参数效率, 量子优势

## 3 点简述
- 核心问题：量子生成对抗网络在数据生成中的参数效率优势缺乏系统性研究
- 方法要点：结合经典变分自编码器编码输入数据，使用风格量子生成对抗网络进行生成
- 实验或效果：在SAT4图像生成中，经典判别器与生成器容量相对于量子生成器呈指数缩放

## 摘要（原文）

> Quantum generative modeling is a very active area of research in looking for practical advantage in data analysis. Quantum generative adversarial networks (QGANs) are leading candidates for quantum generative modeling and have been applied to diverse areas, from high-energy physics to image generation. The latent style-based QGAN, relying on a classical variational autoencoder to encode the input data into a latent space and then using a style-based QGAN for data generation has been proven to be efficient for image generation or drug design, hinting at the use of far less trainable parameters than their classical counterpart to achieve comparable performance, however this advantage has never been systematically studied. We present in this work the first comprehensive experimental analysis of this advantage of QGANS applied to SAT4 image generation, obtaining an exponential advantage in capacity scaling for a quantum generator in the hybrid latent style-based QGAN architecture. Careful tuning of the autoencoder is crucial to obtain stable, reliable results. Once this tuning is performed and defining training optimality as when the training is stable and the FID score is low and stable as well, the optimal capacity (or number of trainable parameters) of the classical discriminator scales exponentially with respect to the capacity of the quantum generator, and the same is true for the capacity of the classical generator. This hints toward a type of quantum advantage for quantum generative modeling.

