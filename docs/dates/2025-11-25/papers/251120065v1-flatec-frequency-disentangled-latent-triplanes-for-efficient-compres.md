---
layout: default
title: FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds
---

# FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds
**arXiv**：[2511.20065v1](https://arxiv.org/abs/2511.20065) · [PDF](https://arxiv.org/pdf/2511.20065.pdf)  
**作者**：Xiaoge Zhang, Zijie Wu, Mingtao Feng, Zichen Geng, Mehwish Nasim, Saeed Anwar, Ajmal Mian  

**一句话要点**：提出FLaTEC以高效压缩LiDAR点云，通过频率解耦和潜在三平面表示。

**关键词**：点云压缩, 频率解耦, 潜在三平面, LiDAR数据, 率失真优化, 注意力机制

## 3 点简述
- 点云压缩中低频与高频组件对重建质量贡献不同，难以平衡压缩比与质量。
- 方法使用频率解耦机制分离低频结构和高频纹理，并采用潜在三平面减少稀疏性和成本。
- 在SemanticKITTI和Ford数据集上，BD-rate优于标准编解码器78%和94%。

## 摘要（原文）

> Point cloud compression methods jointly optimize bitrates and reconstruction distortion. However, balancing compression ratio and reconstruction quality is difficult because low-frequency and high-frequency components contribute differently at the same resolution. To address this, we propose FLaTEC, a frequency-aware compression model that enables the compression of a full scan with high compression ratios. Our approach introduces a frequency-aware mechanism that decouples low-frequency structures and high-frequency textures, while hybridizing latent triplanes as a compact proxy for point cloud. Specifically, we convert voxelized embeddings into triplane representations to reduce sparsity, computational cost, and storage requirements. We then devise a frequency-disentangling technique that extracts compact low-frequency content while collecting high-frequency details across scales. The decoupled low-frequency and high-frequency components are stored in binary format. During decoding, full-spectrum signals are progressively recovered via a modulation block. Additionally, to compensate for the loss of 3D correlation, we introduce an efficient frequency-based attention mechanism that fosters local connectivity and outputs arbitrary resolution points. Our method achieves state-of-the-art rate-distortion performance and outperforms the standard codecs by 78\% and 94\% in BD-rate on both SemanticKITTI and Ford datasets.

