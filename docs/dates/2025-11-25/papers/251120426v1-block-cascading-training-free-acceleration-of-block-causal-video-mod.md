---
layout: default
title: Block Cascading: Training Free Acceleration of Block-Causal Video Models
---

# Block Cascading: Training Free Acceleration of Block-Causal Video Models
**arXiv**：[2511.20426v1](https://arxiv.org/abs/2511.20426) · [PDF](https://arxiv.org/pdf/2511.20426.pdf)  
**作者**：Hmrishav Bandyopadhyay, Nikhil Pinnaparaju, Rahim Entezari, Jim Scott, Yi-Zhe Song, Varun Jampani  

**一句话要点**：提出Block Cascading以解决块因果视频模型的推理速度与质量权衡问题

**关键词**：视频生成, 推理加速, 并行计算, 块因果模型, 训练免费优化

## 3 点简述
- 块因果视频生成面临速度与质量权衡，小模型仅16 FPS，大模型仅4.5 FPS
- 方法基于训练免费并行化，利用部分去噪上下文实现多块同时生成
- 实验显示5 GPU下速度提升约2倍，无显著质量损失，消除KV缓存开销

## 摘要（原文）

> Block-causal video generation faces a stark speed-quality trade-off: small 1.3B models manage only 16 FPS while large 14B models crawl at 4.5 FPS, forcing users to choose between responsiveness and quality. Block Cascading significantly mitigates this trade-off through training-free parallelization. Our key insight: future video blocks do not need fully denoised current blocks to begin generation. By starting block generation with partially denoised context from predecessors, we transform sequential pipelines into parallel cascades where multiple blocks denoise simultaneously. With 5 GPUs exploiting temporal parallelism, we achieve ~2x acceleration across all model scales: 1.3B models accelerate from 16 to 30 FPS, 14B models from 4.5 to 12.5 FPS. Beyond inference speed, Block Cascading eliminates overhead from KV-recaching (of ~200ms) during context switches for interactive generation. Extensive evaluations validated against multiple block-causal pipelines demonstrate no significant loss in generation quality when switching from block-causal to Block Cascading pipelines for inference. Project Page: https://hmrishavbandy.github.io/block_cascading_page/

