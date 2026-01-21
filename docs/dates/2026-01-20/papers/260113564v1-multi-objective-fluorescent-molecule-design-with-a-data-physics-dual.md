---
layout: default
title: Multi-objective fluorescent molecule design with a data-physics dual-driven generative framework
---

# Multi-objective fluorescent molecule design with a data-physics dual-driven generative framework
**arXiv**：[2601.13564v1](https://arxiv.org/abs/2601.13564) · [PDF](https://arxiv.org/pdf/2601.13564.pdf)  
**作者**：Yanheng Li, Zhichen Pu, Lijiang Yang, Zehao Zhou, Yi Qin Gao  

**一句话要点**：提出LUMOS框架以解决荧光分子多目标逆向设计中的效率与可靠性问题

**关键词**：荧光分子设计, 逆向设计, 多目标优化, 数据物理双驱动, 生成模型, TD-DFT预测

## 3 点简述
- 核心问题：传统方法在荧光分子多目标设计中效率低、预测不可靠且计算成本高
- 方法要点：结合数据与物理驱动，通过共享潜在表示和互补预测器实现高效探索
- 实验或效果：在基准测试中优于基线模型，并通过TD-DFT和MD模拟验证生成分子有效性

## 摘要（原文）

> Designing fluorescent small molecules with tailored optical and physicochemical properties requires navigating vast, underexplored chemical space while satisfying multiple objectives and constraints. Conventional generate-score-screen approaches become impractical under such realistic design specifications, owing to their low search efficiency, unreliable generalizability of machine-learning prediction, and the prohibitive cost of quantum chemical calculation. Here we present LUMOS, a data-and-physics driven framework for inverse design of fluorescent molecules. LUMOS couples generator and predictor within a shared latent representation, enabling direct specification-to-molecule design and efficient exploration. Moreover, LUMOS combines neural networks with a fast time-dependent density functional theory (TD-DFT) calculation workflow to build a suite of complementary predictors spanning different trade-offs in speed, accuracy, and generalizability, enabling reliable property prediction across diverse scenarios. Finally, LUMOS employs a property-guided diffusion model integrated with multi-objective evolutionary algorithms, enabling de novo design and molecular optimization under multiple objectives and constraints. Across comprehensive benchmarks, LUMOS consistently outperforms baseline models in terms of accuracy, generalizability and physical plausibility for fluorescence property prediction, and demonstrates superior performance in multi-objective scaffold- and fragment-level molecular optimization. Further validation using TD-DFT and molecular dynamics (MD) simulations demonstrates that LUMOS can generate valid fluorophores that meet various target specifications. Overall, these results establish LUMOS as a data-physics dual-driven framework for general fluorophore inverse design.

