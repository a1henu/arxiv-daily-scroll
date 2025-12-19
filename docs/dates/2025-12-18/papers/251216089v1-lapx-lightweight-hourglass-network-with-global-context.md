---
layout: default
title: LAPX: Lightweight Hourglass Network with Global Context
---

# LAPX: Lightweight Hourglass Network with Global Context
**arXiv**：[2512.16089v1](https://arxiv.org/abs/2512.16089) · [PDF](https://arxiv.org/pdf/2512.16089.pdf)  
**作者**：Haopeng Zhao, Marsha Mariya Kappan, Mahdi Bamdad, Francisco Cruz  

**一句话要点**：提出LAPX轻量级沙漏网络，结合自注意力捕获全局上下文，以解决边缘设备上姿态估计的精度与效率平衡问题。

**关键词**：人体姿态估计, 轻量级网络, 自注意力机制, 边缘计算, 沙漏网络, 全局上下文

## 3 点简述
- 核心问题：现有姿态估计方法在边缘设备上部署时，常面临参数多、计算成本高或设计简化导致精度受限的挑战。
- 方法要点：基于LAP改进，引入自注意力模块捕获全局信息，优化阶段设计和轻量级注意力模块，提升模型效率与准确性。
- 实验或效果：在MPII和COCO数据集上取得竞争性结果，仅2.3M参数，实现实时性能，验证了边缘设备适用性。

## 摘要（原文）

> Human pose estimation is a crucial task in computer vision. Methods that have SOTA (State-of-the-Art) accuracy, often involve a large number of parameters and incur substantial computational cost. Many lightweight variants have been proposed to reduce the model size and computational cost of them. However, several of these methods still contain components that are not well suited for efficient deployment on edge devices. Moreover, models that primarily emphasize inference speed on edge devices often suffer from limited accuracy due to their overly simplified designs. To address these limitations, we propose LAPX, an Hourglass network with self-attention that captures global contextual information, based on previous work, LAP. In addition to adopting the self-attention module, LAPX advances the stage design and refine the lightweight attention modules. It achieves competitive results on two benchmark datasets, MPII and COCO, with only 2.3M parameters, and demonstrates real-time performance, confirming its edge-device suitability.

