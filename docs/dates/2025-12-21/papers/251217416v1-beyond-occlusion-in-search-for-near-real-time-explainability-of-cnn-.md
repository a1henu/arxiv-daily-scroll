---
layout: default
title: Beyond Occlusion: In Search for Near Real-Time Explainability of CNN-Based Prostate Cancer Classification
---

# Beyond Occlusion: In Search for Near Real-Time Explainability of CNN-Based Prostate Cancer Classification
**arXiv**：[2512.17416v1](https://arxiv.org/abs/2512.17416) · [PDF](https://arxiv.org/pdf/2512.17416.pdf)  
**作者**：Martin Krebs, Jan Obdržálek, Vít Musil, Tomáš Brázdil  

**一句话要点**：提出快速解释方法替代遮挡法，加速基于CNN的前列腺癌分类系统开发与临床交互

**关键词**：前列腺癌分类, CNN解释性, 遮挡法替代, 快速解释方法, 临床AI应用

## 3 点简述
- 核心问题：遮挡法计算耗时，阻碍CNN前列腺癌分类系统的快速开发和病理学家交互
- 方法要点：建立解释方法比较框架，基于标准选择更快的替代方法
- 实验或效果：新方法将解释时间减少至少10倍，不影响输出质量，促进临床AI辅助检测

## 摘要（原文）

> Deep neural networks are starting to show their worth in critical applications such as assisted cancer diagnosis. However, for their outputs to get accepted in practice, the results they provide should be explainable in a way easily understood by pathologists. A well-known and widely used explanation technique is occlusion, which, however, can take a long time to compute, thus slowing the development and interaction with pathologists. In this work, we set out to find a faster replacement for occlusion in a successful system for detecting prostate cancer. Since there is no established framework for comparing the performance of various explanation methods, we first identified suitable comparison criteria and selected corresponding metrics. Based on the results, we were able to choose a different explanation method, which cut the previously required explanation time at least by a factor of 10, without any negative impact on the quality of outputs. This speedup enables rapid iteration in model development and debugging and brings us closer to adopting AI-assisted prostate cancer detection in clinical settings. We propose that our approach to finding the replacement for occlusion can be used to evaluate candidate methods in other related applications.

