---
layout: default
title: Design and Evaluation of Cost-Aware PoQ for Decentralized LLM Inference
---

# Design and Evaluation of Cost-Aware PoQ for Decentralized LLM Inference
**arXiv**：[2512.16317v1](https://arxiv.org/abs/2512.16317) · [PDF](https://arxiv.org/pdf/2512.16317.pdf)  
**作者**：Arther Tian, Alex Ding, Frank Chen, Alan Wu, Aaron Chan, Bruce Zhang  

**一句话要点**：提出成本感知PoQ框架以解决去中心化LLM推理中异构计算成本忽略的问题

**关键词**：去中心化LLM推理, 成本感知PoQ, 异构计算成本, 评估器架构, 线性奖励函数, 质量成本分析

## 3 点简述
- 核心问题：现有PoQ忽略推理和评估节点的异构计算成本，影响去中心化LLM推理的可扩展性
- 方法要点：集成效率测量到奖励机制，结合F1、轻量评估器和GPT判断，采用线性奖励函数平衡质量和成本
- 实验或效果：实验显示语义文本相似性双编码器评估器性能更优，成本感知奖励方案能有效奖励高质量低成本节点

## 摘要（原文）

> Decentralized large language model (LLM) inference promises transparent and censorship resistant access to advanced AI, yet existing verification approaches struggle to scale to modern models. Proof of Quality (PoQ) replaces cryptographic verification of computation with consensus over output quality, but the original formulation ignores heterogeneous computational costs across inference and evaluator nodes. This paper introduces a cost-aware PoQ framework that integrates explicit efficiency measurements into the reward mechanism for both types of nodes. The design combines ground truth token level F1, lightweight learned evaluators, and GPT based judgments within a unified evaluation pipeline, and adopts a linear reward function that balances normalized quality and cost.
>   Experiments on extractive question answering and abstractive summarization use five instruction tuned LLMs ranging from TinyLlama-1.1B to Llama-3.2-3B and three evaluation models spanning cross encoder and bi encoder architectures. Results show that a semantic textual similarity bi encoder achieves much higher correlation with both ground truth and GPT scores than cross encoders, indicating that evaluator architecture is a critical design choice for PoQ. Quality-cost analysis further reveals that the largest models in the pool are also the most efficient in terms of quality per unit latency. Monte Carlo simulations over 5\,000 PoQ rounds demonstrate that the cost-aware reward scheme consistently assigns higher average rewards to high quality low cost inference models and to efficient evaluators, while penalizing slow low quality nodes. These findings suggest that cost-aware PoQ provides a practical foundation for economically sustainable decentralized LLM inference.

