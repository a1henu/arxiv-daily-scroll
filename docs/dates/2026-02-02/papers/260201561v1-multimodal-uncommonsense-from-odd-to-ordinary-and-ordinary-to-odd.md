---
layout: default
title: Multimodal UNcommonsense: From Odd to Ordinary and Ordinary to Odd
---

# Multimodal UNcommonsense: From Odd to Ordinary and Ordinary to Odd
**arXiv**：[2602.01561v1](https://arxiv.org/abs/2602.01561) · [PDF](https://arxiv.org/pdf/2602.01561.pdf)  
**作者**：Yejin Son, Saejin Kim, Dongjun Min, Younjae Yu  

**一句话要点**：提出多模态非常识基准MUN与检索式上下文学习框架R-ICL，以评估和提升模型在非典型场景中的推理能力。

**关键词**：多模态常识推理, 检索式上下文学习, 基准评估, 非典型场景, 视觉语言模型

## 3 点简述
- 核心问题：多模态常识推理在偏离典型视觉或上下文期望的场景中仍面临挑战。
- 方法要点：通过检索式上下文学习框架R-ICL，利用多模态集成检索器MER从大模型向小模型迁移推理能力。
- 实验或效果：在MUN基准上，R-ICL相比基线方法平均提升8.3%，有效处理低频和非典型设置。

## 摘要（原文）

> Commonsense reasoning in multimodal contexts remains a foundational challenge in artificial intelligence. We introduce Multimodal UNcommonsense(MUN), a benchmark designed to evaluate models' ability to handle scenarios that deviate from typical visual or contextual expectations. MUN pairs visual scenes with surprising or unlikely outcomes described in natural language, prompting models to either rationalize seemingly odd images using everyday logic or uncover unexpected interpretations in ordinary scenes. To support this task, we propose a retrieval-based in-context learning (R-ICL) framework that transfers reasoning capabilities from larger models to smaller ones without additional training. Leveraging a novel Multimodal Ensemble Retriever (MER), our method identifies semantically relevant exemplars even when image and text pairs are deliberately discordant. Experiments show an average improvement of 8.3% over baseline ICL methods, highlighting the effectiveness of R-ICL in low-frequency, atypical settings. MUN opens new directions for evaluating and improving visual-language models' robustness and adaptability in real-world, culturally diverse, and non-prototypical scenarios.

