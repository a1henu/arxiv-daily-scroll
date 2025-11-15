---
layout: default
title: Rethinking Visual Information Processing in Multimodal LLMs
---

# Rethinking Visual Information Processing in Multimodal LLMs
**arXiv**：[2511.10301v1](https://arxiv.org/abs/2511.10301) · [PDF](https://arxiv.org/pdf/2511.10301.pdf)  
**作者**：Dongwan Kim, Viresh Ranjan, Takashi Nagata, Arnab Dhua, Amit Kumar K C  

**一句话要点**：提出LLaViT以解决多模态LLM中视觉特征整合不足的问题

**关键词**：多模态大语言模型, 视觉语言建模, 视觉编码器, 双向注意力, 全局局部表示

## 3 点简述
- 核心问题：LLaVA架构因文本与视觉模态不匹配，难以有效整合视觉特征
- 方法要点：通过分离视觉QKV投影、双向注意力和全局局部表示，使LLM同时作为视觉编码器
- 实验或效果：在多种基准测试中显著超越LLaVA，甚至优于参数翻倍的模型

## 摘要（原文）

> Despite the remarkable success of the LLaVA architecture for vision-language tasks, its design inherently struggles to effectively integrate visual features due to the inherent mismatch between text and vision modalities. We tackle this issue from a novel perspective in which the LLM not only serves as a language model but also a powerful vision encoder. To this end, we present LLaViT - Large Language Models as extended Vision Transformers - which enables the LLM to simultaneously function as a vision encoder through three key modifications: (1) learning separate QKV projections for vision modality, (2) enabling bidirectional attention on visual tokens, and (3) incorporating both global and local visual representations. Through extensive controlled experiments on a wide range of LLMs, we demonstrate that LLaViT significantly outperforms the baseline LLaVA method on a multitude of benchmarks, even surpassing models with double its parameter count, establishing a more effective approach to vision-language modeling.

