---
layout: default
title: Neutral Prompts, Non-Neutral People: Quantifying Gender and Skin-Tone Bias in Gemini Flash 2.5 Image and GPT Image 1.5
---

# Neutral Prompts, Non-Neutral People: Quantifying Gender and Skin-Tone Bias in Gemini Flash 2.5 Image and GPT Image 1.5
**arXiv**：[2602.12133v1](https://arxiv.org/abs/2602.12133) · [PDF](https://arxiv.org/pdf/2602.12133.pdf)  
**作者**：Roberto Balestri  

**一句话要点**：量化Gemini Flash 2.5与GPT Image 1.5在性别和肤色上的偏见，揭示中性提示的默认极化现象。

**关键词**：图像生成偏见, 肤色量化, 性别偏见, 算法审计, 合成图像分析, 中性提示诊断

## 3 点简述
- 核心问题：中性提示是否导致图像生成模型输出人口统计学中性结果，量化性别和肤色偏见。
- 方法要点：使用混合颜色归一化、面部地标掩码和感知均匀肤色量化（MST、PERLA、Fitzpatrick尺度）的严格分析流程。
- 实验或效果：生成3200张照片级真实图像，发现模型存在强烈默认白人偏见，但性别偏好不同。

## 摘要（原文）

> This study quantifies gender and skin-tone bias in two widely deployed commercial image generators - Gemini Flash 2.5 Image (NanoBanana) and GPT Image 1.5 - to test the assumption that neutral prompts yield demographically neutral outputs. We generated 3,200 photorealistic images using four semantically neutral prompts. The analysis employed a rigorous pipeline combining hybrid color normalization, facial landmark masking, and perceptually uniform skin tone quantification using the Monk (MST), PERLA, and Fitzpatrick scales. Neutral prompts produced highly polarized defaults. Both models exhibited a strong "default white" bias (>96% of outputs). However, they diverged sharply on gender: Gemini favored female-presenting subjects, while GPT favored male-presenting subjects with lighter skin tones. This research provides a large-scale, comparative audit of state-of-the-art models using an illumination-aware colorimetric methodology, distinguishing aesthetic rendering from underlying pigmentation in synthetic imagery. The study demonstrates that neutral prompts function as diagnostic probes rather than neutral instructions. It offers a robust framework for auditing algorithmic visual culture and challenges the sociolinguistic assumption that unmarked language results in inclusive representation.

