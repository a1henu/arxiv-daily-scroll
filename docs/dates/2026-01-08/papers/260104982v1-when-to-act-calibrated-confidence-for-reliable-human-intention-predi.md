---
layout: default
title: When to Act: Calibrated Confidence for Reliable Human Intention Prediction in Assistive Robotics
---

# When to Act: Calibrated Confidence for Reliable Human Intention Prediction in Assistive Robotics
**arXiv**：[2601.04982v1](https://arxiv.org/abs/2601.04982) · [PDF](https://arxiv.org/pdf/2601.04982.pdf)  
**作者**：Johannes A. Gaus, Winfried Ilg, Daniel Haeufle  

**一句话要点**：提出基于校准概率的安全触发框架，用于辅助机器人中可靠的人类意图预测。

**关键词**：辅助机器人, 意图预测, 置信度校准, 安全触发, 日常活动, 多模态预测

## 3 点简述
- 核心问题：原始模型置信度常无法反映真实正确性，在辅助机器人中带来安全风险。
- 方法要点：通过事后校准对齐预测置信度与经验可靠性，不降低准确性下减少误校准约一个数量级。
- 实验或效果：校准置信度驱动简单ACT/HOLD规则，仅在可靠性高时行动，否则保留辅助，使置信度阈值成为可量化安全参数。

## 摘要（原文）

> Assistive devices must determine both what a user intends to do and how reliable that prediction is before providing support. We introduce a safety-critical triggering framework based on calibrated probabilities for multimodal next-action prediction in Activities of Daily Living. Raw model confidence often fails to reflect true correctness, posing a safety risk. Post-hoc calibration aligns predicted confidence with empirical reliability and reduces miscalibration by about an order of magnitude without affecting accuracy. The calibrated confidence drives a simple ACT/HOLD rule that acts only when reliability is high and withholds assistance otherwise. This turns the confidence threshold into a quantitative safety parameter for assisted actions and enables verifiable behavior in an assistive control loop.

