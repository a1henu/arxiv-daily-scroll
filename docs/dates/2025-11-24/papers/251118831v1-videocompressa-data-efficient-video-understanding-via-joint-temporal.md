---
layout: default
title: VideoCompressa: Data-Efficient Video Understanding via Joint Temporal Compression and Spatial Reconstruction
---

# VideoCompressa: Data-Efficient Video Understanding via Joint Temporal Compression and Spatial Reconstruction
**arXiv**：[2511.18831v1](https://arxiv.org/abs/2511.18831) · [PDF](https://arxiv.org/pdf/2511.18831.pdf)  
**作者**：Shaobo Wang, Tianle Niu, Runkang Yang, Deshan Liu, Xu He, Zichen Wen, Conghui He, Xuming Hu, Linfeng Zhang  

**一句话要点**：提出VideoCompressa框架，通过联合时间压缩和空间重建解决视频数据效率问题

**关键词**：视频数据合成, 时间压缩, 空间重建, 数据效率, 关键帧选择, 变分自编码器

## 3 点简述
- 核心问题：视频数据效率低源于帧级冗余，而非样本间冗余
- 方法要点：联合优化可微分关键帧选择器和VAE，压缩帧为语义丰富潜码
- 实验效果：在UCF101上仅用0.13%数据超越全数据训练，速度提升5800倍

## 摘要（原文）

> The scalability of video understanding models is increasingly limited by the prohibitive storage and computational costs of large-scale video datasets. While data synthesis has improved data efficiency in the image domain, its extension to video remains challenging due to pervasive temporal redundancy and complex spatiotemporal dynamics. In this work, we uncover a critical insight: the primary source of inefficiency in video datasets is not inter-sample redundancy, but intra-sample frame-level redundancy. To leverage this insight, we introduce VideoCompressa, a novel framework for video data synthesis that reframes the problem as dynamic latent compression. Specifically, VideoCompressa jointly optimizes a differentiable keyframe selector-implemented as a lightweight ConvNet with Gumbel-Softmax sampling-to identify the most informative frames, and a pretrained, frozen Variational Autoencoder (VAE) to compress these frames into compact, semantically rich latent codes. These latent representations are then fed into a compression network, enabling end-to-end backpropagation. Crucially, the keyframe selector and synthetic latent codes are co-optimized to maximize retention of task-relevant information. Experiments show that our method achieves unprecedented data efficiency: on UCF101 with ConvNets, VideoCompressa surpasses full-data training by 2.34\% points using only 0.13\% of the original data, with over 5800x speedup compared to traditional synthesis method. Moreover, when fine-tuning Qwen2.5-7B-VL on HMDB51, VideoCompressa matches full-data performance using just 0.41\% of the training data-outperforming zero-shot baseline by 10.61\%.

