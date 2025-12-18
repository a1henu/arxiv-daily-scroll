---
layout: default
title: Explaining the Reasoning of Large Language Models Using Attribution Graphs
---

# Explaining the Reasoning of Large Language Models Using Attribution Graphs
**arXiv**：[2512.15663v1](https://arxiv.org/abs/2512.15663) · [PDF](https://arxiv.org/pdf/2512.15663.pdf)  
**作者**：Chase Walker, Rickard Ewetz  

**一句话要点**：提出CAGE框架以解决大语言模型推理解释中忽略代际影响的问题

**关键词**：大语言模型解释, 上下文归因, 归因图, 推理透明度, 忠实度评估

## 3 点简述
- 核心问题：现有上下文归因方法忽略生成代际影响，导致解释不完整
- 方法要点：引入归因图量化提示和所有先前生成对当前生成的影响
- 实验或效果：CAGE提升上下文归因忠实度，平均增益达40%

## 摘要（原文）

> Large language models (LLMs) exhibit remarkable capabilities, yet their reasoning remains opaque, raising safety and trust concerns. Attribution methods, which assign credit to input features, have proven effective for explaining the decision making of computer vision models. From these, context attributions have emerged as a promising approach for explaining the behavior of autoregressive LLMs. However, current context attributions produce incomplete explanations by directly relating generated tokens to the prompt, discarding inter-generational influence in the process. To overcome these shortcomings, we introduce the Context Attribution via Graph Explanations (CAGE) framework. CAGE introduces an attribution graph: a directed graph that quantifies how each generation is influenced by both the prompt and all prior generations. The graph is constructed to preserve two properties-causality and row stochasticity. The attribution graph allows context attributions to be computed by marginalizing intermediate contributions along paths in the graph. Across multiple models, datasets, metrics, and methods, CAGE improves context attribution faithfulness, achieving average gains of up to 40%.

