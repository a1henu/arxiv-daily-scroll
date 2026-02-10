---
layout: default
title: TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions
---

# TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions
**arXiv**：[2602.08711v1](https://arxiv.org/abs/2602.08711) · [PDF](https://arxiv.org/pdf/2602.08711.pdf)  
**作者**：Linli Yao, Yuancheng Wei, Yaojie Zhang, Lei Li, Xinlong Chen, Feifan Song, Ziyue Wang, Kun Ouyang, Yuanxin Liu, Lingpeng Kong, Qi Liu, Pengfei Wan, Kun Gai, Yuanxing Zhang, Xu Sun  

**一句话要点**：提出Omni Dense Captioning任务，通过结构化音频视觉描述生成连续细粒度视频脚本。

**关键词**：密集视频描述, 音频视觉叙事, 时间感知描述, 结构化模式, 基准构建, 下游任务增强

## 3 点简述
- 核心问题：生成带时间戳的连续细粒度音频视觉描述，以覆盖密集语义。
- 方法要点：引入六维结构模式创建脚本式描述，并构建基准与统一评估指标。
- 实验或效果：TimeChat-Captioner-7B在基准测试中超越Gemini-2.5-Pro，提升下游任务性能。

## 摘要（原文）

> This paper proposes Omni Dense Captioning, a novel task designed to generate continuous, fine-grained, and structured audio-visual narratives with explicit timestamps. To ensure dense semantic coverage, we introduce a six-dimensional structural schema to create "script-like" captions, enabling readers to vividly imagine the video content scene by scene, akin to a cinematographic screenplay. To facilitate research, we construct OmniDCBench, a high-quality, human-annotated benchmark, and propose SodaM, a unified metric that evaluates time-aware detailed descriptions while mitigating scene boundary ambiguity. Furthermore, we construct a training dataset, TimeChatCap-42K, and present TimeChat-Captioner-7B, a strong baseline trained via SFT and GRPO with task-specific rewards. Extensive experiments demonstrate that TimeChat-Captioner-7B achieves state-of-the-art performance, surpassing Gemini-2.5-Pro, while its generated dense descriptions significantly boost downstream capabilities in audio-visual reasoning (DailyOmni and WorldSense) and temporal grounding (Charades-STA). All datasets, models, and code will be made publicly available at https://github.com/yaolinli/TimeChat-Captioner.

