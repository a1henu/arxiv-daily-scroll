---
layout: default
title: DREAMS: A Social Exchange Theory-Informed Modeling of Misinformation Engagement on Social Media
---

# DREAMS: A Social Exchange Theory-Informed Modeling of Misinformation Engagement on Social Media
**arXiv**：[2602.01567v1](https://arxiv.org/abs/2602.01567) · [PDF](https://arxiv.org/pdf/2602.01567.pdf)  
**作者**：Lin Tian, Marian-Andrei Rizoiu  

**一句话要点**：提出DREAMS框架，基于社会交换理论建模社交媒体上的虚假信息参与动态过程。

**关键词**：虚假信息参与预测, 社会交换理论, 序列到序列建模, 跨平台分析, 自适应机制, 社交媒体建模

## 3 点简述
- 核心问题：现有方法将参与视为同质时间序列，忽略社会机制和平台设计的异质性影响。
- 方法要点：DREAMS将参与建模为序列到序列适应问题，整合自适应机制学习情感和上下文信号传播。
- 实验或效果：在跨平台数据集上，DREAMS实现19.25%的平均绝对百分比误差，比最强基线提升43.6%。

## 摘要（原文）

> Social media engagement prediction is a central challenge in computational social science, particularly for understanding how users interact with misinformation. Existing approaches often treat engagement as a homogeneous time-series signal, overlooking the heterogeneous social mechanisms and platform designs that shape how misinformation spreads. In this work, we ask: ``Can neural architectures discover social exchange principles from behavioral data alone?'' We introduce \textsc{Dreams} (\underline{D}isentangled \underline{R}epresentations and \underline{E}pisodic \underline{A}daptive \underline{M}odeling for \underline{S}ocial media misinformation engagements), a social exchange theory-guided framework that models misinformation engagement as a dynamic process of social exchange. Rather than treating engagement as a static outcome, \textsc{Dreams} models it as a sequence-to-sequence adaptation problem, where each action reflects an evolving negotiation between user effort and social reward conditioned by platform context. It integrates adaptive mechanisms to learn how emotional and contextual signals propagate through time and across platforms. On a cross-platform dataset spanning $7$ platforms and 2.37M posts collected between 2021 and 2025, \textsc{Dreams} achieves state-of-the-art performance in predicting misinformation engagements, reaching a mean absolute percentage error of $19.25$\%. This is a $43.6$\% improvement over the strongest baseline. Beyond predictive gains, the model reveals consistent cross-platform patterns that align with social exchange principles, suggesting that integrating behavioral theory can enhance empirical modeling of online misinformation engagement. The source code is available at: https://github.com/ltian678/DREAMS.

