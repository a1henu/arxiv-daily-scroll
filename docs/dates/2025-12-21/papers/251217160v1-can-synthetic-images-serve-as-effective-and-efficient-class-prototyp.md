---
layout: default
title: Can Synthetic Images Serve as Effective and Efficient Class Prototypes?
---

# Can Synthetic Images Serve as Effective and Efficient Class Prototypes?
**arXiv**：[2512.17160v1](https://arxiv.org/abs/2512.17160) · [PDF](https://arxiv.org/pdf/2512.17160.pdf)  
**作者**：Dianxing Shi, Dingjie Fu, Yuqiao Liu, Jun Wang  

**一句话要点**：提出LGCLIP框架，利用LLM生成提示和扩散模型合成图像作为视觉原型，以解决零样本分类中依赖标注图像-文本对和双塔编码器的问题。

**关键词**：零样本图像分类, 视觉-语言模型, 合成图像原型, 轻量化框架, 扩散模型生成

## 3 点简述
- 核心问题：现有视觉-语言模型依赖标注图像-文本对进行模态对齐，导致数据准备成本高且模型轻量化受限。
- 方法要点：通过大型语言模型生成类特定提示，指导扩散模型合成参考图像作为视觉原型，仅使用视觉编码器进行特征比较预测。
- 实验或效果：实验验证LGCLIP在零样本分类任务中的可行性和高效性，仅需类标签输入，无需手动标注对。

## 摘要（原文）

> Vision-Language Models (VLMs) have shown strong performance in zero-shot image classification tasks. However, existing methods, including Contrastive Language-Image Pre-training (CLIP), all rely on annotated text-to-image pairs for aligning visual and textual modalities. This dependency introduces substantial cost and accuracy requirement in preparing high-quality datasets. At the same time, processing data from two modes also requires dual-tower encoders for most models, which also hinders their lightweight. To address these limitations, we introduce a ``Contrastive Language-Image Pre-training via Large-Language-Model-based Generation (LGCLIP)" framework. LGCLIP leverages a Large Language Model (LLM) to generate class-specific prompts that guide a diffusion model in synthesizing reference images. Afterwards these generated images serve as visual prototypes, and the visual features of real images are extracted and compared with the visual features of these prototypes to achieve comparative prediction. By optimizing prompt generation through the LLM and employing only a visual encoder, LGCLIP remains lightweight and efficient. Crucially, our framework requires only class labels as input during whole experimental procedure, eliminating the need for manually annotated image-text pairs and extra pre-processing. Experimental results validate the feasibility and efficiency of LGCLIP, demonstrating great performance in zero-shot classification tasks and establishing a novel paradigm for classification.

