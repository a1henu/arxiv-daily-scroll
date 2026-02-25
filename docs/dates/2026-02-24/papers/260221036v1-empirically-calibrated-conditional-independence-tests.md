---
layout: default
title: Empirically Calibrated Conditional Independence Tests
---

# Empirically Calibrated Conditional Independence Tests
**arXiv**：[2602.21036v1](https://arxiv.org/abs/2602.21036) · [PDF](https://arxiv.org/pdf/2602.21036.pdf)  
**作者**：Milleno Pan, Antoine de Mathelin, Wesley Tansey  

**一句话要点**：提出经验校准条件独立性检验以解决小样本和大样本下检验失效问题

**关键词**：条件独立性检验, 经验校准, 因果发现, 特征选择, 错误发现率控制, 模型误设

## 3 点简述
- 条件独立性检验在因果发现和特征选择中常用，但常因小样本渐近不准确或大样本模型误设而失效
- ECCIT方法通过优化对抗者选择特征和响应函数，测量并校正基础检验的校准偏差
- 在合成和真实数据基准测试中，ECCIT实现有效FDR控制，比现有校准策略具有更高功效

## 摘要（原文）

> Conditional independence tests (CIT) are widely used for causal discovery and feature selection. Even with false discovery rate (FDR) control procedures, they often fail to provide frequentist guarantees in practice. We highlight two common failure modes: (i) in small samples, asymptotic guarantees for many CITs can be inaccurate and even correctly specified models fail to estimate the noise levels and control the error, and (ii) when sample sizes are large but models are misspecified, unaccounted dependencies skew the test's behavior and fail to return uniform p-values under the null. We propose Empirically Calibrated Conditional Independence Tests (ECCIT), a method that measures and corrects for miscalibration. For a chosen base CIT (e.g., GCM, HRT), ECCIT optimizes an adversary that selects features and response functions to maximize a miscalibration metric. ECCIT then fits a monotone calibration map that adjusts the base-test p-values in proportion to the observed miscalibration. Across empirical benchmarks on synthetic and real data, ECCIT achieves valid FDR with higher power than existing calibration strategies while remaining test agnostic.

