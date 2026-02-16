---
layout: default
title: CoPE-VideoLM: Codec Primitives For Efficient Video Language Models
---

# CoPE-VideoLM: Codec Primitives For Efficient Video Language Models
**arXiv**：[2602.13191v1](https://arxiv.org/abs/2602.13191) · [PDF](https://arxiv.org/pdf/2602.13191.pdf)  
**作者**：Sayan Deb Sarkar, Rémi Pautrat, Ondrej Miksik, Marc Pollefeys, Iro Armeni, Mahdi Rad, Mihai Dusmanu  

**一句话要点**：提出利用视频编解码原语（运动向量和残差）以高效处理视频语言模型，减少计算开销并提升性能。

**关键词**：视频语言模型, 编解码原语, 运动向量, 残差编码, 高效计算, 视频理解基准

## 3 点简述
- 当前视频语言模型采用关键帧采样，可能遗漏宏观事件和微观细节，且全图像处理计算成本高。
- 引入轻量级Transformer编码器聚合编解码原语，通过预训练对齐图像编码器嵌入，加速端到端微调收敛。
- 相比标准方法，首令牌时间减少达86%，令牌使用减少达93%，在14个视频理解基准上保持或超越性能。

## 摘要（原文）

> Video Language Models (VideoLMs) empower AI systems to understand temporal dynamics in videos. To fit to the maximum context window constraint, current methods use keyframe sampling which can miss both macro-level events and micro-level details due to the sparse temporal coverage. Furthermore, processing full images and their tokens for each frame incurs substantial computational overhead. To address these limitations, we propose to leverage video codec primitives (specifically motion vectors and residuals) which natively encode video redundancy and sparsity without requiring expensive full-image encoding for most frames. To this end, we introduce lightweight transformer-based encoders that aggregate codec primitives and align their representations with image encoder embeddings through a pre-training strategy that accelerates convergence during end-to-end fine-tuning. Our approach reduces the time-to-first-token by up to $86\%$ and token usage by up to $93\%$ compared to standard VideoLMs. Moreover, by varying the keyframe and codec primitive densities we are able to maintain or exceed performance on $14$ diverse video understanding benchmarks spanning general question answering, temporal reasoning, long-form understanding, and spatial scene understanding.

