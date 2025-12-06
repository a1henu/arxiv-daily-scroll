---
layout: default
title: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens
---

# Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens
**arXiv**：[2512.04857v1](https://arxiv.org/abs/2512.04857) · [PDF](https://arxiv.org/pdf/2512.04857.pdf)  
**作者**：Ziran Qin, Youru Lv, Mingbao Lin, Zeren Zhang, Chanfan Gan, Tieyuan Chen, Weiyao Lin  

**一句话要点**：提出LineAR以解决自回归图像生成中的内存瓶颈问题，通过训练无关的KV缓存压缩提升效率。

**关键词**：自回归图像生成, KV缓存压缩, 视觉注意力, 内存优化, 训练无关方法

## 3 点简述
- 自回归图像生成需缓存所有先前视觉令牌，导致高内存需求和低吞吐量。
- LineAR利用视觉注意力特性，在线级别管理缓存，逐步淘汰对后续生成无害的令牌。
- 实验在多个模型上验证，减少内存达67.61%，加速达7.57倍，同时提升生成质量。

## 摘要（原文）

> Autoregressive (AR) visual generation has emerged as a powerful paradigm for image and multimodal synthesis, owing to its scalability and generality. However, existing AR image generation suffers from severe memory bottlenecks due to the need to cache all previously generated visual tokens during decoding, leading to both high storage requirements and low throughput. In this paper, we introduce \textbf{LineAR}, a novel, training-free progressive key-value (KV) cache compression pipeline for autoregressive image generation. By fully exploiting the intrinsic characteristics of visual attention, LineAR manages the cache at the line level using a 2D view, preserving the visual dependency regions while progressively evicting less-informative tokens that are harmless for subsequent line generation, guided by inter-line attention. LineAR enables efficient autoregressive (AR) image generation by utilizing only a few lines of cache, achieving both memory savings and throughput speedup, while maintaining or even improving generation quality. Extensive experiments across six autoregressive image generation models, including class-conditional and text-to-image generation, validate its effectiveness and generality. LineAR improves ImageNet FID from 2.77 to 2.68 and COCO FID from 23.85 to 22.86 on LlamaGen-XL and Janus-Pro-1B, while retaining only 1/6 KV cache. It also improves DPG on Lumina-mGPT-768 with just 1/8 KV cache. Additionally, LineAR achieves significant memory and throughput gains, including up to 67.61% memory reduction and 7.57x speedup on LlamaGen-XL, and 39.66% memory reduction and 5.62x speedup on Janus-Pro-7B.

