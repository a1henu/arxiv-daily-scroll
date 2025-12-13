---
layout: default
title: GDKVM: Echocardiography Video Segmentation via Spatiotemporal Key-Value Memory with Gated Delta Rule
---

# GDKVM: Echocardiography Video Segmentation via Spatiotemporal Key-Value Memory with Gated Delta Rule
**arXiv**：[2512.10252v1](https://arxiv.org/abs/2512.10252) · [PDF](https://arxiv.org/pdf/2512.10252.pdf)  
**作者**：Rui Wang, Yimu Sun, Jingxing Guo, Huisi Wu, Jing Qin  

**一句话要点**：提出GDKVM模型，通过时空键值记忆与门控增量规则解决超声心动图视频分割中的长程依赖与效率平衡问题。

**关键词**：超声心动图分割, 时空键值记忆, 门控增量规则, 视频分析, 深度学习

## 3 点简述
- 核心问题：超声心动图视频分割面临噪声、伪影及心脏变形运动挑战，现有方法在长程时空依赖捕获与计算效率间难以权衡。
- 方法要点：采用线性键值关联建模帧间相关性，引入门控增量规则高效存储记忆状态，设计关键像素特征融合模块整合多尺度局部与全局特征。
- 实验或效果：在CAMUS和EchoNet-Dynamic数据集上验证，GDKVM在分割精度、鲁棒性和实时性能方面优于现有方法。

## 摘要（原文）

> Accurate segmentation of cardiac chambers in echocardiography sequences is crucial for the quantitative analysis of cardiac function, aiding in clinical diagnosis and treatment. The imaging noise, artifacts, and the deformation and motion of the heart pose challenges to segmentation algorithms. While existing methods based on convolutional neural networks, Transformers, and space-time memory networks have improved segmentation accuracy, they often struggle with the trade-off between capturing long-range spatiotemporal dependencies and maintaining computational efficiency with fine-grained feature representation. In this paper, we introduce GDKVM, a novel architecture for echocardiography video segmentation. The model employs Linear Key-Value Association (LKVA) to effectively model inter-frame correlations, and introduces Gated Delta Rule (GDR) to efficiently store intermediate memory states. Key-Pixel Feature Fusion (KPFF) module is designed to integrate local and global features at multiple scales, enhancing robustness against boundary blurring and noise interference. We validated GDKVM on two mainstream echocardiography video datasets (CAMUS and EchoNet-Dynamic) and compared it with various state-of-the-art methods. Experimental results show that GDKVM outperforms existing approaches in terms of segmentation accuracy and robustness, while ensuring real-time performance. Code is available at https://github.com/wangrui2025/GDKVM.

