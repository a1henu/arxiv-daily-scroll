---
layout: default
title: Distributionally Robust Optimization via Generative Ambiguity Modeling
---

# Distributionally Robust Optimization via Generative Ambiguity Modeling
**arXiv**：[2602.08976v1](https://arxiv.org/abs/2602.08976) · [PDF](https://arxiv.org/pdf/2602.08976.pdf)  
**作者**：Jiaqi Wen, Jianyi Yang  

**一句话要点**：提出基于生成模型的模糊集以增强分布鲁棒优化的泛化能力

**关键词**：分布鲁棒优化, 生成模型模糊集, 扩散模型, OOD泛化, 机器学习任务

## 3 点简述
- 研究分布鲁棒优化中模糊集设计问题，需平衡一致性与多样性
- 提出生成模型模糊集，捕捉超出名义分布的对抗分布，保持一致性
- 实现GAS-DRO算法，理论证明收敛性，实验展示优越OOD泛化性能

## 摘要（原文）

> This paper studies Distributionally Robust Optimization (DRO), a fundamental framework for enhancing the robustness and generalization of statistical learning and optimization. An effective ambiguity set for DRO must involve distributions that remain consistent to the nominal distribution while being diverse enough to account for a variety of potential scenarios. Moreover, it should lead to tractable DRO solutions. To this end, we propose generative model-based ambiguity sets that capture various adversarial distributions beyond the nominal support space while maintaining consistency with the nominal distribution. Building on this generative ambiguity modeling, we propose DRO with Generative Ambiguity Set (GAS-DRO), a tractable DRO algorithm that solves the inner maximization over the parameterized generative model space. We formally establish the stationary convergence performance of GAS-DRO. We implement GAS-DRO with a diffusion model and empirically demonstrate its superior Out-of-Distribution (OOD) generalization performance in ML tasks.

