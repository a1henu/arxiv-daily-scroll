---
layout: default
title: Latent Reasoning with Supervised Thinking States
---

# Latent Reasoning with Supervised Thinking States
**arXiv**：[2602.08332v1](https://arxiv.org/abs/2602.08332) · [PDF](https://arxiv.org/pdf/2602.08332.pdf)  
**作者**：Ido Amos, Avi Caciularu, Mor Geva, Amir Globerson, Jonathan Herzig, Lior Shani, Idan Szpektor  

**一句话要点**：提出Thinking States方法，在输入处理时进行推理以降低大语言模型推理成本。

**关键词**：潜在推理, 思考状态, 推理成本优化, 大语言模型, 并行化训练

## 3 点简述
- 核心问题：链式思维推理导致大语言模型生成长理性，增加推理成本。
- 方法要点：在输入处理过程中生成思考令牌，转换为嵌入空间并添加到后续输入。
- 实验或效果：在数学问题和2-Hop QA上优于其他潜在推理方法，缩小与链式思维的差距。

## 摘要（原文）

> Reasoning with a chain-of-thought (CoT) enables Large Language Models (LLMs) to solve complex tasks but incurs significant inference costs due to the generation of long rationales. We propose Thinking States, a method that performs reasoning {\em while} the input is processing. Specifically, Thinking States generates sequences of thinking tokens every few input tokens, transforms the thoughts back into embedding space, and adds them to the following input tokens. This has two key advantages. First, it captures the recurrent nature of CoT, but where the thought tokens are generated as input is processing. Second, since the thoughts are represented as tokens, they can be learned from natural language supervision, and using teacher-forcing, which is parallelizable. Empirically, Thinking States outperforms other latent reasoning methods on multiple reasoning tasks, narrowing the gap to CoT on math problems, and matching its performance on 2-Hop QA with improved latency. On state-tracking tasks, we show Thinking States leads to stronger reasoning behavior than CoT, successfully extrapolating to longer sequences than seen during training.

