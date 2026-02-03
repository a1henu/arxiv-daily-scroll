---
layout: default
title: Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models
---

# Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models
**arXiv**：[2602.02462v1](https://arxiv.org/abs/2602.02462) · [PDF](https://arxiv.org/pdf/2602.02462.pdf)  
**作者**：Gabriele Maraia, Marco Valentino, Fabio Massimo Zanzotto, Leonardo Ranaldi  

**一句话要点**：提出抽象激活空间框架以减轻大语言模型在形式推理中的语义干扰

**关键词**：大语言模型, 形式推理, 语义干扰, 抽象激活空间, 跨语言迁移, 模型干预

## 3 点简述
- 大语言模型在演绎推理中常混淆语义合理性与形式有效性，即内容效应问题
- 通过构建抽象推理空间和轻量级抽象器，在模型前向传播中进行多层干预
- 实验显示该方法减少内容驱动错误，提升跨语言推理的稳健性

## 摘要（原文）

> Large Language Models (LLMs) often struggle with deductive judgment in syllogistic reasoning, systematically conflating semantic plausibility with formal validity a phenomenon known as content effect. This bias persists even when models generate step-wise explanations, indicating that intermediate rationales may inherit the same semantic shortcuts that affect answers. Recent approaches propose mitigating this issue by increasing inference-time structural constraints, either by encouraging abstract intermediate representations or by intervening directly in the model's internal computations; however, reliably suppressing semantic interference remains an open challenge. To make formal deduction less sensitive to semantic content, we introduce a framework for abstraction-guided reasoning that explicitly separates structural inference from lexical semantics. We construct paired content-laden and abstract syllogisms and use the model's activations on abstract inputs to define an abstract reasoning space. We then learn lightweight Abstractors that, from content-conditioned residual-stream states, predict representations aligned with this space and integrate these predictions via multi-layer interventions during the forward pass. Using cross-lingual transfer as a test bed, we show that abstraction-aligned steering reduces content-driven errors and improves validity-sensitive performance. Our results position activation-level abstraction as a scalable mechanism for enhancing the robustness of formal reasoning in LLMs against semantic interference.

