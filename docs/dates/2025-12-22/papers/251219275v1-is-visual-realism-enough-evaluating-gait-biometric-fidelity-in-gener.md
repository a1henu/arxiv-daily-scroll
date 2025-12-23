---
layout: default
title: Is Visual Realism Enough? Evaluating Gait Biometric Fidelity in Generative AI Human Animation
---

# Is Visual Realism Enough? Evaluating Gait Biometric Fidelity in Generative AI Human Animation
**arXiv**：[2512.19275v1](https://arxiv.org/abs/2512.19275) · [PDF](https://arxiv.org/pdf/2512.19275.pdf)  
**作者**：Ivan DeAndres-Tame, Chengwei Ye, Ruben Tolosana, Ruben Vera-Rodriguez, Shiqi Yu  

**一句话要点**：评估生成式AI人体动画在步态生物识别中的保真度，揭示视觉真实性与身份识别间的差距

**关键词**：生成式AI, 步态生物识别, 人体动画, 身份转移, 视觉保真度, 时空细节

## 3 点简述
- 核心问题：生成式AI模型在人体动画中视觉真实度高，但步态生物识别保真度低，难以分离身份与运动。
- 方法要点：评估四种生成式AI模型在步态模式恢复和身份转移任务中的表现，分析时空细节保留能力。
- 实验或效果：结果显示身份识别任务中生物识别保真度低，身份转移任务暴露基于外观的步态识别缺陷，模型依赖视觉属性而非时间动态。

## 摘要（原文）

> Generative AI (GenAI) models have revolutionized animation, enabling the synthesis of humans and motion patterns with remarkable visual fidelity. However, generating truly realistic human animation remains a formidable challenge, where even minor inconsistencies can make a subject appear unnatural. This limitation is particularly critical when AI-generated videos are evaluated for behavioral biometrics, where subtle motion cues that define identity are easily lost or distorted. The present study investigates whether state-of-the-art GenAI human animation models can preserve the subtle spatio-temporal details needed for person identification through gait biometrics. Specifically, we evaluate four different GenAI models across two primary evaluation tasks to assess their ability to i) restore gait patterns from reference videos under varying conditions of complexity, and ii) transfer these gait patterns to different visual identities. Our results show that while visual quality is mostly high, biometric fidelity remains low in tasks focusing on identification, suggesting that current GenAI models struggle to disentangle identity from motion. Furthermore, through an identity transfer task, we expose a fundamental flaw in appearance-based gait recognition: when texture is disentangled from motion, identification collapses, proving current GenAI models rely on visual attributes rather than temporal dynamics.

