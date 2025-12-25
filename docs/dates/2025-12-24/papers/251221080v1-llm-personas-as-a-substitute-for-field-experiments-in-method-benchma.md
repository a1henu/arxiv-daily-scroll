---
layout: default
title: LLM Personas as a Substitute for Field Experiments in Method Benchmarking
---

# LLM Personas as a Substitute for Field Experiments in Method Benchmarking
**arXiv**：[2512.21080v1](https://arxiv.org/abs/2512.21080) · [PDF](https://arxiv.org/pdf/2512.21080.pdf)  
**作者**：Enoch Hyunwook Kang  

**一句话要点**：提出LLM角色模拟作为社会系统方法基准测试中现场实验的替代方案，并证明其有效性条件。

**关键词**：LLM角色模拟, 基准测试, 现场实验替代, 信息论分析, 社会系统方法, 算法评估

## 3 点简述
- 核心问题：现场实验成本高、延迟大，阻碍方法迭代开发，LLM角色模拟能否替代人类保持基准接口？
- 方法要点：证明在聚合观察和算法盲评条件下，角色替换等同于人群更换，不影响方法优化。
- 实验或效果：定义信息论可区分性，推导角色评估样本量界限，确保基准决策相关性。

## 摘要（原文）

> Field experiments (A/B tests) are often the most credible benchmark for methods in societal systems, but their cost and latency create a major bottleneck for iterative method development. LLM-based persona simulation offers a cheap synthetic alternative, yet it is unclear whether replacing humans with personas preserves the benchmark interface that adaptive methods optimize against. We prove an if-and-only-if characterization: when (i) methods observe only the aggregate outcome (aggregate-only observation) and (ii) evaluation depends only on the submitted artifact and not on the algorithm's identity or provenance (algorithm-blind evaluation), swapping humans for personas is just panel change from the method's point of view, indistinguishable from changing the evaluation population (e.g., New York to Jakarta). Furthermore, we move from validity to usefulness: we define an information-theoretic discriminability of the induced aggregate channel and show that making persona benchmarking as decision-relevant as a field experiment is fundamentally a sample-size question, yielding explicit bounds on the number of independent persona evaluations required to reliably distinguish meaningfully different methods at a chosen resolution.

