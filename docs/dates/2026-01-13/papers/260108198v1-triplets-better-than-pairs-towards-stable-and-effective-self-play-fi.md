---
layout: default
title: Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs
---

# Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs
**arXiv**：[2601.08198v1](https://arxiv.org/abs/2601.08198) · [PDF](https://arxiv.org/pdf/2601.08198.pdf)  
**作者**：Yibo Wang, Hai-Long Sun, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang  

**一句话要点**：提出T-SPIN方法以解决自对弈微调中的优化不稳定和训练生成不一致问题

**关键词**：自对弈微调, 三元组学习, 大语言模型, 优化稳定性, 熵约束

## 3 点简述
- SPIN方法在迭代中当前奖励优势可能消失，导致优化不稳定
- T-SPIN引入历史优势和熵约束，稳定优化并消除训练生成差异
- 实验显示T-SPIN性能优于SPIN，在少量标注数据下效果显著

## 摘要（原文）

> Recently, self-play fine-tuning (SPIN) has been proposed to adapt large language models to downstream applications with scarce expert-annotated data, by iteratively generating synthetic responses from the model itself. However, SPIN is designed to optimize the current reward advantages of annotated responses over synthetic responses at hand, which may gradually vanish during iterations, leading to unstable optimization. Moreover, the utilization of reference policy induces a misalignment issue between the reward formulation for training and the metric for generation. To address these limitations, we propose a novel Triplet-based Self-Play fIne-tuNing (T-SPIN) method that integrates two key designs. First, beyond current advantages, T-SPIN additionally incorporates historical advantages between iteratively generated responses and proto-synthetic responses produced by the initial policy. Even if the current advantages diminish, historical advantages remain effective, stabilizing the overall optimization. Second, T-SPIN introduces the entropy constraint into the self-play framework, which is theoretically justified to support reference-free fine-tuning, eliminating the training-generation discrepancy. Empirical results on various tasks demonstrate not only the superior performance of T-SPIN over SPIN, but also its stable evolution during iterations. Remarkably, compared to supervised fine-tuning, T-SPIN achieves comparable or even better performance with only 25% samples, highlighting its effectiveness when faced with scarce annotated data.

