---
layout: default
title: A Picture is Worth a Thousand (Correct) Captions: A Vision-Guided Judge-Corrector System for Multimodal Machine Translation
---

# A Picture is Worth a Thousand (Correct) Captions: A Vision-Guided Judge-Corrector System for Multimodal Machine Translation
**arXiv**：[2511.07010v1](https://arxiv.org/abs/2511.07010) · [PDF](https://arxiv.org/pdf/2511.07010.pdf)  
**作者**：Siddharth Betala, Kushan Raj, Vipul Betala, Rohan Saswade  

**一句话要点**：提出视觉引导的评判-纠正系统，通过自动错误检测与纠正提升多模态机器翻译质量。

**关键词**：多模态机器翻译, 错误检测与纠正, 参数高效微调, 视觉引导系统, BLEU分数评估

## 3 点简述
- 核心问题：训练数据中存在翻译错误和视觉歧义，影响多模态机器翻译性能。
- 方法要点：使用多模态语言模型分类翻译错误，并路由到GPT-4o-mini或IndicTrans2进行纠正。
- 实验效果：在英语-孟加拉语等语言对上，BLEU分数平均提升0.10至1.30点。

## 摘要（原文）

> In this paper, we describe our system under the team name BLEU Monday for the
> English-to-Indic Multimodal Translation Task at WAT 2025. We participate in the
> text-only translation tasks for English-Hindi, English-Bengali,
> English-Malayalam, and English-Odia language pairs. We present a two-stage
> approach that addresses quality issues in the training data through automated
> error detection and correction, followed by parameter-efficient model
> fine-tuning.
>   Our methodology introduces a vision-augmented judge-corrector pipeline that
> leverages multimodal language models to systematically identify and correct
> translation errors in the training data. The judge component classifies
> translations into three categories: correct, visually ambiguous (requiring
> image context), or mistranslated (poor translation quality). Identified errors
> are routed to specialized correctors: GPT-4o-mini regenerates captions
> requiring visual disambiguation, while IndicTrans2 retranslates cases with pure
> translation quality issues. This automated pipeline processes 28,928 training
> examples across four languages, correcting an average of 17.1% of captions per
> language.
>   We then apply Low-Rank Adaptation (LoRA) to fine-tune the IndicTrans2
> en-indic 200M distilled model on both original and corrected datasets. Training
> on corrected data yields consistent improvements, with BLEU score gains of
> +1.30 for English-Bengali on the evaluation set (42.00 -> 43.30) and +0.70 on
> the challenge set (44.90 -> 45.60), +0.60 for English-Odia on the evaluation
> set (41.00 -> 41.60), and +0.10 for English-Hindi on the challenge set (53.90
> -> 54.00).

