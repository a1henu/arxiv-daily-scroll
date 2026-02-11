---
layout: default
title: Surrogate-Guided Quantum Discovery in Black-Box Landscapes with Latent-Quadratic Interaction Embedding Transformers
---

# Surrogate-Guided Quantum Discovery in Black-Box Landscapes with Latent-Quadratic Interaction Embedding Transformers
**arXiv**：[2602.09374v1](https://arxiv.org/abs/2602.09374) · [PDF](https://arxiv.org/pdf/2602.09374.pdf)  
**作者**：Saisubramaniam Gopalakrishnan, Dagnachew Birru  

**一句话要点**：提出基于自注意力与二次投影的量子辅助黑盒发现方法，以提升结构多样性与极端风险发现

**关键词**：量子辅助优化, 黑盒发现, 高阶交互建模, 二次哈密顿量投影, 结构多样性采样, 风险发现

## 3 点简述
- 核心问题：黑盒评估下高效用与结构多样配置的发现受限于查询预算和经典方法模式集中
- 方法要点：通过自注意力建模高阶依赖，投影为半正定二次哈密顿量，结合QAOA进行量子采样
- 实验或效果：在文档处理风险发现中，相比基线提升结构多样性和极端风险发现，覆盖更多非重叠高效用配置

## 摘要（原文）

> Discovering configurations that are both high-utility and structurally diverse under expensive black-box evaluation and strict query budgets remains a central challenge in data-driven discovery. Many classical optimizers concentrate on dominant modes, while quality-diversity methods require large evaluation budgets to populate high-dimensional archives. Quantum Approximate Optimization Algorithm (QAOA) provides distributional sampling but requires an explicit problem Hamiltonian, which is unavailable in black-box settings. Practical quantum circuits favor quadratic Hamiltonians since higher-order interaction terms are costly to realize. Learned quadratic surrogates such as Factorization Machines (FM) have been used as proxies, but are limited to pairwise structure. We extend this surrogate-to-Hamiltonian approach by modelling higher-order variable dependencies via self-attention and projects them into a valid Positive Semi-Definite quadratic form compatible with QAOA. This enables diversity-oriented quantum sampling from learned energy landscapes while capturing interaction structure beyond pairwise terms. We evaluate on risk discovery for enterprise document processing systems against diverse classical optimizers. Quantum-guided samplers achieve competitive utility while consistently improving structural diversity and exclusive discovery. FM surrogates provide stronger early coverage, whereas ours yields higher-fidelity surrogate landscapes and better extreme-case discovery. Our method recovers roughly twice as many structurally tail-risk outliers as most classical baselines and identify an exclusive non-overlapping fraction of high-utility configurations not found by competing methods, highlighting that an effective mechanism for learning higher-order interaction structure and projecting it into quadratic surrogate Hamiltonians for quantum-assisted black-box discovery.

