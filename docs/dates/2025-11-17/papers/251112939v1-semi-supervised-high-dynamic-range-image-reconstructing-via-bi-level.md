---
layout: default
title: Semi-Supervised High Dynamic Range Image Reconstructing via Bi-Level Uncertain Area Masking
---

# Semi-Supervised High Dynamic Range Image Reconstructing via Bi-Level Uncertain Area Masking
**arXiv**：[2511.12939v1](https://arxiv.org/abs/2511.12939) · [PDF](https://arxiv.org/pdf/2511.12939.pdf)  
**作者**：Wei Jiang, Jiahao Cui, Yizheng Wu, Zhan Peng, Zhiyu Pan, Zhiguo Cao  

**一句话要点**：提出双层不确定性掩码的半监督方法以解决HDR图像重建中标注数据稀缺问题

**关键词**：高动态范围图像重建, 半监督学习, 不确定性掩码, 师生模型, 计算摄影

## 3 点简述
- 核心问题：HDR图像重建依赖LDR-HDR图像对，但标注数据难以获取，导致性能受限
- 方法要点：采用师生模型框架，通过像素和补丁级不确定性掩码过滤伪标签中的不可靠区域
- 实验或效果：仅使用6.7%标注数据，性能优于现有半监督方法，并媲美全监督方法

## 摘要（原文）

> Reconstructing high dynamic range (HDR) images from low dynamic range (LDR) bursts plays an essential role in the computational photography. Impressive progress has been achieved by learning-based algorithms which require LDR-HDR image pairs. However, these pairs are hard to obtain, which motivates researchers to delve into the problem of annotation-efficient HDR image reconstructing: how to achieve comparable performance with limited HDR ground truths (GTs). This work attempts to address this problem from the view of semi-supervised learning where a teacher model generates pseudo HDR GTs for the LDR samples without GTs and a student model learns from pseudo GTs. Nevertheless, the confirmation bias, i.e., the student may learn from the artifacts in pseudo HDR GTs, presents an impediment. To remove this impediment, an uncertainty-based masking process is proposed to discard unreliable parts of pseudo GTs at both pixel and patch levels, then the trusted areas can be learned from by the student. With this novel masking process, our semi-supervised HDR reconstructing method not only outperforms previous annotation-efficient algorithms, but also achieves comparable performance with up-to-date fully-supervised methods by using only 6.7% HDR GTs.

