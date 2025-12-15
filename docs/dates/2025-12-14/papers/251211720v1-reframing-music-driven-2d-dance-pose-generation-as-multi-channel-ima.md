---
layout: default
title: Reframing Music-Driven 2D Dance Pose Generation as Multi-Channel Image Generation
---

# Reframing Music-Driven 2D Dance Pose Generation as Multi-Channel Image Generation
**arXiv**：[2512.11720v1](https://arxiv.org/abs/2512.11720) · [PDF](https://arxiv.org/pdf/2512.11720.pdf)  
**作者**：Yan Zhang, Han Zou, Lincong Feng, Cong Xie, Ruiqi Yu, Zhenpeng Zhan  

**一句话要点**：提出基于多通道图像生成的音乐驱动2D舞蹈姿态生成方法，以解决复杂分布下的时序一致性和节奏对齐问题。

**关键词**：音乐驱动舞蹈生成, 多通道图像生成, 时序一致性, 姿态序列编码, 参考姿态条件, 野外数据集

## 3 点简述
- 核心问题：从音乐生成时序一致、节奏对齐的2D舞蹈姿态，尤其在复杂高方差分布下。
- 方法要点：将姿态序列编码为独热图像，使用预训练VAE压缩和DiT风格骨干建模，引入时间共享索引和参考姿态条件。
- 实验效果：在野外舞蹈数据集和AIST++2D基准上，姿态和视频指标及人类偏好优于现有方法。

## 摘要（原文）

> Recent pose-to-video models can translate 2D pose sequences into photorealistic, identity-preserving dance videos, so the key challenge is to generate temporally coherent, rhythm-aligned 2D poses from music, especially under complex, high-variance in-the-wild distributions. We address this by reframing music-to-dance generation as a music-token-conditioned multi-channel image synthesis problem: 2D pose sequences are encoded as one-hot images, compressed by a pretrained image VAE, and modeled with a DiT-style backbone, allowing us to inherit architectural and training advances from modern text-to-image models and better capture high-variance 2D pose distributions. On top of this formulation, we introduce (i) a time-shared temporal indexing scheme that explicitly synchronizes music tokens and pose latents over time and (ii) a reference-pose conditioning strategy that preserves subject-specific body proportions and on-screen scale while enabling long-horizon segment-and-stitch generation. Experiments on a large in-the-wild 2D dance corpus and the calibrated AIST++2D benchmark show consistent improvements over representative music-to-dance methods in pose- and video-space metrics and human preference, and ablations validate the contributions of the representation, temporal indexing, and reference conditioning. See supplementary videos at https://hot-dance.github.io

