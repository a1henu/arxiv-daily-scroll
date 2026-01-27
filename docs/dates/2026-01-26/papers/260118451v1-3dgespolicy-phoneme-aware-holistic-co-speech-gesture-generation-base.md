---
layout: default
title: 3DGesPolicy: Phoneme-Aware Holistic Co-Speech Gesture Generation Based on Action Control
---

# 3DGesPolicy: Phoneme-Aware Holistic Co-Speech Gesture Generation Based on Action Control
**arXiv**：[2601.18451v1](https://arxiv.org/abs/2601.18451) · [PDF](https://arxiv.org/pdf/2601.18451.pdf)  
**作者**：Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba, Yuki Uranishi  

**一句话要点**：提出3DGesPolicy框架，基于动作控制解决全身协同语音手势生成中的语义不协调和空间不稳定问题。

**关键词**：协同语音手势生成, 全身动作控制, 扩散策略, 多模态融合, 语音对齐

## 3 点简述
- 核心问题：现有方法导致全身手势与面部表情语义不协调及空间运动不稳定。
- 方法要点：将手势生成重构为连续轨迹控制问题，使用扩散策略建模整体动作模式。
- 实验或效果：在BEAT2数据集上验证，生成自然、表达性强且语音对齐的全身手势。

## 摘要（原文）

> Generating holistic co-speech gestures that integrate full-body motion with facial expressions suffers from semantically incoherent coordination on body motion and spatially unstable meaningless movements due to existing part-decomposed or frame-level regression methods, We introduce 3DGesPolicy, a novel action-based framework that reformulates holistic gesture generation as a continuous trajectory control problem through diffusion policy from robotics. By modeling frame-to-frame variations as unified holistic actions, our method effectively learns inter-frame holistic gesture motion patterns and ensures both spatially and semantically coherent movement trajectories that adhere to realistic motion manifolds. To further bridge the gap in expressive alignment, we propose a Gesture-Audio-Phoneme (GAP) fusion module that can deeply integrate and refine multi-modal signals, ensuring structured and fine-grained alignment between speech semantics, body motion, and facial expressions. Extensive quantitative and qualitative experiments on the BEAT2 dataset demonstrate the effectiveness of our 3DGesPolicy across other state-of-the-art methods in generating natural, expressive, and highly speech-aligned holistic gestures.

