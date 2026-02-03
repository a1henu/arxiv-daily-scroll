---
layout: default
title: Fat-Cat: Document-Driven Metacognitive Multi-Agent System for Complex Reasoning
---

# Fat-Cat: Document-Driven Metacognitive Multi-Agent System for Complex Reasoning
**arXiv**：[2602.02206v1](https://arxiv.org/abs/2602.02206) · [PDF](https://arxiv.org/pdf/2602.02206.pdf)  
**作者**：Tong Yang, Yemin Wang, Chaoning Zhang, Aming Wu  

**一句话要点**：提出Fat-Cat文档驱动多智能体系统，以提升复杂推理中状态管理的信噪比。

**关键词**：文档驱动智能体, 状态管理优化, 语义文件系统, 文本策略演进, 复杂推理, 多智能体系统

## 3 点简述
- 核心问题：现有智能体框架依赖刚性JSON状态表示，导致模型注意力浪费于语法处理而非语义推理。
- 方法要点：集成语义文件系统、文本策略演进和闭环监控器，将状态表示为Markdown文档以优化信息利用。
- 实验或效果：在推理、检索和编码基准测试中表现优异，使Kimi-k2模型在HotPotQA上超越GPT-4o基线。

## 摘要（原文）

> The effectiveness of LLM-based agents is often limited not by model capacity alone, but by how efficiently contextual information is utilized at runtime. Existing agent frameworks rely on rigid, syntax-heavy state representations such as nested JSON, which require models to devote a substantial portion of their limited attention to syntactic processing rather than semantic reasoning. In this paper, we propose Fat-Cat, a document-driven agent architecture that improves the signal-to-noise ratio of state management. By integrating three key components: (1) a Semantic File System that represents agent state as Markdown documents aligned with common pre-training corpora, (2) a Textual Strategy Evolution module that accumulates task-solving knowledge without parameter updates, and (3) a Closed-Loop Watcher that monitors reasoning trajectories to reduce hallucinations. Extensive reasoning, retrieval, and coding benchmarks, Fat-Cat consistently improves agent performance. It enables the Kimi-k2 model to outperform the proprietary GPT-4o baseline on HotPotQA. Replacing the document-based state with JSON leads to performance drop, while empirically validating the critical necessity of document-driven state modeling over rigid syntax. The code is available at https://github.com/answeryt/Fat-Cat.

