---
layout: default
title: ICLR: Inter-Chrominance and Luminance Interaction for Natural Color Restoration in Low-Light Image Enhancement
---

# ICLR: Inter-Chrominance and Luminance Interaction for Natural Color Restoration in Low-Light Image Enhancement
**arXiv**：[2511.13607v1](https://arxiv.org/abs/2511.13607) · [PDF](https://arxiv.org/pdf/2511.13607.pdf)  
**作者**：Xin Xu, Hao Liu, Wei Liu, Wei Wang, Jiayi Wu, Kui Jiang  

**一句话要点**：提出ICLR框架以解决低光图像增强中色度与亮度交互问题

**关键词**：低光图像增强, 色度亮度交互, 双流交互模块, 协方差校正损失, 自然色彩恢复

## 3 点简述
- 核心问题：色度与亮度分支分布差异大，导致特征提取受限和误差传播。
- 方法要点：引入DIEM模块增强互补信息提取，CCL损失平衡梯度冲突。
- 实验或效果：在多个数据集上优于现有方法，提升图像细节恢复。

## 摘要（原文）

> Low-Light Image Enhancement (LLIE) task aims at improving contrast while restoring details and textures for images captured in low-light conditions. HVI color space has made significant progress in this task by enabling precise decoupling of chrominance and luminance. However, for the interaction of chrominance and luminance branches, substantial distributional differences between the two branches prevalent in natural images limit complementary feature extraction, and luminance errors are propagated to chrominance channels through the nonlinear parameter. Furthermore, for interaction between different chrominance branches, images with large homogeneous-color regions usually exhibit weak correlation between chrominance branches due to concentrated distributions. Traditional pixel-wise losses exploit strong inter-branch correlations for co-optimization, causing gradient conflicts in weakly correlated regions. Therefore, we propose an Inter-Chrominance and Luminance Interaction (ICLR) framework including a Dual-stream Interaction Enhancement Module (DIEM) and a Covariance Correction Loss (CCL). The DIEM improves the extraction of complementary information from two dimensions, fusion and enhancement, respectively. The CCL utilizes luminance residual statistics to penalize chrominance errors and balances gradient conflicts by constraining chrominance branches covariance. Experimental results on multiple datasets show that the proposed ICLR framework outperforms state-of-the-art methods.

