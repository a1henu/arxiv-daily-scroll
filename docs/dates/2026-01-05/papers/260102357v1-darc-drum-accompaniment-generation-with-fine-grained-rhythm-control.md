---
layout: default
title: DARC: Drum accompaniment generation with fine-grained rhythm control
---

# DARC: Drum accompaniment generation with fine-grained rhythm control
**arXiv**：[2601.02357v1](https://arxiv.org/abs/2601.02357) · [PDF](https://arxiv.org/pdf/2601.02357.pdf)  
**作者**：Trey Brosnan  

**一句话要点**：提出DARC模型，通过细粒度节奏控制生成鼓伴奏，以解决音乐创作中结构控制与风格灵活性的平衡问题。

**关键词**：鼓伴奏生成, 细粒度节奏控制, 参数高效微调, 音乐上下文建模, 生成模型

## 3 点简述
- 核心问题：现有生成工具在音乐创作中难以同时提供结构控制和风格灵活性，节奏控制有限。
- 方法要点：基于STAGE模型，使用参数高效微调，结合音乐上下文和显式节奏提示（如节拍盒或敲击音轨）生成鼓伴奏。
- 实验或效果：增强细粒度节奏控制，同时保持音乐上下文感知，提升鼓伴奏生成的实用性和灵活性。

## 摘要（原文）

> In music creation, rapid prototyping is essential for exploring and refining ideas, yet existing generative tools often fall short when users require both structural control and stylistic flexibility. Prior approaches in stem-to-stem generation can condition on other musical stems but offer limited control over rhythm, and timbre-transfer methods allow users to specify specific rhythms, but cannot condition on musical context. We introduce DARC, a generative drum accompaniment model that conditions both on musical context from other stems and explicit rhythm prompts such as beatboxing or tapping tracks. Using parameter-efficient fine-tuning, we augment STAGE, a state-of-the-art drum stem generator, with fine-grained rhythm control while maintaining musical context awareness.

