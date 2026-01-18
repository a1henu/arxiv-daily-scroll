---
layout: default
title: Alterbute: Editing Intrinsic Attributes of Objects in Images
---

# Alterbute: Editing Intrinsic Attributes of Objects in Images
**arXiv**：[2601.10714v1](https://arxiv.org/abs/2601.10714) · [PDF](https://arxiv.org/pdf/2601.10714.pdf)  
**作者**：Tal Reiss, Daniel Winter, Matan Cohen, Alex Rav-Acha, Yael Pritch, Ariel Shamir, Yedid Hoshen  

**一句话要点**：提出Alterbute方法，基于扩散模型编辑图像中对象的内在属性，如颜色、纹理、材质和形状，同时保持身份和场景上下文。

**关键词**：扩散模型, 对象属性编辑, 身份保持, 视觉命名实体, 图像生成, 视觉语言模型

## 3 点简述
- 核心问题：现有方法在编辑对象内在属性时，要么依赖无监督先验导致身份保持失败，要么使用过度限制的监督阻碍有意义的属性变化。
- 方法要点：采用松弛训练目标，结合身份参考图像、文本提示和背景图像与对象掩码，推理时重用原始背景和掩码以限制外在变化；引入视觉命名实体（VNEs）作为细粒度身份类别，利用视觉语言模型自动提取标签和属性描述进行可扩展监督。
- 实验或效果：Alterbute在身份保持的对象内在属性编辑任务上优于现有方法，具体性能指标未知。

## 摘要（原文）

> We introduce Alterbute, a diffusion-based method for editing an object's intrinsic attributes in an image. We allow changing color, texture, material, and even the shape of an object, while preserving its perceived identity and scene context. Existing approaches either rely on unsupervised priors that often fail to preserve identity or use overly restrictive supervision that prevents meaningful intrinsic variations. Our method relies on: (i) a relaxed training objective that allows the model to change both intrinsic and extrinsic attributes conditioned on an identity reference image, a textual prompt describing the target intrinsic attributes, and a background image and object mask defining the extrinsic context. At inference, we restrict extrinsic changes by reusing the original background and object mask, thereby ensuring that only the desired intrinsic attributes are altered; (ii) Visual Named Entities (VNEs) - fine-grained visual identity categories (e.g., ''Porsche 911 Carrera'') that group objects sharing identity-defining features while allowing variation in intrinsic attributes. We use a vision-language model to automatically extract VNE labels and intrinsic attribute descriptions from a large public image dataset, enabling scalable, identity-preserving supervision. Alterbute outperforms existing methods on identity-preserving object intrinsic attribute editing.

