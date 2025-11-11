---
layout: default
title: MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression
---

# MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression
**arXiv**：[2511.06717v1](https://arxiv.org/abs/2511.06717) · [PDF](https://arxiv.org/pdf/2511.06717.pdf)  
**作者**：Han Liu, Hengyu Man, Xingtao Wang, Wenrui Li, Debin Zhao  

**一句话要点**：提出MRT架构以解决极端图像压缩中空间冗余问题

**关键词**：极端图像压缩, 混合RWKV-Transformer, 1-D潜在表示, 注意力机制, 比特率优化

## 3 点简述
- 现有方法使用2-D潜在空间编码图像，存在空间冗余限制压缩性能
- 结合RWKV和Transformer，编码图像为1-D潜在表示，提升紧凑性
- 在低比特率下实现优越重建质量，比特率节省超30%

## 摘要（原文）

> Recent advances in extreme image compression have revealed that mapping pixel
> data into highly compact latent representations can significantly improve
> coding efficiency. However, most existing methods compress images into 2-D
> latent spaces via convolutional neural networks (CNNs) or Swin Transformers,
> which tend to retain substantial spatial redundancy, thereby limiting overall
> compression performance. In this paper, we propose a novel Mixed
> RWKV-Transformer (MRT) architecture that encodes images into more compact 1-D
> latent representations by synergistically integrating the complementary
> strengths of linear-attention-based RWKV and self-attention-based Transformer
> models. Specifically, MRT partitions each image into fixed-size windows,
> utilizing RWKV modules to capture global dependencies across windows and
> Transformer blocks to model local redundancies within each window. The
> hierarchical attention mechanism enables more efficient and compact
> representation learning in the 1-D domain. To further enhance compression
> efficiency, we introduce a dedicated RWKV Compression Model (RCM) tailored to
> the structure characteristics of the intermediate 1-D latent features in MRT.
> Extensive experiments on standard image compression benchmarks validate the
> effectiveness of our approach. The proposed MRT framework consistently achieves
> superior reconstruction quality at bitrates below 0.02 bits per pixel (bpp).
> Quantitative results based on the DISTS metric show that MRT significantly
> outperforms the state-of-the-art 2-D architecture GLC, achieving bitrate
> savings of 43.75%, 30.59% on the Kodak and CLIC2020 test datasets,
> respectively.

