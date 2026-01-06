---
layout: default
title: SynRXN: An Open Benchmark and Curated Dataset for Computational Reaction Modeling
---

# SynRXN: An Open Benchmark and Curated Dataset for Computational Reaction Modeling
**arXiv**：[2601.01943v1](https://arxiv.org/abs/2601.01943) · [PDF](https://arxiv.org/pdf/2601.01943.pdf)  
**作者**：Tieu-Long Phan, Nhu-Ngoc Nguyen Song, Peter F. Stadler  

**一句话要点**：提出SynRXN基准框架与数据集以支持计算机辅助合成规划的公平评估

**关键词**：计算机辅助合成规划, 反应建模基准, 数据集标准化, 评估框架, 开源资源

## 3 点简述
- 核心问题：计算机辅助合成规划缺乏统一基准，数据集异构阻碍方法比较。
- 方法要点：构建五类任务框架，提供版本化数据集、透明划分函数和标准化评估流程。
- 实验或效果：支持公平纵向比较、严格消融测试，降低实际应用中的性能评估门槛。

## 摘要（原文）

> We present SynRXN, a unified benchmarking framework and open-data resource for computer-aided synthesis planning (CASP). SynRXN decomposes end-to-end synthesis planning into five task families, covering reaction rebalancing, atom-to-atom mapping, reaction classification, reaction property prediction, and synthesis route design. Curated, provenance-tracked reaction corpora are assembled from heterogeneous public sources into a harmonized representation and packaged as versioned datasets for each task family, with explicit source metadata, licence tags, and machine-readable manifests that record checksums, and row counts. For every task, SynRXN provides transparent splitting functions that generate leakage-aware train, validation, and test partitions, together with standardized evaluation workflows and metric suites tailored to classification, regression, and structured prediction settings. For sensitive benchmarking, we combine public training and validation data with held-out gold-standard test sets, and contamination-prone tasks such as reaction rebalancing and atom-to-atom mapping are distributed only as evaluation sets and are explicitly not intended for model training. Scripted build recipes enable bitwise-reproducible regeneration of all corpora across machines and over time, and the entire resource is released under permissive open licences to support reuse and extension. By removing dataset heterogeneity and packaging transparent, reusable evaluation scaffolding, SynRXN enables fair longitudinal comparison of CASP methods, supports rigorous ablations and stress tests along the full reaction-informatics pipeline, and lowers the barrier for practitioners who seek robust and comparable performance estimates for real-world synthesis planning workloads.

