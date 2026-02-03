---
layout: default
title: Preserving Localized Patch Semantics in VLMs
---

# Preserving Localized Patch Semantics in VLMs
**arXiv**：[2602.01530v1](https://arxiv.org/abs/2602.01530) · [PDF](https://arxiv.org/pdf/2602.01530.pdf)  
**作者**：Parsa Esmaeilkhani, Longin Jan Latecki  

**一句话要点**：提出Logit Lens Loss以解决视觉语言模型中图像令牌语义扩散问题，提升可解释性和视觉任务性能。

**关键词**：视觉语言模型, 可解释性, Logit Lens, 自注意力机制, 图像分割

## 3 点简述
- 核心问题：Logit Lens在视觉语言模型中因图像令牌语义扩散至语言令牌，导致可视化失效，无法解释图像概念。
- 方法要点：引入Logit Lens Loss作为补充损失，约束自注意力层中图像与文本令牌混合，保持图像令牌与对应图像区域的语义对齐。
- 实验或效果：LLL使Logit Lens产生有意义的对象置信度图，并提升分割等视觉中心任务性能，无需架构修改或大规模训练。

## 摘要（原文）

> Logit Lens has been proposed for visualizing tokens that contribute most to LLM answers. Recently, Logit Lens was also shown to be applicable in autoregressive Vision-Language Models (VLMs), where it illustrates the conceptual content of image tokens in the form of heatmaps, e.g., which image tokens are likely to depict the concept of cat in a given image. However, the visual content of image tokens often gets diffused to language tokens, and consequently, the locality of visual information gets mostly destroyed, which renders Logit Lens visualization unusable for explainability. To address this issue, we introduce a complementary loss to next-token prediction (NTP) to prevent the visual tokens from losing the visual representation inherited from corresponding image patches. The proposed Logit Lens Loss (LLL) is designed to make visual token embeddings more semantically aligned with the textual concepts that describe their image regions (e.g., patches containing a cat with the word "cat"), without requiring any architectural modification or large-scale training. This way, LLL constrains the mixing of image and text tokens in the self-attention layers in order to prevent image tokens from losing their localized visual information. As our experiments show, LLL not only makes Logit Lens practically relevant by producing meaningful object confidence maps in images, but also improves performance on vision-centric tasks like segmentation without attaching any special heads.

