---
layout: default
title: Autonomous Probe Microscopy with Robust Bag-of-Features Multi-Objective Bayesian Optimization: Pareto-Front Mapping of Nanoscale Structure-Property Trade-Offs
---

# Autonomous Probe Microscopy with Robust Bag-of-Features Multi-Objective Bayesian Optimization: Pareto-Front Mapping of Nanoscale Structure-Property Trade-Offs
**arXiv**：[2601.05528v1](https://arxiv.org/abs/2601.05528) · [PDF](https://arxiv.org/pdf/2601.05528.pdf)  
**作者**：Kamyar Barakati, Haochen Zhu, C Charlotte Buchanan, Dustin A Gilbert, Philip Rack, Sergei V. Kalinin  

**一句话要点**：提出基于BoF-MOBO的自主扫描探针显微镜框架，以高效探索组合材料库中的纳米结构-性能权衡。

**关键词**：自主扫描探针显微镜, 多目标贝叶斯优化, 组合材料库, 纳米结构表征, 帕累托前沿映射

## 3 点简述
- 核心问题：组合材料库表征速度慢、数据复杂，难以提取结构-性能关系。
- 方法要点：集成静态物理信息BoF表示与多目标贝叶斯优化，实现自动化探索。
- 实验或效果：在Au-Co-Ni系统中验证，重建特征景观，揭示帕累托结构与功能区域。

## 摘要（原文）

> Combinatorial materials libraries are an efficient route to generate large families of candidate compositions, but their impact is often limited by the speed and depth of characterization and by the difficulty of extracting actionable structure-property relations from complex characterization data. Here we develop an autonomous scanning probe microscopy (SPM) framework that integrates automated atomic force and magnetic force microscopy (AFM/MFM) to rapidly explore magnetic and structural properties across combinatorial spread libraries. To enable automated exploration of systems without a clear optimization target, we introduce a combination of a static physics-informed bag-of-features (BoF) representation of measured surface morphology and magnetic structure with multi-objective Bayesian optimization (MOBO) to discover the relative significance and robustness of features. The resulting closed-loop workflow selectively samples the compositional gradient and reconstructs feature landscapes consistent with dense grid "ground truth" measurements. The resulting Pareto structure reveals where multiple nanoscale objectives are simultaneously optimized, where trade-offs between roughness, coherence, and magnetic contrast are unavoidable, and how families of compositions cluster into distinct functional regimes, thereby turning multi-feature imaging data into interpretable maps of competing structure-property trends. While demonstrated for Au-Co-Ni and AFM/MFM, the approach is general and can be extended to other combinatorial systems, imaging modalities, and feature sets, illustrating how feature-based MOBO and autonomous SPM can transform microscopy images from static data products into active feedback for real-time, multi-objective materials discovery.

