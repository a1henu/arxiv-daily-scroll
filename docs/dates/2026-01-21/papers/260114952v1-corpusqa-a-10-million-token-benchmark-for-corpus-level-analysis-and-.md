---
layout: default
title: CorpusQA: A 10 Million Token Benchmark for Corpus-Level Analysis and Reasoning
---

# CorpusQA: A 10 Million Token Benchmark for Corpus-Level Analysis and Reasoning
**arXiv**：[2601.14952v1](https://arxiv.org/abs/2601.14952) · [PDF](https://arxiv.org/pdf/2601.14952.pdf)  
**作者**：Zhiyuan Lu, Chenliang Li, Yingcheng Shi, Weizhou Shen, Ming Yan, Fei Huang  

**一句话要点**：提出CorpusQA基准以评估大语言模型在千万令牌级语料上的全局推理能力

**关键词**：语料级分析, 长上下文推理, 数据合成, 基准评估, 全局信息整合, 内存增强架构

## 3 点简述
- 现有基准无法测试模型在分散证据和全局整合上的语料级分析能力
- 通过解耦推理与文本表示的数据合成框架生成复杂查询和程序化真值
- 实验显示长上下文模型和检索增强系统在输入增长时表现不佳，需内存增强架构

## 摘要（原文）

> While large language models now handle million-token contexts, their capacity for reasoning across entire document repositories remains largely untested. Existing benchmarks are inadequate, as they are mostly limited to single long texts or rely on a "sparse retrieval" assumption-that answers can be derived from a few relevant chunks. This assumption fails for true corpus-level analysis, where evidence is highly dispersed across hundreds of documents and answers require global integration, comparison, and statistical aggregation. To address this critical gap, we introduce CorpusQA, a new benchmark scaling up to 10 million tokens, generated via a novel data synthesis framework. By decoupling reasoning from textual representation, this framework creates complex, computation-intensive queries with programmatically guaranteed ground-truth answers, challenging systems to perform holistic reasoning over vast, unstructured text without relying on fallible human annotation. We further demonstrate the utility of our framework beyond evaluation, showing that fine-tuning on our synthesized data effectively enhances an LLM's general long-context reasoning capabilities. Extensive experiments reveal that even state-of-the-art long-context LLMs struggle as input length increases, and standard retrieval-augmented generation systems collapse entirely. Our findings indicate that memory-augmented agentic architectures offer a more robust alternative, suggesting a critical shift is needed from simply extending context windows to developing advanced architectures for global information synthesis.

