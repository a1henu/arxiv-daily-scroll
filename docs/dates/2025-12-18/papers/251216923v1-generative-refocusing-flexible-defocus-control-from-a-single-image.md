---
layout: default
title: Generative Refocusing: Flexible Defocus Control from a Single Image
---

# Generative Refocusing: Flexible Defocus Control from a Single Image
**arXiv**：[2512.16923v1](https://arxiv.org/abs/2512.16923) · [PDF](https://arxiv.org/pdf/2512.16923.pdf)  
**作者**：Chun-Wei Tuan Mu, Jia-Bin Huang, Yu-Lun Liu  

**一句话要点**：提出生成式重聚焦方法，通过两步流程从单张图像实现灵活散焦控制

**关键词**：单图像重聚焦, 散焦控制, 半监督训练, 散景合成, 图像去模糊

## 3 点简述
- 核心问题：单图像重聚焦困难，现有方法需全焦输入、依赖合成数据且孔径控制有限
- 方法要点：采用DeblurNet恢复全焦图像和BokehNet生成可控散景，结合半监督训练利用真实EXIF数据
- 实验或效果：在散焦去模糊、散景合成和重聚焦基准测试中表现优异，支持文本引导调整和自定义孔径形状

## 摘要（原文）

> Depth-of-field control is essential in photography, but getting the perfect focus often takes several tries or special equipment. Single-image refocusing is still difficult. It involves recovering sharp content and creating realistic bokeh. Current methods have significant drawbacks. They need all-in-focus inputs, depend on synthetic data from simulators, and have limited control over aperture. We introduce Generative Refocusing, a two-step process that uses DeblurNet to recover all-in-focus images from various inputs and BokehNet for creating controllable bokeh. Our main innovation is semi-supervised training. This method combines synthetic paired data with unpaired real bokeh images, using EXIF metadata to capture real optical characteristics beyond what simulators can provide. Our experiments show we achieve top performance in defocus deblurring, bokeh synthesis, and refocusing benchmarks. Additionally, our Generative Refocusing allows text-guided adjustments and custom aperture shapes.

