---
layout: default
title: Free-GVC: Towards Training-Free Extreme Generative Video Compression with Temporal Coherence
---

# Free-GVC: Towards Training-Free Extreme Generative Video Compression with Temporal Coherence
**arXiv**：[2602.09868v1](https://arxiv.org/abs/2602.09868) · [PDF](https://arxiv.org/pdf/2602.09868.pdf)  
**作者**：Xiaoyue Ling, Chuqin Zhou, Chunyi Li, Yunuo Chen, Yuan Tian, Guo Lu, Wenjun Zhang  

**一句话要点**：提出Free-GVC，一种免训练生成式视频压缩框架，以解决超低码率下时间一致性差的问题。

**关键词**：生成式视频压缩, 时间一致性, 扩散模型, 免训练框架, 超低码率编码

## 3 点简述
- 现有生成式视频压缩方法在超低码率下时间相关性利用不足，导致闪烁和时间一致性下降。
- Free-GVC将视频编码重构为基于视频扩散先验的潜在轨迹压缩，引入自适应质量控制和组间对齐模块。
- 实验显示，Free-GVC在DISTS指标上平均降低93.29% BD-Rate，用户研究证实其感知质量和时间一致性更优。

## 摘要（原文）

> Building on recent advances in video generation, generative video compression has emerged as a new paradigm for achieving visually pleasing reconstructions. However, existing methods exhibit limited exploitation of temporal correlations, causing noticeable flicker and degraded temporal coherence at ultra-low bitrates. In this paper, we propose Free-GVC, a training-free generative video compression framework that reformulates video coding as latent trajectory compression guided by a video diffusion prior. Our method operates at the group-of-pictures (GOP) level, encoding video segments into a compact latent space and progressively compressing them along the diffusion trajectory. To ensure perceptually consistent reconstruction across GOPs, we introduce an Adaptive Quality Control module that dynamically constructs an online rate-perception surrogate model to predict the optimal diffusion step for each GOP. In addition, an Inter-GOP Alignment module establishes frame overlap and performs latent fusion between adjacent groups, thereby mitigating flicker and enhancing temporal coherence. Experiments show that Free-GVC achieves an average of 93.29% BD-Rate reduction in DISTS over the latest neural codec DCVC-RT, and a user study further confirms its superior perceptual quality and temporal coherence at ultra-low bitrates.

