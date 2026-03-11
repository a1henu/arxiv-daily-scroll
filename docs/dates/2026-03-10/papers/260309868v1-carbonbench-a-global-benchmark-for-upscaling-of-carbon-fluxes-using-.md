---
layout: default
title: CarbonBench: A Global Benchmark for Upscaling of Carbon Fluxes Using Zero-Shot Learning
---

# CarbonBench: A Global Benchmark for Upscaling of Carbon Fluxes Using Zero-Shot Learning
**arXiv**：[2603.09868v1](https://arxiv.org/abs/2603.09868) · [PDF](https://arxiv.org/pdf/2603.09868.pdf)  
**作者**：Aleksei Rozanov, Arvind Renganathan, Yimeng Zhang, Vipin Kumar  

**一句话要点**：提出CarbonBench基准以解决碳通量零样本空间迁移学习评估标准化问题

**关键词**：碳通量上采样, 零样本学习, 空间迁移学习, 时间序列回归, 分布偏移, 地球系统科学

## 3 点简述
- 核心问题：缺乏标准化基准评估碳通量模型在未见生态系统中的零样本空间迁移性能。
- 方法要点：构建全球567个站点数据集，提供分层评估协议和统一特征集。
- 实验或效果：包含树基方法和域泛化架构基线，支持系统比较和分布偏移回归测试。

## 摘要（原文）

> Accurately quantifying terrestrial carbon exchange is essential for climate policy and carbon accounting, yet models must generalize to ecosystems underrepresented in sparse eddy covariance observations. Despite this challenge being a natural instance of zero-shot spatial transfer learning for time series regression, no standardized benchmark exists to rigorously evaluate model performance across geographically distinct locations with different climate regimes and vegetation types.
>   We introduce CarbonBench, the first benchmark for zero-shot spatial transfer in carbon flux upscaling. CarbonBench comprises over 1.3 million daily observations from 567 flux tower sites globally (2000-2024). It provides: (1) stratified evaluation protocols that explicitly test generalization across unseen vegetation types and climate regimes, separating spatial transfer from temporal autocorrelation; (2) a harmonized set of remote sensing and meteorological features to enable flexible architecture design; and (3) baselines ranging from tree-based methods to domain-generalization architectures. By bridging machine learning methodologies and Earth system science, CarbonBench aims to enable systematic comparison of transfer learning methods, serves as a testbed for regression under distribution shift, and contributes to the next-generation climate modeling efforts.

