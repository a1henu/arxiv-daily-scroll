---
layout: default
title: Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs
---

# Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs
**arXiv**：[2602.23136v1](https://arxiv.org/abs/2602.23136) · [PDF](https://arxiv.org/pdf/2602.23136.pdf)  
**作者**：Jayadev Billa  

**一句话要点**：提出模态坍缩为解码器失配问题，基于广义互信息分析多模态LLMs的信息提取极限。

**关键词**：多模态大语言模型, 模态坍缩, 广义互信息, 解码器失配, 信息提取极限, 训练目标优化

## 3 点简述
- 核心问题：多模态LLMs无法有效利用语音和图像中的非文本信息，如说话者身份或纹理，尽管编码器保留了这些信息。
- 方法要点：形式化为解码器失配问题，使用广义互信息理论推导信息提取上限，强调解码器评分规则是关键瓶颈。
- 实验或效果：在五个模型上验证理论，通过LoRA干预证明训练目标可改善特定信息可访问性，如情感识别提升7.5%。

## 摘要（原文）

> Multimodal LLMs can process speech and images, but they cannot hear a speaker's voice or see an object's texture. We show this is not a failure of encoding: speaker identity, emotion, and visual attributes survive through every LLM layer (3--55$\times$ above chance in linear probes), yet removing 64--71% of modality-specific variance improves decoder loss. The decoder has no learned use for these directions; their presence is noise.
>   We formalize this as a mismatched decoder problem: a decoder trained on text can only extract information along text-aligned directions. Accessible information is bounded by the Generalized Mutual Information (GMI), with degradation scaling with distributional distance and decoder sensitivity. The bound is a property of the decoder's scoring rule, not of any particular architecture; it applies whether non-text inputs arrive through a learned projection, a discrete codebook, or no explicit adapter at all. We validate this across five models spanning speech and vision. A controlled experiment (two Prismatic VLMs differing only in encoder text-alignment) confirms the bottleneck is the decoder's scoring rule, not the encoder or projection. A LoRA intervention demonstrates the fix: training with an emotion objective improves emotion accessibility ($+$7.5%) without affecting other attributes, confirming that the training objective determines what becomes accessible.

