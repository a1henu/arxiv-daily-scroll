---
layout: default
title: OmniAgent: Audio-Guided Active Perception Agent for Omnimodal Audio-Video Understanding
---

# OmniAgent: Audio-Guided Active Perception Agent for Omnimodal Audio-Video Understanding
**arXiv**：[2512.23646v1](https://arxiv.org/abs/2512.23646) · [PDF](https://arxiv.org/pdf/2512.23646.pdf)  
**作者**：Keda Tao, Wenjie Du, Bohan Yu, Weiqiang Wang, Jian Liu, Huan Wang  

**一句话要点**：提出OmniAgent，一种音频引导的主动感知代理，以解决全模态音视频理解中的细粒度跨模态对齐问题。

**关键词**：全模态理解, 音频引导感知, 主动代理, 动态规划, 音视频对齐, 细粒度推理

## 3 点简述
- 核心问题：现有全模态大模型在音视频理解中缺乏细粒度跨模态对齐，难以处理模态间动态交互。
- 方法要点：采用音频引导的粗到细感知范式，动态规划工具调用，实现主动多模态查询与任务相关线索聚焦。
- 实验或效果：在三个音视频理解基准测试中，性能超越领先开源和专有模型10%-20%准确率，达到最先进水平。

## 摘要（原文）

> Omnimodal large language models have made significant strides in unifying audio and visual modalities; however, they often lack the fine-grained cross-modal understanding and have difficulty with multimodal alignment. To address these limitations, we introduce OmniAgent, a fully audio-guided active perception agent that dynamically orchestrates specialized tools to achieve more fine-grained audio-visual reasoning. Unlike previous works that rely on rigid, static workflows and dense frame-captioning, this paper demonstrates a paradigm shift from passive response generation to active multimodal inquiry. OmniAgent employs dynamic planning to autonomously orchestrate tool invocation on demand, strategically concentrating perceptual attention on task-relevant cues. Central to our approach is a novel coarse-to-fine audio-guided perception paradigm, which leverages audio cues to localize temporal events and guide subsequent reasoning. Extensive empirical evaluations on three audio-video understanding benchmarks demonstrate that OmniAgent achieves state-of-the-art performance, surpassing leading open-source and proprietary models by substantial margins of 10% - 20% accuracy.

