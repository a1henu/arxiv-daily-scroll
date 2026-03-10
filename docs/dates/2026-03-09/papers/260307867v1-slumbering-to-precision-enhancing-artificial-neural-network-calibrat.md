---
layout: default
title: Slumbering to Precision: Enhancing Artificial Neural Network Calibration Through Sleep-like Processes
---

# Slumbering to Precision: Enhancing Artificial Neural Network Calibration Through Sleep-like Processes
**arXiv**：[2603.07867v1](https://arxiv.org/abs/2603.07867) · [PDF](https://arxiv.org/pdf/2603.07867.pdf)  
**作者**：Jean Erik Delanois, Aditya Ahuja, Giri P. Krishnan, Maxim Bazhenov  

**一句话要点**：提出睡眠回放巩固方法，通过类睡眠过程增强人工神经网络校准，无需监督再训练。

**关键词**：神经网络校准, 睡眠回放巩固, 温度缩放, Brier分数, 置信度估计, 后训练优化

## 3 点简述
- 核心问题：人工神经网络常过度自信，预测概率与实际准确度不匹配，影响可信度。
- 方法要点：受生物睡眠和自发回放启发，引入睡眠回放巩固，选择性回放内部表示以更新权重。
- 实验或效果：与温度缩放等方法竞争互补，结合后获得最佳Brier分数和熵权衡，提升校准效果。

## 摘要（原文）

> Artificial neural networks are often overconfident, undermining trust because their predicted probabilities do not match actual accuracy. Inspired by biological sleep and the role of spontaneous replay in memory and learning, we introduce Sleep Replay Consolidation (SRC), a novel calibration approach. SRC is a post-training, sleep-like phase that selectively replays internal representations to update network weights and improve calibration without supervised retraining. Across multiple experiments, SRC is competitive with and complementary to standard approaches such as temperature scaling. Combining SRC with temperature scaling achieves the best Brier score and entropy trade-offs for AlexNet and VGG19. These results show that SRC provides a fundamentally novel approach to improving neural network calibration. SRC-based calibration offers a practical path toward more trustworthy confidence estimates and narrows the gap between human-like uncertainty handling and modern deep networks.

