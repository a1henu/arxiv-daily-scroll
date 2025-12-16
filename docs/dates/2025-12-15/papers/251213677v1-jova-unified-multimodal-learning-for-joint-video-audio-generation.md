---
layout: default
title: JoVA: Unified Multimodal Learning for Joint Video-Audio Generation
---

# JoVA: Unified Multimodal Learning for Joint Video-Audio Generation
**arXiv**：[2512.13677v1](https://arxiv.org/abs/2512.13677) · [PDF](https://arxiv.org/pdf/2512.13677.pdf)  
**作者**：Xiaohu Huang, Hao Zhou, Qiangpeng Yang, Shilei Wen, Kai Han  

**一句话要点**：提出JoVA框架，通过联合自注意力和嘴部区域损失，实现高质量视频-音频联合生成与唇语同步。

**关键词**：视频-音频联合生成, 唇语同步, 跨模态自注意力, 面部关键点检测, 多模态学习

## 3 点简述
- 现有方法难以生成唇语同步的人类语音，且依赖额外对齐模块增加复杂性。
- JoVA采用视频和音频令牌的联合自注意力，无需额外模块，实现高效跨模态交互。
- 引入基于面部关键点检测的嘴部区域损失，提升唇语同步质量，实验显示在准确性和保真度上优于或竞争于先进方法。

## 摘要（原文）

> In this paper, we present JoVA, a unified framework for joint video-audio generation. Despite recent encouraging advances, existing methods face two critical limitations. First, most existing approaches can only generate ambient sounds and lack the capability to produce human speech synchronized with lip movements. Second, recent attempts at unified human video-audio generation typically rely on explicit fusion or modality-specific alignment modules, which introduce additional architecture design and weaken the model simplicity of the original transformers. To address these issues, JoVA employs joint self-attention across video and audio tokens within each transformer layer, enabling direct and efficient cross-modal interaction without the need for additional alignment modules. Furthermore, to enable high-quality lip-speech synchronization, we introduce a simple yet effective mouth-area loss based on facial keypoint detection, which enhances supervision on the critical mouth region during training without compromising architectural simplicity. Extensive experiments on benchmarks demonstrate that JoVA outperforms or is competitive with both unified and audio-driven state-of-the-art methods in lip-sync accuracy, speech quality, and overall video-audio generation fidelity. Our results establish JoVA as an elegant framework for high-quality multimodal generation.

