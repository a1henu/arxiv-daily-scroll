---
layout: default
title: TextShield-R1: Reinforced Reasoning for Tampered Text Detection
---

# TextShield-R1: Reinforced Reasoning for Tampered Text Detection
**arXiv**：[2602.19828v1](https://arxiv.org/abs/2602.19828) · [PDF](https://arxiv.org/pdf/2602.19828.pdf)  
**作者**：Chenfan Qu, Yiwu Zhong, Jian Liu, Xuekang Zhu, Bohan Yu, Lianwen Jin  

**一句话要点**：提出TextShield-R1，基于强化学习的多模态大语言模型，用于篡改文本检测与推理

**关键词**：篡改文本检测, 多模态大语言模型, 强化学习, OCR校正, 法医持续预训练, TFR基准

## 3 点简述
- 核心问题：篡改图像检测中，现有方法难以识别微观伪影、定位精度低且依赖昂贵标注
- 方法要点：采用法医持续预训练和组相对策略优化，结合OCR校正提升推理与定位能力
- 实验或效果：在包含多语言、多篡改技术的TFR基准上，显著提升可解释篡改文本检测性能

## 摘要（原文）

> The growing prevalence of tampered images poses serious security threats, highlighting the urgent need for reliable detection methods. Multimodal large language models (MLLMs) demonstrate strong potential in analyzing tampered images and generating interpretations. However, they still struggle with identifying micro-level artifacts, exhibit low accuracy in localizing tampered text regions, and heavily rely on expensive annotations for forgery interpretation. To this end, we introduce TextShield-R1, the first reinforcement learning based MLLM solution for tampered text detection and reasoning. Specifically, our approach introduces Forensic Continual Pre-training, an easy-to-hard curriculum that well prepares the MLLM for tampered text detection by harnessing the large-scale cheap data from natural image forensic and OCR tasks. During fine-tuning, we perform Group Relative Policy Optimization with novel reward functions to reduce annotation dependency and improve reasoning capabilities. At inference time, we enhance localization accuracy via OCR Rectification, a method that leverages the MLLM's strong text recognition abilities to refine its predictions. Furthermore, to support rigorous evaluation, we introduce the Text Forensics Reasoning (TFR) benchmark, comprising over 45k real and tampered images across 16 languages, 10 tampering techniques, and diverse domains. Rich reasoning-style annotations are included, allowing for comprehensive assessment. Our TFR benchmark simultaneously addresses seven major limitations of existing benchmarks and enables robust evaluation under cross-style, cross-method, and cross-language conditions. Extensive experiments demonstrate that TextShield-R1 significantly advances the state of the art in interpretable tampered text detection.

