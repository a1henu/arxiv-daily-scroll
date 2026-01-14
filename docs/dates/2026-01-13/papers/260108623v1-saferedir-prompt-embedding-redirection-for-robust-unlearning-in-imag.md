---
layout: default
title: SafeRedir: Prompt Embedding Redirection for Robust Unlearning in Image Generation Models
---

# SafeRedir: Prompt Embedding Redirection for Robust Unlearning in Image Generation Models
**arXiv**：[2601.08623v1](https://arxiv.org/abs/2601.08623) · [PDF](https://arxiv.org/pdf/2601.08623.pdf)  
**作者**：Renyang Liu, Kangjie Chen, Han Qiu, Jie Zhang, Kwok-Yan Lam, Tianwei Zhang, See-Kiong Ng  

**一句话要点**：提出SafeRedir框架，通过提示嵌入重定向实现图像生成模型的鲁棒性遗忘

**关键词**：图像生成模型, 遗忘学习, 提示嵌入, 推理时干预, 鲁棒性安全, 多模态分类器

## 3 点简述
- 图像生成模型易记忆有害概念，如NSFW内容，现有遗忘方法成本高或鲁棒性差。
- SafeRedir在推理时通过嵌入空间干预，将不安全提示重定向到安全语义区域，无需修改模型。
- 实验表明，该方法有效遗忘有害概念，保持生成质量，并抵抗对抗攻击，兼容多种模型。

## 摘要（原文）

> Image generation models (IGMs), while capable of producing impressive and creative content, often memorize a wide range of undesirable concepts from their training data, leading to the reproduction of unsafe content such as NSFW imagery and copyrighted artistic styles. Such behaviors pose persistent safety and compliance risks in real-world deployments and cannot be reliably mitigated by post-hoc filtering, owing to the limited robustness of such mechanisms and a lack of fine-grained semantic control. Recent unlearning methods seek to erase harmful concepts at the model level, which exhibit the limitations of requiring costly retraining, degrading the quality of benign generations, or failing to withstand prompt paraphrasing and adversarial attacks. To address these challenges, we introduce SafeRedir, a lightweight inference-time framework for robust unlearning via prompt embedding redirection. Without modifying the underlying IGMs, SafeRedir adaptively routes unsafe prompts toward safe semantic regions through token-level interventions in the embedding space. The framework comprises two core components: a latent-aware multi-modal safety classifier for identifying unsafe generation trajectories, and a token-level delta generator for precise semantic redirection, equipped with auxiliary predictors for token masking and adaptive scaling to localize and regulate the intervention. Empirical results across multiple representative unlearning tasks demonstrate that SafeRedir achieves effective unlearning capability, high semantic and perceptual preservation, robust image quality, and enhanced resistance to adversarial attacks. Furthermore, SafeRedir generalizes effectively across a variety of diffusion backbones and existing unlearned models, validating its plug-and-play compatibility and broad applicability. Code and data are available at https://github.com/ryliu68/SafeRedir.

