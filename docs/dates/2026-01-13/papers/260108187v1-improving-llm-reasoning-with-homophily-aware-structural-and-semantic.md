---
layout: default
title: Improving LLM Reasoning with Homophily-aware Structural and Semantic Text-Attributed Graph Compression
---

# Improving LLM Reasoning with Homophily-aware Structural and Semantic Text-Attributed Graph Compression
**arXiv**：[2601.08187v1](https://arxiv.org/abs/2601.08187) · [PDF](https://arxiv.org/pdf/2601.08187.pdf)  
**作者**：Zijun Di, Bin Lu, Huquan Kang, Luoyi Fu, Jiaxin Ding, Xiaoying Gan, Lei Zhou, Xinbing Wang, Chenghu Zhou  

**一句话要点**：提出HS2C框架，利用图同质性进行结构和语义压缩，以提升LLM在图推理任务中的性能。

**关键词**：文本属性图, 图压缩, 同质性, 结构熵, 语义聚合, LLM推理

## 3 点简述
- 核心问题：现有方法因上下文窗口限制，常随机采样图节点/边，引入噪声并导致推理不稳定。
- 方法要点：基于结构熵最小化进行全局层次划分，识别同质社区，并引导LLM进行差异化语义聚合以压缩冗余信息。
- 实验或效果：在10个节点级基准测试中，HS2C同时提高压缩率和下游推理准确率，验证其优越性和可扩展性。

## 摘要（原文）

> Large language models (LLMs) have demonstrated promising capabilities in Text-Attributed Graph (TAG) understanding. Recent studies typically focus on verbalizing the graph structures via handcrafted prompts, feeding the target node and its neighborhood context into LLMs. However, constrained by the context window, existing methods mainly resort to random sampling, often implemented via dropping node/edge randomly, which inevitably introduces noise and cause reasoning instability. We argue that graphs inherently contain rich structural and semantic information, and that their effective exploitation can unlock potential gains in LLMs reasoning performance. To this end, we propose Homophily-aware Structural and Semantic Compression for LLMs (HS2C), a framework centered on exploiting graph homophily. Structurally, guided by the principle of Structural Entropy minimization, we perform a global hierarchical partition that decodes the graph's essential topology. This partition identifies naturally cohesive, homophilic communities, while discarding stochastic connectivity noise. Semantically, we deliver the detected structural homophily to the LLM, empowering it to perform differentiated semantic aggregation based on predefined community type. This process compresses redundant background contexts into concise community-level consensus, selectively preserving semantically homophilic information aligned with the target nodes. Extensive experiments on 10 node-level benchmarks across LLMs of varying sizes and families demonstrate that, by feeding LLMs with structurally and semantically compressed inputs, HS2C simultaneously enhances the compression rate and downstream inference accuracy, validating its superiority and scalability. Extensions to 7 diverse graph-level benchmarks further consolidate HS2C's task generalizability.

