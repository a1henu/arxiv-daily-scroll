---
layout: default
title: On the Optimal Reasoning Length for RL-Trained Language Models
---

# On the Optimal Reasoning Length for RL-Trained Language Models
**arXiv**：[2602.09591v1](https://arxiv.org/abs/2602.09591) · [PDF](https://arxiv.org/pdf/2602.09591.pdf)  
**作者**：Daisuke Nohara, Taishi Nakamura, Rio Yokota  

**一句话要点**：分析强化学习训练语言模型的最优推理长度，以平衡效率与性能

**关键词**：强化学习, 推理长度, 长度控制, 计算效率, 语言模型优化

## 3 点简述
- 核心问题：强化学习提升推理但增加输出长度和计算成本，最优长度未知
- 方法要点：比较多种长度控制方法，识别长度惩罚可能阻碍推理获取
- 实验或效果：在Qwen3-1.7B和DeepSeek-R1-Distill-Qwen-1.5B上测试，发现长输出增加分散，短输出导致欠思考

## 摘要（原文）

> Reinforcement learning substantially improves reasoning in large language models, but it also tends to lengthen chain of thought outputs and increase computational cost during both training and inference. Though length control methods have been proposed, it remains unclear what the optimal output length is for balancing efficiency and performance. In this work, we compare several length control methods on two models, Qwen3-1.7B Base and DeepSeek-R1-Distill-Qwen-1.5B. Our results indicate that length penalties may hinder reasoning acquisition, while properly tuned length control can improve efficiency for models with strong prior reasoning. By extending prior work to RL trained policies, we identify two failure modes, 1) long outputs increase dispersion, and 2) short outputs lead to under-thinking.

