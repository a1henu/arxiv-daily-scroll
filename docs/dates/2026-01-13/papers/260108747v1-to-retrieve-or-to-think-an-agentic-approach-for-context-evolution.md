---
layout: default
title: To Retrieve or To Think? An Agentic Approach for Context Evolution
---

# To Retrieve or To Think? An Agentic Approach for Context Evolution
**arXiv**：[2601.08747v1](https://arxiv.org/abs/2601.08747) · [PDF](https://arxiv.org/pdf/2601.08747.pdf)  
**作者**：Rubing Chen, Jian Wang, Wenjie Li, Xiao-Yong Wei, Qing Li  

**一句话要点**：提出Agentic Context Evolution框架，通过动态决策优化知识密集型推理任务中的上下文增强。

**关键词**：检索增强生成, 上下文演化, 多跳问答, 代理决策, 知识密集型推理

## 3 点简述
- 核心问题：现有检索增强方法在每一步都执行检索，导致计算成本高且上下文被无关噪声污染。
- 方法要点：引入受元认知启发的框架，使用中央协调代理通过多数投票动态决定检索或推理，交替激活检索代理和推理代理。
- 实验或效果：在挑战性多跳问答基准上，ACE在准确性和令牌消耗效率方面显著优于基线方法。

## 摘要（原文）

> Current context augmentation methods, such as retrieval-augmented generation, are essential for solving knowledge-intensive reasoning tasks.However, they typically adhere to a rigid, brute-force strategy that executes retrieval at every step. This indiscriminate approach not only incurs unnecessary computational costs but also degrades performance by saturating the context with irrelevant noise. To address these limitations, we introduce Agentic Context Evolution (ACE), a framework inspired by human metacognition that dynamically determines whether to seek new evidence or reason with existing knowledge. ACE employs a central orchestrator agent to make decisions strategically via majority voting.It aims to alternate between activating a retriever agent for external retrieval and a reasoner agent for internal analysis and refinement. By eliminating redundant retrieval steps, ACE maintains a concise and evolved context. Extensive experiments on challenging multi-hop QA benchmarks demonstrate that ACE significantly outperforms competitive baselines in accuracy while achieving efficient token consumption.Our work provides valuable insights into advancing context-evolved generation for complex, knowledge-intensive tasks.

