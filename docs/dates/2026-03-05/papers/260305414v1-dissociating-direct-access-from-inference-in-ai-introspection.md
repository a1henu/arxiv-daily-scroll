---
layout: default
title: Dissociating Direct Access from Inference in AI Introspection
---

# Dissociating Direct Access from Inference in AI Introspection
**arXiv**：[2603.05414v1](https://arxiv.org/abs/2603.05414) · [PDF](https://arxiv.org/pdf/2603.05414.pdf)  
**作者**：Harvey Lederman, Kyle Mahowald  

**一句话要点**：揭示AI内省机制：分离直接访问与推理，发现内容无关的异常检测能力

**关键词**：AI内省, 思想注入检测, 直接访问机制, 概率匹配, 内容无关检测, 大模型分析

## 3 点简述
- 研究AI模型内省机制，复制思想注入检测范式，分析开源大模型行为
- 识别两种可分离机制：概率匹配（基于提示异常推理）和直接访问内部状态
- 直接访问机制内容无关，模型能检测异常但无法可靠识别语义内容

## 摘要（原文）

> Introspection is a foundational cognitive ability, but its mechanism is not well understood. Recent work has shown that AI models can introspect. We study their mechanism of introspection, first extensively replicating Lindsey et al. (2025)'s thought injection detection paradigm in large open-source models. We show that these models detect injected representations via two separable mechanisms: (i) probability-matching (inferring from perceived anomaly of the prompt) and (ii) direct access to internal states. The direct access mechanism is content-agnostic: models detect that an anomaly occurred but cannot reliably identify its semantic content. The two model classes we study confabulate injected concepts that are high-frequency and concrete (e.g., "apple'"); for them correct concept guesses typically require significantly more tokens. This content-agnostic introspective mechanism is consistent with leading theories in philosophy and psychology.

