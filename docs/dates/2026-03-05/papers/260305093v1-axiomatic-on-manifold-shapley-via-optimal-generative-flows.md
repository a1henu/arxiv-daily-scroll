---
layout: default
title: Axiomatic On-Manifold Shapley via Optimal Generative Flows
---

# Axiomatic On-Manifold Shapley via Optimal Generative Flows
**arXiv**：[2603.05093v1](https://arxiv.org/abs/2603.05093) · [PDF](https://arxiv.org/pdf/2603.05093.pdf)  
**作者**：Cenwei Zhang, Lin Zhu, Manxi Lin, Lei You  

**一句话要点**：提出基于最优生成流形的Aumann-Shapley归因理论，解决后验可解释AI中的离流形伪影问题

**关键词**：可解释人工智能, Shapley值归因, 最优传输流, 流形学习, 后验解释方法, 生成模型

## 3 点简述
- 核心问题：传统Shapley归因因启发式基线产生离流形伪影，生成方法存在几何低效与离散漂移
- 方法要点：建立流形上Aumann-Shapley公理化理论，通过动能最小化Wasserstein-2测地线确定唯一梯度线积分
- 实验效果：实现严格流形一致性（零流一致性误差）与优越语义对齐（结构感知总变差），代码已开源

## 摘要（原文）

> Shapley-based attribution is critical for post-hoc XAI but suffers from off-manifold artifacts due to heuristic baselines. While generative methods attempt to address this, they often introduce geometric inefficiency and discretization drift. We propose a formal theory of on-manifold Aumann-Shapley attributions driven by optimal generative flows. We prove a representation theorem establishing the gradient line integral as the unique functional satisfying efficiency and geometric axioms, notably reparameterization invariance. To resolve path ambiguity, we select the kinetic-energy-minimizing Wasserstein-2 geodesic transporting a prior to the data distribution. This yields a canonical attribution family that recovers classical Shapley for additive models and admits provable stability bounds against flow approximation errors. By reframing baseline selection as a variational problem, our method experimentally outperforms baselines, achieving strict manifold adherence via vanishing Flow Consistency Error and superior semantic alignment characterized by Structure-Aware Total Variation. Our code is on https://github.com/cenweizhang/OTFlowSHAP.

