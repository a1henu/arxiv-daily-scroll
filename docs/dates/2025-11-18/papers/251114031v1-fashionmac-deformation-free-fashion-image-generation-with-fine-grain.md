---
layout: default
title: FashionMAC: Deformation-Free Fashion Image Generation with Fine-Grained Model Appearance Customization
---

# FashionMAC: Deformation-Free Fashion Image Generation with Fine-Grained Model Appearance Customization
**arXiv**：[2511.14031v1](https://arxiv.org/abs/2511.14031) · [PDF](https://arxiv.org/pdf/2511.14031.pdf)  
**作者**：Rong Zhang, Jinxiao Li, Jingnan Wang, Zhiwen Zuo, Jianfeng Dong, Wei Li, Chi Wang, Weiwei Xu, Xun Wang  

**一句话要点**：提出FashionMAC框架以解决时尚图像生成中的服装变形和细粒度控制问题

**关键词**：时尚图像生成, 扩散模型, 无变形生成, 细粒度控制, 注意力机制

## 3 点简述
- 核心问题：现有方法需服装变形，导致纹理失真，且缺乏细粒度外观控制机制
- 方法要点：采用无变形框架直接外推服装，并引入RADA机制和链式掩码注入策略
- 实验或效果：广泛实验验证优于现有方法，提升视觉保真度和可控性

## 摘要（原文）

> Garment-centric fashion image generation aims to synthesize realistic and controllable human models dressing a given garment, which has attracted growing interest due to its practical applications in e-commerce. The key challenges of the task lie in two aspects: (1) faithfully preserving the garment details, and (2) gaining fine-grained controllability over the model's appearance. Existing methods typically require performing garment deformation in the generation process, which often leads to garment texture distortions. Also, they fail to control the fine-grained attributes of the generated models, due to the lack of specifically designed mechanisms. To address these issues, we propose FashionMAC, a novel diffusion-based deformation-free framework that achieves high-quality and controllable fashion showcase image generation. The core idea of our framework is to eliminate the need for performing garment deformation and directly outpaint the garment segmented from a dressed person, which enables faithful preservation of the intricate garment details. Moreover, we propose a novel region-adaptive decoupled attention (RADA) mechanism along with a chained mask injection strategy to achieve fine-grained appearance controllability over the synthesized human models. Specifically, RADA adaptively predicts the generated regions for each fine-grained text attribute and enforces the text attribute to focus on the predicted regions by a chained mask injection strategy, significantly enhancing the visual fidelity and the controllability. Extensive experiments validate the superior performance of our framework compared to existing state-of-the-art methods.

