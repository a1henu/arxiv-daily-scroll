---
layout: default
title: LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation
---

# LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation
**arXiv**：[2512.23576v1](https://arxiv.org/abs/2512.23576) · [PDF](https://arxiv.org/pdf/2512.23576.pdf)  
**作者**：Ethan Chern, Zhulin Hu, Bohao Tang, Jiadi Su, Steffi Chern, Zhijie Deng, Pengfei Liu  

**一句话要点**：提出改进策略蒸馏方法以构建实时多模态交互视频扩散系统LiveTalk

**关键词**：实时视频生成, 多模态交互, 策略蒸馏, 视频扩散模型, 人机交互系统

## 3 点简述
- 针对扩散模型实时交互困难，研究多模态条件下策略蒸馏的优化问题
- 改进蒸馏配方，关注条件输入质量及策略优化初始化与调度，减少推理成本
- 在基准测试中实现20倍加速，系统评估显示实时交互性能优于Sora2和Veo3

## 摘要（原文）

> Real-time video generation via diffusion is essential for building general-purpose multimodal interactive AI systems. However, the simultaneous denoising of all video frames with bidirectional attention via an iterative process in diffusion models prevents real-time interaction. While existing distillation methods can make the model autoregressive and reduce sampling steps to mitigate this, they focus primarily on text-to-video generation, leaving the human-AI interaction unnatural and less efficient. This paper targets real-time interactive video diffusion conditioned on a multimodal context, including text, image, and audio, to bridge the gap. Given the observation that the leading on-policy distillation approach Self Forcing encounters challenges (visual artifacts like flickering, black frames, and quality degradation) with multimodal conditioning, we investigate an improved distillation recipe with emphasis on the quality of condition inputs as well as the initialization and schedule for the on-policy optimization. On benchmarks for multimodal-conditioned (audio, image, and text) avatar video generation including HDTF, AVSpeech, and CelebV-HQ, our distilled model matches the visual quality of the full-step, bidirectional baselines of similar or larger size with 20x less inference cost and latency. Further, we integrate our model with audio language models and long-form video inference technique Anchor-Heavy Identity Sinks to build LiveTalk, a real-time multimodal interactive avatar system. System-level evaluation on our curated multi-turn interaction benchmark shows LiveTalk outperforms state-of-the-art models (Sora2, Veo3) in multi-turn video coherence and content quality, while reducing response latency from 1 to 2 minutes to real-time generation, enabling seamless human-AI multimodal interaction.

