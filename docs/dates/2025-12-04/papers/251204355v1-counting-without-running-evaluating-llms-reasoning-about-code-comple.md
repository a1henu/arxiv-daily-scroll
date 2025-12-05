---
layout: default
title: Counting Without Running: Evaluating LLMs' Reasoning About Code Complexity
---

# Counting Without Running: Evaluating LLMs' Reasoning About Code Complexity
**arXiv**：[2512.04355v1](https://arxiv.org/abs/2512.04355) · [PDF](https://arxiv.org/pdf/2512.04355.pdf)  
**作者**：Gregory Bolet, Giorgis Georgakoudis, Konstantinos Parasyris, Harshitha Menon, Niranjan Hasabnis, Kirk W. Cameron, Gal Oren  

**一句话要点**：提出gpuFLOPBench基准以评估LLMs在GPU代码复杂度推理中的性能

**关键词**：GPU性能推理, LLM评估基准, 代码复杂度分析, CUDA内核, FLOP计数预测, 硬件微码效应

## 3 点简述
- 核心问题：现有LLMs在预测GPU代码FLOP计数等前瞻性性能推理方面缺乏评估
- 方法要点：基于HeCBench构建包含577个CUDA内核的基准，标注真实FLOP计数和八种执行属性
- 实验或效果：最新LLMs在简单内核上表现完美，但在涉及隐式FLOP的复杂场景中误差巨大

## 摘要（原文）

> Modern GPU software stacks demand developers who can anticipate performance bottlenecks before ever launching a kernel; misjudging floating-point workloads upstream can derail tuning, scheduling, and even hardware procurement. Yet despite rapid progress in code generation, today's Large Language Models (LLMs) are rarely tested on this kind of forward-looking reasoning. We close that gap with gpuFLOPBench, a benchmark that asks models to "count without running" by predicting single and double-precision FLOP counts for 577 CUDA kernels drawn from HeCBench, annotated with ground-truth profiles and eight execution attributes that distinguish trivially analyzable code from kernels whose FLOPs depend on hidden compiler or runtime behavior. Evaluating current closed-source reasoning models shows clear but uneven progress: the newest LLMs achieve perfect classification on straightforward kernels but still incur multiple order-of-magnitude errors whenever implicit FLOPs arise from division, intrinsic math functions, or common subexpressions. These results surface a core limitation of existing code assistants -- the inability to internalize hardware-specific microcode effects -- and position gpuFLOPBench as a focused testbed for developing LLM tooling that can reason about performance with the same rigor as experienced GPU developers. Sources are available at our repository: https://github.com/Scientific-Computing-Lab/gpuFLOPBench

