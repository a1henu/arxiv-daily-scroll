---
layout: default
title: Informative Object-centric Next Best View for Object-aware 3D Gaussian Splatting in Cluttered Scenes
---

# Informative Object-centric Next Best View for Object-aware 3D Gaussian Splatting in Cluttered Scenes
**arXiv**：[2602.08266v1](https://arxiv.org/abs/2602.08266) · [PDF](https://arxiv.org/pdf/2602.08266.pdf)  
**作者**：Seunghoon Jeong, Eunho Lee, Jeongyun Kim, Ayoung Kim  

**一句话要点**：提出实例感知的下一最佳视角策略，以提升杂乱场景中对象感知3D高斯溅射的表示可靠性

**关键词**：3D高斯溅射, 下一最佳视角, 对象感知, 杂乱场景, 信息增益, 机器人操作

## 3 点简述
- 核心问题：现有方法依赖几何线索，忽视语义信息，在杂乱场景中难以选择信息丰富的视角。
- 方法要点：通过蒸馏实例级信息为独热对象向量，计算置信加权信息增益，指导识别错误和不确定的高斯区域。
- 实验效果：在合成和真实数据集上深度误差显著降低，对象中心策略进一步减少目标对象误差。

## 摘要（原文）

> In cluttered scenes with inevitable occlusions and incomplete observations, selecting informative viewpoints is essential for building a reliable representation. In this context, 3D Gaussian Splatting (3DGS) offers a distinct advantage, as it can explicitly guide the selection of subsequent viewpoints and then refine the representation with new observations. However, existing approaches rely solely on geometric cues, neglect manipulation-relevant semantics, and tend to prioritize exploitation over exploration. To tackle these limitations, we introduce an instance-aware Next Best View (NBV) policy that prioritizes underexplored regions by leveraging object features. Specifically, our object-aware 3DGS distills instancelevel information into one-hot object vectors, which are used to compute confidence-weighted information gain that guides the identification of regions associated with erroneous and uncertain Gaussians. Furthermore, our method can be easily adapted to an object-centric NBV, which focuses view selection on a target object, thereby improving reconstruction robustness to object placement. Experiments demonstrate that our NBV policy reduces depth error by up to 77.14% on the synthetic dataset and 34.10% on the real-world GraspNet dataset compared to baselines. Moreover, compared to targeting the entire scene, performing NBV on a specific object yields an additional reduction of 25.60% in depth error for that object. We further validate the effectiveness of our approach through real-world robotic manipulation tasks.

