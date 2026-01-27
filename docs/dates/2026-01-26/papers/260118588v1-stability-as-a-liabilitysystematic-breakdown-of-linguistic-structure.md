---
layout: default
title: Stability as a Liability:Systematic Breakdown of Linguistic Structure in LLMs
---

# Stability as a Liability:Systematic Breakdown of Linguistic Structure in LLMs
**arXiv**：[2601.18588v1](https://arxiv.org/abs/2601.18588) · [PDF](https://arxiv.org/pdf/2601.18588.pdf)  
**作者**：Xianzhe Meng, Qiangsheng Zeng, Ling Luo, Qinghan Yang, Jiarui Hao, Wenbo Wu, Qinyu Wang, Rui Yin, Lin Qi, Renzhi Lu  

**一句话要点**：揭示训练稳定性导致大语言模型生成分布退化，提出稳定性与表达性不匹配的观点。

**关键词**：大语言模型, 训练稳定性, 生成分布, KL散度, 熵减少, 优化稳定性

## 3 点简述
- 核心问题：训练稳定性可能使模型生成分布集中于有限模式，导致低熵和重复输出。
- 方法要点：通过反馈训练框架稳定内部生成统计，分析稳定参数轨迹对KL散度和熵的影响。
- 实验或效果：在不同架构和随机种子下验证了稳定训练导致生成质量下降的现象。

## 摘要（原文）

> Training stability is typically regarded as a prerequisite for reliable optimization in large language models. In this work, we analyze how stabilizing training dynamics affects the induced generation distribution. We show that under standard maximum likelihood training, stable parameter trajectories lead stationary solutions to approximately minimize the forward KL divergence to the empirical distribution, while implicitly reducing generative entropy. As a consequence, the learned model can concentrate probability mass on a limited subset of empirical modes, exhibiting systematic degeneration despite smooth loss convergence. We empirically validate this effect using a controlled feedback-based training framework that stabilizes internal generation statistics, observing consistent low-entropy outputs and repetitive behavior across architectures and random seeds. It indicates that optimization stability and generative expressivity are not inherently aligned, and that stability alone is an insufficient indicator of generative quality.

