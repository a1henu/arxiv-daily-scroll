---
layout: default
title: Subtractive Modulative Network with Learnable Periodic Activations
---

# Subtractive Modulative Network with Learnable Periodic Activations
**arXiv**：[2602.16337v1](https://arxiv.org/abs/2602.16337) · [PDF](https://arxiv.org/pdf/2602.16337.pdf)  
**作者**：Tiou Wang, Zhuoqian Yang, Markus Flierl, Mathieu Salzmann, Sabine Süsstrunk  

**一句话要点**：提出Subtractive Modulative Network，基于减法合成原理构建参数高效的隐式神经表示架构。

**关键词**：隐式神经表示, 减法合成, 可学习激活, 参数效率, 图像重建, 新视角合成

## 3 点简述
- 核心问题：设计参数高效的隐式神经表示架构以提升信号重建精度。
- 方法要点：引入可学习周期性激活层生成多频基，结合调制掩模模块主动产生高阶谐波。
- 实验或效果：在图像数据集上PSNR达40+ dB，并在3D NeRF新视角合成任务中表现优异。

## 摘要（原文）

> We propose the Subtractive Modulative Network (SMN), a novel, parameter-efficient Implicit Neural Representation (INR) architecture inspired by classical subtractive synthesis. The SMN is designed as a principled signal processing pipeline, featuring a learnable periodic activation layer (Oscillator) that generates a multi-frequency basis, and a series of modulative mask modules (Filters) that actively generate high-order harmonics. We provide both theoretical analysis and empirical validation for our design. Our SMN achieves a PSNR of $40+$ dB on two image datasets, comparing favorably against state-of-the-art methods in terms of both reconstruction accuracy and parameter efficiency. Furthermore, consistent advantage is observed on the challenging 3D NeRF novel view synthesis task. Supplementary materials are available at https://inrainbws.github.io/smn/.

