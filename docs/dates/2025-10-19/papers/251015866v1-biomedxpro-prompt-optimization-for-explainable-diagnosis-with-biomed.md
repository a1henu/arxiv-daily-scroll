---
layout: default
title: BiomedXPro: Prompt Optimization for Explainable Diagnosis with Biomedical Vision Language Models
---

# BiomedXPro: Prompt Optimization for Explainable Diagnosis with Biomedical Vision Language Models
**arXiv**：[2510.15866v1](https://arxiv.org/abs/2510.15866) · [PDF](https://arxiv.org/pdf/2510.15866.pdf)  
**作者**：Kaushitha Silva, Mansitha Eashwara, Sanduni Ubayasiri, Ruwan Tennakoon, Damayanthi Herath  

**一句话要点**：提出BiomedXPro框架以优化生物医学视觉语言模型的提示生成，提升诊断可解释性。

**关键词**：生物医学视觉语言模型, 提示优化, 可解释诊断, 进化框架, 少样本学习

## 3 点简述
- 核心问题：现有提示优化方法缺乏透明度，无法捕捉临床诊断的多面性，限制模型可信度。
- 方法要点：使用进化框架和大语言模型自动生成多样、可解释的自然语言提示对。
- 实验或效果：在多个生物医学基准上优于先进方法，尤其在少样本设置中表现突出。

## 摘要（原文）

> The clinical adoption of biomedical vision-language models is hindered by
> prompt optimization techniques that produce either uninterpretable latent
> vectors or single textual prompts. This lack of transparency and failure to
> capture the multi-faceted nature of clinical diagnosis, which relies on
> integrating diverse observations, limits their trustworthiness in high-stakes
> settings. To address this, we introduce BiomedXPro, an evolutionary framework
> that leverages a large language model as both a biomedical knowledge extractor
> and an adaptive optimizer to automatically generate a diverse ensemble of
> interpretable, natural-language prompt pairs for disease diagnosis. Experiments
> on multiple biomedical benchmarks show that BiomedXPro consistently outperforms
> state-of-the-art prompt-tuning methods, particularly in data-scarce few-shot
> settings. Furthermore, our analysis demonstrates a strong semantic alignment
> between the discovered prompts and statistically significant clinical features,
> grounding the model's performance in verifiable concepts. By producing a
> diverse ensemble of interpretable prompts, BiomedXPro provides a verifiable
> basis for model predictions, representing a critical step toward the
> development of more trustworthy and clinically-aligned AI systems.

