---
layout: default
title: LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification
---

# LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification
**arXiv**：[2602.21044v1](https://arxiv.org/abs/2602.21044) · [PDF](https://arxiv.org/pdf/2602.21044.pdf)  
**作者**：Yanrui Wu, Lingling Zhang, Xinyu Zhang, Jiayu Chang, Pengyu Li, Xu Jiang, Jingtao Hu, Jun Liu  

**一句话要点**：提出LogicGraph基准以评估多路径逻辑推理，通过神经符号生成与验证构建

**关键词**：多路径逻辑推理, 神经符号生成, 基准评估, 逻辑验证, 语言模型评估

## 3 点简述
- 核心问题：现有LLM评估侧重收敛推理，忽略多路径逻辑推理需求
- 方法要点：基于神经符号框架，利用后向逻辑生成和语义实例化构建基准
- 实验或效果：实验显示模型倾向于早期固定路径，覆盖差距随推理深度增大

## 摘要（原文）

> Evaluations of large language models (LLMs) primarily emphasize convergent logical reasoning, where success is defined by producing a single correct proof. However, many real-world reasoning problems admit multiple valid derivations, requiring models to explore diverse logical paths rather than committing to one route. To address this limitation, we introduce LogicGraph, the first benchmark aimed to systematically evaluate multi-path logical reasoning, constructed via a neuro-symbolic framework that leverages backward logic generation and semantic instantiation. This pipeline yields solver-verified reasoning problems formalized by high-depth multi-path reasoning and inherent logical distractions, where each instance is associated with an exhaustive set of minimal proofs. We further propose a reference-free evaluation framework to rigorously assess model performance in both convergent and divergent regimes. Experiments on state-of-the-art language models reveal a common limitation: models tend to commit early to a single route and fail to explore alternatives, and the coverage gap grows substantially with reasoning depth. LogicGraph exposes this divergence gap and provides actionable insights to motivate future improvements. Our code and data will be released at https://github.com/kkkkarry/LogicGraph.

