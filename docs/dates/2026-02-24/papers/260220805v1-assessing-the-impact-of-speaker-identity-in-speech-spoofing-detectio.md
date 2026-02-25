---
layout: default
title: Assessing the Impact of Speaker Identity in Speech Spoofing Detection
---

# Assessing the Impact of Speaker Identity in Speech Spoofing Detection
**arXiv**：[2602.20805v1](https://arxiv.org/abs/2602.20805) · [PDF](https://arxiv.org/pdf/2602.20805.pdf)  
**作者**：Anh-Tuan Dao, Driss Matrouf, Nicholas Evans  

**一句话要点**：提出说话人不变多任务框架，以评估并降低说话人身份对语音欺骗检测的影响。

**关键词**：语音欺骗检测, 说话人身份影响, 多任务学习, 梯度反转层, 说话人不变性

## 3 点简述
- 核心问题：语音欺骗检测系统通常假设嵌入与说话人身份无关，但此假设未经验证。
- 方法要点：在SInMT框架中，通过多任务学习联合说话人识别与欺骗检测，并引入梯度反转层。
- 实验或效果：在四个数据集上评估，说话人不变模型比基线平均等错误率降低17%，对挑战性攻击最高降低48%。

## 摘要（原文）

> Spoofing detection systems are typically trained using diverse recordings from multiple speakers, often assuming that the resulting embeddings are independent of speaker identity. However, this assumption remains unverified. In this paper, we investigate the impact of speaker information on spoofing detection systems. We propose two approaches within our Speaker-Invariant Multi-Task framework, one that models speaker identity within the embeddings and another that removes it. SInMT integrates multi-task learning for joint speaker recognition and spoofing detection, incorporating a gradient reversal layer. Evaluated using four datasets, our speaker-invariant model reduces the average equal error rate by 17% compared to the baseline, with up to 48% reduction for the most challenging attacks (e.g., A11).

