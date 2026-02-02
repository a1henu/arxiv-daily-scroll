---
layout: default
title: Statistical Estimation of Adversarial Risk in Large Language Models under Best-of-N Sampling
---

# Statistical Estimation of Adversarial Risk in Large Language Models under Best-of-N Sampling
**arXiv**：[2601.22636v1](https://arxiv.org/abs/2601.22636) · [PDF](https://arxiv.org/pdf/2601.22636.pdf)  
**作者**：Mingqian Feng, Xiaodong Liu, Weiwei Yang, Chenliang Xu, Christopher White, Jianfeng Gao  

**一句话要点**：提出SABER方法以评估大语言模型在最佳N采样下的对抗风险

**关键词**：大语言模型安全, 对抗风险估计, 最佳N采样, Beta分布建模, 缩放定律, 安全评估方法

## 3 点简述
- 核心问题：现有评估低估大规模并行采样下的对抗风险，缺乏预测方法
- 方法要点：使用Beta分布建模样本级成功概率，推导解析缩放定律进行外推
- 实验或效果：仅用100样本预测1000样本攻击成功率，误差降低86.2%

## 摘要（原文）

> Large Language Models (LLMs) are typically evaluated for safety under single-shot or low-budget adversarial prompting, which underestimates real-world risk. In practice, attackers can exploit large-scale parallel sampling to repeatedly probe a model until a harmful response is produced. While recent work shows that attack success increases with repeated sampling, principled methods for predicting large-scale adversarial risk remain limited. We propose a scaling-aware Best-of-N estimation of risk, SABER, for modeling jailbreak vulnerability under Best-of-N sampling. We model sample-level success probabilities using a Beta distribution, the conjugate prior of the Bernoulli distribution, and derive an analytic scaling law that enables reliable extrapolation of large-N attack success rates from small-budget measurements. Using only n=100 samples, our anchored estimator predicts ASR@1000 with a mean absolute error of 1.66, compared to 12.04 for the baseline, which is an 86.2% reduction in estimation error. Our results reveal heterogeneous risk scaling profiles and show that models appearing robust under standard evaluation can experience rapid nonlinear risk amplification under parallel adversarial pressure. This work provides a low-cost, scalable methodology for realistic LLM safety assessment. We will release our code and evaluation scripts upon publication to future research.

