---
layout: default
title: CogDrive: Cognition-Driven Multimodal Prediction-Planning Fusion for Safe Autonomy
---

# CogDrive: Cognition-Driven Multimodal Prediction-Planning Fusion for Safe Autonomy
**arXiv**：[2512.02777v1](https://arxiv.org/abs/2512.02777) · [PDF](https://arxiv.org/pdf/2512.02777.pdf)  
**作者**：Heye Huang, Yibin Yang, Mingfeng Fan, Haoran Wang, Xiaocong Zhao, Jianqiang Wang  

**一句话要点**：提出CogDrive框架，通过认知驱动多模态预测与规划融合，解决混合交通中安全自动驾驶问题。

**关键词**：自动驾驶安全, 多模态预测, 认知驱动规划, 轨迹优化, 混合交通交互

## 3 点简述
- 核心问题：现有方法难以捕捉罕见但关键的安全行为，规则系统在复杂交互中缺乏适应性。
- 方法要点：采用基于拓扑运动语义和最近邻关系编码的认知表示，结合可微分模态损失和多模态高斯解码优化预测与规划。
- 实验或效果：在Argoverse2和INTERACTION数据集上验证了轨迹精度和漏检率优势，闭环模拟显示在合并和交叉口场景中具有自适应行为。

## 摘要（原文）

> Safe autonomous driving in mixed traffic requires a unified understanding of multimodal interactions and dynamic planning under uncertainty. Existing learning based approaches struggle to capture rare but safety critical behaviors, while rule based systems often lack adaptability in complex interactions. To address these limitations, CogDrive introduces a cognition driven multimodal prediction and planning framework that integrates explicit modal reasoning with safety aware trajectory optimization. The prediction module adopts cognitive representations of interaction modes based on topological motion semantics and nearest neighbor relational encoding. With a differentiable modal loss and multimodal Gaussian decoding, CogDrive learns sparse and unbalanced interaction behaviors and improves long horizon trajectory prediction. The planning module incorporates an emergency response concept and optimizes safety stabilized trajectories, where short term consistent branches ensure safety during replanning cycles and long term branches support smooth and collision free motion under low probability switching modes. Experiments on Argoverse2 and INTERACTION datasets show that CogDrive achieves strong performance in trajectory accuracy and miss rate, while closed loop simulations confirm adaptive behavior in merge and intersection scenarios. By combining cognitive multimodal prediction with safety oriented planning, CogDrive offers an interpretable and reliable paradigm for safe autonomy in complex traffic.

