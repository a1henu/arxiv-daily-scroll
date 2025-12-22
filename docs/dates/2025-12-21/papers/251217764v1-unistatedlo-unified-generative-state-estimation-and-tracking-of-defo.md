---
layout: default
title: UniStateDLO: Unified Generative State Estimation and Tracking of Deformable Linear Objects Under Occlusion for Constrained Manipulation
---

# UniStateDLO: Unified Generative State Estimation and Tracking of Deformable Linear Objects Under Occlusion for Constrained Manipulation
**arXiv**：[2512.17764v1](https://arxiv.org/abs/2512.17764) · [PDF](https://arxiv.org/pdf/2512.17764.pdf)  
**作者**：Kangchen Lv, Mingrui Yu, Shihefeng Wang, Xiangyang Ji, Xiang Li  

**一句话要点**：提出UniStateDLO，利用扩散模型实现遮挡下可变形线性物体的统一状态估计与跟踪

**关键词**：可变形线性物体, 状态估计, 扩散模型, 遮挡处理, 仿真到真实泛化, 点云处理

## 3 点简述
- 核心问题：可变形线性物体在受限环境中易受遮挡，导致视觉感知不可靠
- 方法要点：将状态估计与跟踪建模为条件生成问题，基于扩散模型处理部分点云输入
- 实验或效果：在合成数据上训练，实现零样本仿真到真实泛化，实时预测全局平滑且局部精确的状态

## 摘要（原文）

> Perception of deformable linear objects (DLOs), such as cables, ropes, and wires, is the cornerstone for successful downstream manipulation. Although vision-based methods have been extensively explored, they remain highly vulnerable to occlusions that commonly arise in constrained manipulation environments due to surrounding obstacles, large and varying deformations, and limited viewpoints. Moreover, the high dimensionality of the state space, the lack of distinctive visual features, and the presence of sensor noises further compound the challenges of reliable DLO perception. To address these open issues, this paper presents UniStateDLO, the first complete DLO perception pipeline with deep-learning methods that achieves robust performance under severe occlusion, covering both single-frame state estimation and cross-frame state tracking from partial point clouds. Both tasks are formulated as conditional generative problems, leveraging the strong capability of diffusion models to capture the complex mapping between highly partial observations and high-dimensional DLO states. UniStateDLO effectively handles a wide range of occlusion patterns, including initial occlusion, self-occlusion, and occlusion caused by multiple objects. In addition, it exhibits strong data efficiency as the entire network is trained solely on a large-scale synthetic dataset, enabling zero-shot sim-to-real generalization without any real-world training data. Comprehensive simulation and real-world experiments demonstrate that UniStateDLO outperforms all state-of-the-art baselines in both estimation and tracking, producing globally smooth yet locally precise DLO state predictions in real time, even under substantial occlusions. Its integration as the front-end module in a closed-loop DLO manipulation system further demonstrates its ability to support stable feedback control in complex, constrained 3-D environments.

