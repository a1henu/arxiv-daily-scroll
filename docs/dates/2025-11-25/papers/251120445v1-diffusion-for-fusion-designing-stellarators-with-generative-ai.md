---
layout: default
title: Diffusion for Fusion: Designing Stellarators with Generative AI
---

# Diffusion for Fusion: Designing Stellarators with Generative AI
**arXiv**：[2511.20445v1](https://arxiv.org/abs/2511.20445) · [PDF](https://arxiv.org/pdf/2511.20445.pdf)  
**作者**：Misha Padidar, Teresa Huang, Andrew Giuliani, Marina Spivak  

**一句话要点**：提出条件扩散模型以快速生成高质量仿星器设计

**关键词**：仿星器设计, 条件扩散模型, 生成式AI, 等离子体约束, 准对称性

## 3 点简述
- 仿星器设计耗时，传统方法需数小时计算集群求解
- 使用条件扩散模型基于QUASR数据库生成准对称仿星器
- 生成设计偏差小于5%，接近1%目标，可推广未见特性

## 摘要（原文）

> Stellarators are a prospective class of fusion-based power plants that confine a hot plasma with three-dimensional magnetic fields. Typically framed as a PDE-constrained optimization problem, stellarator design is a time-consuming process that can take hours to solve on a computing cluster. Developing fast methods for designing stellarators is crucial for advancing fusion research. Given the recent development of large datasets of optimized stellarators, machine learning approaches have emerged as a potential candidate. Motivated by this, we present an open inverse problem to the machine learning community: to rapidly generate high-quality stellarator designs which have a set of desirable characteristics. As a case study in the problem space, we train a conditional diffusion model on data from the QUASR database to generate quasisymmetric stellarator designs with desirable characteristics (aspect ratio and mean rotational transform). The diffusion model is applied to design stellarators with characteristics not seen during training. We provide evaluation protocols and show that many of the generated stellarators exhibit solid performance: less than 5% deviation from quasisymmetry and the target characteristics. The modest deviation from quasisymmetry highlights an opportunity to reach the sub 1% target. Beyond the case study, we share multiple promising avenues for generative modeling to advance stellarator design.

