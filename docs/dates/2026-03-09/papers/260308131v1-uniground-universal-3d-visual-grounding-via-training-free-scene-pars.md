---
layout: default
title: UniGround: Universal 3D Visual Grounding via Training-Free Scene Parsing
---

# UniGround: Universal 3D Visual Grounding via Training-Free Scene Parsing
**arXiv**：[2603.08131v1](https://arxiv.org/abs/2603.08131) · [PDF](https://arxiv.org/pdf/2603.08131.pdf)  
**作者**：Jiaxi Zhang, Yunheng Wang, Wei Lu, Taowen Wang, Weisheng Xu, Shuning Zhang, Yixiao Feng, Yuetong Fang, Renjing Xu  

**一句话要点**：提出UniGround通过免训练场景解析实现通用3D视觉定位

**关键词**：3D视觉定位, 免训练推理, 场景解析, 零-shot学习, 多视图语义编码, 空间关系理解

## 3 点简述
- 核心问题：现有3D视觉定位依赖预训练模型，泛化能力受限，难以处理未见空间关系和分布外场景。
- 方法要点：采用两阶段免训练推理，包括全局候选过滤和局部精确定位，结合3D拓扑与多视图语义编码。
- 实验或效果：在ScanRefer和EmbodiedScan基准上实现零-shot最优性能，并在真实环境中展示鲁棒泛化能力。

## 摘要（原文）

> Understanding and localizing objects in complex 3D environments from natural language descriptions, known as 3D Visual Grounding (3DVG), is a foundational challenge in embodied AI, with broad implications for robotics, augmented reality, and human-machine interaction. Large-scale pre-trained foundation models have driven significant progress on this front, enabling open-vocabulary 3DVG that allows systems to locate arbitrary objects in a given scene. However, their reliance on pre-trained models constrains 3D perception and reasoning within the inherited knowledge boundaries, resulting in limited generalization to unseen spatial relationships and poor robustness to out-of-distribution scenes. In this paper, we replace this constrained perception with training-free visual and geometric reasoning, thereby unlocking open-world 3DVG that enables the localization of any object in any scene beyond the training data. Specifically, the proposed UniGround operates in two stages: a Global Candidate Filtering stage that constructs scene candidates through training-free 3D topology and multi-view semantic encoding, and a Local Precision Grounding stage that leverages multi-scale visual prompting and structured reasoning to precisely identify the target object. Experiments on ScanRefer and EmbodiedScan show that UniGround achieves 46.1\%/34.1\% Acc@0.25/0.5 on ScanRefer and 28.7\% Acc@0.25 on EmbodiedScan, establishing a new state-of-the-art among zero-shot methods on EmbodiedScan without any 3D supervision. We further evaluate UniGround in real-world environments under uncontrolled reconstruction conditions and substantial domain shift, showing training-free reasoning generalizes robustly beyond curated benchmarks.

