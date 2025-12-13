---
layout: default
title: Causal Reasoning Favors Encoders: On The Limits of Decoder-Only Models
---

# Causal Reasoning Favors Encoders: On The Limits of Decoder-Only Models
**arXiv**：[2512.10561v1](https://arxiv.org/abs/2512.10561) · [PDF](https://arxiv.org/pdf/2512.10561.pdf)  
**作者**：Amartya Roy, Elamparithy M, Kripabandhu Ghosh, Ponnurangam Kumaraguru, Adrian de Wynter  

**一句话要点**：比较编码器与解码器模型在因果推理中的性能，发现编码器架构更稳健

**关键词**：因果推理, 上下文学习, 编码器解码器架构, 微调, 分布偏移, 多跳推理

## 3 点简述
- 研究因果推理中上下文学习的不足，强调多跳组合和严格合取控制的需求
- 假设编码器架构因潜在空间投影能力更适合因果推理，通过微调实验验证
- 实验显示解码器模型对分布偏移脆弱，编码器模型在非自然语言场景中更稳健

## 摘要（原文）

> In context learning (ICL) underpins recent advances in large language models (LLMs), although its role and performance in causal reasoning remains unclear. Causal reasoning demands multihop composition and strict conjunctive control, and reliance on spurious lexical relations of the input could provide misleading results. We hypothesize that, due to their ability to project the input into a latent space, encoder and encoder decoder architectures are better suited for said multihop conjunctive reasoning versus decoder only models. To do this, we compare fine-tuned versions of all the aforementioned architectures with zero and few shot ICL in both natural language and non natural language scenarios. We find that ICL alone is insufficient for reliable causal reasoning, often overfocusing on irrelevant input features. In particular, decoder only models are noticeably brittle to distributional shifts, while finetuned encoder and encoder decoder models can generalize more robustly across our tests, including the non natural language split. Both architectures are only matched or surpassed by decoder only architectures at large scales. We conclude by noting that for cost effective, short horizon robust causal reasoning, encoder or encoder decoder architectures with targeted finetuning are preferable.

