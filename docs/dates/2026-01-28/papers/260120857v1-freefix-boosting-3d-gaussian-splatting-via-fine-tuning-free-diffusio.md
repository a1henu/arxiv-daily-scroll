---
layout: default
title: FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models
---

# FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models
**arXiv**：[2601.20857v1](https://arxiv.org/abs/2601.20857) · [PDF](https://arxiv.org/pdf/2601.20857.pdf)  
**作者**：Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  

**一句话要点**：提出FreeFix以通过免微调扩散模型提升3D高斯溅射的泛化与保真度

**关键词**：3D高斯溅射, 扩散模型, 免微调方法, 视图合成, 多帧一致性, 泛化能力

## 3 点简述
- 核心问题：3D高斯溅射依赖密集输入，外推视图质量下降，现有方法在泛化与保真度间存在权衡
- 方法要点：采用免微调预训练图像扩散模型，结合交错2D-3D精炼策略和逐像素置信掩码
- 实验或效果：在多个数据集上提升多帧一致性，性能媲美或超越微调方法，保持强泛化能力

## 摘要（原文）

> Neural Radiance Fields and 3D Gaussian Splatting have advanced novel view synthesis, yet still rely on dense inputs and often degrade at extrapolated views. Recent approaches leverage generative models, such as diffusion models, to provide additional supervision, but face a trade-off between generalization and fidelity: fine-tuning diffusion models for artifact removal improves fidelity but risks overfitting, while fine-tuning-free methods preserve generalization but often yield lower fidelity. We introduce FreeFix, a fine-tuning-free approach that pushes the boundary of this trade-off by enhancing extrapolated rendering with pretrained image diffusion models. We present an interleaved 2D-3D refinement strategy, showing that image diffusion models can be leveraged for consistent refinement without relying on costly video diffusion models. Furthermore, we take a closer look at the guidance signal for 2D refinement and propose a per-pixel confidence mask to identify uncertain regions for targeted improvement. Experiments across multiple datasets show that FreeFix improves multi-frame consistency and achieves performance comparable to or surpassing fine-tuning-based methods, while retaining strong generalization ability.

