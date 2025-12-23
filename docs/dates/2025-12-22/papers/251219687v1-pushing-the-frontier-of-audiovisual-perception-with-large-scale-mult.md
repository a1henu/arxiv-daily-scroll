---
layout: default
title: Pushing the Frontier of Audiovisual Perception with Large-Scale Multimodal Correspondence Learning
---

# Pushing the Frontier of Audiovisual Perception with Large-Scale Multimodal Correspondence Learning
**arXiv**：[2512.19687v1](https://arxiv.org/abs/2512.19687) · [PDF](https://arxiv.org/pdf/2512.19687.pdf)  
**作者**：Apoorv Vyas, Heng-Jui Chang, Cheng-Fu Yang, Po-Yao Huang, Luya Gao, Julius Richter, Sanyuan Chen, Matt Le, Piotr Dollár, Christoph Feichtenhofer, Ann Lee, Wei-Ning Hsu  

**一句话要点**：提出PE-AV编码器家族，通过大规模对比学习实现音频-视频-文本多模态统一嵌入，提升视听感知性能。

**关键词**：多模态学习, 对比学习, 视听感知, 统一嵌入, 零样本泛化, 数据引擎

## 3 点简述
- 核心问题：现有视听表示学习常受限于单模态或小规模数据，难以实现跨模态统一嵌入和零样本泛化。
- 方法要点：基于PE框架，构建大规模高质量音频-视频对数据引擎，采用十种对比目标进行跨模态对齐训练。
- 实验或效果：在标准音频和视频基准测试中达到新SOTA，支持语音检索等新任务，并通过PE-A-Frame实现细粒度音频帧对齐。

## 摘要（原文）

> We introduce Perception Encoder Audiovisual, PE-AV, a new family of encoders for audio and video understanding trained with scaled contrastive learning. Built on PE, PE-AV makes several key contributions to extend representations to audio, and natively support joint embeddings across audio-video, audio-text, and video-text modalities. PE-AV's unified cross-modal embeddings enable novel tasks such as speech retrieval, and set a new state of the art across standard audio and video benchmarks. We unlock this by building a strong audiovisual data engine that synthesizes high-quality captions for O(100M) audio-video pairs, enabling large-scale supervision consistent across modalities. Our audio data includes speech, music, and general sound effects-avoiding single-domain limitations common in prior work. We exploit ten pairwise contrastive objectives, showing that scaling cross-modality and caption-type pairs strengthens alignment and improves zero-shot performance. We further develop PE-A-Frame by fine-tuning PE-AV with frame-level contrastive objectives, enabling fine-grained audio-frame-to-text alignment for tasks such as sound event detection.

