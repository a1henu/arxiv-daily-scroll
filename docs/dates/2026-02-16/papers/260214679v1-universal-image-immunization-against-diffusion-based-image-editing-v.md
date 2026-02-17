---
layout: default
title: Universal Image Immunization against Diffusion-based Image Editing via Semantic Injection
---

# Universal Image Immunization against Diffusion-based Image Editing via Semantic Injection
**arXiv**：[2602.14679v1](https://arxiv.org/abs/2602.14679) · [PDF](https://arxiv.org/pdf/2602.14679.pdf)  
**作者**：Chanhui Lee, Seunghyun Shin, Donggyu Choi, Hae-gon Jeon, Jeany Son  

**一句话要点**：提出通用图像免疫框架，通过语义注入防御基于扩散模型的图像编辑风险。

**关键词**：图像免疫, 通用对抗扰动, 扩散模型, 语义注入, 数据无关防御

## 3 点简述
- 核心问题：扩散模型图像编辑带来伦理和法律风险，现有免疫方法依赖图像特定扰动，可扩展性差。
- 方法要点：生成通用对抗扰动，注入语义目标并抑制原始内容，误导模型注意力，无需训练数据。
- 实验或效果：在通用扰动设置中显著优于基线，在受限预算下与图像特定方法相当，具有强黑盒可迁移性。

## 摘要（原文）

> Recent advances in diffusion models have enabled powerful image editing capabilities guided by natural language prompts, unlocking new creative possibilities. However, they introduce significant ethical and legal risks, such as deepfakes and unauthorized use of copyrighted visual content. To address these risks, image immunization has emerged as a promising defense against AI-driven semantic manipulation. Yet, most existing approaches rely on image-specific adversarial perturbations that require individual optimization for each image, thereby limiting scalability and practicality. In this paper, we propose the first universal image immunization framework that generates a single, broadly applicable adversarial perturbation specifically designed for diffusion-based editing pipelines. Inspired by universal adversarial perturbation (UAP) techniques used in targeted attacks, our method generates a UAP that embeds a semantic target into images to be protected. Simultaneously, it suppresses original content to effectively misdirect the model's attention during editing. As a result, our approach effectively blocks malicious editing attempts by overwriting the original semantic content in the image via the UAP. Moreover, our method operates effectively even in data-free settings without requiring access to training data or domain knowledge, further enhancing its practicality and broad applicability in real-world scenarios. Extensive experiments show that our method, as the first universal immunization approach, significantly outperforms several baselines in the UAP setting. In addition, despite the inherent difficulty of universal perturbations, our method also achieves performance on par with image-specific methods under a more restricted perturbation budget, while also exhibiting strong black-box transferability across different diffusion models.

