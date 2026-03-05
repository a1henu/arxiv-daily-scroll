---
layout: default
title: EgoPoseFormer v2: Accurate Egocentric Human Motion Estimation for AR/VR
---

# EgoPoseFormer v2: Accurate Egocentric Human Motion Estimation for AR/VR
**arXiv**：[2603.04090v1](https://arxiv.org/abs/2603.04090) · [PDF](https://arxiv.org/pdf/2603.04090.pdf)  
**作者**：Zhenyu Li, Sai Kumar Dwivedi, Filip Maric, Carlos Chacon, Nadine Bertsch, Filippo Arcadu, Tomas Hodan, Michael Ramamonjisoa, Peter Wonka, Amy Zhao, Robin Kips, Cem Keskin, Anastasia Tkach, Chenhongyi Yang  

**一句话要点**：提出EgoPoseFormer v2，通过Transformer模型和自动标注系统提升AR/VR中第一人称人体运动估计的准确性和一致性。

**关键词**：第一人称运动估计, Transformer模型, 自动标注系统, 半监督学习, AR/VR应用, 不确定性蒸馏

## 3 点简述
- 核心问题：第一人称视角下人体运动估计面临身体覆盖有限、频繁遮挡和标注数据稀缺的挑战。
- 方法要点：采用基于Transformer的模型，引入身份条件查询、多视图空间优化和因果时间注意力，并开发不确定性感知的半监督自动标注系统。
- 实验或效果：在EgoBody3M基准上，模型精度提升12.2%和19.4%，时间抖动减少22.2%和51.7%，自动标注系统进一步降低手腕MPJPE 13.1%。

## 摘要（原文）

> Egocentric human motion estimation is essential for AR/VR experiences, yet remains challenging due to limited body coverage from the egocentric viewpoint, frequent occlusions, and scarce labeled data. We present EgoPoseFormer v2, a method that addresses these challenges through two key contributions: (1) a transformer-based model for temporally consistent and spatially grounded body pose estimation, and (2) an auto-labeling system that enables the use of large unlabeled datasets for training. Our model is fully differentiable, introduces identity-conditioned queries, multi-view spatial refinement, causal temporal attention, and supports both keypoints and parametric body representations under a constant compute budget. The auto-labeling system scales learning to tens of millions of unlabeled frames via uncertainty-aware semi-supervised training. The system follows a teacher-student schema to generate pseudo-labels and guide training with uncertainty distillation, enabling the model to generalize to different environments. On the EgoBody3M benchmark, with a 0.8 ms latency on GPU, our model outperforms two state-of-the-art methods by 12.2% and 19.4% in accuracy, and reduces temporal jitter by 22.2% and 51.7%. Furthermore, our auto-labeling system further improves the wrist MPJPE by 13.1%.

