---
layout: default
title: UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking
---

# UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking
**arXiv**：[2512.09327v1](https://arxiv.org/abs/2512.09327) · [PDF](https://arxiv.org/pdf/2512.09327.pdf)  
**作者**：Xuangeng Chu, Ruicong Liu, Yifei Huang, Yun Liu, Yichen Peng, Bo Zheng  

**一句话要点**：提出UniLS框架，通过双轨音频端到端生成统一听说的虚拟人表情，解决听者建模僵硬问题。

**关键词**：音频驱动虚拟人, 听说统一生成, 两阶段训练, 听者建模, 端到端框架, 表情生成

## 3 点简述
- 核心问题：听者表情建模困难，音频驱动训练导致僵硬，现有方法依赖额外运动数据或非端到端设计。
- 方法要点：采用两阶段训练，先学习内部运动先验，再引入双轨音频微调，实现音频驱动的听说统一生成。
- 实验或效果：在听说准确性上达到先进水平，听者指标提升44.1%，生成更自然多样的表情，缓解僵硬问题。

## 摘要（原文）

> Generating lifelike conversational avatars requires modeling not just isolated speakers, but the dynamic, reciprocal interaction of speaking and listening. However, modeling the listener is exceptionally challenging: direct audio-driven training fails, producing stiff, static listening motions. This failure stems from a fundamental imbalance: the speaker's motion is strongly driven by speech audio, while the listener's motion primarily follows an internal motion prior and is only loosely guided by external speech. This challenge has led most methods to focus on speak-only generation. The only prior attempt at joint generation relies on extra speaker's motion to produce the listener. This design is not end-to-end, thereby hindering the real-time applicability. To address this limitation, we present UniLS, the first end-to-end framework for generating unified speak-listen expressions, driven by only dual-track audio. Our method introduces a novel two-stage training paradigm. Stage 1 first learns the internal motion prior by training an audio-free autoregressive generator, capturing the spontaneous dynamics of natural facial motion. Stage 2 then introduces the dual-track audio, fine-tuning the generator to modulate the learned motion prior based on external speech cues. Extensive evaluations show UniLS achieves state-of-the-art speaking accuracy. More importantly, it delivers up to 44.1\% improvement in listening metrics, generating significantly more diverse and natural listening expressions. This effectively mitigates the stiffness problem and provides a practical, high-fidelity audio-driven solution for interactive digital humans.

