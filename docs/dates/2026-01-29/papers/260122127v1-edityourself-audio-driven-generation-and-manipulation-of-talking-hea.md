---
layout: default
title: EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers
---

# EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers
**arXiv**：[2601.22127v1](https://arxiv.org/abs/2601.22127) · [PDF](https://arxiv.org/pdf/2601.22127.pdf)  
**作者**：John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  

**一句话要点**：提出EditYourself框架，基于扩散变换器实现音频驱动的说话头视频编辑，以解决脚本修改中的运动保持与唇同步问题。

**关键词**：音频驱动视频编辑, 扩散变换器, 说话头视频, 时空修复, 唇同步, 视频后期制作

## 3 点简述
- 核心问题：现有视频生成模型难以编辑预录视频，需在脚本修改时保持运动、时序一致性和唇同步。
- 方法要点：基于通用视频扩散模型，通过音频条件和区域感知训练扩展，实现时空修复和内容增删改。
- 实验或效果：支持精确唇同步和时序重构，在长视频中保持视觉保真度和身份一致性，适用于专业后期制作。

## 摘要（原文）

> Current generative video models excel at producing novel content from text and image prompts, but leave a critical gap in editing existing pre-recorded videos, where minor alterations to the spoken script require preserving motion, temporal coherence, speaker identity, and accurate lip synchronization. We introduce EditYourself, a DiT-based framework for audio-driven video-to-video (V2V) editing that enables transcript-based modification of talking head videos, including the seamless addition, removal, and retiming of visually spoken content. Building on a general-purpose video diffusion model, EditYourself augments its V2V capabilities with audio conditioning and region-aware, edit-focused training extensions. This enables precise lip synchronization and temporally coherent restructuring of existing performances via spatiotemporal inpainting, including the synthesis of realistic human motion in newly added segments, while maintaining visual fidelity and identity consistency over long durations. This work represents a foundational step toward generative video models as practical tools for professional video post-production.

