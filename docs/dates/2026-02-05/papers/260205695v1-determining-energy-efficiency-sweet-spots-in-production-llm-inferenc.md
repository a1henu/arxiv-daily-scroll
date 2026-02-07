---
layout: default
title: Determining Energy Efficiency Sweet Spots in Production LLM Inference
---

# Determining Energy Efficiency Sweet Spots in Production LLM Inference
**arXiv**：[2602.05695v1](https://arxiv.org/abs/2602.05695) · [PDF](https://arxiv.org/pdf/2602.05695.pdf)  
**作者**：Hiari Pizzini Cavagna, Andrea Proia, Giacomo Madella, Giovanni B. Esposito, Francesco Antici, Daniele Cesarini, Zeynep Kiziltan, Andrea Bartolini  

**一句话要点**：提出基于Transformer复杂度的分析模型，以确定LLM推理中的能效甜点，支持生产系统优化。

**关键词**：LLM推理能效, Transformer复杂度分析, 序列长度优化, 生产系统节能, GPU能耗建模

## 3 点简述
- 核心问题：现有方法用线性函数估计LLM推理能耗，但能效呈现非线性依赖，需准确建模。
- 方法要点：从Transformer计算和内存访问复杂度推导分析模型，能精确描述输入输出长度与能效的关系。
- 实验或效果：在NVIDIA H100 GPU上测试1B至9B参数模型，平均MAPE为1.79%，验证模型准确性，指导序列长度优化。

## 摘要（原文）

> Large Language Models (LLMs) inference is central in modern AI applications, making it critical to understand their energy footprint. Existing approaches typically estimate energy consumption through simple linear functions of input and output sequence lengths, yet our observations reveal clear Energy Efficiency regimes: peak efficiency occurs with short-to-moderate inputs and medium-length outputs, while efficiency drops sharply for long inputs or very short outputs, indicating a non-linear dependency. In this work, we propose an analytical model derived from the computational and memory-access complexity of the Transformer architecture, capable of accurately characterizing the efficiency curve as a function of input and output lengths. To assess its accuracy, we evaluate energy consumption using TensorRT-LLM on NVIDIA H100 GPUs across a diverse set of LLMs ranging from 1B to 9B parameters, including OPT, LLaMA, Gemma, Falcon, Qwen2, and Granite, tested over input and output lengths from 64 to 4096 tokens, achieving a mean MAPE of 1.79%. Our results show that aligning sequence lengths with these efficiency "Sweet Spots" can substantially reduce energy usage, supporting informed truncation, summarization, and adaptive generation strategies in production systems.

