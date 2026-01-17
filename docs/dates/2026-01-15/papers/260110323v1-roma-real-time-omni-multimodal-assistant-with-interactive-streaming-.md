---
layout: default
title: ROMA: Real-time Omni-Multimodal Assistant with Interactive Streaming Understanding
---

# ROMA: Real-time Omni-Multimodal Assistant with Interactive Streaming Understanding
**arXiv**：[2601.10323v1](https://arxiv.org/abs/2601.10323) · [PDF](https://arxiv.org/pdf/2601.10323.pdf)  
**作者**：Xueyun Tian, Wei Li, Bingbing Xu, Heng Dong, Yuanzhuo Wang, Huawei Shen  

**一句话要点**：提出ROMA实时全模态助手，通过同步多模态单元和轻量级说话头解决流式音视频理解中的模态不完整和主动监控缺失问题。

**关键词**：流式音视频理解, 全模态大语言模型, 同步多模态单元, 轻量级说话头, 主动监控, 实时交互

## 3 点简述
- 核心问题：现有全模态大语言模型在流式音视频理解中存在模态支持不完整和缺乏自主主动监控能力。
- 方法要点：采用同步多模态单元对齐密集音频与离散视频帧，并引入轻量级说话头解耦响应触发与生成以实现精确在线决策。
- 实验或效果：在12个基准测试中，ROMA在主动任务上达到最先进性能，在反应性任务上表现竞争性，验证了其统一实时全模态理解的鲁棒性。

## 摘要（原文）

> Recent Omni-multimodal Large Language Models show promise in unified audio, vision, and text modeling. However, streaming audio-video understanding remains challenging, as existing approaches suffer from disjointed capabilities: they typically exhibit incomplete modality support or lack autonomous proactive monitoring. To address this, we present ROMA, a real-time omni-multimodal assistant for unified reactive and proactive interaction. ROMA processes continuous inputs as synchronized multimodal units, aligning dense audio with discrete video frames to handle granularity mismatches. For online decision-making, we introduce a lightweight speak head that decouples response initiation from generation to ensure precise triggering without task conflict. We train ROMA with a curated streaming dataset and a two-stage curriculum that progressively optimizes for streaming format adaptation and proactive responsiveness. To standardize the fragmented evaluation landscape, we reorganize diverse benchmarks into a unified suite covering both proactive (alert, narration) and reactive (QA) settings. Extensive experiments across 12 benchmarks demonstrate ROMA achieves state-of-the-art performance on proactive tasks while competitive in reactive settings, validating its robustness in unified real-time omni-multimodal understanding.

