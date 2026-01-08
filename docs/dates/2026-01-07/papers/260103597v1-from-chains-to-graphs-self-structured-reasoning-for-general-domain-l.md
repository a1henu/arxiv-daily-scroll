---
layout: default
title: From Chains to Graphs: Self-Structured Reasoning for General-Domain LLMs
---

# From Chains to Graphs: Self-Structured Reasoning for General-Domain LLMs
**arXiv**：[2601.03597v1](https://arxiv.org/abs/2601.03597) · [PDF](https://arxiv.org/pdf/2601.03597.pdf)  
**作者**：Yingjian Chen, Haoran Liu, Yinhong Liu, Sherry T. Tong, Aosong Feng, Jinghui Lu, Juntao Zhang, Yusuke Iwasawa, Yutaka Matsuo, Irene Li  

**一句话要点**：提出自图推理框架以提升大语言模型在开放域问答中的推理一致性与性能

**关键词**：自图推理, 结构化推理, 开放域问答, 大语言模型, 推理一致性

## 3 点简述
- 核心问题：大语言模型推理过程线性且逻辑不一致，难以处理并行子问题。
- 方法要点：自图推理框架使模型将推理过程显式表示为结构化图，并构建图结构数据集进行训练。
- 实验或效果：在五个基准测试中提升推理一致性，性能增益达17.74%，媲美GPT-4o。

## 摘要（原文）

> Large Language Models (LLMs) show strong reasoning ability in open-domain question answering, yet their reasoning processes are typically linear and often logically inconsistent. In contrast, real-world reasoning requires integrating multiple premises and solving subproblems in parallel. Existing methods, such as Chain-of-Thought (CoT), express reasoning in a linear textual form, which may appear coherent but frequently leads to inconsistent conclusions. Recent approaches rely on externally provided graphs and do not explore how LLMs can construct and use their own graph-structured reasoning, particularly in open-domain QA. To fill this gap, we novelly explore graph-structured reasoning of LLMs in general-domain question answering. We propose Self-Graph Reasoning (SGR), a framework that enables LLMs to explicitly represent their reasoning process as a structured graph before producing the final answer. We further construct a graph-structured reasoning dataset that merges multiple candidate reasoning graphs into refined graph structures for model training. Experiments on five QA benchmarks across both general and specialized domains show that SGR consistently improves reasoning consistency and yields a 17.74% gain over the base model. The LLaMA-3.3-70B model fine-tuned with SGR performs comparably to GPT-4o and surpasses Claude-3.5-Haiku, demonstrating the effectiveness of graph-structured reasoning.

