---
layout: default
title: Enhancing Cross-View UAV Geolocalization via LVLM-Driven Relational Modeling
---

# Enhancing Cross-View UAV Geolocalization via LVLM-Driven Relational Modeling
**arXiv**：[2603.08063v1](https://arxiv.org/abs/2603.08063) · [PDF](https://arxiv.org/pdf/2603.08063.pdf)  
**作者**：Bowen Liu, Pengyue Jia, Wanyu Wang, Derong Xu, Jiawei Cheng, Jiancheng Dong, Xiao Han, Zimo Zhao, Chao Zhang, Bowen Yu, Fangyu Hong, Xiangyu Zhao  

**一句话要点**：提出基于LVLM的关系建模插件架构以提升跨视角无人机地理定位精度

**关键词**：跨视角地理定位, 无人机图像匹配, 关系建模, 视觉语言模型, 检索精度提升

## 3 点简述
- 核心问题：现有方法独立提取特征，未显式建模无人机与卫星图像间的交互关系。
- 方法要点：利用大型视觉语言模型学习视觉语义关联，并设计关系感知损失函数优化训练。
- 实验或效果：在多个基准测试中显著提升检索准确率，尤其在苛刻条件下表现优异。

## 摘要（原文）

> The primary objective of cross-view UAV geolocalization is to identify the exact spatial coordinates of drone-captured imagery by aligning it with extensive, geo-referenced satellite databases. Current approaches typically extract features independently from each perspective and rely on basic heuristics to compute similarity, thereby failing to explicitly capture the essential interactions between different views. To address this limitation, we introduce a novel, plug-and-play ranking architecture designed to explicitly perform joint relational modeling for improved UAV-to-satellite image matching. By harnessing the capabilities of a Large Vision-Language Model (LVLM), our framework effectively learns the deep visual-semantic correlations linking UAV and satellite imagery. Furthermore, we present a novel relational-aware loss function to optimize the training phase. By employing soft labels, this loss provides fine-grained supervision that avoids overly penalizing near-positive matches, ultimately boosting both the model's discriminative power and training stability. Comprehensive evaluations across various baseline architectures and standard benchmarks reveal that the proposed method substantially boosts the retrieval accuracy of existing models, yielding superior performance even under highly demanding conditions.

