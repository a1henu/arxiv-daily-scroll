---
layout: default
title: BRIDGE the Gap: Mitigating Bias Amplification in Automated Scoring of English Language Learners via Inter-group Data Augmentation
---

# BRIDGE the Gap: Mitigating Bias Amplification in Automated Scoring of English Language Learners via Inter-group Data Augmentation
**arXiv**：[2602.23580v1](https://arxiv.org/abs/2602.23580) · [PDF](https://arxiv.org/pdf/2602.23580.pdf)  
**作者**：Yun Wang, Xuansheng Wu, Jingyuan Huang, Lei Liu, Xiaoming Zhai, Ninghao Liu  

**一句话要点**：提出BRIDGE框架，通过组间数据增强缓解英语学习者自动评分中的偏见放大问题。

**关键词**：自动评分系统, 偏见放大, 数据增强, 公平性评估, 英语学习者

## 3 点简述
- 核心问题：自动评分系统因少数样本稀缺，放大英语学习者与非学习者间的预测差距，损害公平性。
- 方法要点：BRIDGE合成高评分英语学习者样本，将非学习者的知识内容融入其真实语言模式，并引入鉴别器确保质量。
- 实验或效果：在加州科学测试数据集上，有效减少高评分英语学习者的预测偏见，同时保持整体评分性能。

## 摘要（原文）

> In the field of educational assessment, automated scoring systems increasingly rely on deep learning and large language models (LLMs). However, these systems face significant risks of bias amplification, where model prediction gaps between student groups become larger than those observed in training data. This issue is especially severe for underrepresented groups such as English Language Learners (ELLs), as models may inherit and further magnify existing disparities in the data. We identify that this issue is closely tied to representation bias: the scarcity of minority (high-scoring ELL) samples makes models trained with empirical risk minimization favor majority (non-ELL) linguistic patterns. Consequently, models tend to under-predict ELL students who even demonstrate comparable domain knowledge but use different linguistic patterns, thereby undermining the fairness of automated scoring outcomes. To mitigate this, we propose BRIDGE, a Bias-Reducing Inter-group Data GEneration framework designed for low-resource assessment settings. Instead of relying on the limited minority samples, BRIDGE synthesizes high-scoring ELL samples by "pasting" construct-relevant (i.e., rubric-aligned knowledge and evidence) content from abundant high-scoring non-ELL samples into authentic ELL linguistic patterns. We further introduce a discriminator model to ensure the quality of synthetic samples. Experiments on California Science Test (CAST) datasets demonstrate that BRIDGE effectively reduces prediction bias for high-scoring ELL students while maintaining overall scoring performance. Notably, our method achieves fairness gains comparable to using additional real human data, offering a cost-effective solution for ensuring equitable scoring in large-scale assessments.

