---
layout: default
title: Attention-MoA: Enhancing Mixture-of-Agents via Inter-Agent Semantic Attention and Deep Residual Synthesis
---

# Attention-MoA: Enhancing Mixture-of-Agents via Inter-Agent Semantic Attention and Deep Residual Synthesis
**arXiv**：[2601.16596v1](https://arxiv.org/abs/2601.16596) · [PDF](https://arxiv.org/pdf/2601.16596.pdf)  
**作者**：Jianyu Wen, Yang Wei, Xiongxi Yu, Changxuan Xiao, Ke Zeng  

**一句话要点**：提出Attention-MoA框架，通过代理间语义注意力增强混合代理协作，解决深层语义交互不足问题。

**关键词**：混合代理框架, 语义注意力, 残差合成, 大语言模型协作, 幻觉纠正

## 3 点简述
- 核心问题：现有MoA方法代理间语义交互不足，限制幻觉纠正和逻辑精炼能力。
- 方法要点：引入代理间语义注意力机制，结合自适应早停的层间残差模块，提升协作深度和效率。
- 实验或效果：在AlpacaEval 2.0等基准上显著超越基线，小模型集成可超越大型专有模型。

## 摘要（原文）

> As the development of Large Language Models (LLMs) shifts from parameter scaling to inference-time collaboration, the Mixture-of-Agents (MoA) framework has emerged as a general paradigm to harness collective intelligence by layering diverse models. While recent MoA variants have introduced dynamic routing and residual connections to improve efficiency, these methods often fail to facilitate deep semantic interaction between agents, limiting the system's ability to actively correct hallucinations and refine logic. In this paper, we introduce Attention-MoA, a novel MoA-based framework that redefines collaboration through Inter-agent Semantic Attention. Complemented by an Inter-layer Residual Module with Adaptive Early Stopping Mechanism, our architecture mitigates information degradation in deep layers while improving computational efficiency. Extensive evaluations across AlpacaEval 2.0, MT-Bench, and FLASK demonstrate that Attention-MoA significantly outperforms state-of-the-art baselines, achieving a 91.15% Length-Controlled Win Rate on AlpacaEval 2.0 and dominating in 10 out of 12 capabilities on FLASK. Notably, Attention-MoA enables an ensemble of small open-source models to outperform massive proprietary models like Claude-4.5-Sonnet and GPT-4.1, achieving an MT-Bench score of 8.83 and an AlpacaEval 2.0 LC Win Rate of 77.36%.

