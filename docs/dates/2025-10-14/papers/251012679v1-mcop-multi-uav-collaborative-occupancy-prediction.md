---
layout: default
title: MCOP: Multi-UAV Collaborative Occupancy Prediction
---

# MCOP: Multi-UAV Collaborative Occupancy Prediction
**arXiv**：[2510.12679v1](https://arxiv.org/abs/2510.12679) · [PDF](https://arxiv.org/pdf/2510.12679.pdf)  
**作者**：Zefu Lin, Wenbo Chen, Xiaojuan Jin, Yuran Yang, Lue Fan, Yixin Zhang, Yufeng Zhang, Zhaoxiang Zhang  

**一句话要点**：提出多无人机协作占用预测框架以解决BEV方法语义几何信息缺失与性能下降问题

**关键词**：多无人机协作, 占用预测, 3D感知, 特征整合, 通信优化, 无人机群系统

## 3 点简述
- BEV方法因边界框表示无法捕捉完整语义几何信息，且对未定义或遮挡对象性能显著下降
- 集成空间感知特征编码与跨代理特征整合，保留3D结构与语义；引入高度感知特征压缩与双掩码感知指导以提升效率
- 扩展三个数据集评估，实验显示方法在精度上达到最优，同时通信开销大幅降低

## 摘要（原文）

> Unmanned Aerial Vehicle (UAV) swarm systems necessitate efficient
> collaborative perception mechanisms for diverse operational scenarios. Current
> Bird's Eye View (BEV)-based approaches exhibit two main limitations:
> bounding-box representations fail to capture complete semantic and geometric
> information of the scene, and their performance significantly degrades when
> encountering undefined or occluded objects. To address these limitations, we
> propose a novel multi-UAV collaborative occupancy prediction framework. Our
> framework effectively preserves 3D spatial structures and semantics through
> integrating a Spatial-Aware Feature Encoder and Cross-Agent Feature
> Integration. To enhance efficiency, we further introduce Altitude-Aware Feature
> Reduction to compactly represent scene information, along with a Dual-Mask
> Perceptual Guidance mechanism to adaptively select features and reduce
> communication overhead. Due to the absence of suitable benchmark datasets, we
> extend three datasets for evaluation: two virtual datasets (Air-to-Pred-Occ and
> UAV3D-Occ) and one real-world dataset (GauUScene-Occ). Experiments results
> demonstrate that our method achieves state-of-the-art accuracy, significantly
> outperforming existing collaborative methods while reducing communication
> overhead to only a fraction of previous approaches.

