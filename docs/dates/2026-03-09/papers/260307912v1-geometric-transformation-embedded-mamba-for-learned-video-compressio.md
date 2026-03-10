---
layout: default
title: Geometric Transformation-Embedded Mamba for Learned Video Compression
---

# Geometric Transformation-Embedded Mamba for Learned Video Compression
**arXiv**：[2603.07912v1](https://arxiv.org/abs/2603.07912) · [PDF](https://arxiv.org/pdf/2603.07912.pdf)  
**作者**：Hao Wei, Yanhui Zhou, Chenyang Ge  

**一句话要点**：提出嵌入几何变换的Mamba框架，以简化视频压缩并提升低码率下的感知质量。

**关键词**：视频压缩, Mamba模型, 几何变换, 熵模型, 低码率优化

## 3 点简述
- 核心问题：传统学习视频压缩依赖显式运动估计，导致方案复杂。
- 方法要点：采用直接变换策略，结合级联Mamba模块和局部细化前馈网络。
- 实验或效果：在低码率下，优于现有方法，提升感知质量和时间一致性。

## 摘要（原文）

> Although learned video compression methods have exhibited outstanding performance, most of them typically follow a hybrid coding paradigm that requires explicit motion estimation and compensation, resulting in a complex solution for video compression. In contrast, we introduce a streamlined yet effective video compression framework founded on a direct transform strategy, i.e., nonlinear transform, quantization, and entropy coding. We first develop a cascaded Mamba module (CMM) with different embedded geometric transformations to effectively explore both long-range spatial and temporal dependencies. To improve local spatial representation, we introduce a locality refinement feed-forward network (LRFFN) that incorporates a hybrid convolution block based on difference convolutions. We integrate the proposed CMM and LRFFN into the encoder and decoder of our compression framework. Moreover, we present a conditional channel-wise entropy model that effectively utilizes conditional temporal priors to accurately estimate the probability distributions of current latent features. Extensive experiments demonstrate that our method outperforms state-of-the-art video compression approaches in terms of perceptual quality and temporal consistency under low-bitrate constraints. Our source codes and models will be available at https://github.com/cshw2021/GTEM-LVC.

