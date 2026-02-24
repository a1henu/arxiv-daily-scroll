---
layout: default
title: Fore-Mamba3D: Mamba-based Foreground-Enhanced Encoding for 3D Object Detection
---

# Fore-Mamba3D: Mamba-based Foreground-Enhanced Encoding for 3D Object Detection
**arXiv**：[2602.19536v1](https://arxiv.org/abs/2602.19536) · [PDF](https://arxiv.org/pdf/2602.19536.pdf)  
**作者**：Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Runze Yang, Huiying Xu, Xinzhong Zhu, Jie Yang, Wei Liu  

**一句话要点**：提出Fore-Mamba3D以增强前景编码，提升3D物体检测性能

**关键词**：3D物体检测, Mamba模型, 前景增强, 线性建模, 上下文表示, 体素序列

## 3 点简述
- 核心问题：现有Mamba方法编码全序列含无用背景信息，仅编码前景体素导致响应衰减和上下文受限。
- 方法要点：设计区域到全局滑动窗口传播信息，并引入语义辅助状态空间融合模块增强语义和几何感知。
- 实验或效果：在多个基准测试中表现优异，验证了Fore-Mamba3D在3D物体检测任务中的有效性。

## 摘要（原文）

> Linear modeling methods like Mamba have been merged as the effective backbone for the 3D object detection task. However, previous Mamba-based methods utilize the bidirectional encoding for the whole non-empty voxel sequence, which contains abundant useless background information in the scenes. Though directly encoding foreground voxels appears to be a plausible solution, it tends to degrade detection performance. We attribute this to the response attenuation and restricted context representation in the linear modeling for fore-only sequences. To address this problem, we propose a novel backbone, termed Fore-Mamba3D, to focus on the foreground enhancement by modifying Mamba-based encoder. The foreground voxels are first sampled according to the predicted scores. Considering the response attenuation existing in the interaction of foreground voxels across different instances, we design a regional-to-global slide window (RGSW) to propagate the information from regional split to the entire sequence. Furthermore, a semantic-assisted and state spatial fusion module (SASFMamba) is proposed to enrich contextual representation by enhancing semantic and geometric awareness within the Mamba model. Our method emphasizes foreground-only encoding and alleviates the distance-based and causal dependencies in the linear autoregression model. The superior performance across various benchmarks demonstrates the effectiveness of Fore-Mamba3D in the 3D object detection task.

