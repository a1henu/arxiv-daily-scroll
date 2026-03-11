---
layout: default
title: TimberAgent: Gram-Guided Retrieval for Executable Music Effect Control
---

# TimberAgent: Gram-Guided Retrieval for Executable Music Effect Control
**arXiv**：[2603.09332v1](https://arxiv.org/abs/2603.09332) · [PDF](https://arxiv.org/pdf/2603.09332.pdf)  
**作者**：Shihao He, Yihan Xia, Fang Liu, Taotao Wang, Shengli Zhang  

**一句话要点**：提出基于纹理共振检索的可执行音乐效果控制方法，以缩小用户意图与音频处理参数间的语义鸿沟。

**关键词**：音频效果控制, 纹理共振检索, Gram矩阵, 可编辑配置, 语义鸿沟, Wav2Vec2

## 3 点简述
- 核心问题：数字音频工作站中，用户感知意图与低层信号处理参数间存在语义鸿沟，影响可编辑效果配置的生成。
- 方法要点：设计纹理共振检索，基于Wav2Vec2中层激活的Gram矩阵构建音频表示，保留纹理相关的共激活结构。
- 实验或效果：在吉他效果基准上评估，TRR在归一化参数误差上表现最佳，并通过听觉研究提供感知证据。

## 摘要（原文）

> Digital audio workstations expose rich effect chains, yet a semantic gap remains between perceptual user intent and low-level signal-processing parameters. We study retrieval-grounded audio effect control, where the output is an editable plugin configuration rather than a finalized waveform. Our focus is Texture Resonance Retrieval (TRR), an audio representation built from Gram matrices of projected mid-level Wav2Vec2 activations. This design preserves texture-relevant co-activation structure. We evaluate TRR on a guitar-effects benchmark with 1,063 candidate presets and 204 queries. The evaluation follows Protocol-A, a cross-validation scheme that prevents train-test leakage. We compare TRR against CLAP and internal retrieval baselines (Wav2Vec-RAG, Text-RAG, FeatureNN-RAG), using min-max normalized metrics grounded in physical DSP parameter ranges. Ablation studies validate TRR's core design choices: projection dimensionality, layer selection, and projection type. A near-duplicate sensitivity analysis confirms that results are robust to trivial knowledge-base matches. TRR achieves the lowest normalized parameter error among evaluated methods. A multiple-stimulus listening study with 26 participants provides complementary perceptual evidence. We interpret these results as benchmark evidence that texture-aware retrieval is useful for editable audio effect control, while broader personalization and real-audio robustness claims remain outside the verified evidence presented here.

