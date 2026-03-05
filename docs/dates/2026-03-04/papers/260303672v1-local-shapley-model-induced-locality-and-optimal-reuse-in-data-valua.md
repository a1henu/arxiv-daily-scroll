---
layout: default
title: Local Shapley: Model-Induced Locality and Optimal Reuse in Data Valuation
---

# Local Shapley: Model-Induced Locality and Optimal Reuse in Data Valuation
**arXiv**：[2603.03672v1](https://arxiv.org/abs/2603.03672) · [PDF](https://arxiv.org/pdf/2603.03672.pdf)  
**作者**：Xuan Yang, Hsi-Wen Chen, Ming-Syan Chen, Jian Pei  

**一句话要点**：提出Local Shapley方法，利用模型诱导的局部性优化数据估值计算效率

**关键词**：数据估值, Shapley值, 局部性优化, 模型重用, 计算效率

## 3 点简述
- 核心问题：Shapley值计算因指数级联盟空间而#P-hard，现有方法忽略模型预测的局部性。
- 方法要点：基于模型计算路径定义支持集，将Shapley计算投影到局部子集，提出LSMR算法实现最优子集重用。
- 实验或效果：多模型实验显示显著减少重训练次数和加速，同时保持高估值保真度。

## 摘要（原文）

> The Shapley value provides a principled foundation for data valuation, but exact computation is #P-hard due to the exponential coalition space. Existing accelerations remain global and ignore a structural property of modern predictors: for a given test instance, only a small subset of training points influences the prediction. We formalize this model-induced locality through support sets defined by the model's computational pathway (e.g., neighbors in KNN, leaves in trees, receptive fields in GNNs), showing that Shapley computation can be projected onto these supports without loss when locality is exact. This reframes Shapley evaluation as a structured data processing problem over overlapping support-induced subset families rather than exhaustive coalition enumeration. We prove that the intrinsic complexity of Local Shapley is governed by the number of distinct influential subsets, establishing an information-theoretic lower bound on retraining operations. Guided by this result, we propose LSMR (Local Shapley via Model Reuse), an optimal subset-centric algorithm that trains each influential subset exactly once via support mapping and pivot scheduling. For larger supports, we develop LSMR-A, a reuse-aware Monte Carlo estimator that remains unbiased with exponential concentration, with runtime determined by the number of distinct sampled subsets rather than total draws. Experiments across multiple model families demonstrate substantial retraining reductions and speedups while preserving high valuation fidelity.

