---
layout: default
title: OVGGT: O(1) Constant-Cost Streaming Visual Geometry Transformer
---

# OVGGT: O(1) Constant-Cost Streaming Visual Geometry Transformer
**arXiv**：[2603.05959v1](https://arxiv.org/abs/2603.05959) · [PDF](https://arxiv.org/pdf/2603.05959.pdf)  
**作者**：Si-Yu Lu, Po-Ting Chen, Hui-Che Hsu, Sin-Ye Jhong, Wen-Huang Cheng, Yung-Yao Chen  

**一句话要点**：提出OVGGT框架，通过恒定内存与计算成本实现流式视频的3D几何重建。

**关键词**：流式视频处理, 3D几何重建, 恒定成本推理, KV缓存压缩, 视觉Transformer

## 3 点简述
- 核心问题：现有流式几何模型因KV缓存累积导致内存爆炸，无法处理长视频序列。
- 方法要点：结合自选择缓存与动态锚点保护，在训练无关下压缩KV缓存并抑制几何漂移。
- 实验或效果：在室内外及超长序列基准上，OVGGT在恒定VRAM内实现SOTA几何精度。

## 摘要（原文）

> Reconstructing 3D geometry from streaming video requires continuous inference under bounded resources. Recent geometric foundation models achieve impressive reconstruction quality through all-to-all attention, yet their quadratic cost confines them to short, offline sequences. Causal-attention variants such as StreamVGGT enable single-pass streaming but accumulate an ever-growing KV cache, exhausting GPU memory within hundreds of frames and precluding the long-horizon deployment that motivates streaming inference in the first place. We present OVGGT, a training-free framework that bounds both memory and compute to a fixed budget regardless of sequence length. Our approach combines Self-Selective Caching, which leverages FFN residual magnitudes to compress the KV cache while remaining fully compatible with FlashAttention, with Dynamic Anchor Protection, which shields coordinate-critical tokens from eviction to suppress geometric drift over extended trajectories. Extensive experiments on indoor, outdoor, and ultra-long sequence benchmarks demonstrate that OVGGT processes arbitrarily long videos within a constant VRAM envelope while achieving state-of-the-art 3D geometric accuracy.

