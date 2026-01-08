---
layout: default
title: Towards Real-world Lens Active Alignment with Unlabeled Data via Domain Adaptation
---

# Towards Real-world Lens Active Alignment with Unlabeled Data via Domain Adaptation
**arXiv**：[2601.03718v1](https://arxiv.org/abs/2601.03718) · [PDF](https://arxiv.org/pdf/2601.03718.pdf)  
**作者**：Wenyong Lia, Qi Jiang, Weijian Hu, Kailun Yang, Zhanjun Zhang, Wenjun Tian, Kaiwei Wang, Jian Bai  

**一句话要点**：提出域自适应主动对准方法，利用无标签真实数据提升光学系统模拟训练模型的现实性能。

**关键词**：主动对准, 域自适应, 自监督学习, 光学系统组装, 数字孪生, 对抗训练

## 3 点简述
- 核心问题：模拟与真实图像间的域差距限制主动对准模型在现实中的泛化能力。
- 方法要点：结合自回归域变换生成器和对抗特征对齐，通过自监督学习提取域不变特征。
- 实验或效果：在两种镜头类型上，准确率比纯模拟基线提升46%，接近精确标注真实数据性能，减少数据收集时间98.7%。

## 摘要（原文）

> Active Alignment (AA) is a key technology for the large-scale automated assembly of high-precision optical systems. Compared with labor-intensive per-model on-device calibration, a digital-twin pipeline built on optical simulation offers a substantial advantage in generating large-scale labeled data. However, complex imaging conditions induce a domain gap between simulation and real-world images, limiting the generalization of simulation-trained models. To address this, we propose augmenting a simulation baseline with minimal unlabeled real-world images captured at random misalignment positions, mitigating the gap from a domain adaptation perspective. We introduce Domain Adaptive Active Alignment (DA3), which utilizes an autoregressive domain transformation generator and an adversarial-based feature alignment strategy to distill real-world domain information via self-supervised learning. This enables the extraction of domain-invariant image degradation features to facilitate robust misalignment prediction. Experiments on two lens types reveal that DA3 improves accuracy by 46% over a purely simulation pipeline. Notably, it approaches the performance achieved with precisely labeled real-world data collected on 3 lens samples, while reducing on-device data collection time by 98.7%. The results demonstrate that domain adaptation effectively endows simulation-trained models with robust real-world performance, validating the digital-twin pipeline as a practical solution to significantly enhance the efficiency of large-scale optical assembly.

