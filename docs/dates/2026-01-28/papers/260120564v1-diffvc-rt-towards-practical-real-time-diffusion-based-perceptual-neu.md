---
layout: default
title: DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression
---

# DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression
**arXiv**：[2601.20564v1](https://arxiv.org/abs/2601.20564) · [PDF](https://arxiv.org/pdf/2601.20564.pdf)  
**作者**：Wenzhuo Ma, Zhenzhong Chen  

**一句话要点**：提出DiffVC-RT框架以实现实时扩散感知神经视频压缩，解决信息损失、延迟和时序一致性问题。

**关键词**：扩散模型, 神经视频压缩, 实时处理, 时序一致性, 高效架构, 异步解码

## 3 点简述
- 核心问题：扩散神经视频压缩面临信息损失严重、推理延迟高和时序一致性差，阻碍实际部署。
- 方法要点：采用高效信息模型架构减少计算复杂度，结合显隐时序一致性建模提升视频质量，并设计异步并行解码管道加速处理。
- 实验或效果：在HEVC数据集上，相比VTM-17.0节省80.1%比特率，720p视频在NVIDIA H800 GPU上实现206/30 fps实时编解码速度。

## 摘要（原文）

> The practical deployment of diffusion-based Neural Video Compression (NVC) faces critical challenges, including severe information loss, prohibitive inference latency, and poor temporal consistency. To bridge this gap, we propose DiffVC-RT, the first framework designed to achieve real-time diffusion-based perceptual NVC. First, we introduce an Efficient and Informative Model Architecture. Through strategic module replacements and pruning, this architecture significantly reduces computational complexity while mitigating structural information loss. Second, to address generative flickering artifacts, we propose Explicit and Implicit Consistency Modeling. We enhance temporal consistency by explicitly incorporating a zero-cost Online Temporal Shift Module within the U-Net, complemented by hybrid implicit consistency constraints. Finally, we present an Asynchronous and Parallel Decoding Pipeline incorporating Mixed Half Precision, which enables asynchronous latent decoding and parallel frame reconstruction via a Batch-dimension Temporal Shift design. Experiments show that DiffVC-RT achieves 80.1% bitrate savings in terms of LPIPS over VTM-17.0 on HEVC dataset with real-time encoding and decoding speeds of 206 / 30 fps for 720p videos on an NVIDIA H800 GPU, marking a significant milestone in diffusion-based video compression.

