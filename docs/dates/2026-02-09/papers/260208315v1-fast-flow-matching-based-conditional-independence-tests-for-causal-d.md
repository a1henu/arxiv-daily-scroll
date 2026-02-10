---
layout: default
title: Fast Flow Matching based Conditional Independence Tests for Causal Discovery
---

# Fast Flow Matching based Conditional Independence Tests for Causal Discovery
**arXiv**：[2602.08315v1](https://arxiv.org/abs/2602.08315) · [PDF](https://arxiv.org/pdf/2602.08315.pdf)  
**作者**：Shunyu Zhao, Yanfeng Yang, Shuai Li, Kenji Fukumizu  

**一句话要点**：提出基于流匹配的条件独立性检验以加速因果发现

**关键词**：因果发现, 条件独立性检验, 流匹配, PC算法, 计算效率, 统计检验

## 3 点简述
- 核心问题：基于约束的因果发现方法因条件独立性检验计算量大而受限
- 方法要点：利用流匹配高效性，单次训练模型即可加速检验
- 实验或效果：在合成和真实任务中展示高统计功效与效率平衡

## 摘要（原文）

> Constraint-based causal discovery methods require a large number of conditional independence (CI) tests, which severely limits their practical applicability due to high computational complexity. Therefore, it is crucial to design an algorithm that accelerates each individual test. To this end, we propose the Flow Matching-based Conditional Independence Test (FMCIT). The proposed test leverages the high computational efficiency of flow matching and requires the model to be trained only once throughout the entire causal discovery procedure, substantially accelerating causal discovery. According to numerical experiments, FMCIT effectively controls type-I error and maintains high testing power under the alternative hypothesis, even in the presence of high-dimensional conditioning sets. In addition, we further integrate FMCIT into a two-stage guided PC skeleton learning framework, termed GPC-FMCIT, which combines fast screening with guided, budgeted refinement using FMCIT. This design yields explicit bounds on the number of CI queries while maintaining high statistical power. Experiments on synthetic and real-world causal discovery tasks demonstrate favorable accuracy-efficiency trade-offs over existing CI testing methods and PC variants.

