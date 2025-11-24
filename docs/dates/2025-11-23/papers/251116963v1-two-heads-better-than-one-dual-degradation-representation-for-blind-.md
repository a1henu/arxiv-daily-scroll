---
layout: default
title: Two Heads Better than One: Dual Degradation Representation for Blind Super-Resolution
---

# Two Heads Better than One: Dual Degradation Representation for Blind Super-Resolution
**arXiv**：[2511.16963v1](https://arxiv.org/abs/2511.16963) · [PDF](https://arxiv.org/pdf/2511.16963.pdf)  
**作者**：Hsuan Yuan, Shao-Yu Weng, I-Hsuan Lo, Wei-Chen Chiu, Yu-Syuan Xu, Hao-Chien Hsueh, Jen-Hui Chuang, Ching-Chun Huang  

**一句话要点**：提出双分支退化提取网络以解决盲超分辨率问题

**关键词**：盲超分辨率, 退化提取, 双分支网络, 无监督嵌入, 图像超分

## 3 点简述
- 盲超分辨率中实际退化与假设不符导致性能下降
- 预测无监督模糊和噪声嵌入，SR网络分别适应
- 在多个基准测试中实现最先进性能

## 摘要（原文）

> Previous methods have demonstrated remarkable performance in single image super-resolution (SISR) tasks with known and fixed degradation (e.g., bicubic downsampling). However, when the actual degradation deviates from these assumptions, these methods may experience significant declines in performance. In this paper, we propose a Dual Branch Degradation Extractor Network to address the blind SR problem. While some blind SR methods assume noise-free degradation and others do not explicitly consider the presence of noise in the degradation model, our approach predicts two unsupervised degradation embeddings that represent blurry and noisy information. The SR network can then be adapted to blur embedding and noise embedding in distinct ways. Furthermore, we treat the degradation extractor as a regularizer to capitalize on differences between SR and HR images. Extensive experiments on several benchmarks demonstrate our method achieves SOTA performance in the blind SR problem.

