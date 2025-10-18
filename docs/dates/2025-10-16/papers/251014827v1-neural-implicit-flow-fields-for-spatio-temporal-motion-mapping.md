---
layout: default
title: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping
---

# Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping
**arXiv**：[2510.14827v1](https://arxiv.org/abs/2510.14827) · [PDF](https://arxiv.org/pdf/2510.14827.pdf)  
**作者**：Yufei Zhu, Shih-Min Yang, Andrey Rudenko, Tomasz P. Kucner, Achim J. Lilienthal, Martin Magnusson  

**一句话要点**：提出基于隐式神经函数的连续时空运动映射方法以提升机器人操作安全与效率

**关键词**：隐式神经表示, 动态地图建模, 时空运动模式, 机器人导航, 高斯混合模型

## 3 点简述
- 核心问题：现有动态地图使用离散空间采样，构建成本高且难以处理不均匀采样区域。
- 方法要点：采用隐式神经函数直接映射坐标到半包裹高斯混合模型参数，实现连续时空建模。
- 实验或效果：在真实世界数据集上验证，精度更高、稀疏区域速度分布更平滑且计算高效。

## 摘要（原文）

> Safe and efficient robot operation in complex human environments can benefit
> from good models of site-specific motion patterns. Maps of Dynamics (MoDs)
> provide such models by encoding statistical motion patterns in a map, but
> existing representations use discrete spatial sampling and typically require
> costly offline construction. We propose a continuous spatio-temporal MoD
> representation based on implicit neural functions that directly map coordinates
> to the parameters of a Semi-Wrapped Gaussian Mixture Model. This removes the
> need for discretization and imputation for unevenly sampled regions, enabling
> smooth generalization across both space and time. Evaluated on a large public
> dataset with long-term real-world people tracking data, our method achieves
> better accuracy of motion representation and smoother velocity distributions in
> sparse regions while still being computationally efficient, compared to
> available baselines. The proposed approach demonstrates a powerful and
> efficient way of modeling complex human motion patterns.

