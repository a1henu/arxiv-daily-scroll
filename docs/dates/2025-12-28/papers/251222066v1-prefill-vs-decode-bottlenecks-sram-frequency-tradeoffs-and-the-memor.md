---
layout: default
title: Prefill vs. Decode Bottlenecks: SRAM-Frequency Tradeoffs and the Memory-Bandwidth Ceiling
---

# Prefill vs. Decode Bottlenecks: SRAM-Frequency Tradeoffs and the Memory-Bandwidth Ceiling
**arXiv**：[2512.22066v1](https://arxiv.org/abs/2512.22066) · [PDF](https://arxiv.org/pdf/2512.22066.pdf)  
**作者**：Hannah Atmer, Yuan Yao, Thiemo Voigt, Stefanos Kaxiras  

**一句话要点**：分析SRAM大小与频率对LLM推理能效的影响，提出优化硬件配置以提升数据中心能效

**关键词**：大语言模型推理, 能效优化, SRAM设计, 内存带宽瓶颈, 硬件加速器, 数据中心能效

## 3 点简述
- 核心问题：LLM推理中预填充和解码阶段的能效瓶颈，受SRAM大小和频率影响
- 方法要点：结合OpenRAM、LLMCompass和ScaleSIM模拟，量化SRAM泄漏与内存带宽限制
- 实验或效果：识别最优配置为高频率（1200-1400MHz）和小缓冲区（32-64KB），平衡延迟与能效

## 摘要（原文）

> Energy consumption dictates the cost and environmental impact of deploying Large Language Models. This paper investigates the impact of on-chip SRAM size and operating frequency on the energy efficiency and performance of LLM inference, focusing on the distinct behaviors of the compute-bound prefill and memory-bound decode phases. Our simulation methodology combines OpenRAM for energy modeling, LLMCompass for latency simulation, and ScaleSIM for systolic array operational intensity. Our findings show that total energy use is predominantly determined by SRAM size in both phases, with larger buffers significantly increasing static energy due to leakage, which is not offset by corresponding latency benefits. We quantitatively explore the memory-bandwidth bottleneck, demonstrating that while high operating frequencies reduce prefill latency, their positive impact on memory-bound decode latency is capped by the external memory bandwidth. Counter-intuitively, high compute frequency can reduce total energy by reducing execution time and consequently decreasing static energy consumption more than the resulting dynamic power increase. We identify an optimal hardware configuration for the simulated workload: high operating frequencies (1200MHz-1400MHz) and a small local buffer size of 32KB to 64KB. This combination achieves the best energy-delay product, balancing low latency with high energy efficiency. Furthermore, we demonstrate how memory bandwidth acts as a performance ceiling, and that increasing compute frequency only yields performance gains up to the point where the workload becomes memory-bound. This analysis provides concrete architectural insights for designing energy-efficient LLM accelerators, especially for datacenters aiming to minimize their energy overhead.

