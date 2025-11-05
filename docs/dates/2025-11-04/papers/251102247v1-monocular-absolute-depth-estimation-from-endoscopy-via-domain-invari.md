---
layout: default
title: Monocular absolute depth estimation from endoscopy via domain-invariant feature learning and latent consistency
---

# Monocular absolute depth estimation from endoscopy via domain-invariant feature learning and latent consistency
**arXiv**：[2511.02247v1](https://arxiv.org/abs/2511.02247) · [PDF](https://arxiv.org/pdf/2511.02247.pdf)  
**作者**：Hao Li, Daiwei Lu, Jesse d'Almeida, Dilara Isik, Ehsan Khodapanah Aghdam, Nick DiSanto, Ayberk Acar, Susheela Sharma, Jie Ying Wu, Robert J. Webster III, Ipek Oguz  

**一句话要点**：提出域不变特征学习与潜在一致性方法，以改进内窥镜单目绝对深度估计。

**关键词**：单目深度估计, 域适应, 内窥镜图像, 对抗学习, 特征一致性

## 3 点简述
- 核心问题：内窥镜图像中绝对深度估计困难，监督学习受限。
- 方法要点：通过对抗学习和特征一致性，学习域不变潜在特征。
- 实验或效果：在气道模型视频上评估，优于现有方法，提升绝对和相对深度指标。

## 摘要（原文）

> Monocular depth estimation (MDE) is a critical task to guide autonomous
> medical robots. However, obtaining absolute (metric) depth from an endoscopy
> camera in surgical scenes is difficult, which limits supervised learning of
> depth on real endoscopic images. Current image-level unsupervised domain
> adaptation methods translate synthetic images with known depth maps into the
> style of real endoscopic frames and train depth networks using these translated
> images with their corresponding depth maps. However a domain gap often remains
> between real and translated synthetic images. In this paper, we present a
> latent feature alignment method to improve absolute depth estimation by
> reducing this domain gap in the context of endoscopic videos of the central
> airway. Our methods are agnostic to the image translation process and focus on
> the depth estimation itself. Specifically, the depth network takes translated
> synthetic and real endoscopic frames as input and learns latent
> domain-invariant features via adversarial learning and directional feature
> consistency. The evaluation is conducted on endoscopic videos of central airway
> phantoms with manually aligned absolute depth maps. Compared to
> state-of-the-art MDE methods, our approach achieves superior performance on
> both absolute and relative depth metrics, and consistently improves results
> across various backbones and pretrained weights. Our code is available at
> https://github.com/MedICL-VU/MDE.

