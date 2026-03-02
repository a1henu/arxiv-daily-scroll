---
layout: default
title: LLM-Driven Multi-Turn Task-Oriented Dialogue Synthesis for Realistic Reasoning
---

# LLM-Driven Multi-Turn Task-Oriented Dialogue Synthesis for Realistic Reasoning
**arXiv**：[2602.23610v1](https://arxiv.org/abs/2602.23610) · [PDF](https://arxiv.org/pdf/2602.23610.pdf)  
**作者**：Yu Zhu, Kai Yang  

**一句话要点**：提出LLM驱动的多轮任务导向对话合成框架，以解决现实推理场景中数据集不足的问题。

**关键词**：任务导向对话, 大语言模型推理, 数据集合成, 多轮对话生成, 现实场景建模

## 3 点简述
- 现有基准数据集过于简化，脱离现实任务流和领域约束，限制LLM推理能力评估。
- 采用LLM驱动框架，结合三层优化合成基于真实场景的多轮对话，增强上下文连贯性。
- 实验表明合成数据引入非平凡推理挑战，有效支持LLM推理能力提升。

## 摘要（原文）

> The reasoning capability of large language models (LLMs), defined as their ability to analyze, infer, and make decisions based on input information, is essential for building intelligent task-oriented dialogue systems. However, existing benchmarks do not sufficiently reflect the complexity of real-world scenarios, which limits their effectiveness in evaluating and enhancing LLM reasoning in practical contexts. Many current reasoning datasets are overly simplistic and abstract, often disconnected from realistic task flows, domain constraints, and operational rules, making it difficult to effectively evaluate LLMs' logical reasoning ability. In addition, data contamination from pretraining corpora undermines the reliability of evaluation results, and traditional crowdsourcing methods for dataset construction are labor-intensive and difficult to scale. To address these challenges, we propose a LLM-driven framework for synthesizing multi-turn, task-oriented dialogues grounded in realistic reasoning scenarios, leveraging trilevel optimization to enhance dialogue quality. Our method generates dialogues grounded in authentic task scenarios, enriched with real-world information, and exhibiting strong contextual coherence. Corresponding reasoning tasks are carefully designed around these dialogues and iteratively refined to continuously improve the tasks' quality and challenge. The resulting dataset serves as a valuable benchmark for assessing and advancing the realistic logical reasoning capabilities of LLMs. Experimental results show that our synthetic data-based reasoning tasks introduce non-trivial reasoning challenges and provide meaningful support for improving the reasoning capabilities of LLMs.

