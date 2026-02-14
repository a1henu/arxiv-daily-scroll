---
layout: default
title: Neutral Prompts, Non-Neutral People: Quantifying Gender and Skin-Tone Bias in Gemini Flash 2.5 Image and GPT Image 1.5
---

# Neutral Prompts, Non-Neutral People: Quantifying Gender and Skin-Tone Bias in Gemini Flash 2.5 Image and GPT Image 1.5
**arXiv**：[2602.12133v1](https://arxiv.org/abs/2602.12133) · [PDF](https://arxiv.org/pdf/2602.12133.pdf)  
**作者**：Roberto Balestri  

**一句话要点**：量化Gemini Flash 2.5与GPT Image 1.5在性别和肤色上的偏见，揭示中性提示的默认偏差

**关键词**：图像生成偏见, 肤色量化, 性别偏差, 算法审计, 中性提示分析, 合成图像评估

## 3 点简述
- 研究量化了Gemini Flash 2.5和GPT Image 1.5图像生成器中的性别和肤色偏见，挑战中性提示产生中性输出的假设。
- 采用混合颜色归一化、面部地标掩码和感知均匀肤色量化方法，分析3200张真实感图像。
- 结果显示模型存在强烈'默认白人'偏见，但性别偏好相反：Gemini偏向女性，GPT偏向浅肤色男性。

## 摘要（原文）

> This study quantifies gender and skin-tone bias in two widely deployed commercial image generators - Gemini Flash 2.5 Image (NanoBanana) and GPT Image 1.5 - to test the assumption that neutral prompts yield demographically neutral outputs. We generated 3,200 photorealistic images using four semantically neutral prompts. The analysis employed a rigorous pipeline combining hybrid color normalization, facial landmark masking, and perceptually uniform skin tone quantification using the Monk (MST), PERLA, and Fitzpatrick scales. Neutral prompts produced highly polarized defaults. Both models exhibited a strong "default white" bias (>96% of outputs). However, they diverged sharply on gender: Gemini favored female-presenting subjects, while GPT favored male-presenting subjects with lighter skin tones. This research provides a large-scale, comparative audit of state-of-the-art models using an illumination-aware colorimetric methodology, distinguishing aesthetic rendering from underlying pigmentation in synthetic imagery. The study demonstrates that neutral prompts function as diagnostic probes rather than neutral instructions. It offers a robust framework for auditing algorithmic visual culture and challenges the sociolinguistic assumption that unmarked language results in inclusive representation.

