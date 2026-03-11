---
layout: default
title: Progressive Representation Learning for Multimodal Sentiment Analysis with Incomplete Modalities
---

# Progressive Representation Learning for Multimodal Sentiment Analysis with Incomplete Modalities
**arXiv**：[2603.09111v1](https://arxiv.org/abs/2603.09111) · [PDF](https://arxiv.org/pdf/2603.09111.pdf)  
**作者**：Jindi Bao, Jianjun Qian, Mengkai Yan, Jian Yang  

**一句话要点**：提出PRLF框架以解决多模态情感分析中模态缺失导致的特征不对齐问题

**关键词**：多模态情感分析, 模态缺失, 表示学习, 自适应可靠性估计, 渐进式交互

## 3 点简述
- 核心问题：现实应用中模态缺失导致特征不对齐，直接融合可能扭曲完整模态表示
- 方法要点：引入AMRE动态评估模态可靠性，ProgInteract模块迭代对齐模态以增强一致性
- 实验或效果：在CMU-MOSI等数据集上优于现有方法，验证了鲁棒性和泛化能力

## 摘要（原文）

> Multimodal Sentiment Analysis (MSA) seeks to infer human emotions by integrating textual, acoustic, and visual cues. However, existing approaches often rely on all modalities are completeness, whereas real-world applications frequently encounter noise, hardware failures, or privacy restrictions that result in missing modalities. There exists a significant feature misalignment between incomplete and complete modalities, and directly fusing them may even distort the well-learned representations of the intact modalities. To this end, we propose PRLF, a Progressive Representation Learning Framework designed for MSA under uncertain missing-modality conditions. PRLF introduces an Adaptive Modality Reliability Estimator (AMRE), which dynamically quantifies the reliability of each modality using recognition confidence and Fisher information to determine the dominant modality. In addition, the Progressive Interaction (ProgInteract) module iteratively aligns the other modalities with the dominant one, thereby enhancing cross-modal consistency while suppressing noise. Extensive experiments on CMU-MOSI, CMU-MOSEI, and SIMS verify that PRLF outperforms state-of-the-art methods across both inter- and intra-modality missing scenarios, demonstrating its robustness and generalization capability.

