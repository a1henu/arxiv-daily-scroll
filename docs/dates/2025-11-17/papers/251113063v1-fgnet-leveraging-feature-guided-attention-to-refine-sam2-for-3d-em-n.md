---
layout: default
title: FGNet: Leveraging Feature-Guided Attention to Refine SAM2 for 3D EM Neuron Segmentation
---

# FGNet: Leveraging Feature-Guided Attention to Refine SAM2 for 3D EM Neuron Segmentation
**arXiv**：[2511.13063v1](https://arxiv.org/abs/2511.13063) · [PDF](https://arxiv.org/pdf/2511.13063.pdf)  
**作者**：Zhenghua Li, Hang Chen, Zihao Sun, Kai Li, Xiaolin Hu  

**一句话要点**：提出FGNet框架，利用特征引导注意力优化SAM2，以解决电子显微镜神经元分割问题

**关键词**：神经元分割, 特征引导注意力, 域适应, SAM2迁移, 电子显微镜图像

## 3 点简述
- 核心问题：电子显微镜图像中神经元分割面临形态复杂、噪声高和标注稀缺的挑战
- 方法要点：引入特征引导注意力模块，桥接自然图像与EM领域的域差距
- 实验或效果：在SAM2权重冻结时性能可比SOTA，微调后显著超越现有方法

## 摘要（原文）

> Accurate segmentation of neural structures in Electron Microscopy (EM) images is paramount for neuroscience. However, this task is challenged by intricate morphologies, low signal-to-noise ratios, and scarce annotations, limiting the accuracy and generalization of existing methods. To address these challenges, we seek to leverage the priors learned by visual foundation models on a vast amount of natural images to better tackle this task. Specifically, we propose a novel framework that can effectively transfer knowledge from Segment Anything 2 (SAM2), which is pre-trained on natural images, to the EM domain. We first use SAM2 to extract powerful, general-purpose features. To bridge the domain gap, we introduce a Feature-Guided Attention module that leverages semantic cues from SAM2 to guide a lightweight encoder, the Fine-Grained Encoder (FGE), in focusing on these challenging regions. Finally, a dual-affinity decoder generates both coarse and refined affinity maps. Experimental results demonstrate that our method achieves performance comparable to state-of-the-art (SOTA) approaches with the SAM2 weights frozen. Upon further fine-tuning on EM data, our method significantly outperforms existing SOTA methods. This study validates that transferring representations pre-trained on natural images, when combined with targeted domain-adaptive guidance, can effectively address the specific challenges in neuron segmentation.

