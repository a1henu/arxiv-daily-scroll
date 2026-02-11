---
layout: default
title: Maastricht University at AMIYA: Adapting LLMs for Dialectal Arabic using Fine-tuning and MBR Decoding
---

# Maastricht University at AMIYA: Adapting LLMs for Dialectal Arabic using Fine-tuning and MBR Decoding
**arXiv**：[2602.09703v1](https://arxiv.org/abs/2602.09703) · [PDF](https://arxiv.org/pdf/2602.09703.pdf)  
**作者**：Abdulhai Alali, Abderrahmane Issam  

**一句话要点**：提出基于LoRA微调、适配器合并和方言感知MBR解码的方法，以提升阿拉伯语方言的生成与翻译性能。

**关键词**：方言阿拉伯语, LoRA微调, 适配器合并, MBR解码, 方言生成, 语言模型适应

## 3 点简述
- 核心问题：阿拉伯语方言因数据有限和语言变异，在大型语言模型中代表性不足。
- 方法要点：采用LoRA微调、适配器合并和方言感知MBR解码，优化方言保真度。
- 实验或效果：在叙利亚、摩洛哥和沙特阿拉伯方言上验证，方法提升方言保真度并保持语义准确性。

## 摘要（原文）

> Large Language Models (LLMs) are becoming increasingly multilingual, supporting hundreds of languages, especially high resource ones. Unfortunately, Dialect variations are still underrepresented due to limited data and linguistic variation. In this work, we adapt a pre-trained LLM to improve dialectal performance. Specifically, we use Low Rank Adaptation (LoRA) fine-tuning on monolingual and English Dialect parallel data, adapter merging and dialect-aware MBR decoding to improve dialectal fidelity generation and translation. Experiments on Syrian, Moroccan, and Saudi Arabic show that merging and MBR improve dialectal fidelity while preserving semantic accuracy. This combination provides a compact and effective framework for robust dialectal Arabic generation.

