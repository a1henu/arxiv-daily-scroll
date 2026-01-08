---
layout: default
title: In Search of Grandmother Cells: Tracing Interpretable Neurons in Tabular Representations
---

# In Search of Grandmother Cells: Tracing Interpretable Neurons in Tabular Representations
**arXiv**：[2601.03657v1](https://arxiv.org/abs/2601.03657) · [PDF](https://arxiv.org/pdf/2601.03657.pdf)  
**作者**：Ricardo Knauer, Erik Rodner  

**一句话要点**：提出信息论度量以量化神经元对单一概念的显著性和选择性，应用于表格基础模型TabPFN。

**关键词**：祖母细胞, 神经元可解释性, 信息论度量, 表格基础模型, 显著性分析, 选择性分析

## 3 点简述
- 核心问题：探索基础模型中是否存在类似祖母细胞的神经元，即对单一概念具有内在可解释性的神经元。
- 方法要点：设计两个信息论度量，评估神经元对概念的显著性和选择性，并进行神经元-概念对的简单搜索。
- 实验或效果：在TabPFN模型中首次发现部分神经元对高级概念表现出中等、统计显著的显著性和选择性。

## 摘要（原文）

> Foundation models are powerful yet often opaque in their decision-making. A topic of continued interest in both neuroscience and artificial intelligence is whether some neurons behave like grandmother cells, i.e., neurons that are inherently interpretable because they exclusively respond to single concepts. In this work, we propose two information-theoretic measures that quantify the neuronal saliency and selectivity for single concepts. We apply these metrics to the representations of TabPFN, a tabular foundation model, and perform a simple search across neuron-concept pairs to find the most salient and selective pair. Our analysis provides the first evidence that some neurons in such models show moderate, statistically significant saliency and selectivity for high-level concepts. These findings suggest that interpretable neurons can emerge naturally and that they can, in some cases, be identified without resorting to more complex interpretability techniques.

