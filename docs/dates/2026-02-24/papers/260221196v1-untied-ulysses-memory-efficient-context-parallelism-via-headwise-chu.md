---
layout: default
title: Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking
---

# Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking
**arXiv**：[2602.21196v1](https://arxiv.org/abs/2602.21196) · [PDF](https://arxiv.org/pdf/2602.21196.pdf)  
**作者**：Ravi Ghadia, Maksim Abraham, Sergei Vorobyov, Max Ryabinin  

**一句话要点**：提出UPipe技术，通过注意力头级分块提升Transformer长序列处理的内存效率。

**关键词**：上下文并行, 内存优化, 长序列处理, Transformer模型, 注意力机制

## 3 点简述
- 核心问题：现有上下文并行方法内存效率低，限制Transformer模型支持的长序列长度。
- 方法要点：采用注意力头级细粒度分块，显著减少自注意力层的激活内存使用。
- 实验或效果：在32B Transformer上减少激活内存达87.5%，单节点支持5M令牌上下文长度，训练速度与先前方法相当。

## 摘要（原文）

> Efficiently processing long sequences with Transformer models usually requires splitting the computations across accelerators via context parallelism. The dominant approaches in this family of methods, such as Ring Attention or DeepSpeed Ulysses, enable scaling over the context dimension but do not focus on memory efficiency, which limits the sequence lengths they can support. More advanced techniques, such as Fully Pipelined Distributed Transformer or activation offloading, can further extend the possible context length at the cost of training throughput. In this paper, we present UPipe, a simple yet effective context parallelism technique that performs fine-grained chunking at the attention head level. This technique significantly reduces the activation memory usage of self-attention, breaking the activation memory barrier and unlocking much longer context lengths. Our approach reduces intermediate tensor memory usage in the attention layer by as much as 87.5$\%$ for 32B Transformers, while matching previous context parallelism techniques in terms of training speed. UPipe can support the context length of 5M tokens when training Llama3-8B on a single 8$\times$H100 node, improving upon prior methods by over 25$\%$.

