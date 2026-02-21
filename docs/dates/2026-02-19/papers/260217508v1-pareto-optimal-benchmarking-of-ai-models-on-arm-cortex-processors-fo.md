---
layout: default
title: Pareto Optimal Benchmarking of AI Models on ARM Cortex Processors for Sustainable Embedded Systems
---

# Pareto Optimal Benchmarking of AI Models on ARM Cortex Processors for Sustainable Embedded Systems
**arXiv**：[2602.17508v1](https://arxiv.org/abs/2602.17508) · [PDF](https://arxiv.org/pdf/2602.17508.pdf)  
**作者**：Pranay Jain, Maximilian Kasper, Göran Köber, Axel Plinge, Dominik Seuß  

**一句话要点**：提出基于帕累托优化的AI模型基准测试框架，用于ARM Cortex处理器的可持续嵌入式系统设计

**关键词**：嵌入式AI, 能耗优化, 帕累托分析, ARM Cortex处理器, 基准测试框架, 可持续系统

## 3 点简述
- 核心问题：在ARM Cortex处理器上优化AI模型，需平衡能耗、精度和资源利用，以实现可持续嵌入式系统
- 方法要点：设计自动化测试台，通过帕累托分析评估关键性能指标，识别处理器与模型的最佳组合
- 实验或效果：发现浮点运算与推理时间近线性相关，M7适合短推理任务，M4在长任务中能效更高，M0+适用于简单任务

## 摘要（原文）

> This work presents a practical benchmarking framework for optimizing artificial intelligence (AI) models on ARM Cortex processors (M0+, M4, M7), focusing on energy efficiency, accuracy, and resource utilization in embedded systems. Through the design of an automated test bench, we provide a systematic approach to evaluate across key performance indicators (KPIs) and identify optimal combinations of processor and AI model. The research highlights a nearlinear correlation between floating-point operations (FLOPs) and inference time, offering a reliable metric for estimating computational demands. Using Pareto analysis, we demonstrate how to balance trade-offs between energy consumption and model accuracy, ensuring that AI applications meet performance requirements without compromising sustainability. Key findings indicate that the M7 processor is ideal for short inference cycles, while the M4 processor offers better energy efficiency for longer inference tasks. The M0+ processor, while less efficient for complex AI models, remains suitable for simpler tasks. This work provides insights for developers, guiding them to design energy-efficient AI systems that deliver high performance in realworld applications.

