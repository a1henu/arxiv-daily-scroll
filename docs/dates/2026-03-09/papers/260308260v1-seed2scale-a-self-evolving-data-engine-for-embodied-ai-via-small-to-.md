---
layout: default
title: Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation
---

# Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation
**arXiv**：[2603.08260v1](https://arxiv.org/abs/2603.08260) · [PDF](https://arxiv.org/pdf/2603.08260.pdf)  
**作者**：Cong Tai, Zhaoyu Zheng, Haixu Long, Hansheng Wu, Zhengbin Long, Haodong Xiang, Rong Shi, Zhuo Cui, Shizhuang Zhang, Gang Qiu, He Wang, Ruifeng Li, Biao Liu, Zhenzhe Sun, Tao Shen  

**一句话要点**：提出Seed2Scale自演化数据引擎，通过小大模型协同与多模态评估解决具身AI数据瓶颈

**关键词**：具身AI, 自演化数据引擎, 小大模型协同, 多模态评估, 数据生成, 模型稳定性

## 3 点简述
- 现有数据生成方法存在探索限制、具身鸿沟和低信噪比问题，导致自迭代性能下降
- Seed2Scale采用小模型收集、大模型评估和目标模型学习的异构协同机制，从少量种子演示开始自演化
- 实验显示目标模型成功率稳健上升，性能提升131.2%，显著优于现有数据增强方法

## 摘要（原文）

> Existing data generation methods suffer from exploration limits, embodiment gaps, and low signal-to-noise ratios, leading to performance degradation during self-iteration. To address these challenges, we propose Seed2Scale, a self-evolving data engine that overcomes the data bottleneck through a heterogeneous synergy of "small-model collection, large-model evaluation, and target-model learning". Starting with as few as four seed demonstrations, the engine employs the lightweight Vision-Language-Action model, SuperTiny, as a dedicated collector, leveraging its strong inductive bias for robust exploration in parallel environments. Concurrently, a pre-trained Vision-Language Model is integrated as a Verifer to autonomously perform success/failure judgment and quality scoring for the massive generated trajectories. Seed2Scale effectively mitigates model collapse, ensuring the stability of the self-evolution process. Experimental results demonstrate that Seed2Scale exhibits signifcant scaling potential: as iterations progress, the success rate of the target model shows a robust upward trend, achieving a performance improvement of 131.2%. Furthermore, Seed2Scale signifcantly outperforms existing data augmentation methods, providing a scalable and cost-effective pathway for the large-scale development of Generalist Embodied AI. Project page: https://terminators2025.github.io/Seed2Scale.github.io

