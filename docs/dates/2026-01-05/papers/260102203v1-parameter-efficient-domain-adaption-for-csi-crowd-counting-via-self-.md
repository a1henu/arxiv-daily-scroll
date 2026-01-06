---
layout: default
title: Parameter-Efficient Domain Adaption for CSI Crowd-Counting via Self-Supervised Learning with Adapter Modules
---

# Parameter-Efficient Domain Adaption for CSI Crowd-Counting via Self-Supervised Learning with Adapter Modules
**arXiv**：[2601.02203v1](https://arxiv.org/abs/2601.02203) · [PDF](https://arxiv.org/pdf/2601.02203.pdf)  
**作者**：Oliver Custance, Saad Khan, Simon Parkinson, Quan Z. Sheng  

**一句话要点**：提出基于自监督学习和适配器模块的参数高效域适应方法，以解决WiFi CSI人群计数中的域偏移问题。

**关键词**：WiFi CSI人群计数, 域适应, 自监督学习, 适配器模块, 参数高效微调, 物联网感知

## 3 点简述
- 核心问题：WiFi CSI人群计数模型因环境变化导致的域偏移问题，阻碍实际部署。
- 方法要点：采用两阶段框架，包括自监督对比学习预训练和轻量级适配器模块微调，学习域不变表示。
- 实验或效果：在WiFlow数据集上，无监督方法在10-shot场景中MAE为0.44，优于监督基线；在WiAR基准上达到98.8%准确率。

## 摘要（原文）

> Device-free crowd-counting using WiFi Channel State Information (CSI) is a key enabling technology for a new generation of privacy-preserving Internet of Things (IoT) applications. However, practical deployment is severely hampered by the domain shift problem, where models trained in one environment fail to generalise to another. To overcome this, we propose a novel two-stage framework centred on a CSI-ResNet-A architecture. This model is pre-trained via self-supervised contrastive learning to learn domain-invariant representations and leverages lightweight Adapter modules for highly efficient fine-tuning. The resulting event sequence is then processed by a stateful counting machine to produce a final, stable occupancy estimate. We validate our framework extensively. On our WiFlow dataset, our unsupervised approach excels in a 10-shot learning scenario, achieving a final Mean Absolute Error (MAE) of just 0.44--a task where supervised baselines fail. To formally quantify robustness, we introduce the Generalisation Index (GI), on which our model scores near-perfectly, confirming its ability to generalise. Furthermore, our framework sets a new state-of-the-art public WiAR benchmark with 98.8\% accuracy. Our ablation studies reveal the core strength of our design: adapter-based fine-tuning achieves performance within 1\% of a full fine-tune (98.84\% vs. 99.67\%) while training 97.2\% fewer parameters. Our work provides a practical and scalable solution for developing robust sensing systems ready for real-world IoT deployments.

