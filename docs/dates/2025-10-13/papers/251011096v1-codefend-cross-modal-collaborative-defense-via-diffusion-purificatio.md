---
layout: default
title: CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization
---

# CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization
**arXiv**：[2510.11096v1](https://arxiv.org/abs/2510.11096) · [PDF](https://arxiv.org/pdf/2510.11096.pdf)  
**作者**：Fengling Zhu, Boshi Liu, Jingyu Hua, Sheng Zhong  

**一句话要点**：提出监督扩散去噪与提示优化以防御多模态大语言模型的视觉对抗攻击

**关键词**：多模态防御, 扩散去噪, 提示优化, 对抗攻击, 图像重建, 鲁棒性提升

## 3 点简述
- 多模态大语言模型易受视觉对抗攻击，导致有害或误导输出
- 使用监督扩散去噪框架，结合任务特定指导提升图像重建质量与防御鲁棒性
- 在图像描述和视觉问答任务中验证，显著提升鲁棒性并具强迁移性

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable success in
> tasks such as image captioning, visual question answering, and cross-modal
> reasoning by integrating visual and textual modalities. However, their
> multimodal nature also exposes them to adversarial threats, where attackers can
> perturb either modality or both jointly to induce harmful, misleading, or
> policy violating outputs. Existing defense strategies, such as adversarial
> training and input purification, face notable limitations: adversarial training
> typically improves robustness only against known attacks while incurring high
> computational costs, whereas conventional purification approaches often suffer
> from degraded image quality and insufficient generalization to complex
> multimodal tasks.
>   In this work, we focus on defending the visual modality, which frequently
> serves as the primary entry point for adversarial manipulation. We propose a
> supervised diffusion based denoising framework that leverages paired
> adversarial clean image datasets to fine-tune diffusion models with
> directional, task specific guidance. Unlike prior unsupervised purification
> methods such as DiffPure, our approach achieves higher quality reconstructions
> while significantly improving defense robustness in multimodal tasks.
> Furthermore, we incorporate prompt optimization as a complementary defense
> mechanism, enhancing resistance against diverse and unseen attack strategies.
>   Extensive experiments on image captioning and visual question answering
> demonstrate that our method not only substantially improves robustness but also
> exhibits strong transferability to unknown adversarial attacks. These results
> highlight the effectiveness of supervised diffusion based denoising for
> multimodal defense, paving the way for more reliable and secure deployment of
> MLLMs in real world applications.

