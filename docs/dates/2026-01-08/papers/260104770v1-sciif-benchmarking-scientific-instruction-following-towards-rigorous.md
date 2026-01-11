---
layout: default
title: SciIF: Benchmarking Scientific Instruction Following Towards Rigorous Scientific Intelligence
---

# SciIF: Benchmarking Scientific Instruction Following Towards Rigorous Scientific Intelligence
**arXiv**：[2601.04770v1](https://arxiv.org/abs/2601.04770) · [PDF](https://arxiv.org/pdf/2601.04770.pdf)  
**作者**：Encheng Su, Jianyu Wu, Chen Tang, Lintao Wang, Pengze Li, Aoran Wang, Jinouwen Zhang, Yizhou Wang, Yuan Meng, Xinzhu Ma, Shixiang Tang, Houqiang Li  

**一句话要点**：提出SciIF基准以评估大语言模型在科学问题解决中遵循严格约束的能力

**关键词**：科学指令遵循, 基准评估, 大语言模型, 科学推理, 约束满足, 可审计性

## 3 点简述
- 现有基准在评估大语言模型科学能力时存在盲点，如仅关注格式或最终答案正确性
- SciIF通过多学科问题与固定约束目录（科学条件、语义稳定性、特定过程）来评估科学指令遵循
- 基准强调可审计性，要求模型提供约束满足的显式证据，以诊断组合推理失败

## 摘要（原文）

> As large language models (LLMs) transition from general knowledge retrieval to complex scientific discovery, their evaluation standards must also incorporate the rigorous norms of scientific inquiry. Existing benchmarks exhibit a critical blind spot: general instruction-following metrics focus on superficial formatting, while domain-specific scientific benchmarks assess only final-answer correctness, often rewarding models that arrive at the right result with the wrong reasons. To address this gap, we introduce scientific instruction following: the capability to solve problems while strictly adhering to the constraints that establish scientific validity. Specifically, we introduce SciIF, a multi-discipline benchmark that evaluates this capability by pairing university-level problems with a fixed catalog of constraints across three pillars: scientific conditions (e.g., boundary checks and assumptions), semantic stability (e.g., unit and symbol conventions), and specific processes(e.g., required numerical methods). Uniquely, SciIF emphasizes auditability, requiring models to provide explicit evidence of constraint satisfaction rather than implicit compliance. By measuring both solution correctness and multi-constraint adherence, SciIF enables finegrained diagnosis of compositional reasoning failures, ensuring that LLMs can function as reliable agents within the strict logical frameworks of science.

