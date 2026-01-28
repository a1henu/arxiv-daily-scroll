---
layout: default
title: C2NP: A Benchmark for Learning Scale-Dependent Geometric Invariances in 3D Materials Generation
---

# C2NP: A Benchmark for Learning Scale-Dependent Geometric Invariances in 3D Materials Generation
**arXiv**：[2601.19076v1](https://arxiv.org/abs/2601.19076) · [PDF](https://arxiv.org/pdf/2601.19076.pdf)  
**作者**：Can Polat, Erchin Serpedin, Mustafa Kurban, Hasan Kurban  

**一句话要点**：提出C2NP基准以评估3D材料生成模型在晶体与纳米颗粒间尺度转换的几何不变性学习能力

**关键词**：3D材料生成, 几何不变性, 纳米颗粒基准, 晶体结构, 分布偏移, 物理泛化

## 3 点简述
- 核心问题：现有生成模型在从无限晶体单元到有限纳米颗粒的尺度转换中，难以处理表面效应和尺寸依赖的几何失真。
- 方法要点：构建C2NP基准，包含从晶体生成纳米颗粒和从颗粒恢复晶体参数的双任务，基于DFT松弛单元创建超17万纳米颗粒配置。
- 实验或效果：实验显示先进模型在分布偏移下几何失败，产生大晶格恢复误差，表明依赖模板记忆而非可扩展物理泛化。

## 摘要（原文）

> Generative models for materials have achieved strong performance on periodic bulk crystals, yet their ability to generalize across scale transitions to finite nanostructures remains largely untested. We introduce Crystal-to-Nanoparticle (C2NP), a systematic benchmark for evaluating generative models when moving between infinite crystalline unit cells and finite nanoparticles, where surface effects and size-dependent distortions dominate. C2NP defines two complementary tasks: (i) generating nanoparticles of specified radii from periodic unit cells, testing whether models capture surface truncation and geometric constraints; and (ii) recovering bulk lattice parameters and space-group symmetry from finite particle configurations, assessing whether models can infer underlying crystallographic order despite surface perturbations. Using diverse materials as a structurally consistent testbed, we construct over 170,000 nanoparticle configurations by carving particles from supercells derived from DFT-relaxed crystal unit cells, and introduce size-based splits that separate interpolation from extrapolation regimes. Experiments with state-of-the-art approaches, including diffusion, flow-matching, and variational models, show that even when losses are low, models often fail geometrically under distribution shift, yielding large lattice-recovery errors and near-zero joint accuracy on structure and symmetry. Overall, our results suggest that current methods rely on template memorization rather than scalable physical generalization. C2NP offers a controlled, reproducible framework for diagnosing these failures, with immediate applications to nanoparticle catalyst design, nanostructured hydrides for hydrogen storage, and materials discovery. Dataset and code are available at https://github.com/KurbanIntelligenceLab/C2NP.

