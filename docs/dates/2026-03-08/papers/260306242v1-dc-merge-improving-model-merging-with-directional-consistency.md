---
layout: default
title: DC-Merge: Improving Model Merging with Directional Consistency
---

# DC-Merge: Improving Model Merging with Directional Consistency
**arXiv**：[2603.06242v1](https://arxiv.org/abs/2603.06242) · [PDF](https://arxiv.org/pdf/2603.06242.pdf)  
**作者**：Han-Chen Zhang, Zi-Hao Zhou, Mao-Lin Luo, Shimin Di, Min-Ling Zhang, Tong Wei  

**一句话要点**：提出DC-Merge方法以解决模型合并中的方向一致性问题，提升多任务知识保留。

**关键词**：模型合并, 方向一致性, 奇异值平滑, 正交子空间投影, 多任务学习, 视觉语言模型

## 3 点简述
- 核心问题：模型合并时，任务向量能量分布不均和几何不一致导致方向一致性受损，影响知识保留。
- 方法要点：通过平滑奇异值平衡能量分布，并在共享正交子空间投影对齐向量，确保方向一致。
- 实验或效果：在视觉和视觉语言基准测试中，DC-Merge在完整微调和LoRA设置下均达到最先进性能。

## 摘要（原文）

> Model merging aims to integrate multiple task-adapted models into a unified model that preserves the knowledge of each task. In this paper, we identify that the key to this knowledge retention lies in maintaining the directional consistency of singular spaces between merged multi-task vector and individual task vectors. However, this consistency is frequently compromised by two issues: i) an imbalanced energy distribution within task vectors, where a small fraction of singular values dominate the total energy, leading to the neglect of semantically important but weaker components upon merging, and ii) the geometric inconsistency of task vectors in parameter space, which causes direct merging to distort their underlying directional geometry. To address these challenges, we propose DC-Merge, a method for directional-consistent model merging. It first balances the energy distribution of each task vector by smoothing its singular values, ensuring all knowledge components are adequately represented. These energy-balanced vectors are then projected onto a shared orthogonal subspace to align their directional geometries with minimal reconstruction error. Finally, the aligned vectors are aggregated in the shared orthogonal subspace and projected back to the original parameter space. Extensive experiments on vision and vision-language benchmarks show that DC-Merge consistently achieves state-of-the-art performance in both full fine-tuning and LoRA settings. The implementation code is available at https://github.com/Tobeginwith/DC-Merge.

