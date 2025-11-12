---
layout: default
title: Twist and Compute: The Cost of Pose in 3D Generative Diffusion
---

# Twist and Compute: The Cost of Pose in 3D Generative Diffusion
**arXiv**：[2511.08203v1](https://arxiv.org/abs/2511.08203) · [PDF](https://arxiv.org/pdf/2511.08203.pdf)  
**作者**：Kyle Fogarty, Jack Foster, Boqiao Zhang, Jing Yang, Cengiz Öztireli  

**一句话要点**：提出轻量CNN检测输入方向以缓解3D生成模型视角偏差问题

**关键词**：3D生成模型, 视角偏差, 图像到3D生成, 轻量CNN, 泛化能力, 对称感知设计

## 3 点简述
- 核心问题：图像到3D生成模型存在强规范视角偏差，影响多视角泛化能力
- 方法要点：使用轻量CNN检测并校正输入图像方向，不修改生成主干网络
- 实验或效果：在旋转输入下性能下降，经校正后恢复模型性能

## 摘要（原文）

> Despite their impressive results, large-scale image-to-3D generative models remain opaque in their inductive biases. We identify a significant limitation in image-conditioned 3D generative models: a strong canonical view bias. Through controlled experiments using simple 2D rotations, we show that the state-of-the-art Hunyuan3D 2.0 model can struggle to generalize across viewpoints, with performance degrading under rotated inputs. We show that this failure can be mitigated by a lightweight CNN that detects and corrects input orientation, restoring model performance without modifying the generative backbone. Our findings raise an important open question: Is scale enough, or should we pursue modular, symmetry-aware designs?

