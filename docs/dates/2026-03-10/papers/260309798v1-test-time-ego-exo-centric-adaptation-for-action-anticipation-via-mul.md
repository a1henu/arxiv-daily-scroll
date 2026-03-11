---
layout: default
title: Test-time Ego-Exo-centric Adaptation for Action Anticipation via Multi-Label Prototype Growing and Dual-Clue Consistency
---

# Test-time Ego-Exo-centric Adaptation for Action Anticipation via Multi-Label Prototype Growing and Dual-Clue Consistency
**arXiv**：[2603.09798v1](https://arxiv.org/abs/2603.09798) · [PDF](https://arxiv.org/pdf/2603.09798.pdf)  
**作者**：Zhaofeng Shi, Heqian Qiu, Lanxiao Wang, Qingbo Wu, Fanman Meng, Lili Pan, Hongliang Li  

**一句话要点**：提出DCPGN方法，通过多标签原型增长和双线索一致性实现测试时自他视角自适应以预测动作

**关键词**：测试时自适应, 动作预测, 自他视角转换, 多标签学习, 原型增长, 双线索一致性

## 3 点简述
- 核心问题：现有自他视角自适应方法依赖目标视角训练数据，增加计算和数据收集成本，测试时自适应面临多动作候选和时空视角差异挑战。
- 方法要点：设计多标签原型增长模块平衡多正类，结合双线索一致性模块利用文本和视觉线索构建一致性，在线调整模型以适应目标视角。
- 实验或效果：在EgoMe-anti和EgoExoLearn基准上验证，性能显著优于相关先进方法，代码已开源。

## 摘要（原文）

> Efficient adaptation between Egocentric (Ego) and Exocentric (Exo) views is crucial for applications such as human-robot cooperation. However, the success of most existing Ego-Exo adaptation methods relies heavily on target-view data for training, thereby increasing computational and data collection costs. In this paper, we make the first exploration of a Test-time Ego-Exo Adaptation for Action Anticipation (TE$^{2}$A$^{3}$) task, which aims to adjust the source-view-trained model online during test time to anticipate target-view actions. It is challenging for existing Test-Time Adaptation (TTA) methods to address this task due to the multi-action candidates and significant temporal-spatial inter-view gap. Hence, we propose a novel Dual-Clue enhanced Prototype Growing Network (DCPGN), which accumulates multi-label knowledge and integrates cross-modality clues for effective test-time Ego-Exo adaptation and action anticipation. Specifically, we propose a Multi-Label Prototype Growing Module (ML-PGM) to balance multiple positive classes via multi-label assignment and confidence-based reweighting for class-wise memory banks, which are updated by an entropy priority queue strategy. Then, the Dual-Clue Consistency Module (DCCM) introduces a lightweight narrator to generate textual clues indicating action progressions, which complement the visual clues containing various objects. Moreover, we constrain the inferred textual and visual logits to construct dual-clue consistency for temporally and spatially bridging Ego and Exo views. Extensive experiments on the newly proposed EgoMe-anti and the existing EgoExoLearn benchmarks show the effectiveness of our method, which outperforms related state-of-the-art methods by a large margin. Code is available at \href{https://github.com/ZhaofengSHI/DCPGN}{https://github.com/ZhaofengSHI/DCPGN}.

