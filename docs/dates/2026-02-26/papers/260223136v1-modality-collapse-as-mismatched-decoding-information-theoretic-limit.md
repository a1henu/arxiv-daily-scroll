---
layout: default
title: Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs
---

# Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs
**arXiv**：[2602.23136v1](https://arxiv.org/abs/2602.23136) · [PDF](https://arxiv.org/pdf/2602.23136.pdf)  
**作者**：Jayadev Billa  

**一句话要点**：提出模态坍缩为解码器失配问题，揭示多模态大语言模型的信息理论极限

**关键词**：多模态大语言模型, 模态坍缩, 解码器失配, 广义互信息, 信息理论极限, 评分规则

## 3 点简述
- 核心问题：多模态LLMs无法有效利用语音身份、情感等非文本信息，尽管编码器保留了这些信息
- 方法要点：将问题形式化为解码器失配，用广义互信息理论分析可访问信息的上界
- 实验或效果：通过控制实验和干预验证解码器评分规则是瓶颈，调整训练目标可提升特定信息可访问性

## 摘要（原文）

> Multimodal LLMs can process speech and images, but they cannot hear a speaker's voice or see an object's texture. We show this is not a failure of encoding: speaker identity, emotion, and visual attributes survive through every LLM layer (3--55$\times$ above chance in linear probes), yet removing 64--71% of modality-specific variance improves decoder loss. The decoder has no learned use for these directions; their presence is noise.
>   We formalize this as a mismatched decoder problem: a decoder trained on text can only extract information along text-aligned directions. Accessible information is bounded by the Generalized Mutual Information (GMI), with degradation scaling with distributional distance and decoder sensitivity. The bound is a property of the decoder's scoring rule, not of any particular architecture; it applies whether non-text inputs arrive through a learned projection, a discrete codebook, or no explicit adapter at all. We validate this across five models spanning speech and vision. A controlled experiment (two Prismatic VLMs differing only in encoder text-alignment) confirms the bottleneck is the decoder's scoring rule, not the encoder or projection. A LoRA intervention demonstrates the fix: training with an emotion objective improves emotion accessibility ($+$7.5%) without affecting other attributes, confirming that the training objective determines what becomes accessible.

