---
layout: default
title: HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection
---

# HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection
**arXiv**：[2512.17601v1](https://arxiv.org/abs/2512.17601) · [PDF](https://arxiv.org/pdf/2512.17601.pdf)  
**作者**：Zhaolin Cai, Fan Li, Ziwei Zheng, Haixia Bi, Lijun He  

**一句话要点**：提出HeadHunt-VAD，通过直接识别MLLM中稳健的异常敏感注意力头，实现无需调优的视频异常检测。

**关键词**：视频异常检测, 多模态大语言模型, 注意力机制, 免调优方法, 稳健性分析, 头部级探测

## 3 点简述
- 核心问题：基于MLLM的免调优VAD方法依赖文本输出，存在信息损失、正常性偏差和提示敏感性，难以捕捉细微异常线索。
- 方法要点：设计稳健头部识别模块，通过多标准分析显著性和稳定性，筛选稀疏的异常敏感注意力头，结合轻量级评分器和定位器进行检测。
- 实验或效果：在两个主要VAD基准测试中，HeadHunt-VAD在免调优方法中达到最先进性能，同时保持高效率，验证了头部级探测的实用性。

## 摘要（原文）

> Video Anomaly Detection (VAD) aims to locate events that deviate from normal patterns in videos. Traditional approaches often rely on extensive labeled data and incur high computational costs. Recent tuning-free methods based on Multimodal Large Language Models (MLLMs) offer a promising alternative by leveraging their rich world knowledge. However, these methods typically rely on textual outputs, which introduces information loss, exhibits normalcy bias, and suffers from prompt sensitivity, making them insufficient for capturing subtle anomalous cues. To address these constraints, we propose HeadHunt-VAD, a novel tuning-free VAD paradigm that bypasses textual generation by directly hunting robust anomaly-sensitive internal attention heads within the frozen MLLM. Central to our method is a Robust Head Identification module that systematically evaluates all attention heads using a multi-criteria analysis of saliency and stability, identifying a sparse subset of heads that are consistently discriminative across diverse prompts. Features from these expert heads are then fed into a lightweight anomaly scorer and a temporal locator, enabling efficient and accurate anomaly detection with interpretable outputs. Extensive experiments show that HeadHunt-VAD achieves state-of-the-art performance among tuning-free methods on two major VAD benchmarks while maintaining high efficiency, validating head-level probing in MLLMs as a powerful and practical solution for real-world anomaly detection.

