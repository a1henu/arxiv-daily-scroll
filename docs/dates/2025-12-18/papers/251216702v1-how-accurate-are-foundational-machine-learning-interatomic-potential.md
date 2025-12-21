---
layout: default
title: How accurate are foundational machine learning interatomic potentials for heterogeneous catalysis?
---

# How accurate are foundational machine learning interatomic potentials for heterogeneous catalysis?
**arXiv**：[2512.16702v1](https://arxiv.org/abs/2512.16702) · [PDF](https://arxiv.org/pdf/2512.16702.pdf)  
**作者**：Luuk H. E. Kempen, Raffaele Cheula, Mie Andersen  

**一句话要点**：评估基础机器学习原子间势在异相催化中的零样本准确性，揭示其优势与局限

**关键词**：机器学习原子间势, 异相催化, 零样本评估, 表面吸附, 材料模拟, 性能基准

## 3 点简述
- 核心问题：基础MLIPs在异相催化等实际应用中的性能未知，现有基准多限于有序晶体材料
- 方法要点：系统分析80种MLIPs的零样本性能，覆盖合金、氧化物等表面吸附与反应任务
- 实验或效果：MLIPs在钙钛矿氧化物空位形成能等任务中表现高精度，但在磁性材料中可能灾难性失败

## 摘要（原文）

> Foundational machine learning interatomic potentials (MLIPs) are being developed at a rapid pace, promising closer and closer approximation to ab initio accuracy. This unlocks the possibility to simulate much larger length and time scales. However, benchmarks for these MLIPs are usually limited to ordered, crystalline and bulk materials. Hence, reported performance does not necessarily accurately reflect MLIP performance in real applications such as heterogeneous catalysis. Here, we systematically analyze zero-shot performance of 80 different MLIPs, evaluating tasks typical for heterogeneous catalysis across a range of different data sets, including adsorption and reaction on surfaces of alloyed metals, oxides, and metal-oxide interfacial systems. We demonstrate that current-generation foundational MLIPs can already perform at high accuracy for applications such as predicting vacancy formation energies of perovskite oxides or zero-point energies of supported nanoclusters. However, limitations also exist. We find that many MLIPs catastrophically fail when applied to magnetic materials, and structure relaxation in the MLIP generally increases the energy prediction error compared to single-point evaluation of a previously optimized structure. Comparing low-cost task-specific models to foundational MLIPs, we highlight some core differences between these model approaches and show that -- if considering only accuracy -- these models can compete with the current generation of best-performing MLIPs. Furthermore, we show that no single MLIP universally performs best, requiring users to investigate MLIP suitability for their desired application.

