---
layout: default
title: Agnostic Language Identification and Generation
---

# Agnostic Language Identification and Generation
**arXiv**：[2601.23258v1](https://arxiv.org/abs/2601.23258) · [PDF](https://arxiv.org/pdf/2601.23258.pdf)  
**作者**：Mikael Møller Høgsgaard, Chirag Pabbaraju  

**一句话要点**：提出无实现性假设的语言识别与生成目标，在更一般场景下获得紧致统计率。

**关键词**：语言识别, 语言生成, 不可知学习, 统计率, 无实现性假设

## 3 点简述
- 核心问题：放松语言识别与生成中的强实现性假设，允许输入数据来自任意分布。
- 方法要点：设计无实现性假设的目标函数，研究语言识别与生成在更一般“不可知”设置下的性能。
- 实验或效果：获得新颖特征刻画和接近紧致的统计率，提升理论通用性。

## 摘要（原文）

> Recent works on language identification and generation have established tight statistical rates at which these tasks can be achieved. These works typically operate under a strong realizability assumption: that the input data is drawn from an unknown distribution necessarily supported on some language in a given collection. In this work, we relax this assumption of realizability entirely, and impose no restrictions on the distribution of the input data. We propose objectives to study both language identification and generation in this more general "agnostic" setup. Across both problems, we obtain novel interesting characterizations and nearly tight rates.

