---
layout: default
title: Texo: Formula Recognition within 20M Parameters
---

# Texo: Formula Recognition within 20M Parameters
**arXiv**：[2602.17189v1](https://arxiv.org/abs/2602.17189) · [PDF](https://arxiv.org/pdf/2602.17189.pdf)  
**作者**：Sicheng Mao  

**一句话要点**：提出Texo公式识别模型，以20M参数实现高性能，支持实时推理与浏览器部署。

**关键词**：公式识别, 轻量模型, 蒸馏训练, 实时推理, 浏览器部署

## 3 点简述
- 核心问题：公式识别模型通常参数庞大，难以在消费级硬件或浏览器中实时运行。
- 方法要点：通过注意力设计、词汇与分词器的蒸馏与迁移，构建仅20M参数的轻量模型。
- 实验或效果：性能媲美UniMERNet-T和PPFormulaNet-S，模型大小分别减少80%和65%。

## 摘要（原文）

> In this paper we present Texo, a minimalist yet highperformance formula recognition model that contains only 20 million parameters. By attentive design, distillation and transfer of the vocabulary and the tokenizer, Texo achieves comparable performance to state-of-the-art models such as UniMERNet-T and PPFormulaNet-S, while reducing the model size by 80% and 65%, respectively. This enables real-time inference on consumer-grade hardware and even in-browser deployment. We also developed a web application to demonstrate the model capabilities and facilitate its usage for end users.

