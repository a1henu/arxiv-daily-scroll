---
layout: default
title: PathoGen: Diffusion-Based Synthesis of Realistic Lesions in Histopathology Images
---

# PathoGen: Diffusion-Based Synthesis of Realistic Lesions in Histopathology Images
**arXiv**：[2601.08127v1](https://arxiv.org/abs/2601.08127) · [PDF](https://arxiv.org/pdf/2601.08127.pdf)  
**作者**：Mohamad Koohi-Moghadam, Mohammad-Ali Nikouei Mahani, Kyongtae Tyler Bae  

**一句话要点**：提出PathoGen扩散模型以解决组织病理学图像中病变数据稀缺问题

**关键词**：扩散模型, 组织病理学图像, 数据增强, 病变合成, 图像修复, 医学AI

## 3 点简述
- 核心问题：专家标注的病变数据稀缺，阻碍AI模型在罕见病理和亚型中的发展。
- 方法要点：基于扩散模型实现可控高保真病变修复，保留组织边界和细胞结构。
- 实验或效果：在多个数据集上验证，提升图像保真度和分割性能，克服标注瓶颈。

## 摘要（原文）

> The development of robust artificial intelligence models for histopathology diagnosis is severely constrained by the scarcity of expert-annotated lesion data, particularly for rare pathologies and underrepresented disease subtypes. While data augmentation offers a potential solution, existing methods fail to generate sufficiently realistic lesion morphologies that preserve the complex spatial relationships and cellular architectures characteristic of histopathological tissues. Here we present PathoGen, a diffusion-based generative model that enables controllable, high-fidelity inpainting of lesions into benign histopathology images. Unlike conventional augmentation techniques, PathoGen leverages the iterative refinement process of diffusion models to synthesize lesions with natural tissue boundaries, preserved cellular structures, and authentic staining characteristics. We validate PathoGen across four diverse datasets representing distinct diagnostic challenges: kidney, skin, breast, and prostate pathology. Quantitative assessment confirms that PathoGen outperforms state-of-the-art generative baselines, including conditional GAN and Stable Diffusion, in image fidelity and distributional similarity. Crucially, we show that augmenting training sets with PathoGen-synthesized lesions enhances downstream segmentation performance compared to traditional geometric augmentations, particularly in data-scarce regimes. Besides, by simultaneously generating realistic morphology and pixel-level ground truth, PathoGen effectively overcomes the manual annotation bottleneck. This approach offers a scalable pathway for developing generalizable medical AI systems despite limited expert-labeled data.

