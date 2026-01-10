---
layout: default
title: Mechanisms of Prompt-Induced Hallucination in Vision-Language Models
---

# Mechanisms of Prompt-Induced Hallucination in Vision-Language Models
**arXiv**：[2601.05201v1](https://arxiv.org/abs/2601.05201) · [PDF](https://arxiv.org/pdf/2601.05201.pdf)  
**作者**：William Rudman, Michal Golovanevsky, Dana Arad, Yonatan Belinkov, Ritambhara Singh, Carsten Eickhoff, Kyle Mahowald  

**一句话要点**：通过机制分析揭示视觉语言模型中提示诱导幻觉的注意力头作用，实现无训练缓解

**关键词**：视觉语言模型, 提示诱导幻觉, 注意力机制, 对象计数, 机制分析, 无训练缓解

## 3 点简述
- 研究视觉语言模型在对象计数任务中因文本提示过估而忽视视觉证据的幻觉问题
- 通过机制分析识别出少量关键注意力头，其消融可显著减少幻觉至少40%
- 实验表明消融后模型更倾向于纠正提示，向视觉证据对齐，揭示模型间实现差异

## 摘要（原文）

> Large vision-language models (VLMs) are highly capable, yet often hallucinate by favoring textual prompts over visual evidence. We study this failure mode in a controlled object-counting setting, where the prompt overstates the number of objects in the image (e.g., asking a model to describe four waterlilies when only three are present). At low object counts, models often correct the overestimation, but as the number of objects increases, they increasingly conform to the prompt regardless of the discrepancy. Through mechanistic analysis of three VLMs, we identify a small set of attention heads whose ablation substantially reduces prompt-induced hallucinations (PIH) by at least 40% without additional training. Across models, PIH-heads mediate prompt copying in model-specific ways. We characterize these differences and show that PIH ablation increases correction toward visual evidence. Our findings offer insights into the internal mechanisms driving prompt-induced hallucinations, revealing model-specific differences in how these behaviors are implemented.

