---
layout: default
title: LogoDiffuser: Training-Free Multilingual Logo Generation and Stylization via Letter-Aware Attention Control
---

# LogoDiffuser: Training-Free Multilingual Logo Generation and Stylization via Letter-Aware Attention Control
**arXiv**：[2603.09759v1](https://arxiv.org/abs/2603.09759) · [PDF](https://arxiv.org/pdf/2603.09759.pdf)  
**作者**：Mingyu Kang, Hyein Seo, Yuna Jeong, Junhyeong Park, Yong Suk Choi  

**一句话要点**：提出LogoDiffuser以解决多语言标志生成中字符几何失真和无需额外训练的问题。

**关键词**：多语言标志生成, 扩散模型, 注意力控制, 训练免费方法, 字符结构保持

## 3 点简述
- 核心问题：现有方法在多语言标志生成中易扭曲字符几何，且需额外训练支持多语言。
- 方法要点：基于多模态扩散变换器，输入字符图像而非文本提示，通过字母感知注意力控制整合字符结构与视觉设计。
- 实验或效果：实验和用户研究表明，该方法在多语言标志生成中达到先进性能。

## 摘要（原文）

> Recent advances in text-to-image generation have been remarkable, but generating multilingual design logos that harmoniously integrate visual and textual elements remains a challenging task. Existing methods often distort character geometry when applying creative styles and struggle to support multilingual text generation without additional training. To address these challenges, we propose LogoDiffuser, a training-free method that synthesizes multilingual logo designs using the multimodal diffusion transformer. Instead of using textual prompts, we input the target characters as images, enabling robust character structure control regardless of language. We first analyze the joint attention mechanism to identify core tokens, which are tokens that strongly respond to textual structures. With this observation, our method integrates character structure and visual design by injecting the most informative attention maps. Furthermore, we perform layer-wise aggregation of attention maps to mitigate attention shifts across layers and obtain consistent core tokens. Extensive experiments and user studies demonstrate that our method achieves state-of-the-art performance in multilingual logo generation.

