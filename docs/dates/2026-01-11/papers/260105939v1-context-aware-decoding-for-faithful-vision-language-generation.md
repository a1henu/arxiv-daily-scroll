---
layout: default
title: Context-Aware Decoding for Faithful Vision-Language Generation
---

# Context-Aware Decoding for Faithful Vision-Language Generation
**arXiv**：[2601.05939v1](https://arxiv.org/abs/2601.05939) · [PDF](https://arxiv.org/pdf/2601.05939.pdf)  
**作者**：Mehrdad Fazli, Bowen Wei, Ziwei Zhu  

**一句话要点**：提出上下文嵌入注入以缓解大视觉语言模型在开放任务中的幻觉问题

**关键词**：大视觉语言模型, 幻觉缓解, 上下文嵌入注入, 无训练方法, 视觉保真度, 层间生成分析

## 3 点简述
- 核心问题：大视觉语言模型在图像描述等开放任务中易产生与视觉输入不一致的幻觉响应
- 方法要点：基于层间生成动态分析，利用最后输入令牌的隐藏状态作为接地信号，设计无训练的上下文嵌入注入方法
- 实验或效果：在CHAIR等基准测试中，动态变体在三个模型上实现最低整体幻觉率，优于现有方法

## 摘要（原文）

> Hallucinations, generating responses inconsistent with the visual input, remain a critical limitation of large vision-language models (LVLMs), especially in open-ended tasks such as image captioning and visual reasoning. In this work, we probe the layer-wise generation dynamics that drive hallucinations and propose a training-free mitigation strategy. Employing the Logit Lens, we examine how LVLMs construct next-token distributions across decoder layers, uncovering a pronounced commitment-depth gap: truthful tokens accumulate probability mass on their final candidates earlier than hallucinatory ones. Drawing on this discovery, we introduce Context Embedding Injection (CEI), a lightweight method that harnesses the hidden state of the last input token-the context embedding-as a grounding signal to maintain visual fidelity throughout decoding and curb hallucinations. Evaluated on the CHAIR, AMBER, and MMHal-Bench benchmarks (with a maximum token length of 512), CEI outperforms state-of-the-art baselines across three LVLMs, with its dynamic variant yielding the lowest overall hallucination rates. By integrating novel mechanistic insights with a scalable intervention, this work advances the mitigation of hallucinations in LVLMs.

