---
layout: default
title: Hallucination Filtering in Radiology Vision-Language Models Using Discrete Semantic Entropy
---

# Hallucination Filtering in Radiology Vision-Language Models Using Discrete Semantic Entropy
**arXiv**：[2510.09256v1](https://arxiv.org/abs/2510.09256) · [PDF](https://arxiv.org/pdf/2510.09256.pdf)  
**作者**：Patrick Wienholt, Sophie Caselitz, Robert Siepmann, Philipp Bruners, Keno Bressem, Christiane Kuhl, Jakob Nikolas Kather, Sven Nebelung, Daniel Truhn  
**一句话要点**：提出离散语义熵以过滤放射学视觉语言模型中的幻觉，提升诊断准确性
**关键词**：视觉语言模型, 离散语义熵, 幻觉过滤, 放射学视觉问答, 诊断准确性

## 3 点简述
- 核心问题：黑盒视觉语言模型在放射学视觉问答中易产生幻觉，影响诊断准确性。
- 方法要点：使用离散语义熵量化语义不一致性，过滤高熵问题以减少幻觉。
- 实验或效果：在706个图像-问题对中，过滤后GPT-4o准确率从51.7%提升至76.3%。

## 摘要（原文）

> To determine whether using discrete semantic entropy (DSE) to reject
> questions likely to generate hallucinations can improve the accuracy of
> black-box vision-language models (VLMs) in radiologic image based visual
> question answering (VQA). This retrospective study evaluated DSE using two
> publicly available, de-identified datasets: (i) the VQA-Med 2019 benchmark (500
> images with clinical questions and short-text answers) and (ii) a diagnostic
> radiology dataset (206 cases: 60 computed tomography scans, 60 magnetic
> resonance images, 60 radiographs, 26 angiograms) with corresponding
> ground-truth diagnoses. GPT-4o and GPT-4.1 answered each question 15 times
> using a temperature of 1.0. Baseline accuracy was determined using
> low-temperature answers (temperature 0.1). Meaning-equivalent responses were
> grouped using bidirectional entailment checks, and DSE was computed from the
> relative frequencies of the resulting semantic clusters. Accuracy was
> recalculated after excluding questions with DSE > 0.6 or > 0.3. p-values and
> 95% confidence intervals were obtained using bootstrap resampling and a
> Bonferroni-corrected threshold of p < .004 for statistical significance. Across
> 706 image-question pairs, baseline accuracy was 51.7% for GPT-4o and 54.8% for
> GPT-4.1. After filtering out high-entropy questions (DSE > 0.3), accuracy on
> the remaining questions was 76.3% (retained questions: 334/706) for GPT-4o and
> 63.8% (retained questions: 499/706) for GPT-4.1 (both p < .001). Accuracy gains
> were observed across both datasets and largely remained statistically
> significant after Bonferroni correction. DSE enables reliable hallucination
> detection in black-box VLMs by quantifying semantic inconsistency. This method
> significantly improves diagnostic answer accuracy and offers a filtering
> strategy for clinical VLM applications.

