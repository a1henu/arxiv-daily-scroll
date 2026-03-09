---
layout: default
title: The EpisTwin: A Knowledge Graph-Grounded Neuro-Symbolic Architecture for Personal AI
---

# The EpisTwin: A Knowledge Graph-Grounded Neuro-Symbolic Architecture for Personal AI
**arXiv**：[2603.06290v1](https://arxiv.org/abs/2603.06290) · [PDF](https://arxiv.org/pdf/2603.06290.pdf)  
**作者**：Giovanni Servedio, Potito Aghilar, Alessio Mattiace, Gianni Carmosino, Francesco Musicco, Gabriele Conte, Vito Walter Anelli, Tommaso Di Noia, Francesco Maria Donini  

**一句话要点**：提出EpisTwin神经符号框架，通过个人知识图谱解决个人AI数据碎片化问题。

**关键词**：个人人工智能, 神经符号架构, 知识图谱, 检索增强生成, 多模态语言模型, 视觉细化

## 3 点简述
- 核心问题：个人AI因用户数据分散在孤立孤岛中而受限，现有检索增强生成方法依赖非结构化向量相似性，无法捕捉语义拓扑和时间依赖。
- 方法要点：EpisTwin利用多模态语言模型将异构数据转换为语义三元组，构建可验证的个人知识图谱，并通过图检索增强生成与在线深度视觉细化实现复杂推理。
- 实验或效果：引入PersonalQA-71-100合成基准评估，在多个先进评判模型中展示稳健性能，为可信个人AI提供方向。

## 摘要（原文）

> Personal Artificial Intelligence is currently hindered by the fragmentation of user data across isolated silos. While Retrieval-Augmented Generation offers a partial remedy, its reliance on unstructured vector similarity fails to capture the latent semantic topology and temporal dependencies essential for holistic sensemaking. We introduce EpisTwin, a neuro-symbolic framework that grounds generative reasoning in a verifiable, user-centric Personal Knowledge Graph. EpisTwin leverages Multimodal Language Models to lift heterogeneous, cross-application data into semantic triples. At inference, EpisTwin enables complex reasoning over the personal semantic graph via an agentic coordinator that combines Graph Retrieval-Augmented Generation with Online Deep Visual Refinement, dynamically re-grounding symbolic entities in their raw visual context. We also introduce PersonalQA-71-100, a synthetic benchmark designed to simulate a realistic user's digital footprint and evaluate EpisTwin performance. Our framework demonstrates robust results across a suite of state-of-the-art judge models, offering a promising direction for trustworthy Personal AI.

