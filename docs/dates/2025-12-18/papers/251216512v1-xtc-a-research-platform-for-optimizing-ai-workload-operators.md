---
layout: default
title: XTC, A Research Platform for Optimizing AI Workload Operators
---

# XTC, A Research Platform for Optimizing AI Workload Operators
**arXiv**：[2512.16512v1](https://arxiv.org/abs/2512.16512) · [PDF](https://arxiv.org/pdf/2512.16512.pdf)  
**作者**：Pompougnac Hugo, Guillon Christophe, Noiry Sylvain, Dutilleul Alban, Iooss Guillaume, Rastello Fabrice  

**一句话要点**：提出XTC平台以统一跨编译器的调度与性能评估，解决AI算子优化研究中的可移植性问题。

**关键词**：AI算子优化, 调度语言, 编译器生态, 性能评估, 可移植实验

## 3 点简述
- 核心问题：现有调度语言绑定于特定编译器生态，阻碍公平比较和跨框架重用。
- 方法要点：XTC提供通用API和可复现测量框架，解耦调度规范与代码生成。
- 实验或效果：平台支持可移植实验，加速优化策略研究，具体效果未知。

## 摘要（原文）

> Achieving high efficiency on AI operators demands precise control over computation and data movement. However, existing scheduling languages are locked into specific compiler ecosystems, preventing fair comparison, reuse, and evaluation across frameworks. No unified interface currently decouples scheduling specification from code generation and measurement. We introduce XTC, a platform that unifies scheduling and performance evaluation across compilers. With its common API and reproducible measurement framework, XTC enables portable experimentation and accelerates research on optimization strategies.

