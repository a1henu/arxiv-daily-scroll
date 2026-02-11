---
layout: default
title: AGMark: Attention-Guided Dynamic Watermarking for Large Vision-Language Models
---

# AGMark: Attention-Guided Dynamic Watermarking for Large Vision-Language Models
**arXiv**：[2602.09611v1](https://arxiv.org/abs/2602.09611) · [PDF](https://arxiv.org/pdf/2602.09611.pdf)  
**作者**：Yue Li, Xin Yi, Dongsheng Shi, Yongyi Cui, Gerard de Melo, Linlin Wang  

**一句话要点**：提出AGMark框架，通过注意力引导动态水印解决大型视觉语言模型中的视觉保真度问题。

**关键词**：大型视觉语言模型, 动态水印, 注意力机制, 视觉保真度, 语义关键标记

## 3 点简述
- 核心问题：现有水印方法可能引入视觉无关标记或忽略视觉依赖的动态变化，影响生成质量。
- 方法要点：基于注意力权重动态识别语义关键证据，结合不确定性和证据校准自适应划分词汇。
- 实验或效果：AGMark在保持高检测精度和攻击鲁棒性的同时，显著提升生成质量和视觉语义保真度。

## 摘要（原文）

> Watermarking has emerged as a pivotal solution for content traceability and intellectual property protection in Large Vision-Language Models (LVLMs). However, vision-agnostic watermarks may introduce visually irrelevant tokens and disrupt visual grounding by enforcing indiscriminate pseudo-random biases. Additionally, current vision-specific watermarks rely on a static, one-time estimation of vision critical weights and ignore the weight distribution density when determining the proportion of protected tokens. This design fails to account for dynamic changes in visual dependence during generation and may introduce low-quality tokens in the long tail. To address these challenges, we propose Attention-Guided Dynamic Watermarking (AGMark), a novel framework that embeds detectable signals while strictly preserving visual fidelity. At each decoding step, AGMark first dynamically identifies semantic-critical evidence based on attention weights for visual relevance, together with context-aware coherence cues, resulting in a more adaptive and well-calibrated evidence-weight distribution. It then determines the proportion of semantic-critical tokens by jointly considering uncertainty awareness (token entropy) and evidence calibration (weight density), thereby enabling adaptive vocabulary partitioning to avoid irrelevant tokens. Empirical results confirm that AGMark outperforms conventional methods, observably improving generation quality and yielding particularly strong gains in visual semantic fidelity in the later stages of generation. The framework maintains highly competitive detection accuracy (at least 99.36\% AUC) and robust attack resilience (at least 88.61\% AUC) without sacrificing inference efficiency, effectively establishing a new standard for reliability-preserving multi-modal watermarking.

