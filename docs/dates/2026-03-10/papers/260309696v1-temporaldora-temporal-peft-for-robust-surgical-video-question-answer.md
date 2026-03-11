---
layout: default
title: TemporalDoRA: Temporal PEFT for Robust Surgical Video Question Answering
---

# TemporalDoRA: Temporal PEFT for Robust Surgical Video Question Answering
**arXiv**：[2603.09696v1](https://arxiv.org/abs/2603.09696) · [PDF](https://arxiv.org/pdf/2603.09696.pdf)  
**作者**：Luca Carlini, Chiara Lena, Cesare Hassan, Danail Stoyanov, Elena De Momi, Sophia Bano, Mobarak I. Hoque  

**一句话要点**：提出TemporalDoRA以增强手术视频问答的时序建模与语言鲁棒性

**关键词**：手术视频问答, 参数高效微调, 时序建模, 语言鲁棒性, 低秩适应, 注意力机制

## 3 点简述
- 手术视频问答需时序定位，但标准PEFT方法缺乏帧间交互建模，限制稀疏时序证据利用。
- TemporalDoRA扩展Weight-Decomposed Low-Rank Adaptation，在视觉编码器低秩瓶颈中插入轻量时序注意力，并选择性分解权重。
- 在REAL-Colon-VQA和EndoVis18-VQA数据集上验证，提升Out-of-Template性能，时序混合是主要增益来源。

## 摘要（原文）

> Surgical Video Question Answering (VideoQA) requires accurate temporal grounding while remaining robust to natural variation in how clinicians phrase questions, where linguistic bias can arise. Standard Parameter Efficient Fine Tuning (PEFT) methods adapt pretrained projections without explicitly modeling frame-to-frame interactions within the adaptation pathway, limiting their ability to exploit sparse temporal evidence. We introduce TemporalDoRA, a video-specific PEFT formulation that extends Weight-Decomposed Low-Rank Adaptation by (i) inserting lightweight temporal Multi-Head Attention (MHA) inside the low-rank bottleneck of the vision encoder and (ii) selectively applying weight decomposition only to the trainable low-rank branch rather than the full adapted weight. This design enables temporally-aware updates while preserving a frozen backbone and stable scaling. By mixing information across frames within the adaptation subspace, TemporalDoRA steers updates toward temporally consistent visual cues and improves robustness with minimal parameter overhead. To benchmark this setting, we present REAL-Colon-VQA, a colonoscopy VideoQA dataset with 6,424 clip--question pairs, including paired rephrased Out-of-Template questions to evaluate sensitivity to linguistic variation. TemporalDoRA improves Out-of-Template performance, and ablation studies confirm that temporal mixing inside the low-rank branch is the primary driver of these gains. We also validate on EndoVis18-VQA adapted to short clips and observe consistent improvements on the Out-of-Template split. Code and dataset available at~\href{https://anonymous.4open.science/r/TemporalDoRA-BFC8/}{Anonymous GitHub}.

