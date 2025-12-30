---
layout: default
title: KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta
---

# KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta
**arXiv**：[2512.23236v1](https://arxiv.org/abs/2512.23236) · [PDF](https://arxiv.org/pdf/2512.23236.pdf)  
**作者**：Gang Liao, Hongsen Qin, Ying Wang, Alicia Golden, Michael Kuchnik, Yavuz Yetim, Jia Jiunn Ang, Chunli Fu, Yihan He, Samuel Hsia, Zewei Jiang, Dianshi Li, Uladzimir Pashkevich, Varna Puvvada, Feng Shi, Matt Steiner, Ruichao Xiao, Nathan Yan, Xiayu Yu, Zhou Fang, Abdul Zainul-Abedin, Ketan Singh, Hongtao Yu, Wenyuan Chi, Barney Huang, Sean Zhang, Noah Weller, Zach Marine, Wyatt Cook, Carole-Jean Wu, Gaoxiang Liu  

**一句话要点**：提出KernelEvolve框架以解决推荐模型在异构AI加速器上的内核生成与优化挑战

**关键词**：内核优化, 异构硬件, 推荐模型, 自动化生成, 图搜索

## 3 点简述
- 核心问题：推荐模型训练与推理面临模型架构、内核原语和硬件异构性三大系统挑战
- 方法要点：基于图搜索的代理内核编码框架，通过多编程抽象层自动化内核生成与优化
- 实验或效果：在KernelBench上实现100%正确率，显著缩短开发时间并提升性能

## 摘要（原文）

> Making deep learning recommendation model (DLRM) training and inference fast and efficient is important. However, this presents three key system challenges - model architecture diversity, kernel primitive diversity, and hardware generation and architecture heterogeneity. This paper presents KernelEvolve-an agentic kernel coding framework-to tackle heterogeneity at-scale for DLRM. KernelEvolve is designed to take kernel specifications as input and automate the process of kernel generation and optimization for recommendation model across heterogeneous hardware architectures. KernelEvolve does so by operating at multiple programming abstractions, from Triton and CuTe DSL to low-level hardware agnostic languages, spanning the full hardware-software optimization stack. The kernel optimization process is described as graph-based search with selection policy, universal operator, fitness function, and termination rule, dynamically adapts to runtime execution context through retrieval-augmented prompt synthesis. We designed, implemented, and deployed KernelEvolve to optimize a wide variety of production recommendation models across generations of NVIDIA and AMD GPUs, as well as Meta's AI accelerators. We validate KernelEvolve on the publicly-available KernelBench suite, achieving 100% pass rate on all 250 problems across three difficulty levels, and 160 PyTorch ATen operators across three heterogeneous hardware platforms, demonstrating 100% correctness. KernelEvolve reduces development time from weeks to hours and achieves substantial performance improvements over PyTorch baselines across diverse production use cases and for heterogeneous AI systems at-scale. Beyond performance efficiency improvements, KernelEvolve significantly mitigates the programmability barrier for new AI hardware by enabling automated kernel generation for in-house developed AI hardware.

