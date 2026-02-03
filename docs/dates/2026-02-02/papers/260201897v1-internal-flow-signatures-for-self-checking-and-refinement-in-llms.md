---
layout: default
title: Internal Flow Signatures for Self-Checking and Refinement in LLMs
---

# Internal Flow Signatures for Self-Checking and Refinement in LLMs
**arXiv**：[2602.01897v1](https://arxiv.org/abs/2602.01897) · [PDF](https://arxiv.org/pdf/2602.01897.pdf)  
**作者**：Sungheon Jeong, Sanggeon Yun, Ryozo Masukawa, Wenjun Haung, Hanning Chen, Mohsen Imani  

**一句话要点**：提出内部流签名方法，通过深度动态监控实现大语言模型的自我检查与精炼。

**关键词**：大语言模型, 自我检查, 内部动态监控, 深度事件定位, 模型精炼, 轻量验证器

## 3 点简述
- 核心问题：大语言模型生成流畅但不可靠答案，现有方法依赖外部验证。
- 方法要点：在固定块间边界监控深度动态，构建移动对齐子空间以总结轨迹，训练轻量GRU验证器。
- 实验或效果：实现自我检查、定位深度事件，并支持针对性精炼，代码已开源。

## 摘要（原文）

> Large language models can generate fluent answers that are unfaithful to the provided context, while many safeguards rely on external verification or a separate judge after generation. We introduce \emph{internal flow signatures} that audit decision formation from depthwise dynamics at a fixed inter-block monitoring boundary. The method stabilizes token-wise motion via bias-centered monitoring, then summarizes trajectories in compact \emph{moving} readout-aligned subspaces constructed from the top token and its close competitors within each depth window. Neighboring window frames are aligned by an orthogonal transport, yielding depth-comparable transported step lengths, turning angles, and subspace drift summaries that are invariant to within-window basis choices. A lightweight GRU validator trained on these signatures performs self-checking without modifying the base model. Beyond detection, the validator localizes a culprit depth event and enables a targeted refinement: the model rolls back to the culprit token and clamps an abnormal transported step at the identified block while preserving the orthogonal residual. The resulting pipeline provides actionable localization and low-overhead self-checking from internal decision dynamics. \emph{Code is available at} \texttt{github.com/EavnJeong/Internal-Flow-Signatures-for-Self-Checking-and-Refinement-in-LLMs}.

