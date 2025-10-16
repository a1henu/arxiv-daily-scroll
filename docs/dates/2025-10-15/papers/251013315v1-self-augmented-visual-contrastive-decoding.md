---
layout: default
title: Self-Augmented Visual Contrastive Decoding
---

# Self-Augmented Visual Contrastive Decoding
**arXiv**：[2510.13315v1](https://arxiv.org/abs/2510.13315) · [PDF](https://arxiv.org/pdf/2510.13315.pdf)  
**作者**：Eun Woo Im, Muhammad Kashif Ali, Vivek Gupta  

**一句话要点**：提出自增强视觉对比解码策略，以解决大型视觉语言模型幻觉问题

**关键词**：大型视觉语言模型, 视觉对比解码, 自增强提示, 自适应阈值, 事实一致性, 解码策略

## 3 点简述
- 核心问题：大型视觉语言模型继承语言模型幻觉倾向，现有视觉对比解码方法忽视文本查询上下文
- 方法要点：采用自增强提示策略动态对齐语义，自适应阈值算法调整候选令牌大小
- 实验或效果：在四个模型和七个基准测试中显著提升事实一致性，优于先进方法

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have demonstrated remarkable multimodal
> capabilities, but they inherit the tendency to hallucinate from their
> underlying language models. While visual contrastive decoding has been proposed
> to mitigate this issue, existing methods often apply generic visual
> augmentations that disregard the specific context provided by the text query,
> limiting their effectiveness. This study introduces a novel training-free
> decoding strategy that addresses these limitations, featuring two key
> contributions. First, a self-augmentation prompting strategy that leverages the
> intrinsic knowledge of the model to dynamically align semantics between the
> query and the visual augmentation. Second, an adaptive thresholding algorithm
> that adaptively adjusts next token candidate size based on the output sparsity,
> utilizing full information from the logit distribution. Extensive experiments
> across four LVLMs and seven benchmarks demonstrate that the proposed decoding
> significantly enhances factual consistency compared to state-of-the-art
> decoding methods. This work highlights the importance of integrating
> query-dependent augmentation and entropy-aware decoding for improving effective
> generation of LVLMs.

