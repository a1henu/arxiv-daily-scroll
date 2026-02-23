---
layout: default
title: UAOR: Uncertainty-aware Observation Reinjection for Vision-Language-Action Models
---

# UAOR: Uncertainty-aware Observation Reinjection for Vision-Language-Action Models
**arXiv**：[2602.18020v1](https://arxiv.org/abs/2602.18020) · [PDF](https://arxiv.org/pdf/2602.18020.pdf)  
**作者**：Jiabing Yang, Yixiang Chen, Yuan Xu, Peiyan Li, Xiangnan Wu, Zichen Wen, Bowen Fang, Tao Yu, Zhengbo Zhang, Yingda Li, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  

**一句话要点**：提出不确定性感知观测重注入模块，以增强视觉-语言-动作模型在推理时的观测关注度。

**关键词**：视觉-语言-动作模型, 不确定性感知, 观测重注入, 前馈网络, 机器人操作, 训练免费模块

## 3 点简述
- 现有VLA模型依赖额外观测线索或模块提升性能，但需高成本数据收集和训练。
- UAOR利用语言模型前馈网络作为记忆，在不确定性高时通过注意力检索重注入观测信息。
- 实验表明UAOR能一致提升多种VLA模型性能，无需额外训练或模块，开销极小。

## 摘要（原文）

> Vision-Language-Action (VLA) models leverage pretrained Vision-Language Models (VLMs) as backbones to map images and instructions to actions, demonstrating remarkable potential for generalizable robotic manipulation. To enhance performance, existing methods often incorporate extra observation cues (e.g., depth maps, point clouds) or auxiliary modules (e.g., object detectors, encoders) to enable more precise and reliable task execution, yet these typically require costly data collection and additional training. Inspired by the finding that Feed-Forward Network (FFN) in language models can act as "key-value memory", we propose Uncertainty-aware Observation Reinjection (UAOR), an effective, training-free and plug-and-play module for VLA models. Specifically, when the current language model layer exhibits high uncertainty, measured by Action Entropy, it reinjects key observation information into the next layer's Feed-Forward Network (FFN) through attention retrieval. This mechanism helps VLAs better attend to observations during inference, enabling more confident and faithful action generation. Comprehensive experiments show that our method consistently improves diverse VLA models across simulation and real-world tasks with minimal overhead. Notably, UAOR eliminates the need for additional observation cues or modules, making it a versatile and practical plug-in for existing VLA pipelines. The project page is at https://uaor.jiabingyang.cn.

