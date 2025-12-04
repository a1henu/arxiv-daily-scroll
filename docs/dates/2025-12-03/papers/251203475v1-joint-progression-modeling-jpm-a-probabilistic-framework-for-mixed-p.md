---
layout: default
title: Joint Progression Modeling (JPM): A Probabilistic Framework for Mixed-Pathology Progression
---

# Joint Progression Modeling (JPM): A Probabilistic Framework for Mixed-Pathology Progression
**arXiv**：[2512.03475v1](https://arxiv.org/abs/2512.03475) · [PDF](https://arxiv.org/pdf/2512.03475.pdf)  
**作者**：Hongtao Hao, Joseph L. Austerweil  

**一句话要点**：提出联合进展模型以解决神经退行性疾病中混合病理的进展建模问题

**关键词**：混合病理进展建模, 概率框架, 事件模型, 神经退行性疾病, 排序模型

## 3 点简述
- 核心问题：基于事件模型假设单一疾病，但神经退行性疾病常涉及混合病理，需建模联合进展
- 方法要点：引入概率框架，将单病轨迹视为部分排序，构建联合进展先验，研究多种变体
- 实验或效果：在合成实验中，JPM比基线模型提升约21%排序准确率，Mallows变体与基线在AD和VaD混合病理分析中更符合文献

## 摘要（原文）

> Event-based models (EBMs) infer disease progression from cross-sectional data, and standard EBMs assume a single underlying disease per individual. In contrast, mixed pathologies are common in neurodegeneration. We introduce the Joint Progression Model (JPM), a probabilistic framework that treats single-disease trajectories as partial rankings and builds a prior over joint progressions. We study several JPM variants (Pairwise, Bradley-Terry, Plackett-Luce, and Mallows) and analyze three properties: (i) calibration -- whether lower model energy predicts smaller distance to the ground truth ordering; (ii) separation -- the degree to which sampled rankings are distinguishable from random permutations; and (iii) sharpness -- the stability of sampled aggregate rankings. All variants are calibrated, and all achieve near-perfect separation; sharpness varies by variant and is well-predicted by simple features of the input partial rankings (number and length of rankings, conflict, and overlap). In synthetic experiments, JPM improves ordering accuracy by roughly 21 percent over a strong EBM baseline (SA-EBM) that treats the joint disease as a single condition. Finally, using NACC, we find that the Mallows variant of JPM and the baseline model (SA-EBM) have results that are more consistent with prior literature on the possible disease progression of the mixed pathology of AD and VaD.

