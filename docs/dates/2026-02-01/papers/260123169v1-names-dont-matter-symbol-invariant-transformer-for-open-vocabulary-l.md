---
layout: default
title: Names Don't Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning
---

# Names Don't Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning
**arXiv**：[2601.23169v1](https://arxiv.org/abs/2601.23169) · [PDF](https://arxiv.org/pdf/2601.23169.pdf)  
**作者**：İlker Işık, Wenchao Li  

**一句话要点**：提出符号不变Transformer以解决开放词汇学习中不可见符号的泛化问题

**关键词**：符号不变性, 开放词汇学习, Transformer架构, 可互换符号, 泛化能力

## 3 点简述
- 核心问题：现有模型对可互换符号（如绑定变量）缺乏处理能力，导致泛化困难
- 方法要点：采用并行嵌入流和聚合注意力机制，实现符号重命名不变性
- 实验或效果：实验验证理论保证，在开放词汇任务上显著提升性能

## 摘要（原文）

> Current neural architectures lack a principled way to handle interchangeable tokens, i.e., symbols that are semantically equivalent yet distinguishable, such as bound variables. As a result, models trained on fixed vocabularies often struggle to generalize to unseen symbols, even when the underlying semantics remain unchanged. We propose a novel Transformer-based mechanism that is provably invariant to the renaming of interchangeable tokens. Our approach employs parallel embedding streams to isolate the contribution of each interchangeable token in the input, combined with an aggregated attention mechanism that enables structured information sharing across streams. Experimental results confirm the theoretical guarantees of our method and demonstrate substantial performance gains on open-vocabulary tasks that require generalization to novel symbols.

