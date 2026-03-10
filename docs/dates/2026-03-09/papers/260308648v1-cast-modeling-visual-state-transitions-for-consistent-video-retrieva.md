---
layout: default
title: CAST: Modeling Visual State Transitions for Consistent Video Retrieval
---

# CAST: Modeling Visual State Transitions for Consistent Video Retrieval
**arXiv**：[2603.08648v1](https://arxiv.org/abs/2603.08648) · [PDF](https://arxiv.org/pdf/2603.08648.pdf)  
**作者**：Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  

**一句话要点**：提出CAST适配器以解决长视频检索中的状态一致性问题

**关键词**：一致视频检索, 状态转换建模, 视觉语言嵌入, 长视频理解, 适配器方法

## 3 点简述
- 核心问题：现有视频检索方法忽略上下文，导致状态和身份不一致
- 方法要点：CAST通过预测视觉历史的状态条件残差更新，建模潜在状态演化
- 实验或效果：在YouCook2和CrossTask上提升性能，并为黑盒视频生成提供重排序信号

## 摘要（原文）

> As video content creation shifts toward long-form narratives, composing short clips into coherent storylines becomes increasingly important. However, prevailing retrieval formulations remain context-agnostic at inference time, prioritizing local semantic alignment while neglecting state and identity consistency. To address this structural limitation, we formalize the task of Consistent Video Retrieval (CVR) and introduce a diagnostic benchmark spanning YouCook2, COIN, and CrossTask. We propose CAST (Context-Aware State Transition), a lightweight, plug-and-play adapter compatible with diverse frozen vision-language embedding spaces. By predicting a state-conditioned residual update ($Δ$) from visual history, CAST introduces an explicit inductive bias for latent state evolution. Extensive experiments show that CAST improves performance on YouCook2 and CrossTask, remains competitive on COIN, and consistently outperforms zero-shot baselines across diverse foundation backbones. Furthermore, CAST provides a useful reranking signal for black-box video generation candidates (e.g., from Veo), promoting more temporally coherent continuations.

