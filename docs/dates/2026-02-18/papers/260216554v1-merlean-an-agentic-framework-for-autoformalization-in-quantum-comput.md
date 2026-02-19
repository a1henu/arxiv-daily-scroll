---
layout: default
title: MerLean: An Agentic Framework for Autoformalization in Quantum Computation
---

# MerLean: An Agentic Framework for Autoformalization in Quantum Computation
**arXiv**：[2602.16554v1](https://arxiv.org/abs/2602.16554) · [PDF](https://arxiv.org/pdf/2602.16554.pdf)  
**作者**：Yuanjie Ren, Jinzheng Li, Yidi Qi  

**一句话要点**：提出MerLean框架以自动化量子计算中的形式化验证

**关键词**：自动形式化, 量子计算, Lean验证, 代理框架, 数学库集成

## 3 点简述
- 核心问题：量子计算领域数学陈述的手动形式化验证耗时且易错
- 方法要点：基于代理框架从LaTeX提取陈述，用Lean 4在Mathlib中形式化并验证
- 实验或效果：在三篇论文中实现端到端形式化，生成2050个Lean声明，减少验证负担

## 摘要（原文）

> We introduce MerLean, a fully automated agentic framework for autoformalization in quantum computation. MerLean extracts mathematical statements from \LaTeX{} source files, formalizes them into verified Lean~4 code built on Mathlib, and translates the result back into human-readable \LaTeX{} for semantic review. We evaluate MerLean on three theoretical quantum computing papers producing 2,050 Lean declarations from 114 statements in total. MerLean achieves end-to-end formalization on all three papers, reducing the verification burden to only the newly introduced definitions and axioms. Our results demonstrate that agentic autoformalization can scale to frontier research, offering both a practical tool for machine-verified peer review and a scalable engine for mining high-quality synthetic data to train future reasoning models. Our approach can also be generalized to any other rigorous research in mathematics and theoretical physics.

