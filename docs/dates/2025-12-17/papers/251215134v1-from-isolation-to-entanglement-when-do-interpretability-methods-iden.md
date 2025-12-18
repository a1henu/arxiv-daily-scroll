---
layout: default
title: From Isolation to Entanglement: When Do Interpretability Methods Identify and Disentangle Known Concepts?
---

# From Isolation to Entanglement: When Do Interpretability Methods Identify and Disentangle Known Concepts?
**arXiv**：[2512.15134v1](https://arxiv.org/abs/2512.15134) · [PDF](https://arxiv.org/pdf/2512.15134.pdf)  
**作者**：Aaron Mueller, Andrew Lee, Shruti Joshi, Ekdeep Singh Lubana, Dhanya Sridhar, Patrik Reizinger  

**一句话要点**：提出多概念评估框架，分析相关性增强下稀疏自编码器与稀疏探针的解缠能力。

**关键词**：可解释性, 概念解缠, 稀疏自编码器, 稀疏探针, 相关性评估, 特征操纵

## 3 点简述
- 核心问题：现有可解释性方法在概念相关性下能否恢复解缠表示？
- 方法要点：控制文本概念间相关性，评估特征化方法在增强相关性下的表现。
- 实验或效果：发现特征与概念呈一对多关系，且特征操纵影响多个概念，解缠指标不足。

## 摘要（原文）

> A central goal of interpretability is to recover representations of causally relevant concepts from the activations of neural networks. The quality of these concept representations is typically evaluated in isolation, and under implicit independence assumptions that may not hold in practice. Thus, it is unclear whether common featurization methods - including sparse autoencoders (SAEs) and sparse probes - recover disentangled representations of these concepts. This study proposes a multi-concept evaluation setting where we control the correlations between textual concepts, such as sentiment, domain, and tense, and analyze performance under increasing correlations between them. We first evaluate the extent to which featurizers can learn disentangled representations of each concept under increasing correlational strengths. We observe a one-to-many relationship from concepts to features: features correspond to no more than one concept, but concepts are distributed across many features. Then, we perform steering experiments, measuring whether each concept is independently manipulable. Even when trained on uniform distributions of concepts, SAE features generally affect many concepts when steered, indicating that they are neither selective nor independent; nonetheless, features affect disjoint subspaces. These results suggest that correlational metrics for measuring disentanglement are generally not sufficient for establishing independence when steering, and that affecting disjoint subspaces is not sufficient for concept selectivity. These results underscore the importance of compositional evaluations in interpretability research.

