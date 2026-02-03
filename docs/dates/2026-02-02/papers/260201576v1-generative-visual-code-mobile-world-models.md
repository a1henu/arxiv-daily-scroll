---
layout: default
title: Generative Visual Code Mobile World Models
---

# Generative Visual Code Mobile World Models
**arXiv**：[2602.01576v1](https://arxiv.org/abs/2602.01576) · [PDF](https://arxiv.org/pdf/2602.01576.pdf)  
**作者**：Woosung Koh, Sungjun Han, Segyu Lee, Se-Young Yun, Jamin Shin  

**一句话要点**：提出基于可渲染代码生成的视觉移动GUI世界模型，以平衡视觉保真度与文本精确性。

**关键词**：移动GUI世界模型, 视觉语言模型, 代码生成, 视觉保真度, 文本渲染, 数据合成

## 3 点简述
- 当前移动GUI世界模型面临视觉保真度与文本精确性的权衡问题。
- 方法使用视觉语言模型预测可执行网页代码作为GUI状态，结合语言先验与结构化代码预训练。
- 实验表明gWorld在多个基准上优于更大模型，并提升下游策略性能。

## 摘要（原文）

> Mobile Graphical User Interface (GUI) World Models (WMs) offer a promising path for improving mobile GUI agent performance at train- and inference-time. However, current approaches face a critical trade-off: text-based WMs sacrifice visual fidelity, while the inability of visual WMs in precise text rendering led to their reliance on slow, complex pipelines dependent on numerous external models. We propose a novel paradigm: visual world modeling via renderable code generation, where a single Vision-Language Model (VLM) predicts the next GUI state as executable web code that renders to pixels, rather than generating pixels directly. This combines the strengths of both approaches: VLMs retain their linguistic priors for precise text rendering while their pre-training on structured web code enables high-fidelity visual generation. We introduce gWorld (8B, 32B), the first open-weight visual mobile GUI WMs built on this paradigm, along with a data generation framework (gWorld) that automatically synthesizes code-based training data. In extensive evaluation across 4 in- and 2 out-of-distribution benchmarks, gWorld sets a new pareto frontier in accuracy versus model size, outperforming 8 frontier open-weight models over 50.25x larger. Further analyses show that (1) scaling training data via gWorld yields meaningful gains, (2) each component of our pipeline improves data quality, and (3) stronger world modeling improves downstream mobile GUI policy performance.

