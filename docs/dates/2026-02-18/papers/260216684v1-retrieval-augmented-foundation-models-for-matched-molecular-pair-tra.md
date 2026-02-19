---
layout: default
title: Retrieval-Augmented Foundation Models for Matched Molecular Pair Transformations to Recapitulate Medicinal Chemistry Intuition
---

# Retrieval-Augmented Foundation Models for Matched Molecular Pair Transformations to Recapitulate Medicinal Chemistry Intuition
**arXiv**：[2602.16684v1](https://arxiv.org/abs/2602.16684) · [PDF](https://arxiv.org/pdf/2602.16684.pdf)  
**作者**：Bo Pan, Peter Zhiping Zhang, Hao-Wei Pang, Alex Zhu, Xiang Yu, Liying Zhang, Liang Zhao  

**一句话要点**：提出检索增强基础模型以生成匹配分子对变换，模拟药物化学直觉

**关键词**：匹配分子对变换, 检索增强生成, 药物化学设计, 可控分子生成, 基础模型

## 3 点简述
- 核心问题：现有方法在分子编辑可控性受限或学习场景局限，难以模拟药物化学家的设计过程。
- 方法要点：基于大规模MMP变换训练基础模型，引入提示机制和检索增强框架MMPT-RAG，实现可控和上下文引导的分子生成。
- 实验或效果：在通用化学语料和专利数据集上验证，提升多样性、新颖性和可控性，并在实际发现场景中恢复真实类似结构。

## 摘要（原文）

> Matched molecular pairs (MMPs) capture the local chemical edits that medicinal chemists routinely use to design analogs, but existing ML approaches either operate at the whole-molecule level with limited edit controllability or learn MMP-style edits from restricted settings and small models. We propose a variable-to-variable formulation of analog generation and train a foundation model on large-scale MMP transformations (MMPTs) to generate diverse variables conditioned on an input variable. To enable practical control, we develop prompting mechanisms that let the users specify preferred transformation patterns during generation. We further introduce MMPT-RAG, a retrieval-augmented framework that uses external reference analogs as contextual guidance to steer generation and generalize from project-specific series. Experiments on general chemical corpora and patent-specific datasets demonstrate improved diversity, novelty, and controllability, and show that our method recovers realistic analog structures in practical discovery scenarios.

