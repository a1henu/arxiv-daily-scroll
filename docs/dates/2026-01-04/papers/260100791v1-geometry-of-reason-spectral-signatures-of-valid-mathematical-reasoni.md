---
layout: default
title: Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning
---

# Geometry of Reason: Spectral Signatures of Valid Mathematical Reasoning
**arXiv**：[2601.00791v1](https://arxiv.org/abs/2601.00791) · [PDF](https://arxiv.org/pdf/2601.00791.pdf)  
**作者**：Valentin Noël  

**一句话要点**：提出基于注意力谱分析的免训练方法，以检测大语言模型中的有效数学推理。

**关键词**：数学推理验证, 注意力谱分析, 免训练检测, 图信号处理, AI安全监控

## 3 点简述
- 核心问题：如何无监督地验证大语言模型生成的数学推理的有效性。
- 方法要点：将注意力矩阵视为动态图，提取四个可解释的谱诊断指标（如Fiedler值、高频能量比）。
- 实验效果：在七个Transformer模型上实现高达95.6%的分类准确率，无需训练数据或微调。

## 摘要（原文）

> We present a training-free method for detecting valid mathematical reasoning in large language models through spectral analysis of attention patterns. By treating attention matrices as adjacency matrices of dynamic graphs over tokens, we extract four interpretable spectral diagnostics, the Fiedler value (algebraic connectivity), high-frequency energy ratio (HFER), graph signal smoothness, and spectral entropy, that exhibit statistically significant differences between valid and invalid mathematical proofs. Experiments across seven transformer models from four independent architectural families (Meta Llama, Alibaba Qwen, Microsoft Phi, and Mistral AI) demonstrate that this spectral signature produces effect sizes up to Cohen's $d = 3.30$ ($p < 10^{-116}$), enabling 85.0--95.6\% classification accuracy under rigorous evaluation, with calibrated thresholds reaching 93--95\% on the full dataset. The method requires no training data, fine-tuning, or learned classifiers: a single threshold on a spectral metric suffices for high accuracy. Through systematic label correction, we discover that the spectral method detects logical coherence rather than compiler acceptance, identifying mathematically valid proofs that formal verifiers reject due to technical failures. We further identify an architectural dependency: Mistral-7B's Sliding Window Attention shifts the discriminative signal from HFER to late-layer Smoothness ($d = 2.09$, $p_{\text{MW}} = 1.16 \times 10^{-48}$), revealing that attention mechanism design affects which spectral features capture reasoning validity. These findings establish spectral graph analysis as a principled framework for reasoning verification with immediate applications to hallucination detection and AI safety monitoring.

