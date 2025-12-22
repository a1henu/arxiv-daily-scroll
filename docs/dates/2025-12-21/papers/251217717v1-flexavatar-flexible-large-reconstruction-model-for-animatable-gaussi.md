---
layout: default
title: FlexAvatar: Flexible Large Reconstruction Model for Animatable Gaussian Head Avatars with Detailed Deformation
---

# FlexAvatar: Flexible Large Reconstruction Model for Animatable Gaussian Head Avatars with Detailed Deformation
**arXiv**：[2512.17717v1](https://arxiv.org/abs/2512.17717) · [PDF](https://arxiv.org/pdf/2512.17717.pdf)  
**作者**：Cheng Peng, Zhuo Su, Liao Wang, Chen Guo, Zhaohu Li, Chengjiang Long, Zheng Lv, Jingxiang Sun, Chenyangguang Zhang, Yebin Liu  

**一句话要点**：提出FlexAvatar以从单张或稀疏图像创建高保真可动画3D头部化身，无需相机姿态或表情标签。

**关键词**：3D头部重建, 可动画化身, 动态变形, Transformer模型, UV空间解码, 数据分布调整

## 3 点简述
- 核心问题：从单张或稀疏图像重建高保真3D头部化身，无需相机姿态或表情标签，并实现详细动态变形。
- 方法要点：基于Transformer的重建模型聚合灵活输入，轻量UNet解码器在UV空间生成实时表情相关变形，训练中采用数据分布调整策略。
- 实验或效果：在3D一致性和动态真实感上优于先前方法，支持10秒轻量细化以增强身份细节。

## 摘要（原文）

> We present FlexAvatar, a flexible large reconstruction model for high-fidelity 3D head avatars with detailed dynamic deformation from single or sparse images, without requiring camera poses or expression labels. It leverages a transformer-based reconstruction model with structured head query tokens as canonical anchor to aggregate flexible input-number-agnostic, camera-pose-free and expression-free inputs into a robust canonical 3D representation. For detailed dynamic deformation, we introduce a lightweight UNet decoder conditioned on UV-space position maps, which can produce detailed expression-dependent deformations in real time. To better capture rare but critical expressions like wrinkles and bared teeth, we also adopt a data distribution adjustment strategy during training to balance the distribution of these expressions in the training set. Moreover, a lightweight 10-second refinement can further enhances identity-specific details in extreme identities without affecting deformation quality. Extensive experiments demonstrate that our FlexAvatar achieves superior 3D consistency, detailed dynamic realism compared with previous methods, providing a practical solution for animatable 3D avatar creation.

