---
layout: default
title: Metacognitive Sensitivity for Test-Time Dynamic Model Selection
---

# Metacognitive Sensitivity for Test-Time Dynamic Model Selection
**arXiv**：[2512.10451v1](https://arxiv.org/abs/2512.10451) · [PDF](https://arxiv.org/pdf/2512.10451.pdf)  
**作者**：Le Tuan Minh Trinh, Le Minh Vu Pham, Thi Minh Anh Pham, An Duc Nguyen  

**一句话要点**：提出基于元认知敏感性的测试时动态模型选择框架，以提升集成推理准确性。

**关键词**：元认知敏感性, 测试时模型选择, 置信度校准, 多臂老虎机, 集成学习, 深度学习评估

## 3 点简述
- 核心问题：深度学习模型置信度校准不佳，无法可靠反映自身准确性。
- 方法要点：引入心理学指标meta-d'评估元认知敏感性，并用于基于多臂老虎机的动态模型选择。
- 实验或效果：在多个数据集和模型组合上验证，该方法能超越组成模型的联合推理准确性。

## 摘要（原文）

> A key aspect of human cognition is metacognition - the ability to assess one's own knowledge and judgment reliability. While deep learning models can express confidence in their predictions, they often suffer from poor calibration, a cognitive bias where expressed confidence does not reflect true competence. Do models truly know what they know? Drawing from human cognitive science, we propose a new framework for evaluating and leveraging AI metacognition. We introduce meta-d', a psychologically-grounded measure of metacognitive sensitivity, to characterise how reliably a model's confidence predicts its own accuracy. We then use this dynamic sensitivity score as context for a bandit-based arbiter that performs test-time model selection, learning which of several expert models to trust for a given task. Our experiments across multiple datasets and deep learning model combinations (including CNNs and VLMs) demonstrate that this metacognitive approach improves joint-inference accuracy over constituent models. This work provides a novel behavioural account of AI models, recasting ensemble selection as a problem of evaluating both short-term signals (confidence prediction scores) and medium-term traits (metacognitive sensitivity).

