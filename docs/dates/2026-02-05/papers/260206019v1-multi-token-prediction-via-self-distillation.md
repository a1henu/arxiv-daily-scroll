---
layout: default
title: Multi-Token Prediction via Self-Distillation
---

# Multi-Token Prediction via Self-Distillation
**arXiv**：[2602.06019v1](https://arxiv.org/abs/2602.06019) · [PDF](https://arxiv.org/pdf/2602.06019.pdf)  
**作者**：John Kirchenbauer, Abhimanyu Hans, Brian Bartoldson, Micah Goldblum, Ashwinee Panda, Tom Goldstein  

**一句话要点**：提出自蒸馏方法将自回归语言模型转换为快速多令牌预测模型，以加速推理。

**关键词**：多令牌预测, 自蒸馏, 语言模型加速, 推理优化, 在线蒸馏

## 3 点简述
- 现有加速方法需训练辅助模型和复杂推理流程，部署不便。
- 通过在线蒸馏目标，将预训练模型转换为独立多令牌预测模型，无需额外组件。
- 在GSM8K上，解码速度平均提升3倍以上，准确率下降小于5%。

## 摘要（原文）

> Existing techniques for accelerating language model inference, such as speculative decoding, require training auxiliary speculator models and building and deploying complex inference pipelines. We consider a new approach for converting a pretrained autoregressive language model from a slow single next token prediction model into a fast standalone multi-token prediction model using a simple online distillation objective. The final model retains the exact same implementation as the pretrained initial checkpoint and is deployable without the addition of any auxiliary verifier or other specialized inference code. On GSM8K, our method produces models that can decode more than $3\times$ faster on average at $<5\%$ drop in accuracy relative to single token decoding performance.

