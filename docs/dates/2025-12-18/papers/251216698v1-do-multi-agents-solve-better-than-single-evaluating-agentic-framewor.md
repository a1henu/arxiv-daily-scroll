---
layout: default
title: Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning
---

# Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning
**arXiv**：[2512.16698v1](https://arxiv.org/abs/2512.16698) · [PDF](https://arxiv.org/pdf/2512.16698.pdf)  
**作者**：Mahbub E Sobhani, Md. Faiyaz Abdullah Sayeedi, Mohammad Nehad Alam, Proma Hossain Progga, Swakkhar Shatabda  

**一句话要点**：评估多智能体与单智能体框架在图表几何问题解决中的性能差异

**关键词**：多智能体框架, 图表几何问题解决, 视觉数学基准, 开源模型, 闭源模型, 性能评估

## 3 点简述
- 核心问题：多智能体设计在图表几何问题解决中是否优于单智能体，尚不明确。
- 方法要点：系统比较单智能体与多智能体管道在四个视觉数学基准上的表现。
- 实验或效果：开源模型多智能体性能提升显著，闭源模型在经典基准上单智能体更优。

## 摘要（原文）

> Diagram-grounded geometry problem solving is a critical benchmark for multimodal large language models (MLLMs), yet the benefits of multi-agent design over single-agent remain unclear. We systematically compare single-agent and multi-agent pipelines on four visual math benchmarks: Geometry3K, MathVerse, OlympiadBench, and We-Math. For open-source models, multi-agent consistently improves performance. For example, Qwen-2.5-VL (7B) gains +6.8 points and Qwen-2.5-VL (32B) gains +3.3 on Geometry3K, and both Qwen-2.5-VL variants see further gains on OlympiadBench and We-Math. In contrast, the closed-source Gemini-2.0-Flash generally performs better in single-agent mode on classic benchmarks, while multi-agent yields only modest improvements on the newer We-Math dataset. These findings show that multi-agent pipelines provide clear benefits for open-source models and can assist strong proprietary systems on newer, less familiar benchmarks, but agentic decomposition is not universally optimal. All code, data, and reasoning files are available at https://github.com/faiyazabdullah/Interpreter-Solver

