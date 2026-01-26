---
layout: default
title: SoS: Analysis of Surface over Semantics in Multilingual Text-To-Image Generation
---

# SoS: Analysis of Surface over Semantics in Multilingual Text-To-Image Generation
**arXiv**：[2601.16803v1](https://arxiv.org/abs/2601.16803) · [PDF](https://arxiv.org/pdf/2601.16803.pdf)  
**作者**：Carolin Holtermann, Florian Schneider, Anne Lauscher  

**一句话要点**：提出SoS分析框架以量化多语言文本到图像生成中的表面形式优先倾向

**关键词**：文本到图像生成, 多语言处理, 文化刻板印象, 表面形式优先, 模型分析

## 3 点简述
- 核心问题：多语言T2I模型常优先处理提示的表面形式而非语义，导致文化刻板描绘
- 方法要点：创建覆盖171种文化身份的提示集，翻译为14种语言，并引入新度量量化SoS倾向
- 实验或效果：七种模型中六种在至少两种语言中表现出强表面倾向，且与刻板视觉描绘相关

## 摘要（原文）

> Text-to-image (T2I) models are increasingly employed by users worldwide. However, prior research has pointed to the high sensitivity of T2I towards particular input languages - when faced with languages other than English (i.e., different surface forms of the same prompt), T2I models often produce culturally stereotypical depictions, prioritizing the surface over the prompt's semantics. Yet a comprehensive analysis of this behavior, which we dub Surface-over-Semantics (SoS), is missing. We present the first analysis of T2I models' SoS tendencies. To this end, we create a set of prompts covering 171 cultural identities, translated into 14 languages, and use it to prompt seven T2I models. To quantify SoS tendencies across models, languages, and cultures, we introduce a novel measure and analyze how the tendencies we identify manifest visually. We show that all but one model exhibit strong surface-level tendency in at least two languages, with this effect intensifying across the layers of T2I text encoders. Moreover, these surface tendencies frequently correlate with stereotypical visual depictions.

