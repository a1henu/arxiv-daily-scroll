---
layout: default
title: CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs
---

# CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs
**arXiv**：[2602.05258v1](https://arxiv.org/abs/2602.05258) · [PDF](https://arxiv.org/pdf/2602.05258.pdf)  
**作者**：Haoran Li, Sucheng Ren, Alan Yuille, Feng Wang  

**一句话要点**：提出CoPE方法，通过软截断RoPE低频分量以提升大语言模型的长上下文扩展能力。

**关键词**：长上下文扩展, 旋转位置编码, 软截断策略, 分布外缓解, 语义建模, 大语言模型

## 3 点简述
- 核心问题：RoPE在长上下文扩展中存在分布外异常和语义信号不精问题。
- 方法要点：采用软截断策略处理RoPE低频分量，统一缓解分布外异常并优化语义建模。
- 实验或效果：实验显示CoPE在长达256k上下文长度下显著提升性能，成为新SOTA。

## 摘要（原文）

> Rotary Positional Embedding (RoPE) is a key component of context scaling in Large Language Models (LLMs). While various methods have been proposed to adapt RoPE to longer contexts, their guiding principles generally fall into two categories: (1) out-of-distribution (OOD) mitigation, which scales RoPE frequencies to accommodate unseen positions, and (2) Semantic Modeling, which posits that the attention scores computed with RoPE should always prioritize semantically similar tokens. In this work, we unify these seemingly distinct objectives through a minimalist intervention, namely CoPE: soft clipping lowfrequency components of RoPE. CoPE not only eliminates OOD outliers and refines semantic signals, but also prevents spectral leakage caused by hard clipping. Extensive experiments demonstrate that simply applying our soft clipping strategy to RoPE yields significant performance gains that scale up to 256k context length, validating our theoretical analysis and establishing CoPE as a new state-of-the-art for length generalization. Our code, data, and models are available at https://github.com/hrlics/CoPE.

