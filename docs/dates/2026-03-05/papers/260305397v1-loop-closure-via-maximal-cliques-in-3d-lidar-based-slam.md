---
layout: default
title: Loop Closure via Maximal Cliques in 3D LiDAR-Based SLAM
---

# Loop Closure via Maximal Cliques in 3D LiDAR-Based SLAM
**arXiv**：[2603.05397v1](https://arxiv.org/abs/2603.05397) · [PDF](https://arxiv.org/pdf/2603.05397.pdf)  
**作者**：Javier Laserna, Saurabh Gupta, Oscar Martinez Mozos, Cyrill Stachniss, Pablo San Segundo  

**一句话要点**：提出CliReg算法，通过最大团搜索替代RANSAC，以增强3D LiDAR SLAM中的闭环检测鲁棒性。

**关键词**：3D LiDAR SLAM, 闭环检测, 最大团搜索, 特征对应, 鲁棒性, 实时处理

## 3 点简述
- 核心问题：3D LiDAR SLAM中闭环检测在噪声、环境模糊和视角变化下不可靠，RANSAC易失败导致地图不一致。
- 方法要点：CliReg基于特征对应兼容图进行最大团搜索，避免随机采样，提高对噪声和离群点的鲁棒性。
- 实验或效果：在真实数据集上验证，相比RANSAC，降低位姿误差，提升闭环可靠性，尤其在稀疏或模糊条件下。

## 摘要（原文）

> Reliable loop closure detection remains a critical challenge in 3D LiDAR-based SLAM, especially under sensor noise, environmental ambiguity, and viewpoint variation conditions. RANSAC is often used in the context of loop closures for geometric model fitting in the presence of outliers. However, this approach may fail, leading to map inconsistency. We introduce a novel deterministic algorithm, CliReg, for loop closure validation that replaces RANSAC verification with a maximal clique search over a compatibility graph of feature correspondences. This formulation avoids random sampling and increases robustness in the presence of noise and outliers. We integrated our approach into a real- time pipeline employing binary 3D descriptors and a Hamming distance embedding binary search tree-based matching. We evaluated it on multiple real-world datasets featuring diverse LiDAR sensors. The results demonstrate that our proposed technique consistently achieves a lower pose error and more reliable loop closures than RANSAC, especially in sparse or ambiguous conditions. Additional experiments on 2D projection-based maps confirm its generality across spatial domains, making our approach a robust and efficient alternative for loop closure detection.

