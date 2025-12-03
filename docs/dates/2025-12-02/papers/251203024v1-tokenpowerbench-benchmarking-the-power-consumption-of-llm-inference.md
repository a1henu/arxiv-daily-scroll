---
layout: default
title: TokenPowerBench: Benchmarking the Power Consumption of LLM Inference
---

# TokenPowerBench: Benchmarking the Power Consumption of LLM Inference
**arXiv**：[2512.03024v1](https://arxiv.org/abs/2512.03024) · [PDF](https://arxiv.org/pdf/2512.03024.pdf)  
**作者**：Chenxu Niu, Wei Zhang, Jie Li, Yongjian Zhao, Tongyang Wang, Xi Wang, Yong Chen  

**一句话要点**：提出TokenPowerBench以解决大语言模型推理功耗测量与分析不足的问题

**关键词**：大语言模型推理, 功耗基准, 能效分析, 开源工具, 阶段对齐测量

## 3 点简述
- 核心问题：现有基准缺乏对LLM推理功耗的测量支持，而推理占功耗90%以上
- 方法要点：结合声明式配置、无专用电表的功耗测量和阶段对齐的指标管道
- 实验或效果：评估了Llama等四个模型系列，覆盖1B至405B参数，并开源工具

## 摘要（原文）

> Large language model (LLM) services now answer billions of queries per day, and industry reports show that inference, not training, accounts for more than 90% of total power consumption. However, existing benchmarks focus on either training/fine-tuning or performance of inference and provide little support for power consumption measurement and analysis of inference. We introduce TokenPowerBench, the first lightweight and extensible benchmark designed for LLM-inference power consumption studies. The benchmark combines (i) a declarative configuration interface covering model choice, prompt set, and inference engine, (ii) a measurement layer that captures GPU-, node-, and system-level power without specialized power meters, and (iii) a phase-aligned metrics pipeline that attributes energy to the prefill and decode stages of every request. These elements make it straight-forward to explore the power consumed by an LLM inference run; furthermore, by varying batch size, context length, parallelism strategy and quantization, users can quickly assess how each setting affects joules per token and other energy-efficiency metrics. We evaluate TokenPowerBench on four of the most widely used model series (Llama, Falcon, Qwen, and Mistral). Our experiments cover from 1 billion parameters up to the frontier-scale Llama3-405B model. Furthermore, we release TokenPowerBench as open source to help users to measure power consumption, forecast operating expenses, and meet sustainability targets when deploying LLM services.

