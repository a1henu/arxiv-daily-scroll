---
layout: default
title: ToolWeaver: Weaving Collaborative Semantics for Scalable Tool Use in Large Language Models
---

# ToolWeaver: Weaving Collaborative Semantics for Scalable Tool Use in Large Language Models
**arXiv**：[2601.21947v1](https://arxiv.org/abs/2601.21947) · [PDF](https://arxiv.org/pdf/2601.21947.pdf)  
**作者**：Bowen Fang, Wen Ye, Yunyue Su, Jinghao Zhang, Qiang Liu, Yesheng Liu, Xin Sun, Shu Wu, Jiabing Yang, Baole Wei, Liang Wang  

**一句话要点**：提出ToolWeaver框架，通过分层编码解决大语言模型工具使用的可扩展性与语义协作问题。

**关键词**：大语言模型, 工具使用, 分层编码, 语义协作, 可扩展性, 生成式方法

## 3 点简述
- 核心问题：检索式方法语义捕获不足，生成式方法因工具ID独立编码导致可扩展性差和语义协作瓶颈。
- 方法要点：将工具编码为分层序列，使词汇扩展对数增长，并基于共享代码的密集共现学习协作模式。
- 实验或效果：在近47,000个工具上评估，显著优于现有方法，提升可扩展性、泛化性和语义感知能力。

## 摘要（原文）

> Prevalent retrieval-based tool-use pipelines struggle with a dual semantic challenge: their retrievers often employ encoders that fail to capture complex semantics, while the Large Language Model (LLM) itself lacks intrinsic tool knowledge from its natural language pretraining. Generative methods offer a powerful alternative by unifying selection and execution, tasking the LLM to directly learn and generate tool identifiers. However, the common practice of mapping each tool to a unique new token introduces substantial limitations: it creates a scalability and generalization crisis, as the vocabulary size explodes and each tool is assigned a semantically isolated token. This approach also creates a semantic bottleneck that hinders the learning of collaborative tool relationships, as the model must infer them from sparse co-occurrences of monolithic tool IDs within a vast library. To address these limitations, we propose ToolWeaver, a novel generative tool learning framework that encodes tools into hierarchical sequences. This approach makes vocabulary expansion logarithmic to the number of tools. Crucially, it enables the model to learn collaborative patterns from the dense co-occurrence of shared codes, rather than the sparse co-occurrence of monolithic tool IDs. We generate these structured codes through a novel tokenization process designed to weave together a tool's intrinsic semantics with its extrinsic co-usage patterns. These structured codes are then integrated into the LLM through a generative alignment stage, where the model is fine-tuned to produce the hierarchical code sequences. Evaluation results with nearly 47,000 tools show that ToolWeaver significantly outperforms state-of-the-art methods, establishing a more scalable, generalizable, and semantically-aware foundation for advanced tool-augmented agents.

