---
layout: default
title: From Global to Granular: Revealing IQA Model Performance via Correlation Surface
---

# From Global to Granular: Revealing IQA Model Performance via Correlation Surface
**arXiv**：[2601.21738v1](https://arxiv.org/abs/2601.21738) · [PDF](https://arxiv.org/pdf/2601.21738.pdf)  
**作者**：Baoliang Chen, Danni Huang, Hanwei Zhu, Lingyu Zhu, Wei Zhou, Shiqi Wang, Yuming Fang, Weisi Lin  

**一句话要点**：提出Granularity-Modulated Correlation以细粒度分析图像质量评估模型性能

**关键词**：图像质量评估, 相关表面, 粒度调制, 性能分析, MOS差异

## 3 点简述
- 核心问题：全局相关指标如SRCC和PLCC无法捕捉IQA模型在局部质量谱上的性能变化，且对测试样本分布敏感。
- 方法要点：引入Granularity-Modulated Correlation，包括基于MOS和\|ΔMOS\|的粒度调制器和分布调节器，生成相关表面进行3D性能映射。
- 实验或效果：在标准基准测试中，GMC揭示了标量指标不可见的性能特征，提供更信息丰富和可靠的IQA分析范式。

## 摘要（原文）

> Evaluation of Image Quality Assessment (IQA) models has long been dominated by global correlation metrics, such as Pearson Linear Correlation Coefficient (PLCC) and Spearman Rank-Order Correlation Coefficient (SRCC). While widely adopted, these metrics reduce performance to a single scalar, failing to capture how ranking consistency varies across the local quality spectrum. For example, two IQA models may achieve identical SRCC values, yet one ranks high-quality images (related to high Mean Opinion Score, MOS) more reliably, while the other better discriminates image pairs with small quality/MOS differences (related to $\|Δ$MOS$\|$). Such complementary behaviors are invisible under global metrics. Moreover, SRCC and PLCC are sensitive to test-sample quality distributions, yielding unstable comparisons across test sets. To address these limitations, we propose \textbf{Granularity-Modulated Correlation (GMC)}, which provides a structured, fine-grained analysis of IQA performance. GMC includes: (1) a \textbf{Granularity Modulator} that applies Gaussian-weighted correlations conditioned on absolute MOS values and pairwise MOS differences ($\|Δ$MOS$\|$) to examine local performance variations, and (2) a \textbf{Distribution Regulator} that regularizes correlations to mitigate biases from non-uniform quality distributions. The resulting \textbf{correlation surface} maps correlation values as a joint function of MOS and $\|Δ$MOS$\|$, providing a 3D representation of IQA performance. Experiments on standard benchmarks show that GMC reveals performance characteristics invisible to scalar metrics, offering a more informative and reliable paradigm for analyzing, comparing, and deploying IQA models. Codes are available at https://github.com/Dniaaa/GMC.

