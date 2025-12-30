---
layout: default
title: AKG kernel Agent: A Multi-Agent Framework for Cross-Platform Kernel Synthesis
---

# AKG kernel Agent: A Multi-Agent Framework for Cross-Platform Kernel Synthesis
**arXiv**：[2512.23424v1](https://arxiv.org/abs/2512.23424) · [PDF](https://arxiv.org/pdf/2512.23424.pdf)  
**作者**：Jinye Du, Quan Yuan, Zuyao Zhang, Yanzhi Yi, Jiahui Hu, Wangyi Chen, Yiyang Zhu, Qishui Zheng, Wenxiang Zou, Xiangyu Chang, Zuohe Zheng, Zichun Ye, Chao Liu, Shanni Li, Renwei Zhang, Yiping Deng, Xinwei Hu, Xuefeng Jin, Jie Zhao  

**一句话要点**：提出AKG kernel agent多智能体框架，以自动化跨平台内核生成与优化，应对AI模型计算挑战。

**关键词**：内核生成, 多智能体系统, 跨平台优化, AI计算加速, 领域特定语言

## 3 点简述
- 核心问题：AI模型复杂度提升与硬件多样性导致手动内核优化成为瓶颈，需自动化解决方案。
- 方法要点：基于LLM代码生成能力，设计多智能体系统，支持多种DSL，实现内核生成、迁移与性能调优。
- 实验或效果：在KernelBench上评估，使用Triton DSL在GPU和NPU后端，平均加速比达1.46倍于PyTorch Eager基线。

## 摘要（原文）

> Modern AI models demand high-performance computation kernels. The growing complexity of LLMs, multimodal architectures, and recommendation systems, combined with techniques like sparsity and quantization, creates significant computational challenges. Moreover, frequent hardware updates and diverse chip architectures further complicate this landscape, requiring tailored kernel implementations for each platform. However, manual optimization cannot keep pace with these demands, creating a critical bottleneck in AI system development. Recent advances in LLM code generation capabilities have opened new possibilities for automating kernel development. In this work, we propose AKG kernel agent (AI-driven Kernel Generator), a multi-agent system that automates kernel generation, migration, and performance tuning. AKG kernel agent is designed to support multiple domain-specific languages (DSLs), including Triton, TileLang, CPP, and CUDA-C, enabling it to target different hardware backends while maintaining correctness and portability. The system's modular design allows rapid integration of new DSLs and hardware targets. When evaluated on KernelBench using Triton DSL across GPU and NPU backends, AKG kernel agent achieves an average speedup of 1.46$\times$ over PyTorch Eager baselines implementations, demonstrating its effectiveness in accelerating kernel development for modern AI workloads.

