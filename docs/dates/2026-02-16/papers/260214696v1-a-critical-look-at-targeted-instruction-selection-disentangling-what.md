---
layout: default
title: A Critical Look at Targeted Instruction Selection: Disentangling What Matters (and What Doesn't)
---

# A Critical Look at Targeted Instruction Selection: Disentangling What Matters (and What Doesn't)
**arXiv**：[2602.14696v1](https://arxiv.org/abs/2602.14696) · [PDF](https://arxiv.org/pdf/2602.14696.pdf)  
**作者**：Nihal V. Nayak, Paula Rodriguez-Diaz, Neha Hulkund, Sara Beery, David Alvarez-Melis  

**一句话要点**：提出框架以解耦数据表示与选择算法，澄清大语言模型指令微调中的目标指令选择问题。

**关键词**：指令微调, 数据选择, 梯度基表示, 选择算法, 大语言模型, 泛化界限

## 3 点简述
- 核心问题：目标指令选择方法在文献中碎片化且不透明，缺乏实践指导。
- 方法要点：系统分析梯度基数据表示与选择算法，统一现有方法为近似距离最小化。
- 实验或效果：梯度基表示在低预算下表现最佳，但优势随预算增加减弱，提供泛化界限支持。

## 摘要（原文）

> Instruction fine-tuning of large language models (LLMs) often involves selecting a subset of instruction training data from a large candidate pool, using a small query set from the target task. Despite growing interest, the literature on targeted instruction selection remains fragmented and opaque: methods vary widely in selection budgets, often omit zero-shot baselines, and frequently entangle the contributions of key components. As a result, practitioners lack actionable guidance on selecting instructions for their target tasks. In this work, we aim to bring clarity to this landscape by disentangling and systematically analyzing the two core ingredients: data representation and selection algorithms. Our framework enables controlled comparisons across models, tasks, and budgets. We find that only gradient-based data representations choose subsets whose similarity to the query consistently predicts performance across datasets and models. While no single method dominates, gradient-based representations paired with a greedy round-robin selection algorithm tend to perform best on average at low budgets, but these benefits diminish at larger budgets. Finally, we unify several existing selection algorithms as forms of approximate distance minimization between the selected subset and the query set, and support this view with new generalization bounds. More broadly, our findings provide critical insights and a foundation for more principled data selection in LLM fine-tuning. The code is available at https://github.com/dcml-lab/targeted-instruction-selection.

