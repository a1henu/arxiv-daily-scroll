---
layout: default
title: Cortex-Grounded Diffusion Models for Brain Image Generation
---

# Cortex-Grounded Diffusion Models for Brain Image Generation
**arXiv**：[2601.19498v1](https://arxiv.org/abs/2601.19498) · [PDF](https://arxiv.org/pdf/2601.19498.pdf)  
**作者**：Fabian Bongratz, Yitong Li, Sama Elbaroudy, Christian Wachinger  

**一句话要点**：提出Cor2Vox框架，利用皮层先验生成脑MRI图像以解决现有模型缺乏解剖基础的问题。

**关键词**：脑图像生成, 扩散模型, 皮层形态学, MRI合成, 统计形状模型

## 3 点简述
- 核心问题：现有脑图像生成模型依赖弱条件信号，导致输出缺乏解剖真实性和生物合理性。
- 方法要点：基于皮层表面引导3D形状到图像的布朗桥扩散过程，实现拓扑忠实合成和解剖精确控制。
- 实验或效果：在图像质量、皮层重建和分割评估中优于基线，应用于合成、萎缩模拟和数据集协调。

## 摘要（原文）

> Synthetic neuroimaging data can mitigate critical limitations of real-world datasets, including the scarcity of rare phenotypes, domain shifts across scanners, and insufficient longitudinal coverage. However, existing generative models largely rely on weak conditioning signals, such as labels or text, which lack anatomical grounding and often produce biologically implausible outputs. To this end, we introduce Cor2Vox, a cortex-grounded generative framework for brain magnetic resonance image (MRI) synthesis that ties image generation to continuous structural priors of the cerebral cortex. It leverages high-resolution cortical surfaces to guide a 3D shape-to-image Brownian bridge diffusion process, enabling topologically faithful synthesis and precise control over underlying anatomies. To support the generation of new, realistic brain shapes, we developed a large-scale statistical shape model of cortical morphology derived from over 33,000 UK Biobank scans. We validated the fidelity of Cor2Vox based on traditional image quality metrics, advanced cortical surface reconstruction, and whole-brain segmentation quality, outperforming many baseline methods. Across three applications, namely (i) anatomically consistent synthesis, (ii) simulation of progressive gray matter atrophy, and (iii) harmonization of in-house frontotemporal dementia scans with public datasets, Cor2Vox preserved fine-grained cortical morphology at the sub-voxel level, exhibiting remarkable robustness to variations in cortical geometry and disease phenotype without retraining.

