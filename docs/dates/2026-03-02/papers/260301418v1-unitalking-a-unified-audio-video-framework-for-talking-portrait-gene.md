---
layout: default
title: UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation
---

# UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation
**arXiv**：[2603.01418v1](https://arxiv.org/abs/2603.01418) · [PDF](https://arxiv.org/pdf/2603.01418.pdf)  
**作者**：Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  

**一句话要点**：提出UniTalking统一音频-视频扩散框架，以生成高保真语音和唇形同步的说话肖像。

**关键词**：说话肖像生成, 音频-视频同步, 扩散模型, 多模态Transformer, 个性化语音克隆, 端到端框架

## 3 点简述
- 核心问题：现有先进音频-视频生成模型如Veo3和Sora2闭源，限制了架构和训练范式的可访问性。
- 方法要点：采用多模态Transformer块，通过共享自注意力机制显式建模音频和视频潜在令牌的细粒度时间对应关系。
- 实验或效果：结合预训练视频生成模型的先验，实现高效训练，在唇形同步准确性、音频自然度和整体感知质量上优于现有开源方法。

## 摘要（原文）

> While state-of-the-art audio-video generation models like Veo3 and Sora2 demonstrate remarkable capabilities, their closed-source nature makes their architectures and training paradigms inaccessible. To bridge this gap in accessibility and performance, we introduce UniTalking, a unified, end-to-end diffusion framework for generating high-fidelity speech and lip-synchronized video. At its core, our framework employs Multi-Modal Transformer Blocks to explicitly model the fine-grained temporal correspondence between audio and video latent tokens via a shared self-attention mechanism. By leveraging powerful priors from a pre-trained video generation model, our framework ensures state-of-the-art visual fidelity while enabling efficient training. Furthermore, UniTalking incorporates a personalized voice cloning capability, allowing the generation of speech in a target style from a brief audio reference. Qualitative and quantitative results demonstrate that our method produces highly realistic talking portraits, achieving superior performance over existing open-source approaches in lip-sync accuracy, audio naturalness, and overall perceptual quality.

