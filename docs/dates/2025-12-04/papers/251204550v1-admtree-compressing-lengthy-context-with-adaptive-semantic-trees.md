---
layout: default
title: AdmTree: Compressing Lengthy Context with Adaptive Semantic Trees
---

# AdmTree: Compressing Lengthy Context with Adaptive Semantic Trees
**arXiv**：[2512.04550v1](https://arxiv.org/abs/2512.04550) · [PDF](https://arxiv.org/pdf/2512.04550.pdf)  
**作者**：Yangning Li, Shaoshen Chen, Yinghui Li, Yankai Chen, Hai-Tao Zheng, Hui Wang, Wenhao Jiang, Philip S. Yu  

**一句话要点**：提出AdmTree自适应语义树框架以压缩长上下文，提升LLM处理效率与语义保真度。

**关键词**：长上下文压缩, 自适应语义树, 轻量聚合机制, 位置偏差缓解, 语义保真度, 分层抽象

## 3 点简述
- 核心问题：自注意力二次复杂度限制LLM处理长上下文，现有方法在细节保留、位置偏差或长程依赖捕获上不足。
- 方法要点：基于信息密度动态分段，使用gist令牌构建语义二叉树，轻量聚合机制与冻结主干LLM实现高效分层抽象。
- 实验或效果：未知，但框架旨在保留细粒度细节与全局语义连贯性，动态适应内容以稳健保留语义信息。

## 摘要（原文）

> The quadratic complexity of self-attention constrains Large Language Models (LLMs) in processing long contexts, a capability essential for many advanced applications. Context compression aims to alleviate this computational bottleneck while retaining critical semantic information. However, existing approaches often fall short: explicit methods may compromise local detail, whereas implicit methods can suffer from positional biases, information degradation, or an inability to capture long-range semantic dependencies. We propose AdmTree, a novel framework for adaptive, hierarchical context compression with a central focus on preserving high semantic fidelity while maintaining efficiency. AdmTree dynamically segments input based on information density, utilizing gist tokens to summarize variable-length segments as the leaves of a semantic binary tree. This structure, together with a lightweight aggregation mechanism and a frozen backbone LLM (thereby minimizing new trainable parameters), enables efficient hierarchical abstraction of the context. By preserving fine-grained details alongside global semantic coherence, mitigating positional bias, and dynamically adapting to content, AdmTree robustly retains the semantic information of long contexts.

