---
layout: default
title: A New Benchmark for the Appropriate Evaluation of RTL Code Optimization
---

# A New Benchmark for the Appropriate Evaluation of RTL Code Optimization
**arXiv**：[2601.01765v1](https://arxiv.org/abs/2601.01765) · [PDF](https://arxiv.org/pdf/2601.01765.pdf)  
**作者**：Yao Lu, Shang Liu, Hangan Zhou, Wenji Fang, Qijun Zhang, Zhiyao Xie  

**一句话要点**：提出RTL-OPT基准以评估大语言模型在RTL代码优化中的能力

**关键词**：RTL代码优化, 大语言模型评估, 硬件设计基准, 功耗性能面积, 自动化验证

## 3 点简述
- 现有基准主要评估RTL代码的语法正确性，而非优化质量如功耗、性能和面积
- RTL-OPT包含36个手工设计的数字电路，覆盖组合逻辑、流水线数据路径等类别
- 集成自动化评估框架，验证功能正确性并量化PPA改进，支持标准化评估

## 摘要（原文）

> The rapid progress of artificial intelligence increasingly relies on efficient integrated circuit (IC) design. Recent studies have explored the use of large language models (LLMs) for generating Register Transfer Level (RTL) code, but existing benchmarks mainly evaluate syntactic correctness rather than optimization quality in terms of power, performance, and area (PPA). This work introduces RTL-OPT, a benchmark for assessing the capability of LLMs in RTL optimization. RTL-OPT contains 36 handcrafted digital designs that cover diverse implementation categories including combinational logic, pipelined datapaths, finite state machines, and memory interfaces. Each task provides a pair of RTL codes, a suboptimal version and a human-optimized reference that reflects industry-proven optimization patterns not captured by conventional synthesis tools. Furthermore, RTL-OPT integrates an automated evaluation framework to verify functional correctness and quantify PPA improvements, enabling standardized and meaningful assessment of generative models for hardware design optimization.

