---
layout: default
title: Simulation-based Optimization for Augmented Reading
---

# Simulation-based Optimization for Augmented Reading
**arXiv**：[2602.22735v1](https://arxiv.org/abs/2602.22735) · [PDF](https://arxiv.org/pdf/2602.22735.pdf)  
**作者**：Yunpeng Bai, Shengdong Zhao, Antti Oulasvirta  

**一句话要点**：提出基于模拟优化的增强阅读框架，以资源理性模型为基础，实现自适应、可解释的文本界面设计。

**关键词**：增强阅读, 模拟优化, 资源理性模型, 认知资源分配, 文本用户界面, 个性化界面

## 3 点简述
- 核心问题：现有增强阅读系统依赖启发式或数据驱动模型，缺乏系统性和可解释性。
- 方法要点：将增强阅读建模为模拟优化问题，使用模拟读者分配认知资源，并引入离线和在线优化管道。
- 实验或效果：该方法支持自适应、可解释的界面设计，无需仅依赖人工测试，但具体效果未知。

## 摘要（原文）

> Augmented reading systems aim to adapt text presentation to improve comprehension and task performance, yet existing approaches rely heavily on heuristics, opaque data-driven models, or repeated human involvement in the design loop. We propose framing augmented reading as a simulation-based optimization problem grounded in resource-rational models of human reading. These models instantiate a simulated reader that allocates limited cognitive resources, such as attention, memory, and time under task demands, enabling systematic evaluation of text user interfaces. We introduce two complementary optimization pipelines: an offline approach that explores design alternatives using simulated readers, and an online approach that personalizes reading interfaces in real time using ongoing interaction data. Together, this perspective enables adaptive, explainable, and scalable augmented reading design without relying solely on human testing.

