---
layout: default
title: Style Transfer as Bias Mitigation: Diffusion Models for Synthetic Mental Health Text for Arabic
---

# Style Transfer as Bias Mitigation: Diffusion Models for Synthetic Mental Health Text for Arabic
**arXiv**：[2601.14124v1](https://arxiv.org/abs/2601.14124) · [PDF](https://arxiv.org/pdf/2601.14124.pdf)  
**作者**：Saad Mankarious, Aya Zirikly  

**一句话要点**：提出基于扩散模型的风格迁移方法，以缓解阿拉伯语心理健康文本中的性别偏见。

**关键词**：扩散模型, 风格迁移, 偏见缓解, 合成文本生成, 阿拉伯语心理健康

## 3 点简述
- 核心问题：现有合成数据方法依赖预训练大语言模型，可能输出多样性有限并传播训练数据中的偏见。
- 方法要点：将偏见缓解视为风格迁移问题，使用扩散模型生成高熵、语义保真的合成文本，无需预训练。
- 实验或效果：在CARMA阿拉伯语心理健康语料库上，通过男性到女性风格迁移增强女性内容，定量评估显示高语义保真度和风格差异。

## 摘要（原文）

> Synthetic data offers a promising solution for mitigating data scarcity and demographic bias in mental health analysis, yet existing approaches largely rely on pretrained large language models (LLMs), which may suffer from limited output diversity and propagate biases inherited from their training data. In this work, we propose a pretraining-free diffusion-based approach for synthetic text generation that frames bias mitigation as a style transfer problem. Using the CARMA Arabic mental health corpus, which exhibits a substantial gender imbalance, we focus on male-to-female style transfer to augment underrepresented female-authored content. We construct five datasets capturing varying linguistic and semantic aspects of gender expression in Arabic and train separate diffusion models for each setting. Quantitative evaluations demonstrate consistently high semantic fidelity between source and generated text, alongside meaningful surface-level stylistic divergence, while qualitative analysis confirms linguistically plausible gender transformations. Our results show that diffusion-based style transfer can generate high-entropy, semantically faithful synthetic data without reliance on pretrained LLMs, providing an effective and flexible framework for mitigating gender bias in sensitive, low-resource mental health domains.

