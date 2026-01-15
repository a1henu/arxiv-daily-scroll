---
layout: default
title: SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding
---

# SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding
**arXiv**：[2601.09089v1](https://arxiv.org/abs/2601.09089) · [PDF](https://arxiv.org/pdf/2601.09089.pdf)  
**作者**：Shuyang Hou, Yi Hu, Muhan Zhang  

**一句话要点**：提出SubTokenTest基准以评估大语言模型在实用场景中的子词理解能力

**关键词**：子词理解, 基准测试, 大语言模型, 分词过程, 字符级任务, 实用评估

## 3 点简述
- 核心问题：大语言模型在字符级任务上表现不佳，源于分词过程，但现有基准缺乏实际相关性
- 方法要点：通过实用任务评估子词理解，涵盖四个领域十个任务，隔离分词相关失败
- 实验或效果：评估九个先进模型，研究测试时缩放影响和隐藏状态中字符级信息编码

## 摘要（原文）

> Recent advancements in large language models (LLMs) have significantly enhanced their reasoning capabilities. However, they continue to struggle with basic character-level tasks, such as counting letters in words, a problem rooted in their tokenization process. While existing benchmarks have highlighted this weakness through basic character operations, such failures are often dismissed due to lacking practical relevance. Yet, many real-world applications, such as navigating text-based maps or interpreting structured tables, rely heavily on precise sub-token understanding. In this regard, we introduce SubTokenTest, a comprehensive benchmark that assesses sub-token understanding through practical, utility-driven tasks. Our benchmark includes ten tasks across four domains and isolates tokenization-related failures by decoupling performance from complex reasoning. We provide a comprehensive evaluation of nine advanced LLMs. Additionally, we investigate the impact of test-time scaling on sub-token reasoning and explore how character-level information is encoded within the hidden states.

