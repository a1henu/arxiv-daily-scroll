---
layout: default
title: SafeBench-Seq: A Homology-Clustered, CPU-Only Baseline for Protein Hazard Screening with Physicochemical/Composition Features and Cluster-Aware Confidence Intervals
---

# SafeBench-Seq: A Homology-Clustered, CPU-Only Baseline for Protein Hazard Screening with Physicochemical/Composition Features and Cluster-Aware Confidence Intervals
**arXiv**：[2512.17527v1](https://arxiv.org/abs/2512.17527) · [PDF](https://arxiv.org/pdf/2512.17527.pdf)  
**作者**：Muhammad Haris Khan  

**一句话要点**：提出SafeBench-Seq基准，用于蛋白质序列级危害筛查，基于同源聚类和可解释特征，在CPU上实现可复现评估。

**关键词**：蛋白质危害筛查, 同源聚类评估, 可解释特征, 基准测试, CPU计算, 生物安全

## 3 点简述
- 核心问题：蛋白质设计基础模型存在生物安全风险，缺乏简单、可复现的序列级危害筛查基线。
- 方法要点：使用公开数据构建基准，基于同源聚类（≤40%相似度）和可解释特征（理化描述符和氨基酸组成）。
- 实验或效果：通过聚类级保留评估性能，提供校准概率和置信区间，量化模型鲁棒性和校准质量。

## 摘要（原文）

> Foundation models for protein design raise concrete biosecurity risks, yet the community lacks a simple, reproducible baseline for sequence-level hazard screening that is explicitly evaluated under homology control and runs on commodity CPUs. We introduce SafeBench-Seq, a metadata-only, reproducible benchmark and baseline classifier built entirely from public data (SafeProtein hazards and UniProt benigns) and interpretable features (global physicochemical descriptors and amino-acid composition). To approximate "never-before-seen" threats, we homology-cluster the combined dataset at <=40% identity and perform cluster-level holdouts (no cluster overlap between train/test). We report discrimination (AUROC/AUPRC) and screening-operating points (TPR@1% FPR; FPR@95% TPR) with 95% bootstrap confidence intervals (n=200), and we provide calibrated probabilities via CalibratedClassifierCV (isotonic for Logistic Regression / Random Forest; Platt sigmoid for Linear SVM). We quantify probability quality using Brier score, Expected Calibration Error (ECE; 15 bins), and reliability diagrams. Shortcut susceptibility is probed via composition-preserving residue shuffles and length-/composition-only ablations. Empirically, random splits substantially overestimate robustness relative to homology-clustered evaluation; calibrated linear models exhibit comparatively good calibration, while tree ensembles retain slightly higher Brier/ECE. SafeBench-Seq is CPU-only, reproducible, and releases metadata only (accessions, cluster IDs, split labels), enabling rigorous evaluation without distributing hazardous sequences.

