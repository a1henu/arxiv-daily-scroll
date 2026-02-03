---
layout: default
title: Enhancing Automated Essay Scoring with Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training
---

# Enhancing Automated Essay Scoring with Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training
**arXiv**：[2602.01747v1](https://arxiv.org/abs/2602.01747) · [PDF](https://arxiv.org/pdf/2602.01747.pdf)  
**作者**：Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, Jin-Xia Huang  

**一句话要点**：提出两阶段微调、分数对齐和自训练三种技术，以增强有限数据和全数据场景下的自动作文评分性能。

**关键词**：自动作文评分, 两阶段微调, 分数对齐, 自训练, 低秩适应, DualBERT

## 3 点简述
- 核心问题：真实场景中标记数据极度稀缺，限制了自动作文评分系统的开发和实际应用。
- 方法要点：采用两阶段微调、分数对齐和不确定性感知自训练，基于DualBERT模型实现。
- 实验或效果：在ASAP++数据集上，集成三种技术后，在32数据设置下达到全数据性能的91.2%，分数对齐技术在全数据设置中取得先进结果。

## 摘要（原文）

> Automated Essay Scoring (AES) plays a crucial role in education by providing scalable and efficient assessment tools. However, in real-world settings, the extreme scarcity of labeled data severely limits the development and practical adoption of robust AES systems. This study proposes a novel approach to enhance AES performance in both limited-data and full-data settings by introducing three key techniques. First, we introduce a Two-Stage fine-tuning strategy that leverages low-rank adaptations to better adapt an AES model to target prompt essays. Second, we introduce a Score Alignment technique to improve consistency between predicted and true score distributions. Third, we employ uncertainty-aware self-training using unlabeled data, effectively expanding the training set with pseudo-labeled samples while mitigating label noise propagation. We implement above three key techniques on DualBERT. We conduct extensive experiments on the ASAP++ dataset. As a result, in the 32-data setting, all three key techniques improve performance, and their integration achieves 91.2% of the full-data performance trained on approximately 1,000 labeled samples. In addition, the proposed Score Alignment technique consistently improves performance in both limited-data and full-data settings: e.g., it achieves state-of-the-art results in the full-data setting when integrated into DualBERT.

