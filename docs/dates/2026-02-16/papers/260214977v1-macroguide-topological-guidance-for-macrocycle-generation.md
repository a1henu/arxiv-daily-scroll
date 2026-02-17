---
layout: default
title: MacroGuide: Topological Guidance for Macrocycle Generation
---

# MacroGuide: Topological Guidance for Macrocycle Generation
**arXiv**：[2602.14977v1](https://arxiv.org/abs/2602.14977) · [PDF](https://arxiv.org/pdf/2602.14977.pdf)  
**作者**：Alicja Maksymiuk, Alexandre Duplessis, Michael Bronstein, Alexander Tong, Fernanda Duarte, İsmail İlkan Ceylan  

**一句话要点**：提出MacroGuide扩散引导机制，利用持久同调指导预训练分子生成模型生成大环化合物

**关键词**：大环化合物生成, 扩散模型, 持久同调, 分子生成, 拓扑引导, 药物发现

## 3 点简述
- 大环化合物因稀缺数据和拓扑约束挑战，在生成建模中未被充分探索
- MacroGuide通过构建Vietoris-Rips复形优化持久同调特征，促进环形成
- 实验显示，应用MacroGuide将大环生成率从1%提升至99%，并保持高质量指标

## 摘要（原文）

> Macrocycles are ring-shaped molecules that offer a promising alternative to small-molecule drugs due to their enhanced selectivity and binding affinity against difficult targets. Despite their chemical value, they remain underexplored in generative modeling, likely owing to their scarcity in public datasets and the challenges of enforcing topological constraints in standard deep generative models. We introduce MacroGuide: Topological Guidance for Macrocycle Generation, a diffusion guidance mechanism that uses Persistent Homology to steer the sampling of pretrained molecular generative models toward the generation of macrocycles, in both unconditional and conditional (protein pocket) settings. At each denoising step, MacroGuide constructs a Vietoris-Rips complex from atomic positions and promotes ring formation by optimizing persistent homology features. Empirically, applying MacroGuide to pretrained diffusion models increases macrocycle generation rates from 1% to 99%, while matching or exceeding state-of-the-art performance on key quality metrics such as chemical validity, diversity, and PoseBusters checks.

