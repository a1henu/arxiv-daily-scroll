---
layout: default
title: MealRec: Multi-granularity Sequential Modeling via Hierarchical Diffusion Models for Micro-Video Recommendation
---

# MealRec: Multi-granularity Sequential Modeling via Hierarchical Diffusion Models for Micro-Video Recommendation
**arXiv**：[2603.01926v1](https://arxiv.org/abs/2603.01926) · [PDF](https://arxiv.org/pdf/2603.01926.pdf)  
**作者**：Xinxin Dong, Haokai Ma, Yuze Zheng, Yongfu Zha, Yonghui Yang, Xiaodong Wang  

**一句话要点**：提出MealRec，通过分层扩散模型进行多粒度序列建模，以解决微视频推荐中的噪声和模态冲突问题。

**关键词**：微视频推荐, 多粒度序列建模, 分层扩散模型, 时序引导内容扩散, 噪声无条件偏好去噪, 多模态分析

## 3 点简述
- 核心问题：微视频推荐中多模态内容噪声和隐式反馈不可靠，导致行为与兴趣对应弱化。
- 方法要点：设计TCD在视频内时序引导下优化表示，NPD在盲去噪中恢复用户偏好，实现语义连贯建模。
- 实验或效果：在四个微视频数据集上验证了有效性、通用性和鲁棒性，并揭示了TCD和NPD的机制。

## 摘要（原文）

> Micro-video recommendation aims to capture user preferences from the collaborative and context information of the interacted micro-videos, thereby predicting the appropriate videos. This target is often hindered by the inherent noise within multimodal content and unreliable implicit feedback, which weakens the correspondence between behaviors and underlying interests. While conventional works have predominantly approached such scenario through behavior-augmented modeling and content-centric multimodal analysis, these paradigms can inadvertently give rise to two non-trivial challenges: preference-irrelative video representation extraction and inherent modality conflicts. To address these issues, we propose a Multi-granularity sequential modeling method via hierarchical diffusion models for micro-video Recommendation (MealRec), which simultaneously considers temporal correlations during preference modeling from intra- and inter-video perspectives. Specifically, we first propose Temporal-guided Content Diffusion (TCD) to refine video representations under intra-video temporal guidance and personalized collaborative signals to emphasize salient content while suppressing redundancy. To achieve the semantically coherent preference modeling, we further design the Noise-unconditional Preference Denoising (NPD) to recovers informative user preferences from corrupted states under the blind denoising. Extensive experiments and analyses on four micro-video datasets from two platforms demonstrate the effectiveness, universality, and robustness of our MealRec, further uncovering the effective mechanism of our proposed TCD and NPD. The source code and corresponding dataset will be available upon acceptance.

