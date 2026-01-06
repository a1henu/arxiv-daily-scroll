---
layout: default
title: Context-Free Recognition with Transformers
---

# Context-Free Recognition with Transformers
**arXiv**：[2601.01754v1](https://arxiv.org/abs/2601.01754) · [PDF](https://arxiv.org/pdf/2601.01754.pdf)  
**作者**：Selim Jerad, Anej Svete, Sophie Hao, Ryan Cotterell, William Merrill  

**一句话要点**：提出循环Transformer以O(log n)层和O(n^6)填充识别上下文无关语言，但自然子类如无歧义CFL仅需O(n^3)填充。

**关键词**：Transformer模型, 上下文无关语言识别, 循环层, 填充令牌, 无歧义语法, 计算复杂度

## 3 点简述
- 核心问题：标准Transformer无法识别上下文无关语言，需探索其语法处理能力。
- 方法要点：通过O(log n)循环层和O(n^6)填充实现CFL识别，无歧义CFL仅需O(n^3)填充。
- 实验或效果：实证验证循环机制在需对数深度的语言上有效，揭示CFL识别复杂性。

## 摘要（原文）

> Transformers excel on tasks that process well-formed inputs according to some grammar, such as natural language and code. However, it remains unclear how they can process grammatical syntax. In fact, under standard complexity conjectures, standard transformers cannot recognize context-free languages (CFLs), a canonical formalism to describe syntax, or even regular languages, a subclass of CFLs (Merrill et al., 2022). Merrill & Sabharwal (2024) show that $\mathcal{O}(\log n)$ looping layers (w.r.t. input length $n$) allows transformers to recognize regular languages, but the question of context-free recognition remained open. In this work, we show that looped transformers with $\mathcal{O}(\log n)$ looping layers and $\mathcal{O}(n^6)$ padding tokens can recognize all CFLs. However, training and inference with $\mathcal{O}(n^6)$ padding tokens is potentially impractical. Fortunately, we show that, for natural subclasses such as unambiguous CFLs, the recognition problem on transformers becomes more tractable, requiring $\mathcal{O}(n^3)$ padding. We empirically validate our results and show that looping helps on a language that provably requires logarithmic depth. Overall, our results shed light on the intricacy of CFL recognition by transformers: While general recognition may require an intractable amount of padding, natural constraints such as unambiguity yield efficient recognition algorithms.

