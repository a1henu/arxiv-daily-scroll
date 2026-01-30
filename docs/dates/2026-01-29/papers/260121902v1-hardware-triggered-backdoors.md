---
layout: default
title: Hardware-Triggered Backdoors
---

# Hardware-Triggered Backdoors
**arXiv**：[2601.21902v1](https://arxiv.org/abs/2601.21902) · [PDF](https://arxiv.org/pdf/2601.21902.pdf)  
**作者**：Jonas Möller, Erik Imgrund, Thorsten Eisenhofer, Konrad Rieck  

**一句话要点**：提出硬件触发后门以利用不同硬件推理时的数值差异

**关键词**：硬件触发后门, 机器学习安全, 数值差异攻击, 决策边界操纵, GPU加速器, 第三方模型威胁

## 3 点简述
- 核心问题：机器学习模型在不同硬件上推理时，设计差异导致微小数值变化，可能被利用创建后门。
- 方法要点：通过调整模型决策边界，使相同输入在不同硬件上产生不同预测，利用数值偏差翻转预测。
- 实验或效果：在常见GPU加速器上可靠创建硬件触发后门，揭示第三方模型使用的新攻击向量，并探讨防御措施。

## 摘要（原文）

> Machine learning models are routinely deployed on a wide range of computing hardware. Although such hardware is typically expected to produce identical results, differences in its design can lead to small numerical variations during inference. In this work, we show that these variations can be exploited to create backdoors in machine learning models. The core idea is to shape the model's decision function such that it yields different predictions for the same input when executed on different hardware. This effect is achieved by locally moving the decision boundary close to a target input and then refining numerical deviations to flip the prediction on selected hardware. We empirically demonstrate that these hardware-triggered backdoors can be created reliably across common GPU accelerators. Our findings reveal a novel attack vector affecting the use of third-party models, and we investigate different defenses to counter this threat.

