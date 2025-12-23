---
layout: default
title: Small Language Models as Compiler Experts: Auto-Parallelization for Heterogeneous Systems
---

# Small Language Models as Compiler Experts: Auto-Parallelization for Heterogeneous Systems
**arXiv**：[2512.19250v1](https://arxiv.org/abs/2512.19250) · [PDF](https://arxiv.org/pdf/2512.19250.pdf)  
**作者**：Prathamesh Devadiga  

**一句话要点**：提出小语言模型驱动编译器自动并行化，以解决异构系统复杂性问题

**关键词**：小语言模型, 编译器优化, 自动并行化, 异构系统, 性能评估

## 3 点简述
- 传统自动并行化编译器依赖刚性启发式，难以处理现代异构系统复杂性
- 评估约1B参数小语言模型（如gemma3、llama3.2、qwen2.5）在11个真实内核上的性能
- 平均加速比达6.81倍，卷积操作峰值性能达43.25倍，验证了正确性和鲁棒性

## 摘要（原文）

> Traditional auto-parallelizing compilers, reliant on rigid heuristics, struggle with the complexity of modern heterogeneous systems. This paper presents a comprehensive evaluation of small (approximately 1B parameter) language-model-driven compiler auto-parallelization. We evaluate three models: gemma3, llama3.2, and qwen2.5, using six reasoning strategies across 11 real-world kernels drawn from scientific computing, graph algorithms, and machine learning. Our system is benchmarked against strong compiler baselines, including LLVM Polly, TVM, and Triton. Across 376 total evaluations, the proposed approach achieves an average speedup of 6.81x and a peak performance of 43.25x on convolution operations. We analyze scalability, verify correctness using multiple sanitizers, and confirm robustness across diverse compilers and hardware platforms. Our results demonstrate that small, efficient language models can serve as powerful reasoning engines for complex compiler optimization tasks.

