---
layout: default
title: Distilling the Thought, Watermarking the Answer: A Principle Semantic Guided Watermark for Large Reasoning Models
---

# Distilling the Thought, Watermarking the Answer: A Principle Semantic Guided Watermark for Large Reasoning Models
**arXiv**：[2601.05144v1](https://arxiv.org/abs/2601.05144) · [PDF](https://arxiv.org/pdf/2601.05144.pdf)  
**作者**：Shuliang Liu, Xingyu Li, Hongyi Liu, Yibo Yan, Bingchen Duan, Qi Zheng, Dong Fang, Lingfeng Su, Xuming Hu  

**一句话要点**：提出ReasonMark框架，通过解耦思维与回答阶段，为推理大模型设计语义引导水印以解决逻辑破坏与高延迟问题。

**关键词**：推理大模型水印, 语义引导水印, 逻辑完整性保护, 低延迟水印, 鲁棒水印检测

## 3 点简述
- 核心问题：现有水印方法易破坏推理大模型的逻辑连贯性或引入高计算成本。
- 方法要点：基于关键性分数提取主语义向量，指导语义自适应水印机制，确保鲁棒性。
- 实验或效果：在降低困惑度、提升翻译BLEU和数学准确率方面优于现有方法，检测AUC更高。

## 摘要（原文）

> Reasoning Large Language Models (RLLMs) excelling in complex tasks present unique challenges for digital watermarking, as existing methods often disrupt logical coherence or incur high computational costs. Token-based watermarking techniques can corrupt the reasoning flow by applying pseudo-random biases, while semantic-aware approaches improve quality but introduce significant latency or require auxiliary models. This paper introduces ReasonMark, a novel watermarking framework specifically designed for reasoning-intensive LLMs. Our approach decouples generation into an undisturbed Thinking Phase and a watermarked Answering Phase. We propose a Criticality Score to identify semantically pivotal tokens from the reasoning trace, which are distilled into a Principal Semantic Vector (PSV). The PSV then guides a semantically-adaptive mechanism that modulates watermark strength based on token-PSV alignment, ensuring robustness without compromising logical integrity. Extensive experiments show ReasonMark surpasses state-of-the-art methods by reducing text Perplexity by 0.35, increasing translation BLEU score by 0.164, and raising mathematical accuracy by 0.67 points. These advancements are achieved alongside a 0.34% higher watermark detection AUC and stronger robustness to attacks, all with a negligible increase in latency. This work enables the traceable and trustworthy deployment of reasoning LLMs in real-world applications.

