---
layout: default
title: Probing the Reliability of Driving VLMs: From Inconsistent Responses to Grounded Temporal Reasoning
---

# Probing the Reliability of Driving VLMs: From Inconsistent Responses to Grounded Temporal Reasoning
**arXiv**：[2603.09512v1](https://arxiv.org/abs/2603.09512) · [PDF](https://arxiv.org/pdf/2603.09512.pdf)  
**作者**：Chun-Peng Chang, Chen-Yu Wang, Holger Caesar, Alain Pagani  

**一句话要点**：提出FutureVQA基准与自监督调优方法，以提升驾驶视觉语言模型的响应一致性与时序推理能力

**关键词**：驾驶视觉语言模型, 响应一致性, 时序推理, FutureVQA基准, 自监督调优, 链式思维推理

## 3 点简述
- 核心问题：驾驶视觉语言模型存在响应不一致和时序推理不足，影响可靠性
- 方法要点：引入FutureVQA基准评估未来场景推理，并提出基于链式思维的自监督调优方法
- 实验或效果：该方法无需时序标签，有效改善模型的一致性和时序推理性能

## 摘要（原文）

> A reliable driving assistant should provide consistent responses based on temporally grounded reasoning derived from observed information. In this work, we investigate whether Vision-Language Models (VLMs), when applied as driving assistants, can response consistantly and understand how present observations shape future outcomes, or whether their outputs merely reflect patterns memorized during training without temporally grounded reasoning. While recent efforts have integrated VLMs into autonomous driving, prior studies typically emphasize scene understanding and instruction generation, implicitly assuming that strong visual interpretation naturally enables consistant future reasoning and thus ensures reliable decision-making, a claim we critically examine. We focus on two major challenges limiting VLM reliability in this setting: response inconsistency, where minor input perturbations yield different answers or, in some cases, responses degenerate toward near-random guessing, and limited temporal reasoning, in which models fail to reason and align sequential events from current observations, often resulting in incorrect or even contradictory responses. Moreover, we find that models with strong visual understanding do not necessarily perform best on tasks requiring temporal reasoning, indicating a tendency to over-rely on pretrained patterns rather than modeling temporal dynamics. To address these issues, we adopt existing evaluation methods and introduce FutureVQA, a human-annotated benchmark dataset specifically designed to assess future scene reasoning. In addition, we propose a simple yet effective self-supervised tuning approach with chain-of-thought reasoning that improves both consistency and temporal reasoning without requiring temporal labels.

