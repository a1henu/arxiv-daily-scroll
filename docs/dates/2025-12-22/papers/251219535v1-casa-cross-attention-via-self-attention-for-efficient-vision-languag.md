---
layout: default
title: CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion
---

# CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion
**arXiv**：[2512.19535v1](https://arxiv.org/abs/2512.19535) · [PDF](https://arxiv.org/pdf/2512.19535.pdf)  
**作者**：Moritz Böhle, Amélie Royer, Juliette Marrie, Edouard Grave, Patrick Pérez  

**一句话要点**：提出CASA方法，通过自注意力实现跨注意力，以高效融合视觉语言信息。

**关键词**：视觉语言模型, 跨注意力, 自注意力, 高效融合, 流视频字幕

## 3 点简述
- 核心问题：现有视觉语言模型在跨注意力方法中存在性能差距，尤其在细粒度视觉任务上。
- 方法要点：在跨注意力层中引入局部文本到文本交互，提升模型对视觉细节的理解能力。
- 实验或效果：在图像理解基准上显著缩小与全令牌插入的性能差距，适用于长上下文多模态任务如流视频字幕。

## 摘要（原文）

> Vision-language models (VLMs) are commonly trained by inserting image tokens from a pretrained vision encoder into the textual stream of a language model. This allows text and image information to fully attend to one another within the model, but becomes extremely costly for high-resolution images, long conversations, or streaming videos, both in memory and compute. VLMs leveraging cross-attention are an efficient alternative to token insertion but exhibit a clear performance gap, in particular on tasks involving fine-grained visual details. We find that a key to improving such models is to also enable local text-to-text interaction in the dedicated cross-attention layers. Building on this, we propose CASA, Cross-Attention via Self-Attention, a simple and efficient paradigm which substantially reduces the gap with full token insertion on common image understanding benchmarks, while enjoying the same scalability as cross-attention models when applied to long-context multimodal tasks such as streaming video captioning. For samples and code, please see our project page at https://kyutai.org/casa .

