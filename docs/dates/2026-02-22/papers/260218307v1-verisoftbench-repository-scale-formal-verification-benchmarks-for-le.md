---
layout: default
title: VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean
---

# VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean
**arXiv**：[2602.18307v1](https://arxiv.org/abs/2602.18307) · [PDF](https://arxiv.org/pdf/2602.18307.pdf)  
**作者**：Yutong Xin, Qiaochu Chen, Greg Durrett, Işil Dillig  

**一句话要点**：提出VeriSoftBench基准，以评估大语言模型在软件验证场景中的定理证明能力。

**关键词**：形式化验证基准, 大语言模型评估, Lean定理证明, 软件验证, 依赖分析

## 3 点简述
- 核心问题：现有基准多基于数学库，缺乏针对软件验证中定义丰富、依赖复杂的代码库的评估。
- 方法要点：构建包含500个Lean 4证明义务的基准，保留真实仓库上下文和跨文件依赖。
- 实验或效果：评估显示，数学库调优的证明器在此场景下表现不佳，性能与依赖闭包大小相关。

## 摘要（原文）

> Large language models have achieved striking results in interactive theorem proving, particularly in Lean. However, most benchmarks for LLM-based proof automation are drawn from mathematics in the Mathlib ecosystem, whereas proofs in software verification are developed inside definition-rich codebases with substantial project-specific libraries. We introduce VeriSoftBench, a benchmark of 500 Lean 4 proof obligations drawn from open-source formal-methods developments and packaged to preserve realistic repository context and cross-file dependencies. Our evaluation of frontier LLMs and specialized provers yields three observations. First, provers tuned for Mathlib-style mathematics transfer poorly to this repository-centric setting. Second, success is strongly correlated with transitive repository dependence: tasks whose proofs draw on large, multi-hop dependency closures are less likely to be solved. Third, providing curated context restricted to a proof's dependency closure improves performance relative to exposing the full repository, but nevertheless leaves substantial room for improvement. Our benchmark and evaluation suite are released at https://github.com/utopia-group/VeriSoftBench.

