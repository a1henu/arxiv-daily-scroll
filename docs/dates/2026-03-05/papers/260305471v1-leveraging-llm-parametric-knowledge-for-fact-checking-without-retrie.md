---
layout: default
title: Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval
---

# Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval
**arXiv**：[2603.05471v1](https://arxiv.org/abs/2603.05471) · [PDF](https://arxiv.org/pdf/2603.05471.pdf)  
**作者**：Artem Vazhentsev, Maria Marina, Daniil Moskovskiy, Sergey Pletenev, Mikhail Seleznyov, Mikhail Salnikov, Elena Tutubalina, Vasily Konovalov, Irina Nikishina, Alexander Panchenko, Viktor Moskvoretskii  

**一句话要点**：提出INTRA方法，利用内部表示交互实现无检索事实核查，提升泛化性能。

**关键词**：无检索事实核查, 内部表示交互, LLM可信度, 泛化评估, 多语言处理

## 3 点简述
- 核心问题：基于检索的事实核查方法受限于检索错误和数据可用性，未充分利用LLM内在验证能力。
- 方法要点：引入无检索事实核查任务，通过内部表示交互设计INTRA方法，避免依赖外部知识。
- 实验或效果：在9个数据集上评估，INTRA实现最优性能，展示对长尾知识、多语言等场景的强泛化。

## 摘要（原文）

> Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the models intrinsic fact-verification capabilities largely unused. We propose the task of fact-checking without retrieval, focusing on the verification of arbitrary natural language claims, independent of their source. To study this setting, we introduce a comprehensive evaluation framework focused on generalization, testing robustness to (i) long-tail knowledge, (ii) variation in claim sources, (iii) multilinguality, and (iv) long-form generation. Across 9 datasets, 18 methods and 3 models, our experiments indicate that logit-based approaches often underperform compared to those that leverage internal model representations. Building on this finding, we introduce INTRA, a method that exploits interactions between internal representations and achieves state-of-the-art performance with strong generalization. More broadly, our work establishes fact-checking without retrieval as a promising research direction that can complement retrieval-based frameworks, improve scalability, and enable the use of such systems as reward signals during training or as components integrated into the generation process.

