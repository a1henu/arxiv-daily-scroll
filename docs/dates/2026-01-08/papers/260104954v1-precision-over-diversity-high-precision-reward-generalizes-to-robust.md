---
layout: default
title: Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following
---

# Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following
**arXiv**：[2601.04954v1](https://arxiv.org/abs/2601.04954) · [PDF](https://arxiv.org/pdf/2601.04954.pdf)  
**作者**：Yirong Zeng, Yufei Liu, Xiao Ding, Yutai Hou, Yuxian Wang, Haonan Song, Wu Ning, Dandan Tu, Qixun Zhang, Bibo Cai, Yuxiang He, Ting Liu  

**一句话要点**：提出基于高精度奖励的数据中心化精炼策略，以提升指令跟随任务的鲁棒性。

**关键词**：指令跟随, 奖励精度, 强化学习, 数据精炼, 泛化能力

## 3 点简述
- 挑战传统观点，发现仅使用硬约束训练模型优于混合数据集，奖励精度是关键驱动因素。
- 分析显示LLM法官在检测错误响应时召回率低，导致奖励黑客问题，削弱多样性益处。
- 提出优先奖励精度的策略，在五个基准上性能提升13.4%，训练时间减少58%，保持强泛化能力。

## 摘要（原文）

> A central belief in scaling reinforcement learning with verifiable rewards for instruction following (IF) tasks is that, a diverse mixture of verifiable hard and unverifiable soft constraints is essential for generalizing to unseen instructions. In this work, we challenge this prevailing consensus through a systematic empirical investigation. Counter-intuitively, we find that models trained on hard-only constraints consistently outperform those trained on mixed datasets. Extensive experiments reveal that reward precision, rather than constraint diversity, is the primary driver of effective alignment. The LLM judge suffers from a low recall rate in detecting false response, which leads to severe reward hacking, thereby undermining the benefits of diversity. Furthermore, analysis of the attention mechanism reveals that high-precision rewards develop a transferable meta-skill for IF. Motivated by these insights, we propose a simple yet effective data-centric refinement strategy that prioritizes reward precision. Evaluated on five benchmarks, our approach outperforms competitive baselines by 13.4\% in performance while achieving a 58\% reduction in training time, maintaining strong generalization beyond instruction following. Our findings advocate for a paradigm shift: moving away from the indiscriminate pursuit of data diversity toward high-precision rewards.

