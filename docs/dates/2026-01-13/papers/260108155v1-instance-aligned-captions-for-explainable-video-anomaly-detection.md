---
layout: default
title: Instance-Aligned Captions for Explainable Video Anomaly Detection
---

# Instance-Aligned Captions for Explainable Video Anomaly Detection
**arXiv**：[2601.08155v1](https://arxiv.org/abs/2601.08155) · [PDF](https://arxiv.org/pdf/2601.08155.pdf)  
**作者**：Inpyo Song, Minjun Joo, Joonhyung Kwon, Eunji Jeon, Jangwon Lee  

**一句话要点**：提出实例对齐描述以解决视频异常检测中解释缺乏空间基础的问题

**关键词**：视频异常检测, 可解释性, 实例对齐, 空间基础, 多实体交互, 基准数据集

## 3 点简述
- 核心问题：现有可解释视频异常检测方法在多实体交互中缺乏空间基础，导致解释不可验证或不完整
- 方法要点：引入实例对齐描述，将文本声明与特定对象实例及其外观和运动属性链接，提供可验证推理
- 实验或效果：在八个VAD基准和扩展的VIEW360+数据集上实验，揭示当前LLM和VLM方法的局限性，为未来研究提供基准

## 摘要（原文）

> Explainable video anomaly detection (VAD) is crucial for safety-critical applications, yet even with recent progress, much of the research still lacks spatial grounding, making the explanations unverifiable. This limitation is especially pronounced in multi-entity interactions, where existing explainable VAD methods often produce incomplete or visually misaligned descriptions, reducing their trustworthiness. To address these challenges, we introduce instance-aligned captions that link each textual claim to specific object instances with appearance and motion attributes. Our framework captures who caused the anomaly, what each entity was doing, whom it affected, and where the explanationis grounded, enabling verifiable and actionable reasoning. We annotate eight widely used VAD benchmarks and extend the 360-degree egocentric dataset, VIEW360, with 868 additional videos, eight locations, and four new anomaly types, creating VIEW360+, a comprehensive testbed for explainable VAD. Experiments show that our instance-level spatially grounded captions reveal significant limitations in current LLM- and VLM-based methods while providing a robust benchmark for future research in trustworthy and interpretable anomaly detection.

