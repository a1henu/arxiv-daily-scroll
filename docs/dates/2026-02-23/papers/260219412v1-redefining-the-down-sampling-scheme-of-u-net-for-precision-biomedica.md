---
layout: default
title: Redefining the Down-Sampling Scheme of U-Net for Precision Biomedical Image Segmentation
---

# Redefining the Down-Sampling Scheme of U-Net for Precision Biomedical Image Segmentation
**arXiv**：[2602.19412v1](https://arxiv.org/abs/2602.19412) · [PDF](https://arxiv.org/pdf/2602.19412.pdf)  
**作者**：Mingjie Li, Yizheng Chen, Md Tauhidul Islam, Lei Xing  

**一句话要点**：提出Stair Pooling以解决U-Net在生物医学图像分割中长程信息捕获不足的问题

**关键词**：生物医学图像分割, U-Net架构, 下采样策略, 信息保留, 池化操作, 长程信息捕获

## 3 点简述
- 核心问题：传统下采样技术因追求计算效率导致信息丢失，影响长程信息捕获。
- 方法要点：通过序列化小尺寸多方向池化操作，将每次2D池化的降维比例从1/4降至1/2，减少信息损失。
- 实验或效果：在三个基准测试中，2D和3D U-Net的Dice分数平均提升3.8%，并利用转移熵优化下采样路径。

## 摘要（原文）

> U-Net architectures have been instrumental in advancing biomedical image segmentation (BIS) but often struggle with capturing long-range information. One reason is the conventional down-sampling techniques that prioritize computational efficiency at the expense of information retention. This paper introduces a simple but effective strategy, we call it Stair Pooling, which moderates the pace of down-sampling and reduces information loss by leveraging a sequence of concatenated small and narrow pooling operations in varied orientations. Specifically, our method modifies the reduction in dimensionality within each 2D pooling step from $\frac{1}{4}$ to $\frac{1}{2}$. This approach can also be adapted for 3D pooling to preserve even more information. Such preservation aids the U-Net in more effectively reconstructing spatial details during the up-sampling phase, thereby enhancing its ability to capture long-range information and improving segmentation accuracy. Extensive experiments on three BIS benchmarks demonstrate that the proposed Stair Pooling can increase both 2D and 3D U-Net performance by an average of 3.8\% in Dice scores. Moreover, we leverage the transfer entropy to select the optimal down-sampling paths and quantitatively show how the proposed Stair Pooling reduces the information loss.

