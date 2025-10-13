---
layout: default
title: MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation
---

# MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation
**arXiv**：[2510.09121v1](https://arxiv.org/abs/2510.09121) · [PDF](https://arxiv.org/pdf/2510.09121.pdf)  
**作者**：Dominik Winter, Mai Bui, Monica Azqueta Gavaldon, Nicolas Triltsch, Marco Rosati, Nicolas Brieu  

**一句话要点**：提出多模态语义扩散模型以生成病理图像-掩码对，提升细胞和核分割性能

**关键词**：计算病理学, 扩散模型, 细胞分割, 合成数据生成, 多模态条件生成

## 3 点简述
- 核心问题：标注数据稀缺，尤其对罕见或非典型形态细胞和核分割构成挑战
- 方法要点：使用多模态条件扩散模型，整合形态、颜色和元数据生成图像-掩码对
- 实验或效果：合成图像与真实数据相似，显著提高分割模型在特定细胞上的准确率

## 摘要（原文）

> Scarcity of annotated data, particularly for rare or atypical morphologies,
> present significant challenges for cell and nuclei segmentation in
> computational pathology. While manual annotation is labor-intensive and costly,
> synthetic data offers a cost-effective alternative. We introduce a Multimodal
> Semantic Diffusion Model (MSDM) for generating realistic pixel-precise
> image-mask pairs for cell and nuclei segmentation. By conditioning the
> generative process with cellular/nuclear morphologies (using horizontal and
> vertical maps), RGB color characteristics, and BERT-encoded assay/indication
> metadata, MSDM generates datasests with desired morphological properties. These
> heterogeneous modalities are integrated via multi-head cross-attention,
> enabling fine-grained control over the generated images. Quantitative analysis
> demonstrates that synthetic images closely match real data, with low
> Wasserstein distances between embeddings of generated and real images under
> matching biological conditions. The incorporation of these synthetic samples,
> exemplified by columnar cells, significantly improves segmentation model
> accuracy on columnar cells. This strategy systematically enriches data sets,
> directly targeting model deficiencies. We highlight the effectiveness of
> multimodal diffusion-based augmentation for advancing the robustness and
> generalizability of cell and nuclei segmentation models. Thereby, we pave the
> way for broader application of generative models in computational pathology.

