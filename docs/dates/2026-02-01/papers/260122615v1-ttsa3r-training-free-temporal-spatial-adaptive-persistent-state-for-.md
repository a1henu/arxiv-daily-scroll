---
layout: default
title: TTSA3R: Training-Free Temporal-Spatial Adaptive Persistent State for Streaming 3D Reconstruction
---

# TTSA3R: Training-Free Temporal-Spatial Adaptive Persistent State for Streaming 3D Reconstruction
**arXiv**：[2601.22615v1](https://arxiv.org/abs/2601.22615) · [PDF](https://arxiv.org/pdf/2601.22615.pdf)  
**作者**：Zhijie Zheng, Xinhao Xiang, Jiawei Zhang  

**一句话要点**：提出TTSA3R训练免费框架，通过时空自适应状态更新解决流式3D重建中的长期记忆遗忘问题。

**关键词**：流式3D重建, 自适应状态更新, 时空一致性, 训练免费框架, 长期记忆遗忘

## 3 点简述
- 核心问题：流式循环模型在长序列3D重建中因平衡历史与新观测而面临灾难性记忆遗忘。
- 方法要点：设计时间自适应更新模块和空间上下文更新模块，融合时空信号以自适应更新状态。
- 实验或效果：在扩展序列上，误差仅增15%，显著优于基线模型超200%的退化，提升重建稳定性。

## 摘要（原文）

> Streaming recurrent models enable efficient 3D reconstruction by maintaining persistent state representations. However, they suffer from catastrophic memory forgetting over long sequences due to balancing historical information with new observations. Recent methods alleviate this by deriving adaptive signals from attention perspective, but they operate on single dimensions without considering temporal and spatial consistency. To this end, we propose a training-free framework termed TTSA3R that leverages both temporal state evolution and spatial observation quality for adaptive state updates in 3D reconstruction. In particular, we devise a Temporal Adaptive Update Module that regulates update magnitude by analyzing temporal state evolution patterns. Then, a Spatial Contextual Update Module is introduced to localize spatial regions that require updates through observation-state alignment and scene dynamics. These complementary signals are finally fused to determine the state updating strategies. Extensive experiments demonstrate the effectiveness of TTSA3R in diverse 3D tasks. Moreover, our method exhibits only 15% error increase compared to over 200% degradation in baseline models on extended sequences, significantly improving long-term reconstruction stability. Our codes will be available soon.

