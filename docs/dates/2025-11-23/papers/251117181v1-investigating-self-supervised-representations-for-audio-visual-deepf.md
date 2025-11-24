---
layout: default
title: Investigating self-supervised representations for audio-visual deepfake detection
---

# Investigating self-supervised representations for audio-visual deepfake detection
**arXiv**：[2511.17181v1](https://arxiv.org/abs/2511.17181) · [PDF](https://arxiv.org/pdf/2511.17181.pdf)  
**作者**：Dragos-Alexandru Boldisor, Stefan Smeu, Dan Oneata, Elisabeta Oneata  

**一句话要点**：系统评估自监督表征在音视频深度伪造检测中的有效性、可解释性和互补性

**关键词**：自监督表征, 音视频深度伪造检测, 多模态评估, 可解释性分析, 跨数据集泛化

## 3 点简述
- 核心问题：自监督表征在音视频深度伪造检测中的应用潜力未被充分探索，且跨数据集泛化能力不足。
- 方法要点：系统评估自监督特征在音频、视频和多模态中的表现，关注语义区域而非虚假伪影。
- 实验或效果：发现特征捕获互补的伪造相关信息，但泛化失败可能源于数据集特性。

## 摘要（原文）

> Self-supervised representations excel at many vision and speech tasks, but their potential for audio-visual deepfake detection remains underexplored. Unlike prior work that uses these features in isolation or buried within complex architectures, we systematically evaluate them across modalities (audio, video, multimodal) and domains (lip movements, generic visual content). We assess three key dimensions: detection effectiveness, interpretability of encoded information, and cross-modal complementarity. We find that most self-supervised features capture deepfake-relevant information, and that this information is complementary. Moreover, models primarily attend to semantically meaningful regions rather than spurious artifacts. Yet none generalize reliably across datasets. This generalization failure likely stems from dataset characteristics, not from the features themselves latching onto superficial patterns. These results expose both the promise and fundamental challenges of self-supervised representations for deepfake detection: while they learn meaningful patterns, achieving robust cross-domain performance remains elusive.

