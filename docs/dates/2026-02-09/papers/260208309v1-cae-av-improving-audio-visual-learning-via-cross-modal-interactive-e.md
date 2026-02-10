---
layout: default
title: CAE-AV: Improving Audio-Visual Learning via Cross-modal Interactive Enrichment
---

# CAE-AV: Improving Audio-Visual Learning via Cross-modal Interactive Enrichment
**arXiv**：[2602.08309v1](https://arxiv.org/abs/2602.08309) · [PDF](https://arxiv.org/pdf/2602.08309.pdf)  
**作者**：Yunzuo Hu, Wen Li, Jing Zhang  

**一句话要点**：提出CAE-AV框架，通过跨模态交互增强解决音视频学习中的模态不对齐问题。

**关键词**：音视频学习, 模态不对齐, 跨模态增强, 时空关系平衡, 语义指导, 轻量目标

## 3 点简述
- 核心问题：音视频学习受离屏声源和背景杂波影响，导致模态不对齐，现有方法易放大无关区域或时刻，降低表示质量。
- 方法要点：采用CASTE和CASE模块，动态平衡时空关系并注入语义指导，结合轻量目标如caption-to-modality InfoNCE，以缓解不对齐。
- 实验或效果：在冻结骨干网络下，CAE-AV在AVE、AVVP、AVS和AVQA基准上达到最先进性能，定性分析验证其对不对齐的鲁棒性。

## 摘要（原文）

> Audio-visual learning suffers from modality misalignment caused by off-screen sources and background clutter, and current methods usually amplify irrelevant regions or moments, leading to unstable training and degraded representation quality. To address this challenge, we proposed a novel Caption-aligned and Agreement-guided Enhancement framework (CAE-AV) for audio-visual learning, which used two complementary modules: Cross-modal Agreement-guided Spatio-Temporal Enrichment (CASTE) and Caption-Aligned Saliency-guided Enrichment (CASE) to relieve audio-visual misalignment. CASTE dynamically balances spatial and temporal relations by evaluating frame-level audio-visual agreement, ensuring that key information is captured from both preceding and subsequent frames under misalignment. CASE injects cross-modal semantic guidance into selected spatio-temporal positions, leveraging high-level semantic cues to further alleviate misalignment. In addition, we design lightweight objectives, caption-to-modality InfoNCE, visual-audio consistency, and entropy regularization to guide token selection and strengthen cross-modal semantic alignment. With frozen backbones, CAE-AV achieves state-of-the-art performance on AVE, AVVP, AVS, and AVQA benchmarks, and qualitative analyses further validate its robustness against audio-visual misalignment.

