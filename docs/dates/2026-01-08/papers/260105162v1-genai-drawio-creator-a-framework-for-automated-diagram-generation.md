---
layout: default
title: GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation
---

# GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation
**arXiv**：[2601.05162v1](https://arxiv.org/abs/2601.05162) · [PDF](https://arxiv.org/pdf/2601.05162.pdf)  
**作者**：Jinze Yu, Dayuan Jiang  

**一句话要点**：提出GenAI-DrawIO-Creator框架，利用LLMs自动化生成和修改draw.io格式图表

**关键词**：图表生成, 大型语言模型, 结构化视觉推理, 自动化工具, XML格式

## 3 点简述
- 核心问题：图表创建和修改耗时费力，需要自动化解决方案
- 方法要点：集成Claude 3.7进行结构化视觉推理，生成有效XML表示
- 实验或效果：原型能生成准确图表，显著减少创建时间，提高结构保真度

## 摘要（原文）

> Diagrams are crucial for communicating complex information, yet creating and modifying them remains a labor-intensive task. We present GenAI-DrawIO-Creator, a novel framework that leverages Large Language Models (LLMs) to automate diagram generation and manipulation in the structured XML format used by draw.io. Our system integrates Claude 3.7 to reason about structured visual data and produce valid diagram representations. Key contributions include a high-level system design enabling real-time diagram updates, specialized prompt engineering and error-checking to ensure well-formed XML outputs. We demonstrate a working prototype capable of generating accurate diagrams (such as network architectures and flowcharts) from natural language or code, and even replicating diagrams from images. Simulated evaluations show that our approach significantly reduces diagram creation time and produces outputs with high structural fidelity. Our results highlight the promise of Claude 3.7 in handling structured visual reasoning tasks and lay the groundwork for future research in AI-assisted diagramming applications.

