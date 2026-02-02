---
layout: default
title: StreamSense: Streaming Social Task Detection with Selective Vision-Language Model Routing
---

# StreamSense: Streaming Social Task Detection with Selective Vision-Language Model Routing
**arXiv**：[2601.22738v1](https://arxiv.org/abs/2601.22738) · [PDF](https://arxiv.org/pdf/2601.22738.pdf)  
**作者**：Han Wang, Deyi Ji, Lanyun Zhu, Jiebo Luo, Roy Ka-Wei Lee  

**一句话要点**：提出StreamSense，通过选择性路由VLM专家解决直播平台实时社交任务检测问题。

**关键词**：流式社交检测, 选择性路由, 视觉语言模型, 跨模态对齐, 实时监控, 延迟优化

## 3 点简述
- 核心问题：直播平台需实时监控视频、文本和音频的异步证据以检测社交信号。
- 方法要点：结合轻量流编码器与选择性VLM路由，处理多数时间戳并升级困难案例。
- 实验或效果：在情感分类和仇恨内容审核等任务中，比纯VLM流检测更准确且降低延迟。

## 摘要（原文）

> Live streaming platforms require real-time monitoring and reaction to social signals, utilizing partial and asynchronous evidence from video, text, and audio. We propose StreamSense, a streaming detector that couples a lightweight streaming encoder with selective routing to a Vision-Language Model (VLM) expert. StreamSense handles most timestamps with the lightweight streaming encoder, escalates hard/ambiguous cases to the VLM, and defers decisions when context is insufficient. The encoder is trained using (i) a cross-modal contrastive term to align visual/audio cues with textual signals, and (ii) an IoU-weighted loss that down-weights poorly overlapping target segments, mitigating label interference across segment boundaries. We evaluate StreamSense on multiple social streaming detection tasks (e.g., sentiment classification and hate content moderation), and the results show that StreamSense achieves higher accuracy than VLM-only streaming while only occasionally invoking the VLM, thereby reducing average latency and compute. Our results indicate that selective escalation and deferral are effective primitives for understanding streaming social tasks. Code is publicly available on GitHub.

