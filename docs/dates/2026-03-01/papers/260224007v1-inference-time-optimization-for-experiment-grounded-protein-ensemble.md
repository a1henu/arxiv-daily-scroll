---
layout: default
title: Inference-time optimization for experiment-grounded protein ensemble generation
---

# Inference-time optimization for experiment-grounded protein ensemble generation
**arXiv**：[2602.24007v1](https://arxiv.org/abs/2602.24007) · [PDF](https://arxiv.org/pdf/2602.24007.pdf)  
**作者**：Advaith Maddipatla, Anar Rzayev, Marco Pegoraro, Martin Pacesa, Paul Schanda, Ailie Marx, Sanketh Vedula, Alex M. Bronstein  

**一句话要点**：提出推理时优化框架以解决实验引导蛋白质构象集合生成中的采样限制与热力学不合理问题

**关键词**：蛋白质构象集合生成, 推理时优化, 实验引导生成, 玻尔兹曼采样, AlphaFold3, 热力学合理性

## 3 点简述
- 核心问题：现有生成模型如AlphaFold3难以产生匹配实验数据的动态蛋白质构象集合，实验引导方法受固定采样范围和初始化敏感度限制。
- 方法要点：通过优化潜在表示最大化集合对数似然，结合AlphaFold3结构先验和力场先验，设计新颖采样方案绘制玻尔兹曼加权集合。
- 实验或效果：框架在X射线晶体学和NMR中优于现有引导方法，提升多样性、物理能量和数据一致性，并揭示AlphaFold3嵌入扰动可能人为夸大模型置信度。

## 摘要（原文）

> Protein function relies on dynamic conformational ensembles, yet current generative models like AlphaFold3 often fail to produce ensembles that match experimental data. Recent experiment-guided generators attempt to address this by steering the reverse diffusion process. However, these methods are limited by fixed sampling horizons and sensitivity to initialization, often yielding thermodynamically implausible results. We introduce a general inference-time optimization framework to solve these challenges. First, we optimize over latent representations to maximize ensemble log-likelihood, rather than perturbing structures post hoc. This approach eliminates dependence on diffusion length, removes initialization bias, and easily incorporates external constraints. Second, we present novel sampling schemes for drawing Boltzmann-weighted ensembles. By combining structural priors from AlphaFold3 with force-field-based priors, we sample from their product distribution while balancing experimental likelihoods. Our results show that this framework consistently outperforms state-of-the-art guidance, improving diversity, physical energy, and agreement with data in X-ray crystallography and NMR, often fitting the experimental data better than deposited PDB structures. Finally, inference-time optimization experiments maximizing ipTM scores reveal that perturbing AlphaFold3 embeddings can artificially inflate model confidence. This exposes a vulnerability in current design metrics, whose mitigation could offer a pathway to reduce false discovery rates in binder engineering.

