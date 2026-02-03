---
layout: default
title: FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space
---

# FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space
**arXiv**：[2602.02092v1](https://arxiv.org/abs/2602.02092) · [PDF](https://arxiv.org/pdf/2602.02092.pdf)  
**作者**：FSVideo Team, Qingyu Chen, Zhiyuan Fang, Haibin Huang, Xinwei Huang, Tong Jin, Minxuan Lin, Bo Liu, Celong Liu, Chongyang Ma, Xing Mei, Xiaohui Shen, Yaojie Shen, Fuwen Tan, Angtian Wang, Xiao Yang, Yiding Yang, Jiamin Yuan, Lingxi Zhang, Yuxin Zhang  

**一句话要点**：提出FSVideo，一种基于Transformer的快速图像到视频扩散框架，在高度压缩的潜在空间中实现高效生成。

**关键词**：图像到视频生成, 扩散模型, 潜在空间压缩, Transformer架构, 快速生成

## 3 点简述
- 核心问题：图像到视频生成速度慢，现有模型在压缩和生成效率上存在挑战。
- 方法要点：采用高度压缩的视频自编码器、改进的扩散Transformer层内存设计，以及多分辨率生成策略。
- 实验或效果：模型包含14B参数，性能与开源模型竞争，生成速度快一个数量级。

## 摘要（原文）

> We introduce FSVideo, a fast speed transformer-based image-to-video (I2V) diffusion framework. We build our framework on the following key components: 1.) a new video autoencoder with highly-compressed latent space ($64\times64\times4$ spatial-temporal downsampling ratio), achieving competitive reconstruction quality; 2.) a diffusion transformer (DIT) architecture with a new layer memory design to enhance inter-layer information flow and context reuse within DIT, and 3.) a multi-resolution generation strategy via a few-step DIT upsampler to increase video fidelity. Our final model, which contains a 14B DIT base model and a 14B DIT upsampler, achieves competitive performance against other popular open-source models, while being an order of magnitude faster. We discuss our model design as well as training strategies in this report.

