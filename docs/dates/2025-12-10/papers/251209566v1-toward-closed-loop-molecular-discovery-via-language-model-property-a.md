---
layout: default
title: Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search
---

# Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search
**arXiv**：[2512.09566v1](https://arxiv.org/abs/2512.09566) · [PDF](https://arxiv.org/pdf/2512.09566.pdf)  
**作者**：Junkai Ji, Zhangfan Yang, Dong Xu, Ruibin Bai, Jianqiang Li, Tingjun Hou, Zexuan Zhu  

**一句话要点**：提出Trio框架，通过语言模型、强化学习和树搜索实现闭环靶向分子设计。

**关键词**：分子生成, 药物发现, 语言模型, 强化学习, 蒙特卡洛树搜索, 闭环设计

## 3 点简述
- 传统药物发现方法效率低、可扩展性差，生成模型存在泛化不足和忽视关键药性等问题。
- Trio整合基于片段的分子语言建模、强化学习和蒙特卡洛树搜索，实现上下文感知的片段组装和平衡探索与利用。
- 实验显示Trio在结合亲和力、类药性和合成可及性上优于现有方法，并显著提升分子多样性。

## 摘要（原文）

> Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate generalization, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular generation framework integrating fragment-based molecular language modeling, reinforcement learning, and Monte Carlo tree search, for effective and interpretable closed-loop targeted molecular design. Through the three key components, Trio enables context-aware fragment assembly, enforces physicochemical and synthetic feasibility, and guides a balanced search between the exploration of novel chemotypes and the exploitation of promising intermediates within protein binding pockets. Experimental results show that Trio reliably achieves chemically valid and pharmacologically enhanced ligands, outperforming state-of-the-art approaches with improved binding affinity (+7.85%), drug-likeness (+11.10%) and synthetic accessibility (+12.05%), while expanding molecular diversity more than fourfold.

