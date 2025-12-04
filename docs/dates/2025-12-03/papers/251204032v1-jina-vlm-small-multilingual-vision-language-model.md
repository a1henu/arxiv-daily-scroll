---
layout: default
title: Jina-VLM: Small Multilingual Vision Language Model
---

# Jina-VLM: Small Multilingual Vision Language Model
**arXiv**：[2512.04032v1](https://arxiv.org/abs/2512.04032) · [PDF](https://arxiv.org/pdf/2512.04032.pdf)  
**作者**：Andreas Koukounas, Georgios Mastrapas, Florian Hönicke, Sedigheh Eslami, Guillaume Roncari, Scott Martens, Han Xiao  

**一句话要点**：提出Jina-VLM，一种2.4B参数多语言视觉语言模型，在开放2B规模模型中实现最先进的多语言视觉问答。

**关键词**：多语言视觉问答, 小规模视觉语言模型, 注意力池化连接器, 任意分辨率图像处理, SigLIP2视觉编码器, Qwen3语言主干

## 3 点简述
- 核心问题：解决多语言视觉问答中模型规模与性能的平衡问题，提升小规模模型在多语言场景下的表现。
- 方法要点：结合SigLIP2视觉编码器和Qwen3语言主干，通过注意力池化连接器实现任意分辨率图像的高效处理。
- 实验或效果：在标准VQA基准和多语言评估中超越可比模型，同时保持竞争力的纯文本性能。

## 摘要（原文）

> We present Jina-VLM, a 2.4B parameter vision-language model that achieves state-of-the-art multilingual visual question answering among open 2B-scale VLMs. The model couples a SigLIP2 vision encoder with a Qwen3 language backbone through an attention-pooling connector that enables token-efficient processing of arbitrary-resolution images. Across standard VQA benchmarks and multilingual evaluations, Jina-VLM outperforms comparable models while preserving competitive text-only performance.

