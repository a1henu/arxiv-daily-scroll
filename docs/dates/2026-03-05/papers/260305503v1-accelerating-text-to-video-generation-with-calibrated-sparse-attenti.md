---
layout: default
title: Accelerating Text-to-Video Generation with Calibrated Sparse Attention
---

# Accelerating Text-to-Video Generation with Calibrated Sparse Attention
**arXiv**：[2603.05503v1](https://arxiv.org/abs/2603.05503) · [PDF](https://arxiv.org/pdf/2603.05503.pdf)  
**作者**：Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar  

**一句话要点**：提出CalibAtt方法，通过校准稀疏注意力加速文本到视频生成

**关键词**：文本到视频生成, 稀疏注意力, 扩散模型, 推理加速, 训练无关方法

## 3 点简述
- 问题：扩散模型视频生成速度慢，时空注意力是瓶颈
- 方法：离线校准稳定稀疏模式，推理时跳过无关连接
- 效果：在多个模型上实现最高1.58倍加速，保持生成质量

## 摘要（原文）

> Recent diffusion models enable high-quality video generation, but suffer from slow runtimes. The large transformer-based backbones used in these models are bottlenecked by spatiotemporal attention. In this paper, we identify that a significant fraction of token-to-token connections consistently yield negligible scores across various inputs, and their patterns often repeat across queries. Thus, the attention computation in these cases can be skipped with little to no effect on the result. This observation continues to hold for connections among local token blocks. Motivated by this, we introduce CalibAtt, a training-free method that accelerates video generation via calibrated sparse attention. CalibAtt performs an offline calibration pass that identifies block-level sparsity and repetition patterns that are stable across inputs, and compiles these patterns into optimized attention operations for each layer, head, and diffusion timestep. At inference time, we compute the selected input-dependent connections densely, and skip the unselected ones in a hardware-efficient manner. Extensive experiments on Wan 2.1 14B, Mochi 1, and few-step distilled models at various resolutions show that CalibAtt achieves up to 1.58x end-to-end speedup, outperforming existing training-free methods while maintaining video generation quality and text-video alignment.

