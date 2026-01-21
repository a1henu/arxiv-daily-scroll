---
layout: default
title: Progressive self-supervised blind-spot denoising method for LDCT denoising
---

# Progressive self-supervised blind-spot denoising method for LDCT denoising
**arXiv**：[2601.14180v1](https://arxiv.org/abs/2601.14180) · [PDF](https://arxiv.org/pdf/2601.14180.pdf)  
**作者**：Yichao Liu, Yueyang Teng, Junwen Guo  

**一句话要点**：提出渐进式自监督盲点去噪方法，用于低剂量CT图像去噪。

**关键词**：低剂量CT去噪, 自监督学习, 盲点去噪, 渐进式训练, 正则化

## 3 点简述
- 核心问题：自监督学习减少对配对正常剂量CT数据的依赖，但现有方法可能去噪不够精细。
- 方法要点：引入渐进式盲点去噪机制，通过条件独立逐步学习，并添加高斯噪声作为正则化。
- 实验或效果：在Mayo LDCT数据集上优于现有自监督方法，性能接近或优于部分监督方法。

## 摘要（原文）

> Self-supervised learning is increasingly investigated for low-dose computed tomography (LDCT) image denoising, as it alleviates the dependence on paired normal-dose CT (NDCT) data, which are often difficult to acquire in clinical practice. In this paper, we propose a novel self-supervised training strategy that relies exclusively on LDCT images. We introduce a step-wise blind-spot denoising mechanism that enforces conditional independence in a progressive manner, enabling more fine-grained denoising learning. In addition, we add Gaussian noise to LDCT images, which acts as a regularization and mitigates overfitting. Extensive experiments on the Mayo LDCT dataset demonstrate that the proposed method consistently outperforms existing self-supervised approaches and achieves performance comparable to, or better than, several representative supervised denoising methods.

