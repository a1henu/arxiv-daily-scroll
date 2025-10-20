---
layout: default
title: VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation
---

# VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation
**arXiv**：[2510.15530v1](https://arxiv.org/abs/2510.15530) · [PDF](https://arxiv.org/pdf/2510.15530.pdf)  
**作者**：Zehao Ni, Yonghao He, Lingfeng Qian, Jilei Mao, Fa Fu, Wei Sui, Hu Su, Junran Peng, Zhipeng Wang, Bin He  

**一句话要点**：提出VO-DP方法以解决仅视觉机器人操作中的语义-几何特征融合问题

**关键词**：机器人操作, 扩散策略, 视觉基础模型, 特征融合, 鲁棒性评估, 开源训练库

## 3 点简述
- 核心问题：现有方法依赖点云，缺乏对仅视觉方案的深入探索。
- 方法要点：利用预训练视觉基础模型融合语义和几何特征，通过交叉注意力和CNN压缩输入策略头。
- 实验或效果：在仿真和真实任务中，VO-DP性能优于基线，并展示高鲁棒性。

## 摘要（原文）

> In the context of imitation learning, visuomotor-based diffusion policy
> learning is one of the main directions in robotic manipulation. Most of these
> approaches rely on point clouds as observation inputs and construct scene
> representations through point clouds feature learning, which enables them to
> achieve remarkable accuracy. However, the existing literature lacks an in-depth
> exploration of vision-only solutions that have significant potential. In this
> paper, we propose a Vision-Only and single-view Diffusion Policy learning
> method (VO-DP) that leverages pretrained visual foundation models to achieve
> effective fusion of semantic and geometric features. We utilize intermediate
> features from VGGT incorporating semantic features from DINOv2 and geometric
> features from Alternating Attention blocks. Features are fused via
> cross-attention and spatially compressed with a CNN to form the input to the
> policy head. Extensive experiments demonstrate that VO-DP not only outperforms
> the vision-only baseline DP significantly but also exhibits distinct
> performance trends against the point cloud-based method DP3: in simulation
> tasks, VO-DP achieves an average success rate of 64.6% on par with DP3 64.0%
> and far higher than DP 34.8%, while in real-world tasks, it reaches 87.9%,
> outperforming both DP3 67.5% and DP 11.2% by a notable margin. Further
> robustness evaluations confirm that VO-DP remains highly stable under varying
> conditions including color, size, background, and lighting. Lastly, we
> open-source a training library for robotic manipulation. Built on Accelerate,
> this library supports multi-machine and multi-GPU parallel training, as well as
> mixed precision training. It is compatible with visuomotor policies such as DP,
> DP3 and VO-DP, and also supports the RoboTwin simulator.

