---
layout: default
title: Image Generation with a Sphere Encoder
---

# Image Generation with a Sphere Encoder
**arXiv**：[2602.15030v1](https://arxiv.org/abs/2602.15030) · [PDF](https://arxiv.org/pdf/2602.15030.pdf)  
**作者**：Kaiyu Yue, Menglin Jia, Ji Hou, Tom Goldstein  

**一句话要点**：提出Sphere Encoder，通过球面隐空间映射实现高效图像生成，以单次前向传播竞争多步扩散模型。

**关键词**：球面隐空间, 高效图像生成, 单次前向传播, 图像重构损失, 条件生成, 低推理成本

## 3 点简述
- 核心问题：传统扩散模型推理成本高，需多步生成，影响效率。
- 方法要点：学习编码器将图像均匀映射到球面隐空间，解码器从随机点生成图像，仅用重构损失训练。
- 实验或效果：在多个数据集上性能与先进扩散模型竞争，推理成本显著降低，支持条件生成和迭代增强。

## 摘要（原文）

> We introduce the Sphere Encoder, an efficient generative framework capable of producing images in a single forward pass and competing with many-step diffusion models using fewer than five steps. Our approach works by learning an encoder that maps natural images uniformly onto a spherical latent space, and a decoder that maps random latent vectors back to the image space. Trained solely through image reconstruction losses, the model generates an image by simply decoding a random point on the sphere. Our architecture naturally supports conditional generation, and looping the encoder/decoder a few times can further enhance image quality. Across several datasets, the sphere encoder approach yields performance competitive with state of the art diffusions, but with a small fraction of the inference cost. Project page is available at https://sphere-encoder.github.io .

