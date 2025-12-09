---
layout: default
title: ContextAnyone: Context-Aware Diffusion for Character-Consistent Text-to-Video Generation
---

# ContextAnyone: Context-Aware Diffusion for Character-Consistent Text-to-Video Generation
**arXiv**：[2512.07328v1](https://arxiv.org/abs/2512.07328) · [PDF](https://arxiv.org/pdf/2512.07328.pdf)  
**作者**：Ziyang Mai, Yu-Wing Tai  

**一句话要点**：提出ContextAnyone框架，通过上下文感知扩散实现基于文本和单参考图像的字符一致视频生成。

**关键词**：文本到视频生成, 字符一致性, 上下文感知扩散, 参考图像重建, Emphasize-Attention模块, Gap-RoPE位置嵌入

## 3 点简述
- 核心问题：现有文本到视频生成方法难以保持跨场景的字符身份一致性，如发型、服装和体型等上下文线索。
- 方法要点：结合参考图像重建和新帧生成，采用Emphasize-Attention模块和Gap-RoPE位置嵌入，增强参考感知并稳定时序建模。
- 实验或效果：在身份一致性和视觉质量上优于现有参考到视频方法，生成多样动作和场景下的连贯字符视频。

## 摘要（原文）

> Text-to-video (T2V) generation has advanced rapidly, yet maintaining consistent character identities across scenes remains a major challenge. Existing personalization methods often focus on facial identity but fail to preserve broader contextual cues such as hairstyle, outfit, and body shape, which are critical for visual coherence. We propose \textbf{ContextAnyone}, a context-aware diffusion framework that achieves character-consistent video generation from text and a single reference image. Our method jointly reconstructs the reference image and generates new video frames, enabling the model to fully perceive and utilize reference information. Reference information is effectively integrated into a DiT-based diffusion backbone through a novel Emphasize-Attention module that selectively reinforces reference-aware features and prevents identity drift across frames. A dual-guidance loss combines diffusion and reference reconstruction objectives to enhance appearance fidelity, while the proposed Gap-RoPE positional embedding separates reference and video tokens to stabilize temporal modeling. Experiments demonstrate that ContextAnyone outperforms existing reference-to-video methods in identity consistency and visual quality, generating coherent and context-preserving character videos across diverse motions and scenes. Project page: \href{https://github.com/ziyang1106/ContextAnyone}{https://github.com/ziyang1106/ContextAnyone}.

