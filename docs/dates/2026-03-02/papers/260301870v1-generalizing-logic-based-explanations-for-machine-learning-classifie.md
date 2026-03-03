---
layout: default
title: Generalizing Logic-based Explanations for Machine Learning Classifiers via Optimization
---

# Generalizing Logic-based Explanations for Machine Learning Classifiers via Optimization
**arXiv**：[2603.01870v1](https://arxiv.org/abs/2603.01870) · [PDF](https://arxiv.org/pdf/2603.01870.pdf)  
**作者**：Francisco Mateus Rocha Filho, Ajalmar Rêgo da Rocha Neto, Thiago Alves Rocha  

**一句话要点**：提出Onestep和Twostep方法以优化逻辑解释的覆盖范围，解决机器学习分类器解释的约束与计算效率问题。

**关键词**：机器学习解释, 逻辑解释, 分类器, 优化方法, 覆盖范围

## 3 点简述
- 核心问题：逻辑解释方法保证正确性但覆盖范围受限，现有迭代方法在计算成本与覆盖范围间存在权衡。
- 方法要点：Onestep通过单步生成解释消除迭代开销，Twostep采用渐进方法提升覆盖范围。
- 实验或效果：Twostep相比Onestep和先前工作，在数据集上平均提升解释覆盖范围达72.60%。

## 摘要（原文）

> Machine learning models support decision-making, yet the reasons behind their predictions are opaque. Clear and reliable explanations help users make informed decisions and avoid blindly trusting model outputs. However, many existing explanation methods fail to guarantee correctness. Logic-based approaches ensure correctness but often offer overly constrained explanations, limiting coverage. Recent work addresses this by incrementally expanding explanations while maintaining correctness. This process is performed separately for each feature, adjusting both its upper and lower bounds. However, this approach faces a trade-off: smaller increments incur high computational costs, whereas larger ones may lead to explanations covering fewer instances. To overcome this, we propose two novel methods. Onestep builds upon this prior work, generating explanations in a single step for each feature and each bound, eliminating the overhead of an iterative process. \textit{Twostep} takes a gradual approach, improving coverage. Experimental results show that Twostep significantly increases explanation coverage (by up to 72.60\% on average across datasets) compared to Onestep and, consequently, to prior work.

