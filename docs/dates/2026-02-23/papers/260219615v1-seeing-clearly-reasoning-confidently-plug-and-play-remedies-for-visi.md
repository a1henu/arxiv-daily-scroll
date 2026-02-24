---
layout: default
title: Seeing Clearly, Reasoning Confidently: Plug-and-Play Remedies for Vision Language Model Blindness
---

# Seeing Clearly, Reasoning Confidently: Plug-and-Play Remedies for Vision Language Model Blindness
**arXiv**：[2602.19615v1](https://arxiv.org/abs/2602.19615) · [PDF](https://arxiv.org/pdf/2602.19615.pdf)  
**作者**：Xin Hu, Haomiao Ni, Yunbei Zhang, Jihun Hamm, Zechen Li, Zhengming Ding  

**一句话要点**：提出无需微调的即插即用模块，通过精炼视觉令牌和丰富文本提示，提升视觉语言模型对罕见物体的推理能力。

**关键词**：视觉语言模型, 罕见物体推理, 即插即用模块, 多模态嵌入, 注意力增强, 文本提示优化

## 3 点简述
- 核心问题：视觉语言模型在罕见物体推理上表现不佳，因预训练数据稀缺。
- 方法要点：利用视觉基础模型和同义词增强文本学习多模态类嵌入，通过轻量注意力模块精炼视觉令牌，并生成对象感知提示注入文本。
- 实验或效果：在两个基准测试中，预训练模型在罕见物体识别和推理上取得显著提升，分析显示方法增强了模型对罕见物体的关注和推理能力。

## 摘要（原文）

> Vision language models (VLMs) have achieved remarkable success in broad visual understanding, yet they remain challenged by object-centric reasoning on rare objects due to the scarcity of such instances in pretraining data. While prior efforts alleviate this issue by retrieving additional data or introducing stronger vision encoders, these methods are still computationally intensive during finetuning VLMs and don't fully exploit the original training data. In this paper, we introduce an efficient plug-and-play module that substantially improves VLMs' reasoning over rare objects by refining visual tokens and enriching input text prompts, without VLMs finetuning. Specifically, we propose to learn multi-modal class embeddings for rare objects by leveraging prior knowledge from vision foundation models and synonym-augmented text descriptions, compensating for limited training examples. These embeddings refine the visual tokens in VLMs through a lightweight attention-based enhancement module that improves fine-grained object details. In addition, we use the learned embeddings as object-aware detectors to generate informative hints, which are injected into the text prompts to help guide the VLM's attention toward relevant image regions. Experiments on two benchmarks show consistent and substantial gains for pretrained VLMs in rare object recognition and reasoning. Further analysis reveals how our method strengthens the VLM's ability to focus on and reason about rare objects.

