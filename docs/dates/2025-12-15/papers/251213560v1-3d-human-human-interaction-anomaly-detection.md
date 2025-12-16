---
layout: default
title: 3D Human-Human Interaction Anomaly Detection
---

# 3D Human-Human Interaction Anomaly Detection
**arXiv**：[2512.13560v1](https://arxiv.org/abs/2512.13560) · [PDF](https://arxiv.org/pdf/2512.13560.pdf)  
**作者**：Shun Maeda, Chunzhi Gu, Koichiro Kamide, Katsuya Hotta, Shangce Gao, Chao Zhang  

**一句话要点**：提出IADNet以解决3D人-人交互异常检测任务，通过共享时间注意力和距离编码提升准确性。

**关键词**：3D人-人交互异常检测, 时间注意力共享, 距离关系编码, 正常化流, 协作运动分析

## 3 点简述
- 核心问题：现有单人异常检测模型难以捕捉人-人交互的复杂不对称动态，导致检测准确性低。
- 方法要点：设计TASM共享运动嵌入以同步协作相关性，并引入DREM编码空间配置以反映社交线索。
- 实验或效果：在基准测试中，IADNet优于现有以人为中心的异常检测基线，验证了其有效性。

## 摘要（原文）

> Human-centric anomaly detection (AD) has been primarily studied to specify anomalous behaviors in a single person. However, as humans by nature tend to act in a collaborative manner, behavioral anomalies can also arise from human-human interactions. Detecting such anomalies using existing single-person AD models is prone to low accuracy, as these approaches are typically not designed to capture the complex and asymmetric dynamics of interactions. In this paper, we introduce a novel task, Human-Human Interaction Anomaly Detection (H2IAD), which aims to identify anomalous interactive behaviors within collaborative 3D human actions. To address H2IAD, we then propose Interaction Anomaly Detection Network (IADNet), which is formalized with a Temporal Attention Sharing Module (TASM). Specifically, in designing TASM, we share the encoded motion embeddings across both people such that collaborative motion correlations can be effectively synchronized. Moreover, we notice that in addition to temporal dynamics, human interactions are also characterized by spatial configurations between two people. We thus introduce a Distance-Based Relational Encoding Module (DREM) to better reflect social cues in H2IAD. The normalizing flow is eventually employed for anomaly scoring. Extensive experiments on human-human motion benchmarks demonstrate that IADNet outperforms existing Human-centric AD baselines in H2IAD.

