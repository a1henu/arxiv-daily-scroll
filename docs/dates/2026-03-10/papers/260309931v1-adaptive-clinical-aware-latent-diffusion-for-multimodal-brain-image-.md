---
layout: default
title: Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation
---

# Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation
**arXiv**：[2603.09931v1](https://arxiv.org/abs/2603.09931) · [PDF](https://arxiv.org/pdf/2603.09931.pdf)  
**作者**：Rong Zhou, Houliang Zhou, Yao Su, Brian Y. Chen, Yu Zhang, Lifang He, Alzheimer's Disease Neuroimaging Initiative  

**一句话要点**：提出ACADiff框架，通过自适应临床感知扩散生成缺失脑成像模态并补全多模态数据

**关键词**：多模态脑图像生成, 缺失模态补全, 自适应扩散模型, 临床语义引导, 阿尔茨海默病诊断

## 3 点简述
- 核心问题：阿尔茨海默病诊断中多模态神经影像数据常缺失模态，影响分析准确性。
- 方法要点：采用自适应融合和GPT-4o编码的临床语义引导，在潜在空间进行扩散去噪生成目标模态。
- 实验或效果：在ADNI数据集上，ACADiff在80%缺失率下仍保持优越生成质量和诊断性能，超越现有基线。

## 摘要（原文）

> Multimodal neuroimaging provides complementary insights for Alzheimer's disease diagnosis, yet clinical datasets frequently suffer from missing modalities. We propose ACADiff, a framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion. ACADiff learns mappings between incomplete multimodal observations and target modalities by progressively denoising latent representations while attending to available imaging data and clinical metadata. The framework employs adaptive fusion that dynamically reconfigures based on input availability, coupled with semantic clinical guidance via GPT-4o-encoded prompts. Three specialized generators enable bidirectional synthesis among sMRI, FDG-PET, and AV45-PET. Evaluated on ADNI subjects, ACADiff achieves superior generation quality and maintains robust diagnostic performance even under extreme 80\% missing scenarios, outperforming all existing baselines. To promote reproducibility, code is available at https://github.com/rongzhou7/ACADiff

