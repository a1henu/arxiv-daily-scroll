---
layout: default
title: Recursive Language Models
---

# Recursive Language Models
**arXiv**：[2512.24601v1](https://arxiv.org/abs/2512.24601) · [PDF](https://arxiv.org/pdf/2512.24601.pdf)  
**作者**：Alex L. Zhang, Tim Kraska, Omar Khattab  

**一句话要点**：提出递归语言模型以处理超长提示，通过推理时扩展提升大语言模型性能。

**关键词**：递归语言模型, 长上下文处理, 推理时扩展, 大语言模型, 提示分解

## 3 点简述
- 核心问题：大语言模型受限于上下文窗口，难以处理超长提示。
- 方法要点：将长提示视为外部环境，通过编程方式分解并递归调用模型处理片段。
- 实验或效果：在四个长上下文任务中，处理能力提升两个数量级，性能显著优于基线模型，成本相当或更低。

## 摘要（原文）

> We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference strategy that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt. We find that RLMs successfully handle inputs up to two orders of magnitude beyond model context windows and, even for shorter prompts, dramatically outperform the quality of base LLMs and common long-context scaffolds across four diverse long-context tasks, while having comparable (or cheaper) cost per query.

