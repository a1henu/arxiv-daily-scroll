---
layout: default
title: TeCoNeRV: Leveraging Temporal Coherence for Compressible Neural Representations for Videos
---

# TeCoNeRV: Leveraging Temporal Coherence for Compressible Neural Representations for Videos
**arXiv**：[2602.16711v1](https://arxiv.org/abs/2602.16711) · [PDF](https://arxiv.org/pdf/2602.16711.pdf)  
**作者**：Namitha Padmanabhan, Matthew Gwilliam, Abhinav Shrivastava  

**一句话要点**：提出TeCoNeRV方法，利用时间相干性提升视频压缩中神经表示的效率与质量。

**关键词**：视频压缩, 隐式神经表示, 时间相干性, 超网络, 残差编码, 高分辨率视频

## 3 点简述
- 核心问题：基于超网络的隐式神经表示在视频压缩中面临内存开销大、压缩质量低和编码速度慢的挑战。
- 方法要点：通过时空分解、残差存储和时间相干性正则化，减少内存使用并提升压缩性能。
- 实验或效果：在UVG等数据集上实现PSNR显著提升、比特率降低和编码加速，支持高分辨率视频。

## 摘要（原文）

> Implicit Neural Representations (INRs) have recently demonstrated impressive performance for video compression. However, since a separate INR must be overfit for each video, scaling to high-resolution videos while maintaining encoding efficiency remains a significant challenge. Hypernetwork-based approaches predict INR weights (hyponetworks) for unseen videos at high speeds, but with low quality, large compressed size, and prohibitive memory needs at higher resolutions. We address these fundamental limitations through three key contributions: (1) an approach that decomposes the weight prediction task spatially and temporally, by breaking short video segments into patch tubelets, to reduce the pretraining memory overhead by 20$\times$; (2) a residual-based storage scheme that captures only differences between consecutive segment representations, significantly reducing bitstream size; and (3) a temporal coherence regularization framework that encourages changes in the weight space to be correlated with video content. Our proposed method, TeCoNeRV, achieves substantial improvements of 2.47dB and 5.35dB PSNR over the baseline at 480p and 720p on UVG, with 36% lower bitrates and 1.5-3$\times$ faster encoding speeds. With our low memory usage, we are the first hypernetwork approach to demonstrate results at 480p, 720p and 1080p on UVG, HEVC and MCL-JCV. Our project page is available at https://namithap10.github.io/teconerv/ .

