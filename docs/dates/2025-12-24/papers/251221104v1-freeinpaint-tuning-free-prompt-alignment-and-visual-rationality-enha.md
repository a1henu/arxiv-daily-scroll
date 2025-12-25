---
layout: default
title: FreeInpaint: Tuning-free Prompt Alignment and Visual Rationality Enhancement in Image Inpainting
---

# FreeInpaint: Tuning-free Prompt Alignment and Visual Rationality Enhancement in Image Inpainting
**arXiv**：[2512.21104v1](https://arxiv.org/abs/2512.21104) · [PDF](https://arxiv.org/pdf/2512.21104.pdf)  
**作者**：Chao Gong, Dong Li, Yingwei Pan, Jingjing Chen, Ting Yao, Tao Mei  

**一句话要点**：提出FreeInpaint以优化文本引导图像修复中的提示对齐与视觉合理性

**关键词**：图像修复, 扩散模型, 提示对齐, 视觉合理性, 优化方法, 推理优化

## 3 点简述
- 核心问题：现有方法难以同时保证文本提示对齐与视觉合理性。
- 方法要点：通过先验引导噪声优化和复合引导目标，在推理时直接优化扩散潜变量。
- 实验或效果：在多种扩散模型和评估指标上验证了方法的有效性和鲁棒性。

## 摘要（原文）

> Text-guided image inpainting endeavors to generate new content within specified regions of images using textual prompts from users. The primary challenge is to accurately align the inpainted areas with the user-provided prompts while maintaining a high degree of visual fidelity. While existing inpainting methods have produced visually convincing results by leveraging the pre-trained text-to-image diffusion models, they still struggle to uphold both prompt alignment and visual rationality simultaneously. In this work, we introduce FreeInpaint, a plug-and-play tuning-free approach that directly optimizes the diffusion latents on the fly during inference to improve the faithfulness of the generated images. Technically, we introduce a prior-guided noise optimization method that steers model attention towards valid inpainting regions by optimizing the initial noise. Furthermore, we meticulously design a composite guidance objective tailored specifically for the inpainting task. This objective efficiently directs the denoising process, enhancing prompt alignment and visual rationality by optimizing intermediate latents at each step. Through extensive experiments involving various inpainting diffusion models and evaluation metrics, we demonstrate the effectiveness and robustness of our proposed FreeInpaint.

