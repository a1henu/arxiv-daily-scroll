---
layout: default
title: VerLM: Explaining Face Verification Using Natural Language
---

# VerLM: Explaining Face Verification Using Natural Language
**arXiv**：[2601.01798v1](https://arxiv.org/abs/2601.01798) · [PDF](https://arxiv.org/pdf/2601.01798.pdf)  
**作者**：Syed Abdul Hannan, Hazim Bukhari, Thomas Cantalapiedra, Eman Ansar, Massa Baali, Rita Singh, Bhiksha Raj  

**一句话要点**：提出VerLM模型以解决人脸验证系统决策过程不透明的问题，通过自然语言解释决策依据。

**关键词**：人脸验证, 视觉语言模型, 可解释性, 跨模态迁移, 自然语言解释

## 3 点简述
- 核心问题：人脸验证系统缺乏透明度，决策过程难以理解。
- 方法要点：采用视觉语言模型，结合简洁和详细两种解释风格，跨模态迁移音频模型技术。
- 实验或效果：模型性能优于基线方法，提升准确性和可解释性。

## 摘要（原文）

> Face verification systems have seen substantial advancements; however, they often lack transparency in their decision-making processes. In this paper, we introduce an innovative Vision-Language Model (VLM) for Face Verification, which not only accurately determines if two face images depict the same individual but also explicitly explains the rationale behind its decisions. Our model is uniquely trained using two complementary explanation styles: (1) concise explanations that summarize the key factors influencing its decision, and (2) comprehensive explanations detailing the specific differences observed between the images. We adapt and enhance a state-of-the-art modeling approach originally designed for audio-based differentiation to suit visual inputs effectively. This cross-modal transfer significantly improves our model's accuracy and interpretability. The proposed VLM integrates sophisticated feature extraction techniques with advanced reasoning capabilities, enabling clear articulation of its verification process. Our approach demonstrates superior performance, surpassing baseline methods and existing models. These findings highlight the immense potential of vision language models in face verification set up, contributing to more transparent, reliable, and explainable face verification systems.

