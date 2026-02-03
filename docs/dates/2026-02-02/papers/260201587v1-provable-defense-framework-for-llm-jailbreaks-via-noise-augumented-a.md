---
layout: default
title: Provable Defense Framework for LLM Jailbreaks via Noise-Augumented Alignment
---

# Provable Defense Framework for LLM Jailbreaks via Noise-Augumented Alignment
**arXiv**：[2602.01587v1](https://arxiv.org/abs/2602.01587) · [PDF](https://arxiv.org/pdf/2602.01587.pdf)  
**作者**：Zehua Cheng, Jianwei Yang, Wei Dai, Jiahao Sun  

**一句话要点**：提出基于噪声增强对齐的可证明防御框架，以解决大语言模型对抗性越狱问题。

**关键词**：大语言模型安全, 可证明鲁棒性, 对抗性防御, 噪声增强对齐, 语义平滑

## 3 点简述
- 核心问题：大语言模型易受自适应越狱攻击，现有经验防御如GCG效果有限。
- 方法要点：通过分层随机消融实现认证语义平滑，结合噪声增强对齐调优提升稀疏上下文性能。
- 实验或效果：在Llama-3上，将梯度攻击成功率从84.2%降至1.2%，良性效用保持94.1%。

## 摘要（原文）

> Large Language Models (LLMs) remain vulnerable to adaptive jailbreaks that easily bypass empirical defenses like GCG. We propose a framework for certifiable robustness that shifts safety guarantees from single-pass inference to the statistical stability of an ensemble. We introduce Certified Semantic Smoothing (CSS) via Stratified Randomized Ablation, a technique that partitions inputs into immutable structural prompts and mutable payloads to derive rigorous lo norm guarantees using the Hypergeometric distribution. To resolve performance degradation on sparse contexts, we employ Noise-Augmented Alignment Tuning (NAAT), which transforms the base model into a semantic denoiser. Extensive experiments on Llama-3 show that our method reduces the Attack Success Rate of gradient-based attacks from 84.2% to 1.2% while maintaining 94.1% benign utility, significantly outperforming character-level baselines which degrade utility to 74.3%. This framework provides a deterministic certificate of safety, ensuring that a model remains robust against all adversarial variants within a provable radius.

