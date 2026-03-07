---
layout: default
title: MI-DETR: A Strong Baseline for Moving Infrared Small Target Detection with Bio-Inspired Motion Integration
---

# MI-DETR: A Strong Baseline for Moving Infrared Small Target Detection with Bio-Inspired Motion Integration
**arXiv**：[2603.05071v1](https://arxiv.org/abs/2603.05071) · [PDF](https://arxiv.org/pdf/2603.05071.pdf)  
**作者**：Nian Liu, Jin Gao, Shubo Lin, Yutong Kou, Sikui Zhang, Fudong Ge, Zhiqiang Pu, Liang Li, Gang Wang, Yizheng Wang, Weiming Hu  

**一句话要点**：提出MI-DETR，通过生物启发式运动集成解决红外小目标检测中背景复杂与目标低对比度问题。

**关键词**：红外小目标检测, 生物启发式模型, 运动集成, 双通路检测, DETR架构, 无监督运动建模

## 3 点简述
- 核心问题：红外小目标检测中，微小低对比度目标易被复杂动态背景遮挡，传统多帧方法需额外运动监督或对齐模块。
- 方法要点：设计视网膜启发式细胞自动机生成运动图，结合双通路特征交互，无需额外运动标签或对齐操作。
- 实验或效果：在三个ISTD基准上表现优异，如IRDST-H上mAP@50达70.3%，提升显著。

## 摘要（原文）

> Infrared small target detection (ISTD) is challenging because tiny, low-contrast targets are easily obscured by complex and dynamic backgrounds. Conventional multi-frame approaches typically learn motion implicitly through deep neural networks, often requiring additional motion supervision or explicit alignment modules. We propose Motion Integration DETR (MI-DETR), a bio-inspired dual-pathway detector that processes one infrared frame per time step while explicitly modeling motion. First, a retina-inspired cellular automaton (RCA) converts raw frame sequences into a motion map defined on the same pixel grid as the appearance image, enabling parvocellular-like appearance and magnocellular-like motion pathways to be supervised by a single set of bounding boxes without extra motion labels or alignment operations. Second, a Parvocellular-Magnocellular Interconnection (PMI) Block facilitates bidirectional feature interaction between the two pathways, providing a biologically motivated intermediate interconnection mechanism. Finally, a RT-DETR decoder operates on features from the two pathways to produce detection results. Surprisingly, our proposed simple yet effective approach yields strong performance on three commonly used ISTD benchmarks. MI-DETR achieves 70.3% mAP@50 and 72.7% F1 on IRDST-H (+26.35 mAP@50 over the best multi-frame baseline), 98.0% mAP@50 on DAUB-R, and 88.3% mAP@50 on ITSDT-15K, demonstrating the effectiveness of biologically inspired motion-appearance integration. Code is available at https://github.com/nliu-25/MI-DETR.

