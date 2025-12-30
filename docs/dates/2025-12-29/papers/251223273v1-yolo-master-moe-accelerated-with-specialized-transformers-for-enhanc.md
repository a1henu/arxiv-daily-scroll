---
layout: default
title: YOLO-Master: MOE-Accelerated with Specialized Transformers for Enhanced Real-time Detection
---

# YOLO-Master: MOE-Accelerated with Specialized Transformers for Enhanced Real-time Detection
**arXiv**：[2512.23273v1](https://arxiv.org/abs/2512.23273) · [PDF](https://arxiv.org/pdf/2512.23273.pdf)  
**作者**：Xu Lin, Jinlong Peng, Zhenye Gan, Jiawen Zhu, Jun Liu  

**一句话要点**：提出YOLO-Master，通过实例条件自适应计算增强实时目标检测性能

**关键词**：实时目标检测, 自适应计算, 专家混合, 动态路由, 稀疏计算

## 3 点简述
- 现有实时目标检测方法采用静态密集计算，导致资源分配不均和性能下降
- 引入高效稀疏专家混合块，根据场景复杂度动态分配计算资源
- 在MS COCO上实现42.4% AP和1.62ms延迟，优于YOLOv13-N

## 摘要（原文）

> Existing Real-Time Object Detection (RTOD) methods commonly adopt YOLO-like architectures for their favorable trade-off between accuracy and speed. However, these models rely on static dense computation that applies uniform processing to all inputs, misallocating representational capacity and computational resources such as over-allocating on trivial scenes while under-serving complex ones. This mismatch results in both computational redundancy and suboptimal detection performance. To overcome this limitation, we propose YOLO-Master, a novel YOLO-like framework that introduces instance-conditional adaptive computation for RTOD. This is achieved through a Efficient Sparse Mixture-of-Experts (ES-MoE) block that dynamically allocates computational resources to each input according to its scene complexity. At its core, a lightweight dynamic routing network guides expert specialization during training through a diversity enhancing objective, encouraging complementary expertise among experts. Additionally, the routing network adaptively learns to activate only the most relevant experts, thereby improving detection performance while minimizing computational overhead during inference. Comprehensive experiments on five large-scale benchmarks demonstrate the superiority of YOLO-Master. On MS COCO, our model achieves 42.4% AP with 1.62ms latency, outperforming YOLOv13-N by +0.8% mAP and 17.8% faster inference. Notably, the gains are most pronounced on challenging dense scenes, while the model preserves efficiency on typical inputs and maintains real-time inference speed. Code will be available.

