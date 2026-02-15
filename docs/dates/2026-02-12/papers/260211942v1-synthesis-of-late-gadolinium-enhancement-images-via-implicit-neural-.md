---
layout: default
title: Synthesis of Late Gadolinium Enhancement Images via Implicit Neural Representations for Cardiac Scar Segmentation
---

# Synthesis of Late Gadolinium Enhancement Images via Implicit Neural Representations for Cardiac Scar Segmentation
**arXiv**：[2602.11942v1](https://arxiv.org/abs/2602.11942) · [PDF](https://arxiv.org/pdf/2602.11942.pdf)  
**作者**：Soufiane Ben Haddou, Laura Alvarez-Florez, Erik J. Bekkers, Fleur V. Y. Tjong, Ahmad S. Amin, Connie R. Bezzina, Ivana Išgum  

**一句话要点**：提出基于隐式神经表示和扩散模型的LGE图像合成框架，以缓解心脏瘢痕分割的数据稀缺问题。

**关键词**：心脏瘢痕分割, 隐式神经表示, 扩散模型, 数据增强, 医学图像合成, LGE成像

## 3 点简述
- 核心问题：LGE图像标注数据有限，阻碍自动化心脏瘢痕分割方法的发展。
- 方法要点：使用INR捕获连续空间表示，结合扩散模型在潜在空间生成新表示，解码为合成图像和分割掩码。
- 实验或效果：在133个心脏MRI扫描上，添加200个合成体积提升分割性能，Dice分数从0.509增至0.524。

## 摘要（原文）

> Late gadolinium enhancement (LGE) imaging is the clinical standard for myocardial scar assessment, but limited annotated datasets hinder the development of automated segmentation methods. We propose a novel framework that synthesises both LGE images and their corresponding segmentation masks using implicit neural representations (INRs) combined with denoising diffusion models. Our approach first trains INRs to capture continuous spatial representations of LGE data and associated myocardium and fibrosis masks. These INRs are then compressed into compact latent embeddings, preserving essential anatomical information. A diffusion model operates on this latent space to generate new representations, which are decoded into synthetic LGE images with anatomically consistent segmentation masks. Experiments on 133 cardiac MRI scans suggest that augmenting training data with 200 synthetic volumes contributes to improved fibrosis segmentation performance, with the Dice score showing an increase from 0.509 to 0.524. Our approach provides an annotation-free method to help mitigate data scarcity.The code for this research is publicly available.

