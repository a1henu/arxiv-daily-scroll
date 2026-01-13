---
layout: default
title: Thinking Before Constraining: A Unified Decoding Framework for Large Language Models
---

# Thinking Before Constraining: A Unified Decoding Framework for Large Language Models
**arXiv**：[2601.07525v1](https://arxiv.org/abs/2601.07525) · [PDF](https://arxiv.org/pdf/2601.07525.pdf)  
**作者**：Ngoc Trinh Hung Nguyen, Alonso Silva, Laith Zumot, Liubov Tupikina, Armen Aghasaryan, Mehwish Alam  

**一句话要点**：提出触发式切换解码框架，结合自然与结构化生成以提升大语言模型推理与输出可靠性。

**关键词**：大语言模型, 解码框架, 结构化生成, 自然语言推理, 触发机制, 输出可靠性

## 3 点简述
- 核心问题：自然生成推理丰富但输出难解析，结构化生成保证格式但限制推理能力。
- 方法要点：允许模型自由推理直至触发标记，再切换至结构化生成，平衡表达与可靠性。
- 实验或效果：在分类与推理任务上评估，相比自然生成准确率提升高达27%，额外开销仅10-20个标记。

## 摘要（原文）

> Natural generation allows Language Models (LMs) to produce free-form responses with rich reasoning, but the lack of guaranteed structure makes outputs difficult to parse or verify. Structured generation, or constrained decoding, addresses this drawback by producing content in standardized formats such as JSON, ensuring consistency and guaranteed-parsable outputs, but it can inadvertently restrict the model's reasoning capabilities. In this work, we propose a simple approach that combines the advantages of both natural and structured generation. By allowing LLMs to reason freely until specific trigger tokens are generated, and then switching to structured generation, our method preserves the expressive power of natural language reasoning while ensuring the reliability of structured outputs. We further evaluate our approach on several datasets, covering both classification and reasoning tasks, to demonstrate its effectiveness, achieving a substantial gain of up to 27% in accuracy compared to natural generation, while requiring only a small overhead of 10-20 extra tokens.

