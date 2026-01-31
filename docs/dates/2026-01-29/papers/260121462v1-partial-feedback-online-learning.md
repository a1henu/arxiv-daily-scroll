---
layout: default
title: Partial Feedback Online Learning
---

# Partial Feedback Online Learning
**arXiv**：[2601.21462v1](https://arxiv.org/abs/2601.21462) · [PDF](https://arxiv.org/pdf/2601.21462.pdf)  
**作者**：Shihao Shao, Cong Fang, Zhouchen Lin, Dacheng Tao  

**一句话要点**：提出部分反馈在线学习模型，刻画语言生成等场景，并给出最小化遗憾的完整理论分析。

**关键词**：部分反馈在线学习, 最小化遗憾, 集合值学习, 可学习性理论, 语言生成, 复杂度度量

## 3 点简述
- 研究部分反馈在线学习，其中每个实例有多个正确标签，但每轮只观察一个，预测在正确集中即算正确。
- 引入部分反馈Littlestone维度（PFLdim）和部分反馈测量粉碎维度（PMSdim），精确刻画确定性和随机学习者的可学习性与最小化遗憾。
- 识别确定性与随机可学习性不可分离的条件，并扩展到集合值在线学习，解决开放问题，展示与较弱变体的尖锐分离。

## 摘要（原文）

> We study partial-feedback online learning, where each instance admits a set of correct labels, but the learner only observes one correct label per round; any prediction within the correct set is counted as correct. This model captures settings such as language generation, where multiple responses may be valid but data provide only a single reference. We give a near-complete characterization of minimax regret for both deterministic and randomized learners in the set-realizable regime, i.e., in the regime where sublinear regret is generally attainable. For deterministic learners, we introduce the Partial-Feedback Littlestone dimension (PFLdim) and show it precisely governs learnability and minimax regret; technically, PFLdim cannot be defined via the standard version space, requiring a new collection version space viewpoint and an auxiliary dimension used only in the proof. We further develop the Partial-Feedback Measure Shattering dimension (PMSdim) to obtain tight bounds for randomized learners. We identify broad conditions ensuring inseparability between deterministic and randomized learnability (e.g., finite Helly number or nested-inclusion label structure), and extend the argument to set-valued online learning, resolving an open question of Raman et al. [2024b]. Finally, we show a sharp separation from weaker realistic and agnostic variants: outside set realizability, the problem can become information-theoretically intractable, with linear regret possible even for $\|H\|=2$. This highlights the need for fundamentally new, noise-sensitive complexity measures to meaningfully characterize learnability beyond set realizability.

