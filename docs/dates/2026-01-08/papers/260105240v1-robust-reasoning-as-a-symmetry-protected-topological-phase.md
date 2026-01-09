---
layout: default
title: Robust Reasoning as a Symmetry-Protected Topological Phase
---

# Robust Reasoning as a Symmetry-Protected Topological Phase
**arXiv**：[2601.05240v1](https://arxiv.org/abs/2601.05240) · [PDF](https://arxiv.org/pdf/2601.05240.pdf)  
**作者**：Ilmo Sung  

**一句话要点**：提出将稳健推理建模为对称性保护拓扑相，以解决大语言模型中的幻觉问题。

**关键词**：稳健推理, 对称性保护拓扑相, 非阿贝尔规范对称性, 幻觉问题, 拓扑相变, 符号操作

## 3 点简述
- 核心问题：大语言模型易受语义噪声影响，产生逻辑不一致的幻觉。
- 方法要点：将稳健推理形式化为对称性保护拓扑相，类比非阿贝尔任意子编织，替换脆弱几何插值。
- 实验或效果：在符号操作任务中，拓扑模型保持完美保真度外推100倍，而Transformer失去逻辑连贯性。

## 摘要（原文）

> Large language models suffer from "hallucinations"-logical inconsistencies induced by semantic noise. We propose that current architectures operate in a "Metric Phase," where causal order is vulnerable to spontaneous symmetry breaking. Here, we identify robust inference as an effective Symmetry-Protected Topological phase, where logical operations are formally isomorphic to non-Abelian anyon braiding, replacing fragile geometric interpolation with robust topological invariants. Empirically, we demonstrate a sharp topological phase transition: while Transformers and RNNs exhibit gapless decay, our Holonomic Network reveals a macroscopic "mass gap," maintaining invariant fidelity below a critical noise threshold. Furthermore, in a variable-binding task on $S_{10}$ ($3.6 \times 10^6$ states) representing symbolic manipulation, we demonstrate holonomic generalization: the topological model maintains perfect fidelity extrapolating $100\times$ beyond training ($L=50 \to 5000$), consistent with a theoretically indefinite causal horizon, whereas Transformers lose logical coherence. Ablation studies indicate this protection emerges strictly from non-Abelian gauge symmetry. This provides strong evidence for a new universality class for logical reasoning, linking causal stability to the topology of the semantic manifold.

