---
layout: default
title: Towards Long-Form Spatio-Temporal Video Grounding
---

# Towards Long-Form Spatio-Temporal Video Grounding
**arXiv**：[2602.23294v1](https://arxiv.org/abs/2602.23294) · [PDF](https://arxiv.org/pdf/2602.23294.pdf)  
**作者**：Xin Gu, Bing Fan, Jiali Yao, Zhipeng Zhang, Yan Huang, Cheng Han, Heng Fan, Libo Zhang  

**一句话要点**：提出ART-STVG架构以解决长视频时空定位中的效率与上下文建模挑战。

**关键词**：长视频时空定位, 自回归Transformer, 时空记忆库, 级联定位, 视频流处理

## 3 点简述
- 核心问题：现有时空视频定位方法难以处理长视频，因视频时长可达数分钟至数小时，包含大量无关信息。
- 方法要点：采用自回归Transformer架构，将视频作为流输入顺序处理，并设计时空记忆库与级联定位策略。
- 实验或效果：在新扩展的长视频数据集上显著优于现有方法，在短视频任务中也保持竞争力。

## 摘要（原文）

> In real scenarios, videos can span several minutes or even hours. However, existing research on spatio-temporal video grounding (STVG), given a textual query, mainly focuses on localizing targets in short videos of tens of seconds, typically less than one minute, which limits real-world applications. In this paper, we explore Long-Form STVG (LF-STVG), which aims to locate targets in long-term videos. Compared with short videos, long-term videos contain much longer temporal spans and more irrelevant information, making it difficult for existing STVG methods that process all frames at once. To address this challenge, we propose an AutoRegressive Transformer architecture for LF-STVG, termed ART-STVG. Unlike conventional STVG methods that require the entire video sequence to make predictions at once, ART-STVG treats the video as streaming input and processes frames sequentially, enabling efficient handling of long videos. To model spatio-temporal context, we design spatial and temporal memory banks and apply them to the decoders. Since memories from different moments are not always relevant to the current frame, we introduce simple yet effective memory selection strategies to provide more relevant information to the decoders, significantly improving performance. Furthermore, instead of parallel spatial and temporal localization, we propose a cascaded spatio-temporal design that connects the spatial decoder to the temporal decoder, allowing fine-grained spatial cues to assist complex temporal localization in long videos. Experiments on newly extended LF-STVG datasets show that ART-STVG significantly outperforms state-of-the-art methods, while achieving competitive performance on conventional short-form STVG.

