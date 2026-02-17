---
layout: default
title: Adapting VACE for Real-Time Autoregressive Video Diffusion
---

# Adapting VACE for Real-Time Autoregressive Video Diffusion
**arXiv**：[2602.14381v1](https://arxiv.org/abs/2602.14381) · [PDF](https://arxiv.org/pdf/2602.14381.pdf)  
**作者**：Ryan Fosdick  

**一句话要点**：提出VACE实时自回归视频扩散适配方法，以支持流式视频生成场景。

**关键词**：实时视频生成, 自回归模型, 视频扩散, 流式处理, 条件控制

## 3 点简述
- 核心问题：VACE原模型依赖双向注意力，不兼容流式生成所需的固定块大小和因果注意力。
- 方法要点：将参考帧从扩散潜在空间移至并行条件通路，重用预训练权重，无需额外训练。
- 实验或效果：在1.3B和14B模型上，VACE增加20-30%延迟，参考到视频保真度因因果注意力限制而严重下降。

## 摘要（原文）

> We describe an adaptation of VACE (Video All-in-one Creation and Editing) for real-time autoregressive video generation. VACE provides unified video control (reference guidance, structural conditioning, inpainting, and temporal extension) but assumes bidirectional attention over full sequences, making it incompatible with streaming pipelines that require fixed chunk sizes and causal attention. The key modification moves reference frames from the diffusion latent space into a parallel conditioning pathway, preserving the fixed chunk sizes and KV caching that autoregressive models require. This adaptation reuses existing pretrained VACE weights without additional training. Across 1.3B and 14B model scales, VACE adds 20-30% latency overhead for structural control and inpainting, with negligible VRAM cost relative to the base model. Reference-to-video fidelity is severely degraded compared to batch VACE due to causal attention constraints. A reference implementation is available at https://github.com/daydreamlive/scope.

