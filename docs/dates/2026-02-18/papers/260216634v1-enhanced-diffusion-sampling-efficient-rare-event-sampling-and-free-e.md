---
layout: default
title: Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models
---

# Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models
**arXiv**：[2602.16634v1](https://arxiv.org/abs/2602.16634) · [PDF](https://arxiv.org/pdf/2602.16634.pdf)  
**作者**：Yu Xie, Ludwig Winkler, Lixin Sun, Sarah Lewis, Adam E. Foster, José Jiménez Luna, Tim Hempel, Michael Gastegger, Yaoyi Chen, Iryna Zaporozhets, Cecilia Clementi, Christopher M. Bishop, Frank Noé  

**一句话要点**：提出增强扩散采样方法，以解决扩散模型在平衡采样后仍存在的罕见事件采样问题。

**关键词**：罕见事件采样, 扩散模型, 自由能计算, 分子动力学, 增强采样, 平衡统计

## 3 点简述
- 核心问题：扩散模型虽能高效生成平衡样本，但计算依赖罕见状态的观测值（如折叠自由能）时采样不足。
- 方法要点：通过定量精确的引导协议生成偏置系综，并利用精确重加权恢复平衡统计量。
- 实验或效果：在玩具系统、蛋白质折叠景观中，实现快速、准确、可扩展的平衡性质估计，GPU分钟至小时级完成。

## 摘要（原文）

> The rare-event sampling problem has long been the central limiting factor in molecular dynamics (MD), especially in biomolecular simulation. Recently, diffusion models such as BioEmu have emerged as powerful equilibrium samplers that generate independent samples from complex molecular distributions, eliminating the cost of sampling rare transition events. However, a sampling problem remains when computing observables that rely on states which are rare in equilibrium, for example folding free energies. Here, we introduce enhanced diffusion sampling, enabling efficient exploration of rare-event regions while preserving unbiased thermodynamic estimators. The key idea is to perform quantitatively accurate steering protocols to generate biased ensembles and subsequently recover equilibrium statistics via exact reweighting. We instantiate our framework in three algorithms: UmbrellaDiff (umbrella sampling with diffusion models), $Δ$G-Diff (free-energy differences via tilted ensembles), and MetaDiff (a batchwise analogue for metadynamics). Across toy systems, protein folding landscapes and folding free energies, our methods achieve fast, accurate, and scalable estimation of equilibrium properties within GPU-minutes to hours per system -- closing the rare-event sampling gap that remained after the advent of diffusion-model equilibrium samplers.

