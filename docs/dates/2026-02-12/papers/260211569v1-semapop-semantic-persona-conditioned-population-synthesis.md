---
layout: default
title: SemaPop: Semantic-Persona Conditioned Population Synthesis
---

# SemaPop: Semantic-Persona Conditioned Population Synthesis
**arXiv**：[2602.11569v1](https://arxiv.org/abs/2602.11569) · [PDF](https://arxiv.org/pdf/2602.11569.pdf)  
**作者**：Zhenlin Qin, Yancheng Ling, Leizhen Wang, Francisco Câmara Pereira, Zhenliang Ma  

**一句话要点**：提出SemaPop-GAN模型，通过语义-统计融合实现可控人口合成

**关键词**：人口合成, 语义条件生成, 大语言模型, WGAN-GAN, 统计约束, 行为语义

## 3 点简述
- 核心问题：人口合成需兼顾统计结构与潜在行为语义，现有方法缺乏语义条件生成。
- 方法要点：利用大语言模型从调查数据提取高层人物角色，作为语义条件信号，结合WGAN-GAN进行生成。
- 实验或效果：实验显示模型在边际和联合分布对齐、样本可行性与多样性方面表现更优。

## 摘要（原文）

> Population synthesis is a critical component of individual-level socio-economic simulation, yet remains challenging due to the need to jointly represent statistical structure and latent behavioral semantics. Existing population synthesis approaches predominantly rely on structured attributes and statistical constraints, leaving a gap in semantic-conditioned population generation that can capture abstract behavioral patterns implicitly in survey data. This study proposes SemaPop, a semantic-statistical population synthesis model that integrates large language models (LLMs) with generative population modeling. SemaPop derives high-level persona representations from individual survey records and incorporates them as semantic conditioning signals for population generation, while marginal regularization is introduced to enforce alignment with target population marginals. In this study, the framework is instantiated using a Wasserstein GAN with gradient penalty (WGAN-GP) backbone, referred to as SemaPop-GAN. Extensive experiments demonstrate that SemaPop-GAN achieves improved generative performance, yielding closer alignment with target marginal and joint distributions while maintaining sample-level feasibility and diversity under semantic conditioning. Ablation studies further confirm the contribution of semantic persona conditioning and architectural design choices to balancing marginal consistency and structural realism. These results demonstrate that SemaPop-GAN enables controllable and interpretable population synthesis through effective semantic-statistical information fusion. SemaPop-GAN also provides a promising modular foundation for developing generative population projection systems that integrate individual-level behavioral semantics with population-level statistical constraints.

