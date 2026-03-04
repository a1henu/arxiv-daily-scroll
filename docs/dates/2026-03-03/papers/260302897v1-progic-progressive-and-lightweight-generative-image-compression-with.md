---
layout: default
title: ProGIC: Progressive and Lightweight Generative Image Compression with Residual Vector Quantization
---

# ProGIC: Progressive and Lightweight Generative Image Compression with Residual Vector Quantization
**arXiv**：[2603.02897v1](https://arxiv.org/abs/2603.02897) · [PDF](https://arxiv.org/pdf/2603.02897.pdf)  
**作者**：Hao Cao, Chengbin Liang, Wenqi Guo, Zhijin Qin, Jungong Han  

**一句话要点**：提出ProGIC，基于残差向量量化实现轻量级生成式图像压缩，支持渐进传输与高效部署。

**关键词**：生成式图像压缩, 残差向量量化, 渐进传输, 轻量模型, 低比特率压缩

## 3 点简述
- 问题：现有生成式图像压缩模型大而僵化，限制低比特率场景的灵活传输与部署。
- 方法：采用残差向量量化分阶段编码残差，结合深度可分离卷积和小注意力块的轻量骨干网络。
- 效果：在Kodak数据集上，相比MS-ILLM节省比特率超57%，编解码速度提升超10倍。

## 摘要（原文）

> Recent advances in generative image compression (GIC) have delivered remarkable improvements in perceptual quality. However, many GICs rely on large-scale and rigid models, which severely constrain their utility for flexible transmission and practical deployment in low-bitrate scenarios. To address these issues, we propose Progressive Generative Image Compression (ProGIC), a compact codec built on residual vector quantization (RVQ). In RVQ, a sequence of vector quantizers encodes the residuals stage by stage, each with its own codebook. The resulting codewords sum to a coarse-to-fine reconstruction and a progressive bitstream, enabling previews from partial data. We pair this with a lightweight backbone based on depthwise-separable convolutions and small attention blocks, enabling practical deployment on both GPUs and CPU-only devices. Experimental results show that ProGIC attains comparable compression performance compared with previous methods. It achieves bitrate savings of up to 57.57% on DISTS and 58.83% on LPIPS compared to MS-ILLM on the Kodak dataset. Beyond perceptual quality, ProGIC enables progressive transmission for flexibility, and also delivers over 10 times faster encoding and decoding compared with MS-ILLM on GPUs for efficiency.

