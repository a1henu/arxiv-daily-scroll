---
layout: default
title: LeanCat: A Benchmark Suite for Formal Category Theory in Lean (Part I: 1-Categories)
---

# LeanCat: A Benchmark Suite for Formal Category Theory in Lean (Part I: 1-Categories)
**arXiv**：[2512.24796v1](https://arxiv.org/abs/2512.24796) · [PDF](https://arxiv.org/pdf/2512.24796.pdf)  
**作者**：Rongge Xu, Hui Dai, Yiming Fu, Jiedong Jiang, Tianjiao Nie, Hongwei Wang, Junkai Wang, Holiverse Yang, Jiatong Yang, Zhi-Hao Zhang  

**一句话要点**：提出LeanCat基准套件以评估大语言模型在范畴论形式化中的抽象推理能力

**关键词**：形式定理证明, 范畴论形式化, 基准评估, 大语言模型, Lean数学库, 抽象推理

## 3 点简述
- 当前大语言模型在形式定理证明中进展迅速，但现有基准未能充分衡量现代数学的抽象和库中介推理能力。
- 引入LeanCat作为Lean中的范畴论形式化基准，包含100个任务，按主题和难度分级，用于测试结构化和接口级推理。
- 最佳模型在pass@1下解决8.25%任务，实验显示LeanBridge方法优于单模型基线，旨在跟踪AI和人类在Lean中研究级形式化的进展。

## 摘要（原文）

> Large language models (LLMs) have made rapid progress in formal theorem proving, yet current benchmarks under-measure the kind of abstraction and library-mediated reasoning that organizes modern mathematics. In parallel with FATE's emphasis on frontier algebra, we introduce LeanCat, a Lean benchmark for category-theoretic formalization -- a unifying language for mathematical structure and a core layer of modern proof engineering -- serving as a stress test of structural, interface-level reasoning. Part I: 1-Categories contains 100 fully formalized statement-level tasks, curated into topic families and three difficulty tiers via an LLM-assisted + human grading process. The best model solves 8.25% of tasks at pass@1 (32.50%/4.17%/0.00% by Easy/Medium/High) and 12.00% at pass@4 (50.00%/4.76%/0.00%). We also evaluate LeanBridge which use LeanExplore to search Mathlib, and observe consistent gains over single-model baselines. LeanCat is intended as a compact, reusable checkpoint for tracking both AI and human progress toward reliable, research-level formalization in Lean.

