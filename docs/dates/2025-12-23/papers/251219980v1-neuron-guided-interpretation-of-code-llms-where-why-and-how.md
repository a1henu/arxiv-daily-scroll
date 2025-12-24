---
layout: default
title: Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?
---

# Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?
**arXiv**：[2512.19980v1](https://arxiv.org/abs/2512.19980) · [PDF](https://arxiv.org/pdf/2512.19980.pdf)  
**作者**：Zhe Yin, Xiaodong Gu, Beijun Shen  

**一句话要点**：提出神经元引导解释方法，以分析代码大语言模型的多语言内部机制并提升下游任务性能。

**关键词**：代码大语言模型, 神经元解释性, 多语言代码分析, 概念层, 代码生成, 克隆检测

## 3 点简述
- 核心问题：现有NLP神经元解释技术不适用于代码，因编程语言具有形式化、层次化和可执行性。
- 方法要点：在神经元层面定位语言特定神经元和概念层，分析多语言输入下的选择性和层贡献。
- 实验或效果：在代码生成、克隆检测和代码摘要任务中，应用神经元引导方法获得一致性能提升。

## 摘要（原文）

> Code language models excel on code intelligence tasks, yet their internal interpretability is underexplored. Existing neuron interpretability techniques from NLP are suboptimal for source code due to programming languages formal, hierarchical, and executable nature. We empirically investigate code LLMs at the neuron level, localizing language-specific neurons (selectively responsive to one language) and concept layers (feed-forward layers encoding language-agnostic code representations). We analyze Llama-3.1-8B and Qwen2.5-Coder-32B on multilingual inputs in C++, Java, Python, Go, and JavaScript, measuring neuron selectivity and layerwise contributions during generation. We find (1) neurons specialized for individual languages alongside a universal subset supporting general-purpose generation; and (2) lower layers mainly encode language-specific syntax, while middle layers capture semantic abstractions shared across languages, emerging as concept layers. We demonstrate utility on three tasks: neuron-guided fine-tuning for code generation, clone detection via concept-layer embeddings, and concept-layer-guided transfer for code summarization, each yielding consistent gains in multilingual settings.

