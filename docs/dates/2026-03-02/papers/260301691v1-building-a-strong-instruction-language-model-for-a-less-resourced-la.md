---
layout: default
title: Building a Strong Instruction Language Model for a Less-Resourced Language
---

# Building a Strong Instruction Language Model for a Less-Resourced Language
**arXiv**：[2603.01691v1](https://arxiv.org/abs/2603.01691) · [PDF](https://arxiv.org/pdf/2603.01691.pdf)  
**作者**：Domen Vreš, Tjaša Arčon, Timotej Petrič, Dario Vajda, Marko Robnik-Šikonja, Iztok Lebar Bajec  

**一句话要点**：提出GaMS3-12B模型，通过多阶段训练优化斯洛文尼亚语等低资源语言性能

**关键词**：低资源语言适配, 多阶段训练, 斯洛文尼亚语模型, 生成式语言模型, 监督微调

## 3 点简述
- 核心问题：现有开源大语言模型主要基于英语训练，在低资源语言上表现不佳
- 方法要点：采用三阶段持续预训练和两阶段监督微调，结合多语言数据适配斯洛文尼亚语
- 实验或效果：在斯洛文尼亚语评估中超越同规模模型，与更大商业模型性能相当

## 摘要（原文）

> Large language models (LLMs) have become an essential tool for natural language processing and artificial intelligence in general. Current open-source models are primarily trained on English texts, resulting in poorer performance on less-resourced languages and cultures. We present a set of methodological approaches necessary for the successful adaptation of an LLM to a less-resourced language, and demonstrate them using the Slovene language. We present GaMS3-12B, a generative model for Slovene with 12 billion parameters, and demonstrate that it is the best-performing open-source model for Slovene within its parameter range. We adapted the model to the Slovene language using three-stage continual pre-training of the Gemma 3 model, followed by two-stage supervised fine-tuning (SFT). We trained the model on a combination of 140B Slovene, English, Bosnian, Serbian, and Croatian pretraining tokens, and over 200 thousand English and Slovene SFT examples. We evaluate GaMS3-12B on the Slovenian-LLM-Eval datasets, English-to-Slovene translation, and the Slovene LLM arena. We show that the described model outperforms 12B Gemma 3 across all three scenarios and performs comparably to much larger commercial GPT-4o in the Slovene LLM arena, achieving a win rate of over 60 %.

