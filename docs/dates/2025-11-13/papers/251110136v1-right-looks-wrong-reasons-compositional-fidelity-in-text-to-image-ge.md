---
layout: default
title: Right Looks, Wrong Reasons: Compositional Fidelity in Text-to-Image Generation
---

# Right Looks, Wrong Reasons: Compositional Fidelity in Text-to-Image Generation
**arXiv**：[2511.10136v1](https://arxiv.org/abs/2511.10136) · [PDF](https://arxiv.org/pdf/2511.10136.pdf)  
**作者**：Mayank Vatsa, Aparna Bharati, Richa Singh  

**一句话要点**：揭示文本到图像生成中组合保真度失败，提出需根本性架构革新

**关键词**：文本到图像生成, 组合保真度, 逻辑推理, 注意力架构, 评估指标, 训练数据偏差

## 3 点简述
- 核心问题：模型无法处理逻辑组合，在否定、计数和空间关系上表现崩溃
- 方法要点：分析训练数据缺失、注意力架构不适和评估指标偏差
- 实验或效果：显示当前方法无法通过简单扩展解决，需新表示和推理机制

## 摘要（原文）

> The architectural blueprint of today's leading text-to-image models contains a fundamental flaw: an inability to handle logical composition. This survey investigates this breakdown across three core primitives-negation, counting, and spatial relations. Our analysis reveals a dramatic performance collapse: models that are accurate on single primitives fail precipitously when these are combined, exposing severe interference. We trace this failure to three key factors. First, training data show a near-total absence of explicit negations. Second, continuous attention architectures are fundamentally unsuitable for discrete logic. Third, evaluation metrics reward visual plausibility over constraint satisfaction. By analyzing recent benchmarks and methods, we show that current solutions and simple scaling cannot bridge this gap. Achieving genuine compositionality, we conclude, will require fundamental advances in representation and reasoning rather than incremental adjustments to existing architectures.

