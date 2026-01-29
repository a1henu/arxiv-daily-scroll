---
layout: default
title: Scaling Medical Reasoning Verification via Tool-Integrated Reinforcement Learning
---

# Scaling Medical Reasoning Verification via Tool-Integrated Reinforcement Learning
**arXiv**：[2601.20221v1](https://arxiv.org/abs/2601.20221) · [PDF](https://arxiv.org/pdf/2601.20221.pdf)  
**作者**：Hang Zhang, Ruheng Wang, Yuelyu Ji, Mingu Kwak, Xizhi Wu, Chenyu Li, Li Zhang, Wenqi Shi, Yifan Peng, Yanshan Wang  

**一句话要点**：提出工具增强的强化学习框架以提升医疗推理验证的可扩展性与准确性

**关键词**：医疗推理验证, 工具增强学习, 迭代强化学习, 自适应课程机制, 医学语料库检索, 可扩展验证

## 3 点简述
- 核心问题：现有医疗推理验证方法仅提供标量奖励且依赖单次检索，缺乏解释性与自适应知识访问。
- 方法要点：结合工具增强验证与迭代强化学习，训练验证器在评估中动态查询外部医学语料库，仅需轨迹级监督。
- 实验或效果：在四个医疗推理基准上显著提升性能，如MedQA准确率提高23.5%，采样预算需求降低8倍。

## 摘要（原文）

> Large language models have achieved strong performance on medical reasoning benchmarks, yet their deployment in clinical settings demands rigorous verification to ensure factual accuracy. While reward models offer a scalable approach for reasoning trace verification, existing methods face two limitations: they produce only scalar reward values without explicit justification, and they rely on single-pass retrieval that precludes adaptive knowledge access as verification unfolds. We introduce $\method$, an agentic framework that addresses these limitations by training medical reasoning verifiers to iteratively query external medical corpora during evaluation. Our approach combines tool-augmented verification with an iterative reinforcement learning paradigm that requires only trace-level supervision, alongside an adaptive curriculum mechanism that dynamically adjusts training data distribution. Across four medical reasoning benchmarks, $\method$ achieves substantial gains over existing methods, improving MedQA accuracy by 23.5% and MedXpertQA by 32.0% relative to the base generator in particular. Crucially, $\method$ demonstrates an $\mathbf{8\times}$ reduction in sampling budget requirement compared to prior reward model baselines. These findings establish that grounding verification in dynamically retrieved evidence offers a principled path toward more reliable medical reasoning systems.

