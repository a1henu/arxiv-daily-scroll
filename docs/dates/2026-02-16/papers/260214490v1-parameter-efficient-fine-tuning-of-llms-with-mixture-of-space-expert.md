---
layout: default
title: Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts
---

# Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts
**arXiv**：[2602.14490v1](https://arxiv.org/abs/2602.14490) · [PDF](https://arxiv.org/pdf/2602.14490.pdf)  
**作者**：Buze Zhang, Jinkai Tao, Zilang Zeng, Neil He, Ali Maatouk, Menglin Yang, Rex Ying  

**一句话要点**：提出MoSLoRA框架，通过混合几何空间专家实现参数高效微调，以提升语言模型在复杂数据上的表达能力。

**关键词**：参数高效微调, 几何空间混合, 低秩适应, 语言模型, 曲率优化, 路由机制

## 3 点简述
- 现有参数高效微调方法局限于欧几里得空间，难以捕捉语言数据的复杂几何结构。
- MoSLoRA扩展LoRA，引入异质几何专家，动态选择或组合几何空间，并设计轻量路由机制降低计算开销。
- 实验表明，MoSLoRA在MATH500和MAWPS等基准上优于基线，性能提升最高达15.9%。

## 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable progress, with Parameter-Efficient Fine-Tuning (PEFT) emerging as a key technique for downstream task adaptation. However, existing PEFT methods mainly operate in Euclidean space, fundamentally limiting their capacity to capture complex geometric structures inherent in language data. While alternative geometric spaces, like hyperbolic geometries for hierarchical data and spherical manifolds for circular patterns, offer theoretical advantages, forcing representations into a single manifold type ultimately limits expressiveness, even when curvature parameters are learnable. To address this, we propose Mixture of Space (MoS), a unified framework that leverages multiple geometric spaces simultaneously to learn richer, curvature-aware representations. Building on this scheme, we develop MoSLoRA, which extends Low-Rank Adaptation (LoRA) with heterogeneous geometric experts, enabling models to dynamically select or combine appropriate geometric spaces based on input context. Furthermore, to address the computational overhead of frequent manifold switching, we develop a lightweight routing mechanism. Moreover, we provide empirical insights into how curvature optimization impacts training stability and model performance. Our experiments across diverse benchmarks demonstrate that MoSLoRA consistently outperforms strong baselines, achieving up to 5.6% improvement on MATH500 and 15.9% on MAWPS.

