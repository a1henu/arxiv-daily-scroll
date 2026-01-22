---
layout: default
title: SimD3: A Synthetic drone Dataset with Payload and Bird Distractor Modeling for Robust Detection
---

# SimD3: A Synthetic drone Dataset with Payload and Bird Distractor Modeling for Robust Detection
**arXiv**：[2601.14742v1](https://arxiv.org/abs/2601.14742) · [PDF](https://arxiv.org/pdf/2601.14742.pdf)  
**作者**：Ami Pandat, Kanyala Muvva, Punna Rajasekhar, Gopika Vinod, Rohit Shukla  

**一句话要点**：提出SimD3合成数据集以解决复杂空中环境下无人机检测的鲁棒性问题

**关键词**：合成数据集, 无人机检测, 鲁棒检测, YOLOv5, 注意力机制, 跨域评估

## 3 点简述
- 核心问题：无人机检测因真实数据有限、外观多变及鸟类等视觉相似干扰物而困难
- 方法要点：SimD3数据集建模异质载荷无人机和多种鸟类干扰物，使用Unreal Engine 5生成高保真合成数据
- 实验或效果：在YOLOv5框架中评估，Yolov5m+C3b变体在域内和跨数据集评估中优于基线，提升检测鲁棒性

## 摘要（原文）

> Reliable drone detection is challenging due to limited annotated real-world data, large appearance variability, and the presence of visually similar distractors such as birds. To address these challenges, this paper introduces SimD3, a large-scale high-fidelity synthetic dataset designed for robust drone detection in complex aerial environments. Unlike existing synthetic drone datasets, SimD3 explicitly models drones with heterogeneous payloads, incorporates multiple bird species as realistic distractors, and leverages diverse Unreal Engine 5 environments with controlled weather, lighting, and flight trajectories captured using a 360 six-camera rig. Using SimD3, we conduct an extensive experimental evaluation within the YOLOv5 detection framework, including an attention-enhanced variant termed Yolov5m+C3b, where standard bottleneck-based C3 blocks are replaced with C3b modules. Models are evaluated on synthetic data, combined synthetic and real data, and multiple unseen real-world benchmarks to assess robustness and generalization. Experimental results show that SimD3 provides effective supervision for small-object drone detection and that Yolov5m+C3b consistently outperforms the baseline across in-domain and cross-dataset evaluations. These findings highlight the utility of SimD3 for training and benchmarking robust drone detection models under diverse and challenging conditions.

