---
layout: default
title: Towards Pixel-Wise Anomaly Location for High-Resolution PCBA \\ via Self-Supervised Image Reconstruction
---

# Towards Pixel-Wise Anomaly Location for High-Resolution PCBA \\ via Self-Supervised Image Reconstruction
**arXiv**：[2512.17296v1](https://arxiv.org/abs/2512.17296) · [PDF](https://arxiv.org/pdf/2512.17296.pdf)  
**作者**：Wuyi Liu, Le Jin, Junxian Yang, Yuanchao Yu, Zishuo Peng, Jinfeng Xu, Xianzhi Li, Jun Zhou  

**一句话要点**：提出HiSIR-Net框架，通过自监督图像重建实现高分辨率PCBA的像素级缺陷定位。

**关键词**：高分辨率图像, 自监督学习, 图像重建, 缺陷检测, PCBA检测, 像素级定位

## 3 点简述
- 核心问题：高分辨率PCBA图像中微缺陷检测面临标注数据不足和视觉复杂性挑战。
- 方法要点：结合SIR-Gate和ROPS机制，减少重建伪影并实现任意分辨率下的连贯补丁选择。
- 实验或效果：在自建SIPCBA-500数据集和公开基准上验证了优越的定位性能和低误报率。

## 摘要（原文）

> Automated defect inspection of assembled Printed Circuit Board Assemblies (PCBA) is quite challenging due to the insufficient labeled data, micro-defects with just a few pixels in visually-complex and high-resolution images. To address these challenges, we present HiSIR-Net, a High resolution, Self-supervised Reconstruction framework for pixel-wise PCBA localization. Our design combines two lightweight modules that make this practical on real 4K-resolution boards: (i) a Selective Input-Reconstruction Gate (SIR-Gate) that lets the model decide where to trust reconstruction versus the original input, thereby reducing irrelevant reconstruction artifacts and false alarms; and (ii) a Region-level Optimized Patch Selection (ROPS) scheme with positional cues to select overlapping patch reconstructions coherently across arbitrary resolutions. Organically integrating these mechanisms yields clean, high-resolution anomaly maps with low false positive (FP) rate. To bridge the gap in high-resolution PCBA datasets, we further contribute a self-collected dataset named SIPCBA-500 of 500 images. We conduct extensive experiments on our SIPCBA-500 as well as public benchmarks, demonstrating the superior localization performance of our method while running at practical speed. Full code and dataset will be made available upon acceptance.

