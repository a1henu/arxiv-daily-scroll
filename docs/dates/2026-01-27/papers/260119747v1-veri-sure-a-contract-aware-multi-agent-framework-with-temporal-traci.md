---
layout: default
title: Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation
---

# Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation
**arXiv**：[2601.19747v1](https://arxiv.org/abs/2601.19747) · [PDF](https://arxiv.org/pdf/2601.19747.pdf)  
**作者**：Jiale Liu, Taiyu Zhou, Tianqi Jiang  

**一句话要点**：提出Veri-Sure多智能体框架，通过设计契约和形式验证解决RTL代码生成的正确性问题

**关键词**：多智能体框架, RTL代码生成, 形式验证, 设计契约, 静态依赖切片, 电子设计自动化

## 3 点简述
- 核心问题：RTL设计中使用LLM时，仿真测试覆盖不足、迭代调试引入回归和语义漂移阻碍硅级正确性
- 方法要点：建立设计契约对齐智能体意图，结合静态依赖切片和形式验证进行局部修复
- 实验或效果：在扩展的VerilogEval-v2-EXT基准上，实现领先的已验证正确RTL代码生成性能

## 摘要（原文）

> In the rapidly evolving field of Electronic Design Automation (EDA), the deployment of Large Language Models (LLMs) for Register-Transfer Level (RTL) design has emerged as a promising direction. However, silicon-grade correctness remains bottlenecked by: (i) limited test coverage and reliability of simulation-centric evaluation, (ii) regressions and repair hallucinations introduced by iterative debugging, and (iii) semantic drift as intent is reinterpreted across agent handoffs. In this work, we propose Veri-Sure, a multi-agent framework that establishes a design contract to align agents' intent and uses a patching mechanism guided by static dependency slicing to perform precise, localized repairs. By integrating a multi-branch verification pipeline that combines trace-driven temporal analysis with formal verification consisting of assertion-based checking and boolean equivalence proofs, Veri-Sure enables functional correctness beyond pure simulations. We also introduce VerilogEval-v2-EXT, extending the original benchmark with 53 more industrial-grade design tasks and stratified difficulty levels, and show that Veri-Sure achieves state-of-the-art verified-correct RTL code generation performance, surpassing standalone LLMs and prior agentic systems.

