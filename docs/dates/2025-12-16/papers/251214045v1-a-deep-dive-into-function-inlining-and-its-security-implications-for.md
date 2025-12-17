---
layout: default
title: A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis
---

# A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis
**arXiv**：[2512.14045v1](https://arxiv.org/abs/2512.14045) · [PDF](https://arxiv.org/pdf/2512.14045.pdf)  
**作者**：Omar Abusabha, Jiyong Uhm, Tamer Abuhmed, Hyungjoon Koo  

**一句话要点**：探究函数内联对基于机器学习的二进制分析安全性的影响

**关键词**：函数内联, 二进制分析, 机器学习安全, 编译器优化, 模型鲁棒性

## 3 点简述
- 核心问题：函数内联优化如何影响基于静态特征的机器学习二进制分析模型的安全性
- 方法要点：分析LLVM成本模型的内联决策，提出极端内联策略以评估模型鲁棒性
- 实验或效果：使用20个模型在五个安全任务中测试，发现内联可被利用以规避模型

## 摘要（原文）

> A function inlining optimization is a widely used transformation in modern compilers, which replaces a call site with the callee's body in need. While this transformation improves performance, it significantly impacts static features such as machine instructions and control flow graphs, which are crucial to binary analysis. Yet, despite its broad impact, the security impact of function inlining remains underexplored to date. In this paper, we present the first comprehensive study of function inlining through the lens of machine learning-based binary analysis. To this end, we dissect the inlining decision pipeline within the LLVM's cost model and explore the combinations of the compiler options that aggressively promote the function inlining ratio beyond standard optimization levels, which we term extreme inlining. We focus on five ML-assisted binary analysis tasks for security, using 20 unique models to systematically evaluate their robustness under extreme inlining scenarios. Our extensive experiments reveal several significant findings: i) function inlining, though a benign transformation in intent, can (in)directly affect ML model behaviors, being potentially exploited by evading discriminative or generative ML models; ii) ML models relying on static features can be highly sensitive to inlining; iii) subtle compiler settings can be leveraged to deliberately craft evasive binary variants; and iv) inlining ratios vary substantially across applications and build configurations, undermining assumptions of consistency in training and evaluation of ML models.

