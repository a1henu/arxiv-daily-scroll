---
layout: default
title: Stacked from One: Multi-Scale Self-Injection for Context Window Extension
---

# Stacked from One: Multi-Scale Self-Injection for Context Window Extension
**arXiv**：[2603.04759v1](https://arxiv.org/abs/2603.04759) · [PDF](https://arxiv.org/pdf/2603.04759.pdf)  
**作者**：Wei Han, Pan Zhou, Shuicheng Yan  

**一句话要点**：提出基于多粒度压缩与查询感知的堆叠自注入框架，以高效扩展大语言模型上下文窗口。

**关键词**：上下文窗口扩展, 多粒度压缩, 自注入架构, 查询感知检索, 长序列建模, 推理加速

## 3 点简述
- 核心问题：大语言模型上下文窗口有限，传统扩展方法数据与计算成本高。
- 方法要点：使用堆叠短上下文模型，下层压缩长输入为多粒度表示，上层解码，通过自注入在低层高效传递信息。
- 实验或效果：仅用8K令牌训练，可泛化至128K以上输入，在长上下文任务中性能优异，内存与推理速度显著提升。

## 摘要（原文）

> The limited context window of contemporary large language models (LLMs) remains a primary bottleneck for their broader application across diverse domains. Although continual pre-training on long-context data offers a straightforward solution, it incurs prohibitive data acquisition and computational costs. To address this challenge, we propose~\modelname, a novel framework based on multi-grained context compression and query-aware information acquisition. SharedLLM comprises two stacked short-context LLMs: a lower model serving as a compressor and an upper model acting as a decoder. The lower model compresses long inputs into compact, multi-grained representations, which are then forwarded to the upper model for context-aware processing. To maximize efficiency, this information transfer occurs exclusively at the lowest layers, bypassing lengthy forward passes and redundant cross-attention operations. This entire process, wherein the upper and lower models are derived from the same underlying LLM layers, is termed~\textit{self-injection}. To support this architecture, a specialized tree-based data structure enables the efficient encoding and query-aware retrieval of contextual information. Despite being trained on sequences of only 8K tokens, \modelname~effectively generalizes to inputs exceeding 128K tokens. Across a comprehensive suite of long-context modeling and understanding benchmarks, \modelname~achieves performance superior or comparable to strong baselines, striking an optimal balance between efficiency and accuracy. Furthermore, these design choices allow \modelname~to substantially reduce the memory footprint and yield notable inference speedups ($2\times$ over streaming and $3\times$ over encoder-decoder architectures).

