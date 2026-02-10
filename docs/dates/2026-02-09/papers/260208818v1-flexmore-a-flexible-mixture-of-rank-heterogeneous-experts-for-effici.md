---
layout: default
title: FlexMoRE: A Flexible Mixture of Rank-heterogeneous Experts for Efficient Federatedly-trained Large Language Models
---

# FlexMoRE: A Flexible Mixture of Rank-heterogeneous Experts for Efficient Federatedly-trained Large Language Models
**arXiv**：[2602.08818v1](https://arxiv.org/abs/2602.08818) · [PDF](https://arxiv.org/pdf/2602.08818.pdf)  
**作者**：Annemette Brok Pirchert, Jacob Nielsen, Mogens Henrik From, Lukas Galke Poech, Peter Schneider-Kamp  

**一句话要点**：提出FlexMoRE以通过秩异构专家混合提升联邦训练大语言模型的效率与性能

**关键词**：联邦学习, 专家混合, 低秩适配器, 大语言模型, 参数效率

## 3 点简述
- 核心问题：全尺寸专家在联邦训练中可能不必要，需平衡专家秩与下游任务性能
- 方法要点：FlexMoRE混合全尺寸专家与低秩适配器，系统研究秩对性能的影响
- 实验或效果：在推理密集型任务中高秩更优，FlexMoRE以更少参数实现性能提升

## 摘要（原文）

> Recent advances in mixture-of-experts architectures have shown that individual experts models can be trained federatedly, i.e., in isolation from other experts by using a common base model to facilitate coordination. However, we hypothesize that full-sized experts may not be necessary for all domains and that instead low-rank adapters may be sufficient. Here, we introduce FlexMoRE, a Flexible Mixture of Rank-heterogenous Experts, which may be either full-sized experts or adapters of a suitable rank. We systematically investigate the trade-off between expert rank and downstream task performance by evaluating $6$ experts with ranks $2^0$ to $2^{14}$ resulting in experiments covering 150 mixtures (96 with 2 experts, 54 with 7 experts) that are evaluated across $120$ tasks. For our experiments, we build on FlexOlmo and turn its pre-trained experts into low-rank versions. Our regression analysis from expert rank to downstream task performance reveals that the best-performing rank is substantially higher for reasoning-heavy benchmarks than for knowledge-heavy benchmarks. These findings on rank sensitivity come with direct implications for memory efficiency: Using optimal ranks, FlexMoRE yields improved downstream task performance (average score $47.18$) compared to the baseline FlexOlmo-style mixture of full-sized experts (average score $45.46$) at less than one third the parameters ($10.75$B for FlexMoRE vs. $33.27$B for FlexOlmo). All code will be made available.

