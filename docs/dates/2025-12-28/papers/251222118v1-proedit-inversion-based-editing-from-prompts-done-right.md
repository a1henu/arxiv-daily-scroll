---
layout: default
title: ProEdit: Inversion-based Editing From Prompts Done Right
---

# ProEdit: Inversion-based Editing From Prompts Done Right
**arXiv**：[2512.22118v1](https://arxiv.org/abs/2512.22118) · [PDF](https://arxiv.org/pdf/2512.22118.pdf)  
**作者**：Zhi Ouyang, Dian Zheng, Xiao-Ming Wu, Jian-Jian Jiang, Kun-Yu Lin, Jingke Meng, Wei-Shi Zheng  

**一句话要点**：提出ProEdit方法，通过KV-mix和Latents-Shift解决基于反演的视觉编辑中源图像信息过度依赖问题。

**关键词**：视觉编辑, 反演方法, 注意力机制, 潜在空间扰动, 即插即用集成, 图像视频编辑

## 3 点简述
- 现有基于反演的视觉编辑方法在采样过程中过度依赖源图像信息，导致目标图像编辑失败，如无法改变主体姿态、数量或颜色。
- ProEdit在注意力层面引入KV-mix混合源和目标KV特征，在潜在空间层面提出Latents-Shift扰动源潜在区域，以减轻源信息影响并保持背景一致性。
- 实验在多个图像和视频编辑基准上展示SOTA性能，且方法为即插即用，可集成到现有反演和编辑方法中。

## 摘要（原文）

> Inversion-based visual editing provides an effective and training-free way to edit an image or a video based on user instructions. Existing methods typically inject source image information during the sampling process to maintain editing consistency. However, this sampling strategy overly relies on source information, which negatively affects the edits in the target image (e.g., failing to change the subject's atributes like pose, number, or color as instructed). In this work, we propose ProEdit to address this issue both in the attention and the latent aspects. In the attention aspect, we introduce KV-mix, which mixes KV features of the source and the target in the edited region, mitigating the influence of the source image on the editing region while maintaining background consistency. In the latent aspect, we propose Latents-Shift, which perturbs the edited region of the source latent, eliminating the influence of the inverted latent on the sampling. Extensive experiments on several image and video editing benchmarks demonstrate that our method achieves SOTA performance. In addition, our design is plug-and-play, which can be seamlessly integrated into existing inversion and editing methods, such as RF-Solver, FireFlow and UniEdit.

