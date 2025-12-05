---
layout: default
title: Aligned but Stereotypical? The Hidden Influence of System Prompts on Social Bias in LVLM-Based Text-to-Image Models
---

# Aligned but Stereotypical? The Hidden Influence of System Prompts on Social Bias in LVLM-Based Text-to-Image Models
**arXiv**：[2512.04981v1](https://arxiv.org/abs/2512.04981) · [PDF](https://arxiv.org/pdf/2512.04981.pdf)  
**作者**：NaHyeon Park, Namin An, Kunhee Kim, Soyeon Yoon, Jiahao Huo, Hyunjung Shim  

**一句话要点**：提出FairPro框架以解决LVLM文本到图像模型中系统提示引发的社会偏见问题

**关键词**：大型视觉语言模型, 文本到图像生成, 社会偏见, 系统提示, 公平性框架, 图像合成

## 3 点简述
- 核心问题：LVLM模型在图像生成中放大社会偏见，系统提示是主要驱动因素
- 方法要点：通过解码中间表示和嵌入关联分析揭示偏见传播机制，提出训练无关的元提示框架FairPro
- 实验或效果：在SANA和Qwen-Image模型上验证，FairPro显著减少偏见并保持文本图像对齐

## 摘要（原文）

> Large vision-language model (LVLM) based text-to-image (T2I) systems have become the dominant paradigm in image generation, yet whether they amplify social biases remains insufficiently understood. In this paper, we show that LVLM-based models produce markedly more socially biased images than non-LVLM-based models. We introduce a 1,024 prompt benchmark spanning four levels of linguistic complexity and evaluate demographic bias across multiple attributes in a systematic manner. Our analysis identifies system prompts, the predefined instructions guiding LVLMs, as a primary driver of biased behavior. Through decoded intermediate representations, token-probability diagnostics, and embedding-association analyses, we reveal how system prompts encode demographic priors that propagate into image synthesis. To this end, we propose FairPro, a training-free meta-prompting framework that enables LVLMs to self-audit and construct fairness-aware system prompts at test time. Experiments on two LVLM-based T2I models, SANA and Qwen-Image, show that FairPro substantially reduces demographic bias while preserving text-image alignment. We believe our findings provide deeper insight into the central role of system prompts in bias propagation and offer a practical, deployable approach for building more socially responsible T2I systems.

