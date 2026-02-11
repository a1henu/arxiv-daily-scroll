---
layout: default
title: Understanding and Enhancing Encoder-based Adversarial Transferability against Large Vision-Language Models
---

# Understanding and Enhancing Encoder-based Adversarial Transferability against Large Vision-Language Models
**arXiv**：[2602.09431v1](https://arxiv.org/abs/2602.09431) · [PDF](https://arxiv.org/pdf/2602.09431.pdf)  
**作者**：Xinwei Zhang, Li Bai, Tianwei Zhang, Youqian Zhang, Qingqing Ye, Yingnan Zhao, Ruochen Du, Haibo Hu  

**一句话要点**：提出语义引导多模态攻击以增强大型视觉语言模型中的编码器对抗迁移性

**关键词**：大型视觉语言模型, 对抗攻击, 迁移性, 编码器攻击, 多模态安全, 语义引导

## 3 点简述
- 核心问题：现有编码器攻击在大型视觉语言模型间迁移性差，原因包括视觉定位不一致和语义对齐冗余
- 方法要点：设计SGMA框架，通过语义引导扰动关键区域，破坏全局和局部跨模态定位
- 实验或效果：在多种模型和任务上验证，SGMA相比现有攻击实现更高迁移性，揭示安全风险

## 摘要（原文）

> Large vision-language models (LVLMs) have achieved impressive success across multimodal tasks, but their reliance on visual inputs exposes them to significant adversarial threats. Existing encoder-based attacks perturb the input image by optimizing solely on the vision encoder, rather than the entire LVLM, offering a computationally efficient alternative to end-to-end optimization. However, their transferability across different LVLM architectures in realistic black-box scenarios remains poorly understood. To address this gap, we present the first systematic study towards encoder-based adversarial transferability in LVLMs. Our contributions are threefold. First, through large-scale benchmarking over eight diverse LVLMs, we reveal that existing attacks exhibit severely limited transferability. Second, we perform in-depth analysis, disclosing two root causes that hinder the transferability: (1) inconsistent visual grounding across models, where different models focus their attention on distinct regions; (2) redundant semantic alignment within models, where a single object is dispersed across multiple overlapping token representations. Third, we propose Semantic-Guided Multimodal Attack (SGMA), a novel framework to enhance the transferability. Inspired by the discovered causes in our analysis, SGMA directs perturbations toward semantically critical regions and disrupts cross-modal grounding at both global and local levels. Extensive experiments across different victim models and tasks show that SGMA achieves higher transferability than existing attacks. These results expose critical security risks in LVLM deployment and underscore the urgent need for robust multimodal defenses.

