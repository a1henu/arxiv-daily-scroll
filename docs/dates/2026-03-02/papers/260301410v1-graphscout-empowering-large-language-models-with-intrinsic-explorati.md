---
layout: default
title: GraphScout: Empowering Large Language Models with Intrinsic Exploration Ability for Agentic Graph Reasoning
---

# GraphScout: Empowering Large Language Models with Intrinsic Exploration Ability for Agentic Graph Reasoning
**arXiv**：[2603.01410v1](https://arxiv.org/abs/2603.01410) · [PDF](https://arxiv.org/pdf/2603.01410.pdf)  
**作者**：Yuchen Ying, Weiqi Jiang, Tongya Zheng, Yu Wang, Shunyu Liu, Kaixuan Chen, Mingli Song  

**一句话要点**：提出GraphScout框架，通过自主探索知识图谱增强大语言模型的图推理能力。

**关键词**：知识图谱推理, 检索增强生成, 自主探索, 训练数据合成, 跨领域迁移

## 3 点简述
- 现有GraphRAG方法依赖人工指导和预定义工具，限制了图探索的灵活性。
- GraphScout引入灵活工具，使模型能自主交互知识图谱以合成训练数据，无需人工标注。
- 实验表明，小模型增强后性能超越基线大模型，且具有跨领域迁移鲁棒性。

## 摘要（原文）

> Knowledge graphs provide structured and reliable information for many real-world applications, motivating increasing interest in combining large language models (LLMs) with graph-based retrieval to improve factual grounding. Recent Graph-based Retrieval-Augmented Generation (GraphRAG) methods therefore introduce iterative interaction between LLMs and knowledge graphs to enhance reasoning capability. However, existing approaches typically depend on manually designed guidance and interact with knowledge graphs through a limited set of predefined tools, which substantially constrains graph exploration. To address these limitations, we propose GraphScout, a training-centric agentic graph reasoning framework equipped with more flexible graph exploration tools. GraphScout enables models to autonomously interact with knowledge graphs to synthesize structured training data which are then used to post-train LLMs, thereby internalizing agentic graph reasoning ability without laborious manual annotation or task curation. Extensive experiments across five knowledge-graph domains show that a small model (e.g., Qwen3-4B) augmented with GraphScout outperforms baseline methods built on leading LLMs (e.g., Qwen-Max) by an average of 16.7\% while requiring significantly fewer inference tokens. Moreover, GraphScout exhibits robust cross-domain transfer performance. Our code will be made publicly available~\footnote{https://github.com/Ying-Yuchen/_GraphScout_}.

