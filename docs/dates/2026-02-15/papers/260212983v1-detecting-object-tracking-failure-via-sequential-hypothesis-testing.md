---
layout: default
title: Detecting Object Tracking Failure via Sequential Hypothesis Testing
---

# Detecting Object Tracking Failure via Sequential Hypothesis Testing
**arXiv**：[2602.12983v1](https://arxiv.org/abs/2602.12983) · [PDF](https://arxiv.org/pdf/2602.12983.pdf)  
**作者**：Alejandro Monroy Muñoz, Rajeev Verma, Alexander Timans  

**一句话要点**：提出基于序贯假设检验的物体跟踪失败检测方法，以增强实时跟踪系统的安全性。

**关键词**：物体跟踪, 序贯假设测试, 安全保证, 实时系统, 模型无关, 失败检测

## 3 点简述
- 核心问题：实时物体跟踪系统缺乏形式化安全保证，难以可靠判断跟踪失败时机。
- 方法要点：将跟踪失败检测建模为序贯假设检验，利用e-process累积证据，控制误报率。
- 实验或效果：在四个视频基准上验证了两种变体（监督和无监督），对两种跟踪模型有效，计算轻量且模型无关。

## 摘要（原文）

> Real-time online object tracking in videos constitutes a core task in computer vision, with wide-ranging applications including video surveillance, motion capture, and robotics. Deployed tracking systems usually lack formal safety assurances to convey when tracking is reliable and when it may fail, at best relying on heuristic measures of model confidence to raise alerts. To obtain such assurances we propose interpreting object tracking as a sequential hypothesis test, wherein evidence for or against tracking failures is gradually accumulated over time. Leveraging recent advancements in the field, our sequential test (formalized as an e-process) quickly identifies when tracking failures set in whilst provably containing false alerts at a desired rate, and thus limiting potentially costly re-calibration or intervention steps. The approach is computationally light-weight, requires no extra training or fine-tuning, and is in principle model-agnostic. We propose both supervised and unsupervised variants by leveraging either ground-truth or solely internal tracking information, and demonstrate its effectiveness for two established tracking models across four video benchmarks. As such, sequential testing can offer a statistically grounded and efficient mechanism to incorporate safety assurances into real-time tracking systems.

