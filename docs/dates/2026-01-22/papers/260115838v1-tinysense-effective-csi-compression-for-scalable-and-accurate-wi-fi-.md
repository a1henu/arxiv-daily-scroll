---
layout: default
title: TinySense: Effective CSI Compression for Scalable and Accurate Wi-Fi Sensing
---

# TinySense: Effective CSI Compression for Scalable and Accurate Wi-Fi Sensing
**arXiv**：[2601.15838v1](https://arxiv.org/abs/2601.15838) · [PDF](https://arxiv.org/pdf/2601.15838.pdf)  
**作者**：Toan Gian, Dung T. Tran, Viet Quoc Pham, Francesco Restuccia, Van-Dinh Nguyen  

**一句话要点**：提出TinySense压缩框架，基于VQGAN提升Wi-Fi人体姿态估计的可扩展性。

**关键词**：Wi-Fi感知, CSI压缩, VQGAN, 人体姿态估计, 可扩展性, Transformer

## 3 点简述
- 核心问题：现有Wi-Fi感知方法处理大量CSI数据，占用网络资源，影响可扩展性。
- 方法要点：采用VQGAN学习码本压缩CSI，结合K-means动态调整比特率，集成Transformer增强鲁棒性。
- 实验或效果：原型测试显示，在相同压缩率下，HPE准确率提升1.5倍，延迟和网络开销分别降低5倍和2.5倍。

## 摘要（原文）

> With the growing demand for device-free and privacy-preserving sensing solutions, Wi-Fi sensing has emerged as a promising approach for human pose estimation (HPE). However, existing methods often process vast amounts of channel state information (CSI) data directly, ultimately straining networking resources. This paper introduces TinySense, an efficient compression framework that enhances the scalability of Wi-Fi-based human sensing. Our approach is based on a new vector quantization-based generative adversarial network (VQGAN). Specifically, by leveraging a VQGAN-learned codebook, TinySense significantly reduces CSI data while maintaining the accuracy required for reliable HPE. To optimize compression, we employ the K-means algorithm to dynamically adjust compression bitrates to cluster a large-scale pre-trained codebook into smaller subsets. Furthermore, a Transformer model is incorporated to mitigate bitrate loss, enhancing robustness in unreliable networking conditions. We prototype TinySense on an experimental testbed using Jetson Nano and Raspberry Pi to measure latency and network resource use. Extensive results demonstrate that TinySense significantly outperforms state-of-the-art compression schemes, achieving up to 1.5x higher HPE accuracy score (PCK20) under the same compression rate. It also reduces latency and networking overhead, respectively, by up to 5x and 2.5x. The code repository is available online at here.

