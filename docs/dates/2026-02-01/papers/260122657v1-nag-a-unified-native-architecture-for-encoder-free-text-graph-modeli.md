---
layout: default
title: NAG: A Unified Native Architecture for Encoder-free Text-Graph Modeling in Language Models
---

# NAG: A Unified Native Architecture for Encoder-free Text-Graph Modeling in Language Models
**arXiv**：[2601.22657v1](https://arxiv.org/abs/2601.22657) · [PDF](https://arxiv.org/pdf/2601.22657.pdf)  
**作者**：Haisong Gong, Zhibo Liu, Qiang Liu, Shu Wu, Liang Wang  

**一句话要点**：提出NAG统一架构，在语言模型中内部化处理文本图，无需外部图神经网络编码器。

**关键词**：文本图建模, 语言模型, 自注意力机制, 图神经网络, 统一架构, 结构编码

## 3 点简述
- 核心问题：现有方法使用外部GNN编码图结构，导致与语言模型的语义处理分离，需复杂隐式对齐。
- 方法要点：NAG利用自注意力机制强制拓扑依赖，调整位置ID确保结构等价，内部化图处理于语言模型流形。
- 实验或效果：在多种图任务中验证，NAG实现稳健图理解，无需外部编码器开销，提供更简单、连贯的建模范式。

## 摘要（原文）

> Prevailing methods for integrating graphs into Language Models (LMs) typically rely on a segregated architecture: external Graph Neural Networks (GNNs) encode structural topology, while LMs process textual semantics. We argue this approach is suboptimal for text-graphs: it creates a conceptually disjointed interaction paradigm. By segregating structural encoding from semantic processing, these systems must perform a complex implicit alignment between abstract graph tokens and concrete textual elements. Challenging the necessity of external encoders, we propose NAG (Native Architecture for Graphs), a unified framework that internalizes graph processing within the LM's native manifold. Instead of bridging disparate embedding spaces, NAG repurposes the self-attention mechanism to enforce topological dependencies and recalibrates positional IDs to ensure structural equivalence. This allows the model to harness its intrinsic linguistic capability to simultaneously comprehend node and edge content alongside structural topology. We introduce two efficient implementations: NAG-Zero for absolute preservation of the base model's linguistic capabilities, and NAG-LoRA for enhanced structural adaptation. Experiments across diverse graph tasks validate that NAG achieves robust graph comprehension without the overhead of external encoders, offering a simpler, more coherent paradigm for text-graph modeling.

