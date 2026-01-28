---
layout: default
title: Learned split-spectrum metalens for obstruction-free broadband imaging in the visible
---

# Learned split-spectrum metalens for obstruction-free broadband imaging in the visible
**arXiv**：[2601.19403v1](https://arxiv.org/abs/2601.19403) · [PDF](https://arxiv.org/pdf/2601.19403.pdf)  
**作者**：Seungwoo Yoon, Dohyun Kang, Eunsue Choi, Sohyun Lee, Seoyeon Kim, Minho Choi, Hyeonsu Heo, Dong-ha Shin, Suha Kwak, Arka Majumdar, Junsuk Rho, Seung-Hwan Baek  

**一句话要点**：提出学习型分光谱超透镜，实现可见光宽带无遮挡成像

**关键词**：超透镜成像, 光谱滤波, 神经网络增强, 无遮挡视觉, 宽带成像, 紧凑光学系统

## 3 点简述
- 核心问题：传统超透镜难以同时实现宽带成像和近景遮挡物去焦
- 方法要点：通过多波段光谱滤波分割RGB光谱，学习超透镜聚焦远景光并过滤近景光
- 实验或效果：相比传统设计，PSNR提升32.29%，目标检测和语义分割精度显著提高

## 摘要（原文）

> Obstructions such as raindrops, fences, or dust degrade captured images, especially when mechanical cleaning is infeasible. Conventional solutions to obstructions rely on a bulky compound optics array or computational inpainting, which compromise compactness or fidelity. Metalenses composed of subwavelength meta-atoms promise compact imaging, but simultaneous achievement of broadband and obstruction-free imaging remains a challenge, since a metalens that images distant scenes across a broadband spectrum cannot properly defocus near-depth occlusions. Here, we introduce a learned split-spectrum metalens that enables broadband obstruction-free imaging. Our approach divides the spectrum of each RGB channel into pass and stop bands with multi-band spectral filtering and learns the metalens to focus light from far objects through pass bands, while filtering focused near-depth light through stop bands. This optical signal is further enhanced using a neural network. Our learned split-spectrum metalens achieves broadband and obstruction-free imaging with relative PSNR gains of 32.29% and improves object detection and semantic segmentation accuracies with absolute gains of +13.54% mAP, +48.45% IoU, and +20.35% mIoU over a conventional hyperbolic design. This promises robust obstruction-free sensing and vision for space-constrained systems, such as mobile robots, drones, and endoscopes.

