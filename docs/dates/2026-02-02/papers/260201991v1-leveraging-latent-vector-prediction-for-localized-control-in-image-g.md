---
layout: default
title: Leveraging Latent Vector Prediction for Localized Control in Image Generation via Diffusion Models
---

# Leveraging Latent Vector Prediction for Localized Control in Image Generation via Diffusion Models
**arXiv**：[2602.01991v1](https://arxiv.org/abs/2602.01991) · [PDF](https://arxiv.org/pdf/2602.01991.pdf)  
**作者**：Pablo Domingo-Gregorio, Javier Ruiz-Hidalgo  

**一句话要点**：提出基于潜在向量预测的扩散模型训练框架，实现图像生成中的局部区域精确控制。

**关键词**：扩散模型, 图像生成, 局部控制, 潜在向量预测, 掩码训练

## 3 点简述
- 核心问题：现有扩散模型方法通过文本和图像级条件实现全局控制，但缺乏对用户定义区域的局部精确控制。
- 方法要点：引入掩码特征和额外损失项，利用扩散步骤中初始潜在向量的预测，增强潜在空间对应性以实现局部控制。
- 实验或效果：广泛实验表明，该方法能有效合成高质量图像，在保持原始提示生成的同时满足局部条件。

## 摘要（原文）

> Diffusion models emerged as a leading approach in text-to-image generation, producing high-quality images from textual descriptions. However, attempting to achieve detailed control to get a desired image solely through text remains a laborious trial-and-error endeavor. Recent methods have introduced image-level controls alongside with text prompts, using prior images to extract conditional information such as edges, segmentation and depth maps. While effective, these methods apply conditions uniformly across the entire image, limiting localized control. In this paper, we propose a novel methodology to enable precise local control over user-defined regions of an image, while leaving to the diffusion model the task of autonomously generating the remaining areas according to the original prompt. Our approach introduces a new training framework that incorporates masking features and an additional loss term, which leverages the prediction of the initial latent vector at any diffusion step to enhance the correspondence between the current step and the final sample in the latent space. Extensive experiments demonstrate that our method effectively synthesizes high-quality images with controlled local conditions.

