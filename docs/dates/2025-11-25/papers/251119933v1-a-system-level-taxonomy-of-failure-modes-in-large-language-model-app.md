---
layout: default
title: A System-Level Taxonomy of Failure Modes in Large Language Model Applications
---

# A System-Level Taxonomy of Failure Modes in Large Language Model Applications
**arXiv**：[2511.19933v1](https://arxiv.org/abs/2511.19933) · [PDF](https://arxiv.org/pdf/2511.19933.pdf)  
**作者**：Vaishali Vinay  

**一句话要点**：提出系统级故障模式分类法以解决大语言模型应用中的可靠性问题

**关键词**：大语言模型故障模式, 系统级分类法, 可靠性设计原则, 评估监控差距, 生产部署挑战

## 3 点简述
- 核心问题：大语言模型在真实应用中存在隐藏故障模式，如推理漂移和工具调用错误
- 方法要点：构建包含15种故障模式的分类法，分析评估与监控实践的差距
- 实验或效果：未知具体实验，但提出设计原则以提升系统可靠性和成本意识

## 摘要（原文）

> Large language models (LLMs) are being rapidly integrated into decision-support tools, automation workflows, and AI-enabled software systems. However, their behavior in production environments remains poorly understood, and their failure patterns differ fundamentally from those of traditional machine learning models. This paper presents a system-level taxonomy of fifteen hidden failure modes that arise in real-world LLM applications, including multi-step reasoning drift, latent inconsistency, context-boundary degradation, incorrect tool invocation, version drift, and cost-driven performance collapse. Using this taxonomy, we analyze the growing gap in evaluation and monitoring practices: existing benchmarks measure knowledge or reasoning but provide little insight into stability, reproducibility, drift, or workflow integration. We further examine the production challenges associated with deploying LLMs - including observability limitations, cost constraints, and update-induced regressions - and outline high-level design principles for building reliable, maintainable, and cost-aware LLM systems. Finally, we outline high-level design principles for building reliable, maintainable, and cost-aware LLM-based systems. By framing LLM reliability as a system-engineering problem rather than a purely model-centric one, this work provides an analytical foundation for future research on evaluation methodology, AI system robustness, and dependable LLM deployment.

