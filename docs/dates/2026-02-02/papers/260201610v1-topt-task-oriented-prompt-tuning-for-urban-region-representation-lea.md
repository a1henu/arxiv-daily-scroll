---
layout: default
title: ToPT: Task-Oriented Prompt Tuning for Urban Region Representation Learning
---

# ToPT: Task-Oriented Prompt Tuning for Urban Region Representation Learning
**arXiv**：[2602.01610v1](https://arxiv.org/abs/2602.01610) · [PDF](https://arxiv.org/pdf/2602.01610.pdf)  
**作者**：Zitao Guo, Changyang Jiang, Tianhong Zhao, Jinzhou Cao, Genan Dai, Bowen Zhang  

**一句话要点**：提出ToPT框架，通过空间感知嵌入和任务导向提示解决城市区域表示学习中的空间不一致和任务语义对齐问题。

**关键词**：城市区域表示学习, 空间先验建模, 任务导向提示, 多模态大语言模型, 图注意力网络

## 3 点简述
- 核心问题：现有方法缺乏空间先验导致区域建模不连贯，且任务语义对齐机制不明确。
- 方法要点：SREL模块注入空间先验作为注意力偏置，Prompt4RE模块利用MLLM生成语义向量并通过交叉注意力对齐区域嵌入。
- 实验或效果：在多个任务和城市上实现SOTA性能，最高提升64.2%，验证了空间先验和提示对齐的必要性与互补性。

## 摘要（原文）

> Learning effective region embeddings from heterogeneous urban data underpins key urban computing tasks (e.g., crime prediction, resource allocation). However, prevailing two-stage methods yield task-agnostic representations, decoupling them from downstream objectives. Recent prompt-based approaches attempt to fix this but introduce two challenges: they often lack explicit spatial priors, causing spatially incoherent inter-region modeling, and they lack robust mechanisms for explicit task-semantic alignment. We propose ToPT, a two-stage framework that delivers spatially consistent fusion and explicit task alignment. ToPT consists of two modules: spatial-aware region embedding learning (SREL) and task-aware prompting for region embeddings (Prompt4RE). SREL employs a Graphormer-based fusion module that injects spatial priors-distance and regional centrality-as learnable attention biases to capture coherent, interpretable inter-region interactions. Prompt4RE performs task-oriented prompting: a frozen multimodal large language model (MLLM) processes task-specific templates to obtain semantic vectors, which are aligned with region embeddings via multi-head cross-attention for stable task conditioning. Experiments across multiple tasks and cities show state-of-the-art performance, with improvements of up to 64.2\%, validating the necessity and complementarity of spatial priors and prompt-region alignment. The code is available at https://github.com/townSeven/Prompt4RE.git.

