---
layout: default
title: On the Semantic and Syntactic Information Encoded in Proto-Tokens for One-Step Text Reconstruction
---

# On the Semantic and Syntactic Information Encoded in Proto-Tokens for One-Step Text Reconstruction
**arXiv**：[2602.18301v1](https://arxiv.org/abs/2602.18301) · [PDF](https://arxiv.org/pdf/2602.18301.pdf)  
**作者**：Ivan Bondarenko, Egor Palkin, Fedor Tikunov  

**一句话要点**：分析LLM中proto-tokens的语义与句法信息，探索非自回归文本重建的可行性

**关键词**：proto-tokens分析, 非自回归文本重建, 语义句法解耦, 注意力可视化, 关系蒸馏, LLM潜在能力

## 3 点简述
- 研究LLM中两个proto-tokens如何编码语义和句法信息，以超越自回归生成范式
- 通过实验分析proto-tokens的稳定性、注意力模式，并测试正则化方案
- 结果表明m-token更偏向语义信息，关系蒸馏能保持重建质量并转移语义关系

## 摘要（原文）

> Autoregressive large language models (LLMs) generate text token-by-token, requiring n forward passes to produce a sequence of length n. Recent work, Exploring the Latent Capacity of LLMs for One-Step Text Reconstruction (Mezentsev and Oseledets), shows that frozen LLMs can reconstruct hundreds of tokens from only two learned proto-tokens in a single forward pass, suggesting a path beyond the autoregressive paradigm. In this paper, we study what information these proto-tokens encode and how they behave under reconstruction and controlled constraints. We perform a series of experiments aimed at disentangling semantic and syntactic content in the two proto-tokens, analyzing stability properties of the e-token, and visualizing attention patterns to the e-token during reconstruction. Finally, we test two regularization schemes for "imposing" semantic structure on the e-token using teacher embeddings, including an anchor-based loss and a relational distillation objective. Our results indicate that the m-token tends to capture semantic information more strongly than the e-token under standard optimization; anchor-based constraints trade off sharply with reconstruction accuracy; and relational distillation can transfer batch-level semantic relations into the proto-token space without sacrificing reconstruction quality, supporting the feasibility of future non-autoregressive seq2seq systems that predict proto-tokens as an intermediate representation.

