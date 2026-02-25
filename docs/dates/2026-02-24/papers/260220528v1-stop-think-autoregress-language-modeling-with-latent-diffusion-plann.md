---
layout: default
title: Stop-Think-AutoRegress: Language Modeling with Latent Diffusion Planning
---

# Stop-Think-AutoRegress: Language Modeling with Latent Diffusion Planning
**arXiv**：[2602.20528v1](https://arxiv.org/abs/2602.20528) · [PDF](https://arxiv.org/pdf/2602.20528.pdf)  
**作者**：Justin Lovelace, Christian Belardi, Sofian Zalouk, Adhitya Polavaram, Srivatsa Kundurthy, Kilian Q. Weinberger  

**一句话要点**：提出STAR-LDM语言模型，通过潜在扩散规划增强全局语义决策以提升语言生成质量。

**关键词**：语言建模, 潜在扩散规划, 自回归生成, 语义规划, 模型控制, 叙事连贯性

## 3 点简述
- 核心问题：传统自回归语言模型受限于逐词决策，缺乏全局语义规划能力。
- 方法要点：引入“思考”阶段，暂停生成以在连续空间通过扩散过程优化语义计划。
- 实验或效果：在语言理解基准上显著优于同规模模型，并在叙事连贯性和常识推理评估中胜率超过70%。

## 摘要（原文）

> The Stop-Think-AutoRegress Language Diffusion Model (STAR-LDM) integrates latent diffusion planning with autoregressive generation. Unlike conventional autoregressive language models limited to token-by-token decisions, STAR-LDM incorporates a "thinking" phase that pauses generation to refine a semantic plan through diffusion before continuing. This enables global planning in continuous space prior to committing to discrete tokens. Evaluations show STAR-LDM significantly outperforms similar-sized models on language understanding benchmarks and achieves $>70\%$ win rates in LLM-as-judge comparisons for narrative coherence and commonsense reasoning. The architecture also allows straightforward control through lightweight classifiers, enabling fine-grained steering of attributes without model retraining while maintaining better fluency-control trade-offs than specialized approaches.

