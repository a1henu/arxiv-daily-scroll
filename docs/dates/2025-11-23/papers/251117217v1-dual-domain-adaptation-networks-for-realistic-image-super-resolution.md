---
layout: default
title: Dual-domain Adaptation Networks for Realistic Image Super-resolution
---

# Dual-domain Adaptation Networks for Realistic Image Super-resolution
**arXiv**：[2511.17217v1](https://arxiv.org/abs/2511.17217) · [PDF](https://arxiv.org/pdf/2511.17217.pdf)  
**作者**：Chaowei Fang, Bolin Fu, De Cheng, Lechao Cheng, Guanbin Li  

**一句话要点**：提出双域适应网络以解决真实图像超分辨率中数据不足问题

**关键词**：图像超分辨率, 域适应, 频域分析, 低秩适应, 真实图像处理

## 3 点简述
- 核心问题：真实图像超分辨率面临真实LR-HR数据稀缺，影响模型学习基本特征
- 方法要点：结合空间域参数选择更新与低秩适应，并添加频域分支增强高频恢复
- 实验或效果：在RealSR等基准测试中优于现有方法，代码已开源

## 摘要（原文）

> Realistic image super-resolution (SR) focuses on transforming real-world low-resolution (LR) images into high-resolution (HR) ones, handling more complex degradation patterns than synthetic SR tasks. This is critical for applications like surveillance, medical imaging, and consumer electronics. However, current methods struggle with limited real-world LR-HR data, impacting the learning of basic image features. Pre-trained SR models from large-scale synthetic datasets offer valuable prior knowledge, which can improve generalization, speed up training, and reduce the need for extensive real-world data in realistic SR tasks. In this paper, we introduce a novel approach, Dual-domain Adaptation Networks, which is able to efficiently adapt pre-trained image SR models from simulated to real-world datasets. To achieve this target, we first set up a spatial-domain adaptation strategy through selectively updating parameters of pre-trained models and employing the low-rank adaptation technique to adjust frozen parameters. Recognizing that image super-resolution involves recovering high-frequency components, we further integrate a frequency domain adaptation branch into the adapted model, which combines the spectral data of the input and the spatial-domain backbone's intermediate features to infer HR frequency maps, enhancing the SR result. Experimental evaluations on public realistic image SR benchmarks, including RealSR, D2CRealSR, and DRealSR, demonstrate the superiority of our proposed method over existing state-of-the-art models. Codes are available at: https://github.com/dummerchen/DAN.

