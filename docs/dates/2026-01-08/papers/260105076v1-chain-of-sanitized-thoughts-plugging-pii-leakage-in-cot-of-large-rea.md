---
layout: default
title: Chain-of-Sanitized-Thoughts: Plugging PII Leakage in CoT of Large Reasoning Models
---

# Chain-of-Sanitized-Thoughts: Plugging PII Leakage in CoT of Large Reasoning Models
**arXiv**：[2601.05076v1](https://arxiv.org/abs/2601.05076) · [PDF](https://arxiv.org/pdf/2601.05076.pdf)  
**作者**：Arghyadeep Das, Sai Sreenivas Chintha, Rishiraj Girmal, Kinjal Pandey, Sharvi Endait  

**一句话要点**：提出Chain-of-Sanitized-Thoughts方法，通过提示控制和微调减少大型推理模型链式思维中的个人身份信息泄露。

**关键词**：隐私保护推理, 链式思维, 个人身份信息泄露, 提示控制, 微调干预, 基准评估

## 3 点简述
- 核心问题：大型推理模型的链式思维推理过程易泄露个人身份信息，即使最终答案已脱敏。
- 方法要点：引入PII-CoT-Bench数据集和基准，采用提示控制或微调干预，诱导模型进行隐私优先推理。
- 实验或效果：在多种模型和场景下，显著减少信息泄露，同时保持推理性能，为隐私保护推理系统提供实用指导。

## 摘要（原文）

> Large Reasoning Models (LRMs) improve performance, reliability, and interpretability by generating explicit chain-of-thought (CoT) reasoning, but this transparency introduces a serious privacy risk: intermediate reasoning often leaks personally identifiable information (PII) even when final answers are sanitized. We study how to induce privacy-first reasoning, where models reason without exposing sensitive information, using deployable interventions rather than post-hoc redaction. We introduce PII-CoT-Bench, a supervised dataset with privacy-aware CoT annotations, and a category-balanced evaluation benchmark covering realistic and adversarial leakage scenarios. Our results reveal a capability-dependent trend: state-of-the-art models benefit most from prompt-based controls, whereas weaker models require fine-tuning to achieve meaningful leakage reduction. Across models and categories, both approaches substantially reduce PII exposure with minimal degradation in utility, demonstrating that private reasoning can be achieved without sacrificing performance. Overall, we show that private CoT reasoning can be achieved with minimal utility loss, providing practical guidance for building privacy-preserving reasoning systems.

