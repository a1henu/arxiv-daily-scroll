---
layout: default
title: MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control
---

# MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control
**arXiv**：[2601.22501v1](https://arxiv.org/abs/2601.22501) · [PDF](https://arxiv.org/pdf/2601.22501.pdf)  
**作者**：Renjie Lu, Xulong Zhang, Xiaoyang Qu, Jianzong Wang, Shangfei Wang  

**一句话要点**：提出MirrorTalk框架，通过解耦风格与分层运动控制，解决个性化说话人脸合成中风格与内容混淆的挑战。

**关键词**：个性化说话人脸合成, 风格解耦, 条件扩散模型, 分层运动控制, 唇部同步

## 3 点简述
- 核心问题：现有方法中说话风格与语义内容在面部运动中混淆，阻碍个性化风格向任意语音的忠实迁移。
- 方法要点：基于条件扩散模型，结合语义解耦风格编码器提取纯风格表示，并采用分层调制策略动态平衡音频与风格特征。
- 实验或效果：在唇部同步准确性和个性化保持方面，相比先进方法有显著提升。

## 摘要（原文）

> Synthesizing personalized talking faces that uphold and highlight a speaker's unique style while maintaining lip-sync accuracy remains a significant challenge. A primary limitation of existing approaches is the intrinsic confounding of speaker-specific talking style and semantic content within facial motions, which prevents the faithful transfer of a speaker's unique persona to arbitrary speech. In this paper, we propose MirrorTalk, a generative framework based on a conditional diffusion model, combined with a Semantically-Disentangled Style Encoder (SDSE) that can distill pure style representations from a brief reference video. To effectively utilize this representation, we further introduce a hierarchical modulation strategy within the diffusion process. This mechanism guides the synthesis by dynamically balancing the contributions of audio and style features across distinct facial regions, ensuring both precise lip-sync accuracy and expressive full-face dynamics. Extensive experiments demonstrate that MirrorTalk achieves significant improvements over state-of-the-art methods in terms of lip-sync accuracy and personalization preservation.

