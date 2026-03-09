---
layout: default
title: NOVA: Next-step Open-Vocabulary Autoregression for 3D Multi-Object Tracking in Autonomous Driving
---

# NOVA: Next-step Open-Vocabulary Autoregression for 3D Multi-Object Tracking in Autonomous Driving
**arXiv**：[2603.06254v1](https://arxiv.org/abs/2603.06254) · [PDF](https://arxiv.org/pdf/2603.06254.pdf)  
**作者**：Kai Luo, Xu Wang, Rui Fan, Kailun Yang  

**一句话要点**：提出NOVA范式，通过生成式时空语义建模解决自动驾驶中3D多目标跟踪的开放词汇泛化问题。

**关键词**：3D多目标跟踪, 开放词汇泛化, 自回归建模, 时空语义序列, 自动驾驶感知

## 3 点简述
- 核心问题：现有3D多目标跟踪方法受限于闭集假设和语义盲启发式，难以泛化到未知目标。
- 方法要点：将3D轨迹重构为结构化时空语义序列，利用大语言模型的自回归能力进行下一步序列补全。
- 实验或效果：在nuScenes等数据集上验证，NOVA在Novel类别上AMOTA达22.41%，相比基线提升20.21%。

## 摘要（原文）

> Generalizing across unknown targets is critical for open-world perception, yet existing 3D Multi-Object Tracking (3D MOT) pipelines remain limited by closed-set assumptions and ``semantic-blind'' heuristics. To address this, we propose Next-step Open-Vocabulary Autoregression (NOVA), an innovative paradigm that shifts 3D tracking from traditional fragmented distance-based matching toward generative spatio-temporal semantic modeling. NOVA reformulates 3D trajectories as structured spatio-temporal semantic sequences, enabling the simultaneous encoding of physical motion continuity and deep linguistic priors. By leveraging the autoregressive capabilities of Large Language Models (LLMs), we transform the tracking task into a principled process of next-step sequence completion. This mechanism allows the model to explicitly utilize the hierarchical structure of language space to resolve fine-grained semantic ambiguities and maintain identity consistency across complex long-range sequences through high-level commonsense reasoning. Extensive experiments on nuScenes, V2X-Seq-SPD, and KITTI demonstrate the superior performance of NOVA. Notably, on the nuScenes dataset, NOVA achieves an AMOTA of 22.41% for Novel categories, yielding a significant 20.21% absolute improvement over the baseline. These gains are realized through a compact 0.5B autoregressive model. Code will be available at https://github.com/xifen523/NOVA.

