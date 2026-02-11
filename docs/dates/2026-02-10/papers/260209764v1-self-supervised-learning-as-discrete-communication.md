---
layout: default
title: Self-Supervised Learning as Discrete Communication
---

# Self-Supervised Learning as Discrete Communication
**arXiv**：[2602.09764v1](https://arxiv.org/abs/2602.09764) · [PDF](https://arxiv.org/pdf/2602.09764.pdf)  
**作者**：Kawtar Zaher, Ilyass Moummad, Olivier Buisson, Alexis Joly  

**一句话要点**：提出离散通信框架以增强自监督学习中表征的结构化控制

**关键词**：自监督学习, 离散通信, 二进制表征, 结构化表征, 师生网络, 编码率正则化

## 3 点简述
- 核心问题：连续自监督学习对表征维度信息结构控制有限
- 方法要点：将自监督学习建模为师生网络间通过固定容量二进制通道的离散通信
- 实验或效果：在图像分类、检索等任务上优于连续对齐基线，并展示二进制码的紧凑语义捕获能力

## 摘要（原文）

> Most self-supervised learning (SSL) methods learn continuous visual representations by aligning different views of the same input, offering limited control over how information is structured across representation dimensions. In this work, we frame visual self-supervised learning as a discrete communication process between a teacher and a student network, where semantic information is transmitted through a fixed-capacity binary channel. Rather than aligning continuous features, the student predicts multi-label binary messages produced by the teacher. Discrete agreement is enforced through an element-wise binary cross-entropy objective, while a coding-rate regularization term encourages effective utilization of the constrained channel, promoting structured representations. We further show that periodically reinitializing the projection head strengthens this effect by encouraging embeddings that remain predictive across multiple discrete encodings. Extensive experiments demonstrate consistent improvements over continuous agreement baselines on image classification, retrieval, and dense visual prediction tasks, as well as under domain shift through self-supervised adaptation. Beyond backbone representations, we analyze the learned binary codes and show that they form a compact and informative discrete language, capturing semantic factors reusable across classes.

