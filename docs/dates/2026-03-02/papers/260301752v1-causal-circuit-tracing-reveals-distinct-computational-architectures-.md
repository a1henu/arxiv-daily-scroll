---
layout: default
title: Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence
---

# Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence
**arXiv**：[2603.01752v1](https://arxiv.org/abs/2603.01752) · [PDF](https://arxiv.org/pdf/2603.01752.pdf)  
**作者**：Ihor Kendiukhov  

**一句话要点**：提出因果电路追踪方法，揭示单细胞基础模型中抑制主导与生物一致性的计算架构

**关键词**：因果电路追踪, 稀疏自编码器, 单细胞基础模型, 抑制主导, 生物一致性, 跨模型收敛

## 3 点简述
- 核心问题：稀疏自编码器分解特征后，生物基础模型中跨网络深度的因果特征交互未知
- 方法要点：通过消融稀疏自编码器特征并测量下游响应，进行因果电路追踪
- 实验或效果：应用于Geneformer和scGPT，发现抑制主导、生物一致性和跨模型收敛，验证了共表达模式

## 摘要（原文）

> Motivation: Sparse autoencoders (SAEs) decompose foundation model activations into interpretable features, but causal feature-to-feature interactions across network depth remain unknown for biological foundation models.
>   Results: We introduce causal circuit tracing by ablating SAE features and measuring downstream responses, and apply it to Geneformer V2-316M and scGPT whole-human across four conditions (96,892 edges, 80,191 forward passes). Both models show approximately 53 percent biological coherence and 65 to 89 percent inhibitory dominance, invariant to architecture and cell type. scGPT produces stronger effects (mean absolute d = 1.40 vs. 1.05) with more balanced dynamics. Cross-model consensus yields 1,142 conserved domain pairs (10.6x enrichment, p < 0.001). Disease-associated domains are 3.59x more likely to be consensus. Gene-level CRISPRi validation shows 56.4 percent directional accuracy, confirming co-expression rather than causal encoding.

