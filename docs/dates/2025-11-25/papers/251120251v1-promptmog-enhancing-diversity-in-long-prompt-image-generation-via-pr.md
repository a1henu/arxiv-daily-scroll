---
layout: default
title: PromptMoG: Enhancing Diversity in Long-Prompt Image Generation via Prompt Embedding Mixture-of-Gaussian Sampling
---

# PromptMoG: Enhancing Diversity in Long-Prompt Image Generation via Prompt Embedding Mixture-of-Gaussian Sampling
**arXiv**：[2511.20251v1](https://arxiv.org/abs/2511.20251) · [PDF](https://arxiv.org/pdf/2511.20251.pdf)  
**作者**：Bo-Kai Ruan, Teng-Fang Hsiao, Ling Lo, Yi-Lun Wu, Hong-Han Shuai  

**一句话要点**：提出PromptMoG方法以解决长提示图像生成中的多样性下降问题

**关键词**：文本到图像生成, 长提示生成, 多样性增强, 混合高斯采样, 训练免费方法, 语义保持

## 3 点简述
- 核心问题：长提示在文本到图像生成中增强保真度但抑制多样性，导致输出重复
- 方法要点：通过混合高斯采样提示嵌入，增加采样熵以提升多样性，无需训练
- 实验或效果：在多个先进模型上验证，PromptMoG一致改善多样性且保持语义

## 摘要（原文）

> Recent advances in text-to-image (T2I) generation have achieved remarkable visual outcomes through large-scale rectified flow models. However, how these models behave under long prompts remains underexplored. Long prompts encode rich content, spatial, and stylistic information that enhances fidelity but often suppresses diversity, leading to repetitive and less creative outputs. In this work, we systematically study this fidelity-diversity dilemma and reveal that state-of-the-art models exhibit a clear drop in diversity as prompt length increases. To enable consistent evaluation, we introduce LPD-Bench, a benchmark designed for assessing both fidelity and diversity in long-prompt generation. Building on our analysis, we develop a theoretical framework that increases sampling entropy through prompt reformulation and propose a training-free method, PromptMoG, which samples prompt embeddings from a Mixture-of-Gaussians in the embedding space to enhance diversity while preserving semantics. Extensive experiments on four state-of-the-art models, SD3.5-Large, Flux.1-Krea-Dev, CogView4, and Qwen-Image, demonstrate that PromptMoG consistently improves long-prompt generation diversity without semantic drifting.

