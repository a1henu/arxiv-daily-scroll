---
layout: default
title: Right Looks, Wrong Reasons: Compositional Fidelity in Text-to-Image Generation
---

# Right Looks, Wrong Reasons: Compositional Fidelity in Text-to-Image Generation
**arXiv**：[2511.10136v1](https://arxiv.org/abs/2511.10136) · [PDF](https://arxiv.org/pdf/2511.10136.pdf)  
**作者**：Mayank Vatsa, Aparna Bharati, Richa Singh  

**一句话要点**：揭示文本到图像生成中组合逻辑失效问题及其根本原因

**关键词**：文本到图像生成, 组合逻辑, 否定处理, 空间关系, 模型评估, 注意力架构

## 3 点简述
- 核心问题：当前模型无法处理逻辑组合，如否定、计数和空间关系，导致性能崩溃。
- 方法要点：分析训练数据缺失、注意力架构不适用和评估指标偏差三个关键因素。
- 实验或效果：显示简单扩展无法解决，需根本性表示和推理进步。

## 摘要（原文）

> The architectural blueprint of today's leading text-to-image models contains a fundamental flaw: an inability to handle logical composition. This survey investigates this breakdown across three core primitives-negation, counting, and spatial relations. Our analysis reveals a dramatic performance collapse: models that are accurate on single primitives fail precipitously when these are combined, exposing severe interference. We trace this failure to three key factors. First, training data show a near-total absence of explicit negations. Second, continuous attention architectures are fundamentally unsuitable for discrete logic. Third, evaluation metrics reward visual plausibility over constraint satisfaction. By analyzing recent benchmarks and methods, we show that current solutions and simple scaling cannot bridge this gap. Achieving genuine compositionality, we conclude, will require fundamental advances in representation and reasoning rather than incremental adjustments to existing architectures.

