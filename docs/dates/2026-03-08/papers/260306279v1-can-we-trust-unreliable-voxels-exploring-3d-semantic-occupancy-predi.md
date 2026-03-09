---
layout: default
title: Can we Trust Unreliable Voxels? Exploring 3D Semantic Occupancy Prediction under Label Noise
---

# Can we Trust Unreliable Voxels? Exploring 3D Semantic Occupancy Prediction under Label Noise
**arXiv**：[2603.06279v1](https://arxiv.org/abs/2603.06279) · [PDF](https://arxiv.org/pdf/2603.06279.pdf)  
**作者**：Wenxin Li, Kunyu Peng, Di Wen, Junwei Zheng, Jiale Wei, Mengfei Duan, Yuheng Zhang, Rui Fan, Kailun Yang  

**一句话要点**：提出DPR-Occ框架以解决3D语义占据预测中的标签噪声问题

**关键词**：3D语义占据预测, 标签噪声学习, 机器人感知, 动态环境, 部分标签推理

## 3 点简述
- 核心问题：真实世界3D体素标注存在结构伪影和动态拖尾噪声，影响机器人感知可靠性。
- 方法要点：通过双源部分标签推理，结合时间模型记忆和表示级结构亲和性，动态扩展和修剪候选标签集。
- 实验或效果：在SemanticKITTI上，即使90%标签噪声下，性能提升达2.57% mIoU和13.91% IoU。

## 摘要（原文）

> 3D semantic occupancy prediction is a cornerstone of robotic perception, yet real-world voxel annotations are inherently corrupted by structural artifacts and dynamic trailing effects. This raises a critical but underexplored question: can autonomous systems safely rely on such unreliable occupancy supervision? To systematically investigate this issue, we establish OccNL, the first benchmark dedicated to 3D occupancy under occupancy-asymmetric and dynamic trailing noise. Our analysis reveals a fundamental domain gap: state-of-the-art 2D label noise learning strategies collapse catastrophically in sparse 3D voxel spaces, exposing a critical vulnerability in existing paradigms. To address this challenge, we propose DPR-Occ, a principled label noise-robust framework that constructs reliable supervision through dual-source partial label reasoning. By synergizing temporal model memory with representation-level structural affinity, DPR-Occ dynamically expands and prunes candidate label sets to preserve true semantics while suppressing noise propagation. Extensive experiments on SemanticKITTI demonstrate that DPR-Occ prevents geometric and semantic collapse under extreme corruption. Notably, even at 90% label noise, our method achieves significant performance gains (up to 2.57% mIoU and 13.91% IoU) over existing label noise learning baselines adapted to the 3D occupancy prediction task. By bridging label noise learning and 3D perception, OccNL and DPR-Occ provide a reliable foundation for safety-critical robotic perception in dynamic environments. The benchmark and source code will be made publicly available at https://github.com/mylwx/OccNL.

