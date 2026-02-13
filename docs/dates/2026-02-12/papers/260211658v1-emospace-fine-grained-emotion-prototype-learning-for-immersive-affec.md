---
layout: default
title: EmoSpace: Fine-Grained Emotion Prototype Learning for Immersive Affective Content Generation
---

# EmoSpace: Fine-Grained Emotion Prototype Learning for Immersive Affective Content Generation
**arXiv**：[2602.11658v1](https://arxiv.org/abs/2602.11658) · [PDF](https://arxiv.org/pdf/2602.11658.pdf)  
**作者**：Bingyuan Wang, Xingbei Chen, Zongyang Qiu, Linping Yuan, Zeyu Wang  

**一句话要点**：提出EmoSpace框架，通过动态可解释情感原型学习，实现沉浸式情感内容生成中的细粒度控制。

**关键词**：情感原型学习, 视觉-语言对齐, 细粒度情感控制, 沉浸式内容生成, VR环境应用

## 3 点简述
- 核心问题：现有生成方法难以捕捉情感语义的细微差别，缺乏对沉浸式体验至关重要的细粒度控制。
- 方法要点：采用分层情感表示，通过视觉-语言对齐学习动态可解释情感原型，支持多原型引导、时间混合和注意力重加权。
- 实验或效果：在定性和定量评估中优于现有方法，并进行了VR与桌面环境情感感知的用户研究，支持多种应用如情感图像外绘和VR全景生成。

## 摘要（原文）

> Emotion is important for creating compelling virtual reality (VR) content. Although some generative methods have been applied to lower the barrier to creating emotionally rich content, they fail to capture the nuanced emotional semantics and the fine-grained control essential for immersive experiences. To address these limitations, we introduce EmoSpace, a novel framework for emotion-aware content generation that learns dynamic, interpretable emotion prototypes through vision-language alignment. We employ a hierarchical emotion representation with rich learnable prototypes that evolve during training, enabling fine-grained emotional control without requiring explicit emotion labels. We develop a controllable generation pipeline featuring multi-prototype guidance, temporal blending, and attention reweighting that supports diverse applications, including emotional image outpainting, stylized generation, and emotional panorama generation for VR environments. Our experiments demonstrate the superior performance of EmoSpace over existing methods in both qualitative and quantitative evaluations. Additionally, we present a comprehensive user study investigating how VR environments affect emotional perception compared to desktop settings. Our work facilitates immersive visual content generation with fine-grained emotion control and supports applications like therapy, education, storytelling, artistic creation, and cultural preservation. Code and models will be made publicly available.

