---
layout: default
title: ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting
---

# ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting
**arXiv**：[2601.01847v1](https://arxiv.org/abs/2601.01847) · [PDF](https://arxiv.org/pdf/2601.01847.pdf)  
**作者**：Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong  

**一句话要点**：提出ESGaussianFace框架，通过3D高斯泼溅实现情感与风格化音频驱动面部动画

**关键词**：音频驱动面部动画, 3D高斯泼溅, 情感建模, 风格化变形, 多阶段训练

## 3 点简述
- 核心问题：现有音频驱动面部动画多关注中性情感，高效生成高质量情感与风格化视频仍具挑战
- 方法要点：利用3D高斯泼溅重建3D场景，结合情感音频引导空间注意力和3D高斯变形预测器
- 实验或效果：在唇动准确性、表情变化和风格表达上优于现有技术，生成高效高质量3D一致结果

## 摘要（原文）

> Most current audio-driven facial animation research primarily focuses on generating videos with neutral emotions. While some studies have addressed the generation of facial videos driven by emotional audio, efficiently generating high-quality talking head videos that integrate both emotional expressions and style features remains a significant challenge. In this paper, we propose ESGaussianFace, an innovative framework for emotional and stylized audio-driven facial animation. Our approach leverages 3D Gaussian Splatting to reconstruct 3D scenes and render videos, ensuring efficient generation of 3D consistent results. We propose an emotion-audio-guided spatial attention method that effectively integrates emotion features with audio content features. Through emotion-guided attention, the model is able to reconstruct facial details across different emotional states more accurately. To achieve emotional and stylized deformations of the 3D Gaussian points through emotion and style features, we introduce two 3D Gaussian deformation predictors. Futhermore, we propose a multi-stage training strategy, enabling the step-by-step learning of the character's lip movements, emotional variations, and style features. Our generated results exhibit high efficiency, high quality, and 3D consistency. Extensive experimental results demonstrate that our method outperforms existing state-of-the-art techniques in terms of lip movement accuracy, expression variation, and style feature expressiveness.

