---
layout: default
title: ClueTracer: Question-to-Vision Clue Tracing for Training-Free Hallucination Suppression in Multimodal Reasoning
---

# ClueTracer: Question-to-Vision Clue Tracing for Training-Free Hallucination Suppression in Multimodal Reasoning
**arXiv**：[2602.02004v1](https://arxiv.org/abs/2602.02004) · [PDF](https://arxiv.org/pdf/2602.02004.pdf)  
**作者**：Gongli Xi, Kun Wang, Zeming Gao, Huahui Yi, Haolang Lu, Ye Tian, Wendong Wang  

**一句话要点**：提出ClueTracer插件以解决多模态推理中的幻觉问题，无需训练即可抑制幻觉。

**关键词**：多模态推理, 幻觉抑制, 训练免费插件, 视觉线索追踪, 推理漂移

## 3 点简述
- 核心问题：多模态推理模型在长链推理中因关注无关实体导致推理漂移和幻觉。
- 方法要点：ClueTracer从问题出发追踪关键线索在推理路径中的传播，定位相关视觉区域。
- 实验或效果：无需额外训练，在推理基准上提升1.21倍，非推理设置中提升1.14倍。

## 摘要（原文）

> Large multimodal reasoning models solve challenging visual problems via explicit long-chain inference: they gather visual clues from images and decode clues into textual tokens. Yet this capability also increases hallucinations, where the model generates content that is not supported by the input image or the question. To understand this failure mode, we identify \emph{reasoning drift}: during clue gathering, the model over-focuses on question-irrelevant entities, diluting focus on task-relevant cues and gradually decoupling the reasoning trace from visual grounding. As a consequence, many inference-time localization or intervention methods developed for non-reasoning models fail to pinpoint the true clues in reasoning settings. Motivated by these insights, we introduce ClueRecall, a metric for assessing visual clue retrieval, and present ClueTracer, a training-free, parameter-free, and architecture-agnostic plugin for hallucination suppression. ClueTracer starts from the question and traces how key clues propagate along the model's reasoning pathway (question $\rightarrow$ outputs $\rightarrow$ visual tokens), thereby localizing task-relevant patches while suppressing spurious attention to irrelevant regions. Remarkably, \textbf{without any additional training}, ClueTracer improves all \textbf{reasoning} architectures (including \texttt{R1-OneVision}, \texttt{Ocean-R1}, \texttt{MM-Eureka}, \emph{etc}.) by $\mathbf{1.21\times}$ on reasoning benchmarks. When transferred to \textbf{non-reasoning} settings, it yields a $\mathbf{1.14\times}$ gain.

