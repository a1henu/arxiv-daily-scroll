---
layout: default
title: A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis
---

# A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis
**arXiv**：[2512.16063v1](https://arxiv.org/abs/2512.16063) · [PDF](https://arxiv.org/pdf/2512.16063.pdf)  
**作者**：Qidi Xu, Nuzha Amjad, Grace Giles, Alexa Cumming, De'angelo Hermesky, Alexander Wen, Min Ji Kwak, Yejin Kim  

**一句话要点**：提出多智能体大语言模型框架CoTI，以自动化慢性病患者访谈的定性主题分析。

**关键词**：多智能体框架, 大语言模型, 定性主题分析, 慢性病研究, 自动化分析, 人机交互

## 3 点简述
- 核心问题：定性主题分析在慢性病研究中劳动密集、主观性强且难以扩展。
- 方法要点：通过Instructor、Thematizer、CodebookGenerator三个智能体协作，自动识别关键短语、主题和生成代码本。
- 实验或效果：应用于12例心衰患者访谈，CoTI结果比初级研究者和基线NLP模型更接近资深研究者，但人机协作增益有限。

## 摘要（原文）

> Understanding patients experiences is essential for advancing patient centered care, especially in chronic diseases that require ongoing communication. However, qualitative thematic analysis, the primary approach for exploring these experiences, remains labor intensive, subjective, and difficult to scale. In this study, we developed a multi agent large language model framework that automates qualitative thematic analysis through three agents (Instructor, Thematizer, CodebookGenerator), named Collaborative Theme Identification Agent (CoTI). We applied CoTI to 12 heart failure patient interviews to analyze their perceptions of medication intensity. CoTI identified key phrases, themes, and codebook that were more similar to those of the senior investigator than both junior investigators and baseline NLP models. We also implemented CoTI into a user-facing application to enable AI human interaction in qualitative analysis. However, collaboration between CoTI and junior investigators provided only marginal gains, suggesting they may overrely on CoTI and limit their independent critical thinking.

