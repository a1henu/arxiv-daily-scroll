---
layout: default
title: LLM-Driven 3D Scene Generation of Agricultural Simulation Environments
---

# LLM-Driven 3D Scene Generation of Agricultural Simulation Environments
**arXiv**：[2602.11706v1](https://arxiv.org/abs/2602.11706) · [PDF](https://arxiv.org/pdf/2602.11706.pdf)  
**作者**：Arafa Yoncalik, Wouter Jansen, Nico Huebel, Mohammad Hasan Rahmani, Jan Steckel  

**一句话要点**：提出多LLM管道以解决农业模拟环境中3D场景生成的领域特定推理、验证和模块化设计问题。

**关键词**：3D场景生成, 大语言模型, 农业模拟, 模块化管道, 检索增强生成, Unreal引擎

## 3 点简述
- 核心问题：现有LLM驱动3D场景生成缺乏领域特定推理、验证机制和模块化设计，导致控制性差和可扩展性低。
- 方法要点：开发模块化多LLM管道，集成3D资产检索、领域知识注入和Unreal引擎代码生成，采用混合优化策略如少样本提示和RAG。
- 实验或效果：通过结构化提示和语义准确性评估，用户研究验证真实感，专家比较显示相比手动设计显著节省时间。

## 摘要（原文）

> Procedural generation techniques in 3D rendering engines have revolutionized the creation of complex environments, reducing reliance on manual design. Recent approaches using Large Language Models (LLMs) for 3D scene generation show promise but often lack domain-specific reasoning, verification mechanisms, and modular design. These limitations lead to reduced control and poor scalability. This paper investigates the use of LLMs to generate agricultural synthetic simulation environments from natural language prompts, specifically to address the limitations of lacking domain-specific reasoning, verification mechanisms, and modular design. A modular multi-LLM pipeline was developed, integrating 3D asset retrieval, domain knowledge injection, and code generation for the Unreal rendering engine using its API. This results in a 3D environment with realistic planting layouts and environmental context, all based on the input prompt and the domain knowledge. To enhance accuracy and scalability, the system employs a hybrid strategy combining LLM optimization techniques such as few-shot prompting, Retrieval-Augmented Generation (RAG), finetuning, and validation. Unlike monolithic models, the modular architecture enables structured data handling, intermediate verification, and flexible expansion. The system was evaluated using structured prompts and semantic accuracy metrics. A user study assessed realism and familiarity against real-world images, while an expert comparison demonstrated significant time savings over manual scene design. The results confirm the effectiveness of multi-LLM pipelines in automating domain-specific 3D scene generation with improved reliability and precision. Future work will explore expanding the asset hierarchy, incorporating real-time generation, and adapting the pipeline to other simulation domains beyond agriculture.

