---
layout: default
title: Mitigating Long-Tail Bias via Prompt-Controlled Diffusion Augmentation
---

# Mitigating Long-Tail Bias via Prompt-Controlled Diffusion Augmentation
**arXiv**：[2602.04749v1](https://arxiv.org/abs/2602.04749) · [PDF](https://arxiv.org/pdf/2602.04749.pdf)  
**作者**：Buddhi Wijenayake, Nichula Wasalathilake, Roshan Godaliyadda, Vijitha Herath, Parakrama Ekanayake, Vishal M. Patel  

**一句话要点**：提出提示控制扩散增强框架以缓解遥感图像语义分割中的长尾偏差

**关键词**：遥感图像语义分割, 长尾分布, 扩散模型增强, 域适应, 可控数据生成

## 3 点简述
- 核心问题：遥感图像语义分割数据存在长尾像素不平衡，且Urban/Rural域间外观和类别频率差异加剧挑战。
- 方法要点：采用两阶段扩散模型，首阶段生成满足指定类别比例的布局，次阶段转换为域一致的真实图像。
- 实验或效果：合成数据与真实数据混合提升多个分割模型性能，尤其改善少数类表现和跨域泛化能力。

## 摘要（原文）

> Semantic segmentation of high-resolution remote-sensing imagery is critical for urban mapping and land-cover monitoring, yet training data typically exhibits severe long-tailed pixel imbalance. In the dataset LoveDA, this challenge is compounded by an explicit Urban/Rural split with distinct appearance and inconsistent class-frequency statistics across domains. We present a prompt-controlled diffusion augmentation framework that synthesizes paired label--image samples with explicit control of both domain and semantic composition. Stage~A uses a domain-aware, masked ratio-conditioned discrete diffusion model to generate layouts that satisfy user-specified class-ratio targets while respecting learned co-occurrence structure. Stage~B translates layouts into photorealistic, domain-consistent images using Stable Diffusion with ControlNet guidance. Mixing the resulting ratio and domain-controlled synthetic pairs with real data yields consistent improvements across multiple segmentation backbones, with gains concentrated on minority classes and improved Urban and Rural generalization, demonstrating controllable augmentation as a practical mechanism to mitigate long-tail bias in remote-sensing segmentation. Source codes, pretrained models, and synthetic datasets are available at \href{https://github.com/Buddhi19/SyntheticGen.git}{Github}

