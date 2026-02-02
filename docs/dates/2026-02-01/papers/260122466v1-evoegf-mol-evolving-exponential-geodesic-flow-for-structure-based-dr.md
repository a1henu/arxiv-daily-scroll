---
layout: default
title: EvoEGF-Mol: Evolving Exponential Geodesic Flow for Structure-based Drug Design
---

# EvoEGF-Mol: Evolving Exponential Geodesic Flow for Structure-based Drug Design
**arXiv**：[2601.22466v1](https://arxiv.org/abs/2601.22466) · [PDF](https://arxiv.org/pdf/2601.22466.pdf)  
**作者**：Yaowei Jin, Junjie Wang, Cheng Cao, Penglei Wang, Duo An, Qian Shi  

**一句话要点**：提出EvoEGF-Mol，通过指数测地流解决基于结构的药物设计中统计流形不匹配问题。

**关键词**：基于结构的药物设计, 指数测地流, Fisher-Rao度量, 统计流形, 分子生成, 药物发现

## 3 点简述
- 核心问题：传统方法在欧几里得和概率空间分别构建路径，导致与统计流形不匹配。
- 方法要点：将分子建模为复合指数族分布，在Fisher-Rao度量下沿指数测地线定义生成流，避免轨迹崩溃。
- 实验或效果：在CrossDock上达到93.4%的PoseBusters通过率，在MolGenBench任务中超越基线，生成符合MedChem过滤器的候选分子。

## 摘要（原文）

> Structure-Based Drug Design (SBDD) aims to discover bioactive ligands. Conventional approaches construct probability paths separately in Euclidean and probabilistic spaces for continuous atomic coordinates and discrete chemical categories, leading to a mismatch with the underlying statistical manifolds. We address this issue from an information-geometric perspective by modeling molecules as composite exponential-family distributions and defining generative flows along exponential geodesics under the Fisher-Rao metric. To avoid the instantaneous trajectory collapse induced by geodesics directly targeting Dirac distributions, we propose Evolving Exponential Geodesic Flow for SBDD (EvoEGF-Mol), which replaces static Dirac targets with dynamically concentrating distributions, ensuring stable training via a progressive-parameter-refinement architecture. Our model approaches a reference-level PoseBusters passing rate (93.4%) on CrossDock, demonstrating remarkable geometric precision and interaction fidelity, while outperforming baselines on real-world MolGenBench tasks by recovering bioactive scaffolds and generating candidates that meet established MedChem filters.

