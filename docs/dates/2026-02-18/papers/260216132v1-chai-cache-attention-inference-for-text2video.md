---
layout: default
title: CHAI: CacHe Attention Inference for text2video
---

# CHAI: CacHe Attention Inference for text2video
**arXiv**：[2602.16132v1](https://arxiv.org/abs/2602.16132) · [PDF](https://arxiv.org/pdf/2602.16132.pdf)  
**作者**：Joel Mathew Cherian, Ashutosh Muralidhara Bharadwaj, Vima Gupta, Anand Padmanabha Iyer  

**一句话要点**：提出CHAI通过缓存注意力机制加速文本到视频生成，减少去噪步骤并保持质量。

**关键词**：文本到视频生成, 扩散模型加速, 缓存注意力, 推理优化, 潜在空间重用

## 3 点简述
- 文本到视频扩散模型因3D潜在空间顺序去噪导致推理速度慢。
- CHAI引入缓存注意力，跨推理重用共享对象/场景的潜在表示。
- 实验显示仅需8步去噪即可生成高质量视频，速度提升1.65-3.35倍。

## 摘要（原文）

> Text-to-video diffusion models deliver impressive results but remain slow because of the sequential denoising of 3D latents. Existing approaches to speed up inference either require expensive model retraining or use heuristic-based step skipping, which struggles to maintain video quality as the number of denoising steps decreases. Our work, CHAI, aims to use cross-inference caching to reduce latency while maintaining video quality. We introduce Cache Attention as an effective method for attending to shared objects/scenes across cross-inference latents. This selective attention mechanism enables effective reuse of cached latents across semantically related prompts, yielding high cache hit rates. We show that it is possible to generate high-quality videos using Cache Attention with as few as 8 denoising steps. When integrated into the overall system, CHAI is 1.65x - 3.35x faster than baseline OpenSora 1.2 while maintaining video quality.

