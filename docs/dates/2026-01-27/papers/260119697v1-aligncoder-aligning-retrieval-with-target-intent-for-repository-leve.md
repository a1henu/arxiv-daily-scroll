---
layout: default
title: AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion
---

# AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion
**arXiv**：[2601.19697v1](https://arxiv.org/abs/2601.19697) · [PDF](https://arxiv.org/pdf/2601.19697.pdf)  
**作者**：Tianyue Jiang, Yanli Wang, Yanlin Wang, Daya Guo, Ensheng Shi, Yuchi Ma, Jiachi Chen, Zibin Zheng  

**一句话要点**：提出AlignCoder框架，通过查询增强和强化学习训练检索器，以解决仓库级代码补全中检索与目标意图不对齐的问题。

**关键词**：仓库级代码补全, 检索增强生成, 查询增强, 强化学习训练, 代码大语言模型, 语义对齐

## 3 点简述
- 核心问题：现有检索增强方法在仓库级代码补全中存在查询与目标代码语义不对齐，且无法有效利用推理信息。
- 方法要点：引入查询增强机制生成候选补全以构建增强查询，并采用强化学习训练AlignRetriever以提升检索准确性。
- 实验或效果：在CrossCodeEval和RepoEval基准上评估，相比基线在CrossCodeEval上EM分数提升18.1%，展现高泛化性。

## 摘要（原文）

> Repository-level code completion remains a challenging task for existing code large language models (code LLMs) due to their limited understanding of repository-specific context and domain knowledge. While retrieval-augmented generation (RAG) approaches have shown promise by retrieving relevant code snippets as cross-file context, they suffer from two fundamental problems: misalignment between the query and the target code in the retrieval process, and the inability of existing retrieval methods to effectively utilize the inference information. To address these challenges, we propose AlignCoder, a repository-level code completion framework that introduces a query enhancement mechanism and a reinforcement learning based retriever training method. Our approach generates multiple candidate completions to construct an enhanced query that bridges the semantic gap between the initial query and the target code. Additionally, we employ reinforcement learning to train an AlignRetriever that learns to leverage inference information in the enhanced query for more accurate retrieval. We evaluate AlignCoder on two widely-used benchmarks (CrossCodeEval and RepoEval) across five backbone code LLMs, demonstrating an 18.1% improvement in EM score compared to baselines on the CrossCodeEval benchmark. The results show that our framework achieves superior performance and exhibits high generalizability across various code LLMs and programming languages.

