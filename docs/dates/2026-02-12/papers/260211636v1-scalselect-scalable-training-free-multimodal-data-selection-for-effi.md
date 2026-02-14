---
layout: default
title: ScalSelect: Scalable Training-Free Multimodal Data Selection for Efficient Visual Instruction Tuning
---

# ScalSelect: Scalable Training-Free Multimodal Data Selection for Efficient Visual Instruction Tuning
**arXiv**：[2602.11636v1](https://arxiv.org/abs/2602.11636) · [PDF](https://arxiv.org/pdf/2602.11636.pdf)  
**作者**：Changti Wu, Jiahuai Mao, Yuzhuo Miao, Shijie Lian, Bin Yu, Xiaopeng Lin, Cong Huang, Lei Zhang, Kai Chen  

**一句话要点**：提出ScalSelect以解决视觉指令调优中大规模数据选择的高效性问题

**关键词**：视觉指令调优, 数据选择, 无训练方法, 线性复杂度, 多模态学习, 训练效率

## 3 点简述
- 核心问题：大规模视觉指令调优数据冗余导致训练成本高，现有方法依赖训练或计算复杂度高
- 方法要点：通过提取指令相关视觉特征并近似数据集主导子空间，实现线性时间复杂度的无训练数据选择
- 实验或效果：在多种模型和数据集上，仅用16%数据达到全数据训练97.5%以上性能，部分场景超越全数据训练

## 摘要（原文）

> Large-scale Visual Instruction Tuning (VIT) has become a key paradigm for advancing the performance of vision-language models (VLMs) across various multimodal tasks. However, training on the large-scale datasets is computationally expensive and inefficient due to redundancy in the data, which motivates the need for multimodal data selection to improve training efficiency. Existing data selection methods for VIT either require costly training or gradient computation. Training-free alternatives often depend on proxy models or datasets, instruction-agnostic representations, and pairwise similarity with quadratic complexity, limiting scalability and representation fidelity. In this work, we propose ScalSelect, a scalable training-free multimodal data selection method with linear-time complexity with respect to the number of samples, eliminating the need for external models or auxiliary datasets. ScalSelect first constructs sample representations by extracting visual features most attended by instruction tokens in the target VLM, capturing instruction-relevant information. It then identifies samples whose representations best approximate the dominant subspace of the full dataset representations, enabling scalable importance scoring without pairwise comparisons. Extensive experiments across multiple VLMs, datasets, and selection budgets demonstrate that ScalSelect achieves over 97.5% of the performance of training on the full dataset using only 16% of the data, and even outperforms full-data training in some settings. The code is available at \href{https://github.com/ChangtiWu/ScalSelect}{ScalSelect}.

