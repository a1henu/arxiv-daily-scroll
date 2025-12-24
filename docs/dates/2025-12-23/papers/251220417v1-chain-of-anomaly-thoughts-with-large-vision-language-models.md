---
layout: default
title: Chain-of-Anomaly Thoughts with Large Vision-Language Models
---

# Chain-of-Anomaly Thoughts with Large Vision-Language Models
**arXiv**：[2512.20417v1](https://arxiv.org/abs/2512.20417) · [PDF](https://arxiv.org/pdf/2512.20417.pdf)  
**作者**：Pedro Domingos, João Pereira, Vasco Lopes, João Neves, David Semedo  

**一句话要点**：提出Chain-of-Anomaly-Thoughts框架，通过引入异常偏差提升大视觉语言模型在视频监控中的犯罪检测性能。

**关键词**：视频监控, 异常检测, 大视觉语言模型, 多代理推理, 犯罪检测, 推理策略

## 3 点简述
- 核心问题：大视觉语言模型在视频监控中因偏向正常性而难以检测犯罪，现有推理策略缺乏异常偏差。
- 方法要点：设计多代理推理框架，在推理过程中加入归纳性犯罪偏差，通过异常分类层增强检测。
- 实验或效果：在低分辨率视频中异常检测F1分数提升11.8个百分点，高分辨率视频中异常分类提升3.78个百分点。

## 摘要（原文）

> Automated video surveillance with Large Vision-Language Models is limited by their inherent bias towards normality, often failing to detect crimes. While Chain-of-Thought reasoning strategies show significant potential for improving performance in language tasks, the lack of inductive anomaly biases in their reasoning further steers the models towards normal interpretations. To address this, we propose Chain-of-Anomaly-Thoughts (CoAT), a multi-agent reasoning framework that introduces inductive criminal bias in the reasoning process through a final, anomaly-focused classification layer. Our method significantly improves Anomaly Detection, boosting F1-score by 11.8 p.p. on challenging low-resolution footage and Anomaly Classification by 3.78 p.p. in high-resolution videos.

