---
layout: default
title: Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space
---

# Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space
**arXiv**：[2512.24617v1](https://arxiv.org/abs/2512.24617) · [PDF](https://arxiv.org/pdf/2512.24617.pdf)  
**作者**：Xingwei Qu, Shaowen Wang, Zihao Huang, Kai Hua, Fan Yin, Rui-Jie Zhu, Jundong Zhou, Qiyang Min, Zihao Wang, Yizhi Li, Tianyu Zhang, He Xing, Zheng Zhang, Yuxuan Song, Tianyu Zheng, Zhiyuan Zeng, Chenghua Lin, Ge Zhang, Wenhao Huang  

**一句话要点**：提出动态大概念模型以解决语言模型中计算分配不均的问题，通过压缩概念空间提升推理效率。

**关键词**：动态大概念模型, 分层语言建模, 压缩感知缩放定律, 解耦μP参数化, 零样本基准测试, 概念空间推理

## 3 点简述
- 核心问题：大语言模型对所有令牌应用统一计算，但语言信息密度不均，导致计算浪费和关键语义处理不足。
- 方法要点：引入分层语言建模框架，从潜在表示学习语义边界，将计算从令牌转移到压缩概念空间，实现端到端可变长度概念发现。
- 实验或效果：在压缩比R=4时，重新分配约三分之一推理计算到高容量推理骨干，在匹配推理FLOPs下，12个零样本基准平均提升2.69%。

## 摘要（原文）

> Large Language Models (LLMs) apply uniform computation to all tokens, despite language exhibiting highly non-uniform information density. This token-uniform regime wastes capacity on locally predictable spans while under-allocating computation to semantically critical transitions. We propose $\textbf{Dynamic Large Concept Models (DLCM)}$, a hierarchical language modeling framework that learns semantic boundaries from latent representations and shifts computation from tokens to a compressed concept space where reasoning is more efficient. DLCM discovers variable-length concepts end-to-end without relying on predefined linguistic units. Hierarchical compression fundamentally changes scaling behavior. We introduce the first $\textbf{compression-aware scaling law}$, which disentangles token-level capacity, concept-level reasoning capacity, and compression ratio, enabling principled compute allocation under fixed FLOPs. To stably train this heterogeneous architecture, we further develop a $\textbf{decoupled $μ$P parametrization}$ that supports zero-shot hyperparameter transfer across widths and compression regimes. At a practical setting ($R=4$, corresponding to an average of four tokens per concept), DLCM reallocates roughly one-third of inference compute into a higher-capacity reasoning backbone, achieving a $\textbf{+2.69$\%$ average improvement}$ across 12 zero-shot benchmarks under matched inference FLOPs.

