---
layout: default
title: T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation
---

# T2AV-Compass: Towards Unified Evaluation for Text-to-Audio-Video Generation
**arXiv**：[2512.21094v1](https://arxiv.org/abs/2512.21094) · [PDF](https://arxiv.org/pdf/2512.21094.pdf)  
**作者**：Zhe Cao, Tao Wang, Jiaming Wang, Yanghai Wang, Yuanxing Zhang, Jialu Chen, Miao Deng, Jiahao Wang, Yubin Guo, Chenxi Liao, Yize Zhang, Zhaoxiang Zhang, Jiaheng Liu  

**一句话要点**：提出T2AV-Compass统一基准，以解决文本到音视频生成评估碎片化问题。

**关键词**：文本到音视频生成, 跨模态对齐, 统一评估基准, 信号级指标, MLLM-as-a-Judge, 复杂提示

## 3 点简述
- 核心问题：文本到音视频生成评估依赖单模态指标或窄范围基准，难以捕捉跨模态对齐和复杂提示下的感知真实性。
- 方法要点：构建500个多样化复杂提示，结合客观信号级指标和主观MLLM-as-a-Judge协议进行双层次评估。
- 实验或效果：评估11个代表性系统，显示现有模型在音频真实性、细粒度同步和指令遵循方面显著落后于人类水平。

## 摘要（原文）

> Text-to-Audio-Video (T2AV) generation aims to synthesize temporally coherent video and semantically synchronized audio from natural language, yet its evaluation remains fragmented, often relying on unimodal metrics or narrowly scoped benchmarks that fail to capture cross-modal alignment, instruction following, and perceptual realism under complex prompts. To address this limitation, we present T2AV-Compass, a unified benchmark for comprehensive evaluation of T2AV systems, consisting of 500 diverse and complex prompts constructed via a taxonomy-driven pipeline to ensure semantic richness and physical plausibility. Besides, T2AV-Compass introduces a dual-level evaluation framework that integrates objective signal-level metrics for video quality, audio quality, and cross-modal alignment with a subjective MLLM-as-a-Judge protocol for instruction following and realism assessment. Extensive evaluation of 11 representative T2AVsystems reveals that even the strongest models fall substantially short of human-level realism and cross-modal consistency, with persistent failures in audio realism, fine-grained synchronization, instruction following, etc. These results indicate significant improvement room for future models and highlight the value of T2AV-Compass as a challenging and diagnostic testbed for advancing text-to-audio-video generation.

