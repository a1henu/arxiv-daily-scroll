---
layout: default
title: End-to-End Learning-based Video Streaming Enhancement Pipeline: A Generative AI Approach
---

# End-to-End Learning-based Video Streaming Enhancement Pipeline: A Generative AI Approach
**arXiv**：[2512.14185v1](https://arxiv.org/abs/2512.14185) · [PDF](https://arxiv.org/pdf/2512.14185.pdf)  
**作者**：Emanuele Artioli, Farzad Tashtarian, Christian Timmerer  

**一句话要点**：提出ELVIS端到端学习视频流增强管道，结合服务器编码优化与客户端生成修复，以提升视频质量而不增加带宽。

**关键词**：视频流增强, 生成式AI, 端到端学习, 编码优化, 客户端修复

## 3 点简述
- 核心问题：传统编解码器需传输全部视频数据，无法利用上下文，难以平衡高质量与流畅播放。
- 方法要点：采用模块化架构，集成服务器端编码优化和客户端生成修复模型，移除并重建冗余数据。
- 实验或效果：当前技术相比基准提升达11 VMAF点，但实时应用面临计算需求挑战。

## 摘要（原文）

> The primary challenge of video streaming is to balance high video quality with smooth playback. Traditional codecs are well tuned for this trade-off, yet their inability to use context means they must encode the entire video data and transmit it to the client. This paper introduces ELVIS (End-to-end Learning-based VIdeo Streaming Enhancement Pipeline), an end-to-end architecture that combines server-side encoding optimizations with client-side generative in-painting to remove and reconstruct redundant video data. Its modular design allows ELVIS to integrate different codecs, inpainting models, and quality metrics, making it adaptable to future innovations. Our results show that current technologies achieve improvements of up to 11 VMAF points over baseline benchmarks, though challenges remain for real-time applications due to computational demands. ELVIS represents a foundational step toward incorporating generative AI into video streaming pipelines, enabling higher quality experiences without increased bandwidth requirements.

