---
layout: default
title: Fully Unsupervised Self-debiasing of Text-to-Image Diffusion Models
---

# Fully Unsupervised Self-debiasing of Text-to-Image Diffusion Models
**arXiv**：[2512.03749v1](https://arxiv.org/abs/2512.03749) · [PDF](https://arxiv.org/pdf/2512.03749.pdf)  
**作者**：Korada Sri Vardhana, Shrikrishna Lolla, Soma Biswas  

**一句话要点**：提出SelfDebias以无监督方式减少文本到图像扩散模型的偏见输出

**关键词**：文本到图像生成, 无监督去偏, 扩散模型, KL散度优化, 语义聚类

## 3 点简述
- 问题：扩散模型因训练数据偏见产生刻板图像输出
- 方法：基于图像编码器嵌入空间聚类，在推理时引导扩散过程最小化KL散度
- 效果：在多种提示和模型架构中有效去偏，保持图像质量

## 摘要（原文）

> Text-to-image (T2I) diffusion models have achieved widespread success due to their ability to generate high-resolution, photorealistic images. These models are trained on large-scale datasets, like LAION-5B, often scraped from the internet. However, since this data contains numerous biases, the models inherently learn and reproduce them, resulting in stereotypical outputs. We introduce SelfDebias, a fully unsupervised test-time debiasing method applicable to any diffusion model that uses a UNet as its noise predictor. SelfDebias identifies semantic clusters in an image encoder's embedding space and uses these clusters to guide the diffusion process during inference, minimizing the KL divergence between the output distribution and the uniform distribution. Unlike supervised approaches, SelfDebias does not require human-annotated datasets or external classifiers trained for each generated concept. Instead, it is designed to automatically identify semantic modes. Extensive experiments show that SelfDebias generalizes across prompts and diffusion model architectures, including both conditional and unconditional models. It not only effectively debiases images along key demographic dimensions while maintaining the visual fidelity of the generated images, but also more abstract concepts for which identifying biases is also challenging.

