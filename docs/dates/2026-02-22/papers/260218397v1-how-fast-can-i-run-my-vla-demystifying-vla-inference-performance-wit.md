---
layout: default
title: How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf
---

# How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf
**arXiv**：[2602.18397v1](https://arxiv.org/abs/2602.18397) · [PDF](https://arxiv.org/pdf/2602.18397.pdf)  
**作者**：Wenqi Jiang, Jason Clemons, Karu Sankaralingam, Christos Kozyrakis  

**一句话要点**：提出VLA-Perf分析模型以解决VLA推理性能评估与设计优化问题

**关键词**：视觉语言动作模型, 推理性能分析, 实时系统部署, 模型架构优化, 硬件网络协同

## 3 点简述
- 核心问题：VLA模型在机器人部署中面临实时推理性能评估不足的挑战
- 方法要点：开发VLA-Perf分析模型，系统研究模型架构与推理系统的组合性能
- 实验或效果：从模型设计和部署角度分析性能影响因素，提炼15条关键指导原则

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently demonstrated impressive capabilities across various embodied AI tasks. While deploying VLA models on real-world robots imposes strict real-time inference constraints, the inference performance landscape of VLA remains poorly understood due to the large combinatorial space of model architectures and inference systems. In this paper, we ask a fundamental research question: How should we design future VLA models and systems to support real-time inference? To address this question, we first introduce VLA-Perf, an analytical performance model that can analyze inference performance for arbitrary combinations of VLA models and inference systems. Using VLA-Perf, we conduct the first systematic study of the VLA inference performance landscape. From a model-design perspective, we examine how inference performance is affected by model scaling, model architectural choices, long-context video inputs, asynchronous inference, and dual-system model pipelines. From the deployment perspective, we analyze where VLA inference should be executed -- on-device, on edge servers, or in the cloud -- and how hardware capability and network performance jointly determine end-to-end latency. By distilling 15 key takeaways from our comprehensive evaluation, we hope this work can provide practical guidance for the design of future VLA models and inference systems.

