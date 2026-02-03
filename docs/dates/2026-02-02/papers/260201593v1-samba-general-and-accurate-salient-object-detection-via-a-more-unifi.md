---
layout: default
title: Samba+: General and Accurate Salient Object Detection via A More Unified Mamba-based Framework
---

# Samba+: General and Accurate Salient Object Detection via A More Unified Mamba-based Framework
**arXiv**：[2602.01593v1](https://arxiv.org/abs/2602.01593) · [PDF](https://arxiv.org/pdf/2602.01593.pdf)  
**作者**：Wenzhuo Zhao, Keren Fu, Jiahao He, Xiaohong Liu, Qijun Zhao, Guangtao Zhai  

**一句话要点**：提出Samba+框架，基于Mamba统一处理多模态显著目标检测任务

**关键词**：显著目标检测, Mamba模型, 多模态融合, 持续学习, 计算效率, 统一框架

## 3 点简述
- 现有SOD模型受限于CNN的有限感受野和Transformer的二次计算复杂度，Mamba模型能平衡全局感受野与计算效率。
- Samba引入SGMB块和CAU方法，Samba+通过HGA模块和MACL策略实现多任务联合训练，提升统一性和适应性。
- 实验表明Samba在六项任务上优于现有方法，Samba+使用单一模型获得更优结果，计算成本较低。

## 摘要（原文）

> Existing salient object detection (SOD) models are generally constrained by the limited receptive fields of convolutional neural networks (CNNs) and quadratic computational complexity of Transformers. Recently, the emerging state-space model, namely Mamba, has shown great potential in balancing global receptive fields and computational efficiency. As a solution, we propose Saliency Mamba (Samba), a pure Mamba-based architecture that flexibly handles various distinct SOD tasks, including RGB/RGB-D/RGB-T SOD, video SOD (VSOD), RGB-D VSOD, and visible-depth-thermal SOD. Specifically, we rethink the scanning strategy of Mamba for SOD, and introduce a saliency-guided Mamba block (SGMB) that features a spatial neighborhood scanning (SNS) algorithm to preserve the spatial continuity of salient regions. A context-aware upsampling (CAU) method is also proposed to promote hierarchical feature alignment and aggregation by modeling contextual dependencies. As one step further, to avoid the "task-specific" problem as in previous SOD solutions, we develop Samba+, which is empowered by training Samba in a multi-task joint manner, leading to a more unified and versatile model. Two crucial components that collaboratively tackle challenges encountered in input of arbitrary modalities and continual adaptation are investigated. Specifically, a hub-and-spoke graph attention (HGA) module facilitates adaptive cross-modal interactive fusion, and a modality-anchored continual learning (MACL) strategy alleviates inter-modal conflicts together with catastrophic forgetting. Extensive experiments demonstrate that Samba individually outperforms existing methods across six SOD tasks on 22 datasets with lower computational cost, whereas Samba+ achieves even superior results on these tasks and datasets by using a single trained versatile model. Additional results further demonstrate the potential of our Samba framework.

