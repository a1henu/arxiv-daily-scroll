---
layout: default
title: EsoLang-Bench: Evaluating Genuine Reasoning in Large Language Models via Esoteric Programming Languages
---

# EsoLang-Bench: Evaluating Genuine Reasoning in Large Language Models via Esoteric Programming Languages
**arXiv**：[2603.09678v1](https://arxiv.org/abs/2603.09678) · [PDF](https://arxiv.org/pdf/2603.09678.pdf)  
**作者**：Aman Sharma, Paras Chopra  

**一句话要点**：提出EsoLang-Bench基准，通过冷门编程语言评估大语言模型的真实推理能力。

**关键词**：大语言模型评估, 代码生成基准, 冷门编程语言, 推理能力测试, 数据污染抵抗

## 3 点简述
- 核心问题：大语言模型在代码生成基准上表现优异，但可能依赖记忆而非真实推理。
- 方法要点：使用五种冷门编程语言构建基准，减少预训练数据污染，模拟人类学习过程。
- 实验或效果：前沿模型在标准基准得分85-95%，但在冷门任务仅0-11%，显示能力差距显著。

## 摘要（原文）

> Large language models achieve near-ceiling performance on code generation benchmarks, yet these results increasingly reflect memorization rather than genuine reasoning. We introduce EsoLang-Bench, a benchmark using five esoteric programming languages (Brainfuck, Befunge-98, Whitespace, Unlambda, and Shakespeare) that lack benchmark gaming incentives due to their economic irrationality for pre-training. These languages require the same computational primitives as mainstream programming but have 1,000-100,000x fewer public repositories than Python (based on GitHub search counts). We evaluate five frontier models across five prompting strategies and find a dramatic capability gap: models achieving 85-95% on standard benchmarks score only 0-11% on equivalent esoteric tasks, with 0% accuracy beyond the Easy tier. Few-shot learning and self-reflection fail to improve performance, suggesting these techniques exploit training priors rather than enabling genuine learning. EsoLang-Bench provides the first benchmark designed to mimic human learning by acquiring new languages through documentation, interpreter feedback, and iterative experimentation, measuring transferable reasoning skills resistant to data contamination.

