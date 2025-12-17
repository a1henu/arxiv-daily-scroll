---
layout: default
title: From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition
---

# From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition
**arXiv**：[2512.14244v1](https://arxiv.org/abs/2512.14244) · [PDF](https://arxiv.org/pdf/2512.14244.pdf)  
**作者**：Yiqing Zhou, Yu Lei, Shuzheng Si, Qingyan Sun, Wei Wang, Yifei Wu, Hao Wen, Gang Chen, Fanchao Qi, Maosong Sun  

**一句话要点**：提出基于基本语篇单元的上下文压缩框架，以解决长文档处理中的结构保持与成本问题

**关键词**：上下文压缩, 基本语篇单元, 结构保持, 长文档处理, 成本优化, 关系树

## 3 点简述
- 核心问题：现有压缩方法破坏局部连贯性或存在位置偏差，不兼容闭源API
- 方法要点：通过结构-选择两阶段流程，将文本转换为严格锚定源索引的基本语篇单元关系树
- 实验效果：在结构预测准确率上达到最优，显著降低下游任务成本并提升性能

## 摘要（原文）

> Managing extensive context remains a critical bottleneck for Large Language Models (LLMs), particularly in applications like long-document question answering and autonomous agents where lengthy inputs incur high computational costs and introduce noise. Existing compression techniques often disrupt local coherence through discrete token removal or rely on implicit latent encoding that suffers from positional bias and incompatibility with closed-source APIs. To address these limitations, we introduce the EDU-based Context Compressor, a novel explicit compression framework designed to preserve both global structure and fine-grained details. Our approach reformulates context compression as a structure-then-select process. First, our LingoEDU transforms linear text into a structural relation tree of Elementary Discourse Units (EDUs) which are anchored strictly to source indices to eliminate hallucination. Second, a lightweight ranking module selects query-relevant sub-trees for linearization. To rigorously evaluate structural understanding, we release StructBench, a manually annotated dataset of 248 diverse documents. Empirical results demonstrate that our method achieves state-of-the-art structural prediction accuracy and significantly outperforms frontier LLMs while reducing costs. Furthermore, our structure-aware compression substantially enhances performance across downstream tasks ranging from long-context tasks to complex Deep Search scenarios.

