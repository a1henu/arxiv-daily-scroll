---
layout: default
title: GriDiT: Factorized Grid-Based Diffusion for Efficient Long Image Sequence Generation
---

# GriDiT: Factorized Grid-Based Diffusion for Efficient Long Image Sequence Generation
**arXiv**：[2512.21276v1](https://arxiv.org/abs/2512.21276) · [PDF](https://arxiv.org/pdf/2512.21276.pdf)  
**作者**：Snehal Singh Tomar, Alexandros Graikos, Arjun Krishna, Dimitris Samaras, Klaus Mueller  

**一句话要点**：提出GriDiT方法，通过因子化网格扩散实现高效长图像序列生成。

**关键词**：图像序列生成, 扩散模型, 因子化生成, 长序列处理, 高效推理

## 3 点简述
- 核心问题：现有方法将图像序列视为大张量，导致生成效率低和瓶颈。
- 方法要点：先低分辨率生成粗序列，再独立高分辨率细化帧，利用扩散变换器捕获帧间相关性。
- 实验或效果：在质量和推理速度上优于现有方法，支持任意长度序列生成，泛化能力强。

## 摘要（原文）

> Modern deep learning methods typically treat image sequences as large tensors of sequentially stacked frames. However, is this straightforward representation ideal given the current state-of-the-art (SoTA)? In this work, we address this question in the context of generative models and aim to devise a more effective way of modeling image sequence data. Observing the inefficiencies and bottlenecks of current SoTA image sequence generation methods, we showcase that rather than working with large tensors, we can improve the generation process by factorizing it into first generating the coarse sequence at low resolution and then refining the individual frames at high resolution. We train a generative model solely on grid images comprising subsampled frames. Yet, we learn to generate image sequences, using the strong self-attention mechanism of the Diffusion Transformer (DiT) to capture correlations between frames. In effect, our formulation extends a 2D image generator to operate as a low-resolution 3D image-sequence generator without introducing any architectural modifications. Subsequently, we super-resolve each frame individually to add the sequence-independent high-resolution details. This approach offers several advantages and can overcome key limitations of the SoTA in this domain. Compared to existing image sequence generation models, our method achieves superior synthesis quality and improved coherence across sequences. It also delivers high-fidelity generation of arbitrary-length sequences and increased efficiency in inference time and training data usage. Furthermore, our straightforward formulation enables our method to generalize effectively across diverse data domains, which typically require additional priors and supervision to model in a generative context. Our method consistently outperforms SoTA in quality and inference speed (at least twice-as-fast) across datasets.

