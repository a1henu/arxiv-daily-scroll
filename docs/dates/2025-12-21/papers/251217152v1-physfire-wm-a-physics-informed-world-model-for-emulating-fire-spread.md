---
layout: default
title: PhysFire-WM: A Physics-Informed World Model for Emulating Fire Spread Dynamics
---

# PhysFire-WM: A Physics-Informed World Model for Emulating Fire Spread Dynamics
**arXiv**：[2512.17152v1](https://arxiv.org/abs/2512.17152) · [PDF](https://arxiv.org/pdf/2512.17152.pdf)  
**作者**：Nan Zhou, Huandong Wang, Jiahao Li, Yang Li, Xiao-Ping Zhang, Yong Li, Xinlei Chen  

**一句话要点**：提出PhysFire-WM物理信息世界模型以解决火灾蔓延预测中的物理不一致和掩模信息稀疏问题

**关键词**：火灾蔓延预测, 物理信息世界模型, 跨任务协同训练, 红外图像, 细粒度预测, 灾难预测

## 3 点简述
- 核心问题：现有火灾预测方法依赖稀疏二值掩模，难以捕捉复杂动态，且世界模型存在物理不一致性。
- 方法要点：通过物理模拟器编码结构化先验纠正物理差异，并采用跨任务协同训练整合热辐射动态和空间边界信息。
- 实验或效果：在细粒度多模态火灾数据集上验证了PhysFire-WM在火灾蔓延预测中的高准确性，强调了物理先验和跨任务协作的重要性。

## 摘要（原文）

> Fine-grained fire prediction plays a crucial role in emergency response. Infrared images and fire masks provide complementary thermal and boundary information, yet current methods are predominantly limited to binary mask modeling with inherent signal sparsity, failing to capture the complex dynamics of fire. While world models show promise in video generation, their physical inconsistencies pose significant challenges for fire forecasting. This paper introduces PhysFire-WM, a Physics-informed World Model for emulating Fire spread dynamics. Our approach internalizes combustion dynamics by encoding structured priors from a Physical Simulator to rectify physical discrepancies, coupled with a Cross-task Collaborative Training strategy (CC-Train) that alleviates the issue of limited information in mask-based modeling. Through parameter sharing and gradient coordination, CC-Train effectively integrates thermal radiation dynamics and spatial boundary delineation, enhancing both physical realism and geometric accuracy. Extensive experiments on a fine-grained multimodal fire dataset demonstrate the superior accuracy of PhysFire-WM in fire spread prediction. Validation underscores the importance of physical priors and cross-task collaboration, providing new insights for applying physics-informed world models to disaster prediction.

