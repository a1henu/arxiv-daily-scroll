---
layout: default
title: ConceptCaps -- a Distilled Concept Dataset for Interpretability in Music Models
---

# ConceptCaps -- a Distilled Concept Dataset for Interpretability in Music Models
**arXiv**：[2601.14157v1](https://arxiv.org/abs/2601.14157) · [PDF](https://arxiv.org/pdf/2601.14157.pdf)  
**作者**：Bruno Sienkiewicz, Łukasz Neumann, Mateusz Modrzejewski  

**一句话要点**：提出ConceptCaps数据集以解决音乐模型可解释性中概念数据缺乏问题

**关键词**：音乐可解释性, 概念数据集, TCAV方法, 音频合成, 属性分类

## 3 点简述
- 核心问题：现有音乐数据集标签稀疏、噪声大，不适用于基于概念的可解释性方法如TCAV。
- 方法要点：通过VAE学习属性共现模式，LLM生成专业描述，MusicGen合成音频，构建23k音乐-字幕-音频三元组。
- 实验或效果：验证音频-文本对齐、语言质量，TCAV分析确认概念探针恢复音乐有意义模式。

## 摘要（原文）

> Concept-based interpretability methods like TCAV require clean, well-separated positive and negative examples for each concept. Existing music datasets lack this structure: tags are sparse, noisy, or ill-defined. We introduce ConceptCaps, a dataset of 23k music-caption-audio triplets with explicit labels from a 200-attribute taxonomy. Our pipeline separates semantic modeling from text generation: a VAE learns plausible attribute co-occurrence patterns, a fine-tuned LLM converts attribute lists into professional descriptions, and MusicGen synthesizes corresponding audio. This separation improves coherence and controllability over end-to-end approaches. We validate the dataset through audio-text alignment (CLAP), linguistic quality metrics (BERTScore, MAUVE), and TCAV analysis confirming that concept probes recover musically meaningful patterns. Dataset and code are available online.

