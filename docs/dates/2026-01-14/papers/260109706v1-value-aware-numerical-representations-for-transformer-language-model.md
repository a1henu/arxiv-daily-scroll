---
layout: default
title: Value-Aware Numerical Representations for Transformer Language Models
---

# Value-Aware Numerical Representations for Transformer Language Models
**arXiv**：[2601.09706v1](https://arxiv.org/abs/2601.09706) · [PDF](https://arxiv.org/pdf/2601.09706.pdf)  
**作者**：Andreea Dutulescu, Stefan Ruseti, Mihai Dascalu  

**一句话要点**：提出值感知数值表示以增强Transformer语言模型的数值理解能力

**关键词**：数值表示, Transformer模型, 算术任务, 语言模型鲁棒性, 前缀令牌嵌入

## 3 点简述
- 核心问题：Transformer模型将数字作为符号处理，嵌入不编码数值，导致数值理解错误
- 方法要点：通过前缀令牌嵌入数值信息，兼容现有分词器和解码器架构
- 实验或效果：在算术任务中优于基线，提升数值鲁棒性

## 摘要（原文）

> Transformer-based language models often achieve strong results on mathematical reasoning benchmarks while remaining fragile on basic numerical understanding and arithmetic operations. A central limitation is that numbers are processed as symbolic tokens whose embeddings do not explicitly encode numerical value, leading to systematic errors. We introduce a value-aware numerical representation that augments standard tokenized inputs with a dedicated prefix token whose embedding is explicitly conditioned on the underlying numerical value. This mechanism injects magnitude information directly into the model's input space while remaining compatible with existing tokenizers and decoder-only Transformer architectures. Evaluation on arithmetic tasks shows that the proposed approach outperforms baselines across numerical formats, tasks, and operand lengths. These results indicate that explicitly encoding numerical value is an effective and efficient way to improve fundamental numerical robustness in language models.

