---
layout: default
title: LLMStructBench: Benchmarking Large Language Model Structured Data Extraction
---

# LLMStructBench: Benchmarking Large Language Model Structured Data Extraction
**arXiv**：[2602.14743v1](https://arxiv.org/abs/2602.14743) · [PDF](https://arxiv.org/pdf/2602.14743.pdf)  
**作者**：Sönke Tenckhoff, Mario Koddenbrock, Erik Rodner  

**一句话要点**：提出LLMStructBench基准，用于评估大语言模型从自然语言文本提取结构化数据并生成有效JSON输出的能力。

**关键词**：结构化数据提取, JSON生成, 大语言模型评估, 提示策略, 基准测试, 自然语言处理

## 3 点简述
- 核心问题：评估大语言模型在结构化数据提取和JSON生成任务中的性能，缺乏系统基准。
- 方法要点：构建包含多样复杂场景的开放数据集，测试22个模型和五种提示策略，引入互补性能指标。
- 实验或效果：发现提示策略选择比模型大小更重要，能提升结构有效性但可能增加语义错误。

## 摘要（原文）

> We present LLMStructBench, a novel benchmark for evaluating Large Language Models (LLMs) on extracting structured data and generating valid JavaScript Object Notation (JSON) outputs from natural-language text. Our open dataset comprises diverse, manually verified parsing scenarios of varying complexity and enables systematic testing across 22 models and five prompting strategies. We further introduce complementary performance metrics that capture both token-level accuracy and document-level validity, facilitating rigorous comparison of model, size, and prompting effects on parsing reliability.
>   In particular, we show that choosing the right prompting strategy is more important than standard attributes such as model size. This especially ensures structural validity for smaller or less reliable models but increase the number of semantic errors. Our benchmark suite is an step towards future research in the area of LLM applied to parsing or Extract, Transform and Load (ETL) applications.

