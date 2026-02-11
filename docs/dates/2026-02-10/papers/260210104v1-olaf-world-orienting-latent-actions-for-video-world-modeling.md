---
layout: default
title: Olaf-World: Orienting Latent Actions for Video World Modeling
---

# Olaf-World: Orienting Latent Actions for Video World Modeling
**arXiv**：[2602.10104v1](https://arxiv.org/abs/2602.10104) · [PDF](https://arxiv.org/pdf/2602.10104.pdf)  
**作者**：Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, Mike Zheng Shou  

**一句话要点**：提出Olaf-World，通过序列级控制-效果对齐目标，从大规模无标签视频预训练动作条件化世界模型。

**关键词**：视频世界建模, 潜在动作学习, 自监督学习, 动作迁移, 序列对齐, 零样本学习

## 3 点简述
- 核心问题：动作可控世界模型受限于动作标签稀缺，现有潜在动作学习方法因缺乏跨上下文对齐机制，导致动作语义迁移失败。
- 方法要点：引入SeqΔ-REPA目标，基于冻结自监督视频编码器的时序特征差异，对齐潜在动作与可观察语义效果，构建结构化潜在动作空间。
- 实验或效果：在零样本动作迁移和新控制接口适应中，优于现有基线，实现更高效的数据利用和更强的泛化能力。

## 摘要（原文）

> Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, their semantic effects are observable and can serve as a shared reference. We introduce Seq$Δ$-REPA, a sequence-level control-effect alignment objective that anchors integrated latent action to temporal feature differences from a frozen, self-supervised video encoder. Building on this, we present Olaf-World, a pipeline that pretrains action-conditioned video world models from large-scale passive video. Extensive experiments demonstrate that our method learns a more structured latent action space, leading to stronger zero-shot action transfer and more data-efficient adaptation to new control interfaces than state-of-the-art baselines.

