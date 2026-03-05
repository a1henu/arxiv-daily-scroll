---
layout: default
title: Efficient Refusal Ablation in LLM through Optimal Transport
---

# Efficient Refusal Ablation in LLM through Optimal Transport
**arXiv**：[2603.04355v1](https://arxiv.org/abs/2603.04355) · [PDF](https://arxiv.org/pdf/2603.04355.pdf)  
**作者**：Geraldin Nanfack, Eugene Belilovsky, Elvis Dohmatob  

**一句话要点**：提出基于最优传输的分布变换框架，高效移除大语言模型中的拒绝行为以提升攻击成功率。

**关键词**：大语言模型安全, 最优传输, 激活劫持, 分布变换, 层选择性干预, 几何结构分析

## 3 点简述
- 核心问题：现有激活劫持方法将拒绝行为视为一维现象，忽略模型激活的分布结构，导致攻击效果有限。
- 方法要点：结合PCA与闭式高斯最优传输，在保持几何结构的同时，高效变换有害激活分布以匹配无害分布。
- 实验或效果：在六个模型上实现最高11%的攻击成功率提升，发现层选择性干预优于全网络干预，揭示拒绝机制可能局部化。

## 摘要（原文）

> Safety-aligned language models refuse harmful requests through learned refusal behaviors encoded in their internal representations. Recent activation-based jailbreaking methods circumvent these safety mechanisms by applying orthogonal projections to remove refusal directions, but these approaches treat refusal as a one-dimensional phenomenon and ignore the rich distributional structure of model activations. We introduce a principled framework based on optimal transport theory that transforms the entire distribution of harmful activations to match harmless ones. By combining PCA with closed-form Gaussian optimal transport, we achieve efficient computation in high-dimensional representation spaces while preserving essential geometric structure. Across six models (Llama-2, Llama-3.1, Qwen-2.5; 7B-32B parameters), our method achieves up to 11% higher attack success rates than state-of-the-art baselines while maintaining comparable perplexity, demonstrating superior preservation of model capabilities. Critically, we discover that layer-selective intervention (applying optimal transport to 1-2 carefully chosen layers at approximately 40-60% network depth) substantially outperforms full-network interventions, revealing that refusal mechanisms may be localized rather than distributed. Our analysis provides new insights into the geometric structure of safety representations and suggests that current alignment methods may be vulnerable to distributional attacks beyond simple direction removal.

