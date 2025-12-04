---
layout: default
title: A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses
---

# A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses
**arXiv**：[2512.03458v1](https://arxiv.org/abs/2512.03458) · [PDF](https://arxiv.org/pdf/2512.03458.pdf)  
**作者**：Maryam Maghsoudi, Mohsen Rezaeizadeh, Shihab Shamma  

**一句话要点**：提出基于卷积神经网络的框架，将想象听觉MEG映射为感知响应，以支持脑机接口应用。

**关键词**：脑磁图解码, 想象语音映射, 卷积神经网络, 脑机接口, 听觉响应预测

## 3 点简述
- 核心问题：解码想象语音的神经活动存在时序不确定性和数据集有限性，难以解释。
- 方法要点：使用滑动窗口岭回归和带校准层的卷积神经网络，在个体和群体水平映射想象到感知响应。
- 实验或效果：CNN在多数受试者上显著优于基线，预测与真实感知响应相关性更高，证明映射可行。

## 摘要（原文）

> Decoding imagined speech engages complex neural processes that are difficult to interpret due to uncertainty in timing and the limited availability of imagined-response datasets. In this study, we present a Magnetoencephalography (MEG) dataset collected from trained musicians as they imagined and listened to musical and poetic stimuli. We show that both imagined and perceived brain responses contain consistent, condition-specific information. Using a sliding-window ridge regression model, we first mapped imagined responses to listened responses at the single-subject level, but found limited generalization across subjects. At the group level, we developed an encoder-decoder convolutional neural network with a subject-specific calibration layer that produced stable and generalizable mappings. The CNN consistently outperformed the null model, yielding significantly higher correlations between predicted and true listened responses for nearly all held-out subjects. Our findings demonstrate that imagined neural activity can be transformed into perception-like responses, providing a foundation for future brain-computer interface applications involving imagined speech and music.

