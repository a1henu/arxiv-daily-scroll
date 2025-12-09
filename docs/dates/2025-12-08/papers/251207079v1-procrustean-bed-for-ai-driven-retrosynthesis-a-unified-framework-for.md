---
layout: default
title: Procrustean Bed for AI-Driven Retrosynthesis: A Unified Framework for Reproducible Evaluation
---

# Procrustean Bed for AI-Driven Retrosynthesis: A Unified Framework for Reproducible Evaluation
**arXiv**：[2512.07079v1](https://arxiv.org/abs/2512.07079) · [PDF](https://arxiv.org/pdf/2512.07079.pdf)  
**作者**：Anton Morgunov, Victor S. Batista  

**一句话要点**：提出RetroCast统一评估框架以解决计算机辅助合成规划中标准化评估缺失的问题

**关键词**：计算机辅助合成规划, 标准化评估, 可复现基准测试, 化学有效性, 合成路线重构, 模型比较

## 3 点简述
- 核心问题：计算机辅助合成规划领域缺乏标准化评估基础设施，现有指标偏重拓扑完成度而非化学有效性
- 方法要点：引入RetroCast框架，标准化异构模型输出，提供可复现基准测试流程和交互式路线检查平台SynthArena
- 实验或效果：评估主流算法发现高可解性常掩盖化学无效性，搜索方法在长程合成计划重构中性能衰减明显

## 摘要（原文）

> Progress in computer-aided synthesis planning (CASP) is obscured by the lack of standardized evaluation infrastructure and the reliance on metrics that prioritize topological completion over chemical validity. We introduce RetroCast, a unified evaluation suite that standardizes heterogeneous model outputs into a common schema to enable statistically rigorous, apples-to-apples comparison. The framework includes a reproducible benchmarking pipeline with stratified sampling and bootstrapped confidence intervals, accompanied by SynthArena, an interactive platform for qualitative route inspection. We utilize this infrastructure to evaluate leading search-based and sequence-based algorithms on a new suite of standardized benchmarks. Our analysis reveals a divergence between "solvability" (stock-termination rate) and route quality; high solvability scores often mask chemical invalidity or fail to correlate with the reproduction of experimental ground truths. Furthermore, we identify a "complexity cliff" in which search-based methods, despite high solvability rates, exhibit a sharp performance decay in reconstructing long-range synthetic plans compared to sequence-based approaches. We release the full framework, benchmark definitions, and a standardized database of model predictions to support transparent and reproducible development in the field.

