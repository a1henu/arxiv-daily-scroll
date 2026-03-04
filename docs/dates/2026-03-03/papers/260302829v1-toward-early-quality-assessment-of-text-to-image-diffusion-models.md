---
layout: default
title: Toward Early Quality Assessment of Text-to-Image Diffusion Models
---

# Toward Early Quality Assessment of Text-to-Image Diffusion Models
**arXiv**：[2603.02829v1](https://arxiv.org/abs/2603.02829) · [PDF](https://arxiv.org/pdf/2603.02829.pdf)  
**作者**：Huanlei Guo, Hongxin Wei, Bingyi Jing  

**一句话要点**：提出Probe-Select插件模块，通过早期激活预测图像质量，以降低文本到图像模型的采样成本。

**关键词**：文本到图像生成, 扩散模型, 质量评估, 早期终止, 采样效率, 激活预测

## 3 点简述
- 核心问题：文本到图像模型生成-选择模式资源密集，后验评估效率低。
- 方法要点：利用早期去噪器激活预测最终图像质量，实现种子早期终止。
- 实验或效果：在20%轨迹处评估，减少60%以上采样成本，提升保留图像质量。

## 摘要（原文）

> Recent text-to-image (T2I) diffusion and flow-matching models can produce highly realistic images from natural language prompts. In practical scenarios, T2I systems are often run in a ``generate--then--select'' mode: many seeds are sampled and only a few images are kept for use. However, this pipeline is highly resource-intensive since each candidate requires tens to hundreds of denoising steps, and evaluation metrics such as CLIPScore and ImageReward are post-hoc. In this work, we address this inefficiency by introducing Probe-Select, a plug-in module that enables efficient evaluation of image quality within the generation process. We observe that certain intermediate denoiser activations, even at early timesteps, encode a stable coarse structure, object layout and spatial arrangement--that strongly correlates with final image fidelity. Probe-Select exploits this property by predicting final quality scores directly from early activations, allowing unpromising seeds to be terminated early. Across diffusion and flow-matching backbones, our experiments show that early evaluation at only 20\% of the trajectory accurately ranks candidate seeds and enables selective continuation. This strategy reduces sampling cost by over 60\% while improving the quality of the retained images, demonstrating that early structural signals can effectively guide selective generation without altering the underlying generative model. Code is available at https://github.com/Guhuary/ProbeSelect.

