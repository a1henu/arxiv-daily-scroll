---
layout: default
title: AscendCraft: Automatic Ascend NPU Kernel Generation via DSL-Guided Transcompilation
---

# AscendCraft: Automatic Ascend NPU Kernel Generation via DSL-Guided Transcompilation
**arXiv**：[2601.22760v1](https://arxiv.org/abs/2601.22760) · [PDF](https://arxiv.org/pdf/2601.22760.pdf)  
**作者**：Zhongzhen Wen, Shudi Shao, Zhong Li, Yu Ge, Tongtong Xu, Yuanyi Lin, Tian Zhang  

**一句话要点**：提出AscendCraft，通过DSL引导的转编译自动生成Ascend NPU内核

**关键词**：Ascend NPU内核生成, DSL引导转编译, LLM代码生成, 高性能计算, 自动内核优化

## 3 点简述
- 核心问题：LLM直接生成AscendC内核正确率极低，因NPU编程模型复杂且示例稀少
- 方法要点：引入轻量级DSL抽象非关键复杂性，并建模Ascend执行语义，再通过约束驱动LLM转编译为AscendC
- 实验或效果：在MultiKernelBench上实现98.1%编译成功率和90.4%功能正确性，46.2%内核性能匹配或超越PyTorch

## 摘要（原文）

> The performance of deep learning models critically depends on efficient kernel implementations, yet developing high-performance kernels for specialized accelerators remains time-consuming and expertise-intensive. While recent work demonstrates that large language models (LLMs) can generate correct and performant GPU kernels, kernel generation for neural processing units (NPUs) remains largely underexplored due to domain-specific programming models, limited public examples, and sparse documentation. Consequently, directly generating AscendC kernels with LLMs yields extremely low correctness, highlighting a substantial gap between GPU and NPU kernel generation.
>   We present AscendCraft, a DSL-guided approach for automatic AscendC kernel generation. AscendCraft introduces a lightweight DSL that abstracts non-essential complexity while explicitly modeling Ascend-specific execution semantics. Kernels are first generated in the DSL using category-specific expert examples and then transcompiled into AscendC through structured, constraint-driven LLM lowering passes. Evaluated on MultiKernelBench across seven operator categories, AscendCraft achieves 98.1% compilation success and 90.4% functional correctness. Moreover, 46.2% of generated kernels match or exceed PyTorch eager execution performance, demonstrating that DSL-guided transcompilation can enable LLMs to generate both correct and competitive NPU kernels. Beyond benchmarks, AscendCraft further demonstrates its generality by successfully generating two correct kernels for newly proposed mHC architecture, achieving performance that substantially surpasses PyTorch eager execution.

