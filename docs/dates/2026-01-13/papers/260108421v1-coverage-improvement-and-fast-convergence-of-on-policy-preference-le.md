---
layout: default
title: Coverage Improvement and Fast Convergence of On-policy Preference Learning
---

# Coverage Improvement and Fast Convergence of On-policy Preference Learning
**arXiv**：[2601.08421v1](https://arxiv.org/abs/2601.08421) · [PDF](https://arxiv.org/pdf/2601.08421.pdf)  
**作者**：Juno Kim, Jihun Yun, Jason D. Lee, Kwang-Sung Jun  

**一句话要点**：提出覆盖改进原理与混合采样器，以加速在线策略偏好学习的收敛

**关键词**：偏好学习, 在线策略优化, 覆盖改进, 收敛分析, 奖励蒸馏, 上下文赌博机

## 3 点简述
- 分析在线策略偏好学习中采样策略覆盖的演化，解释在线方法优于离线的理论原因
- 在上下文赌博机设置下，证明在线DPO在足够批量大小时指数收敛，而离线方法收敛较慢
- 提出基于优先G-最优设计的混合采样器，移除覆盖依赖，实现两轮收敛，实验验证性能提升

## 摘要（原文）

> Online on-policy preference learning algorithms for language model alignment such as online direct policy optimization (DPO) can significantly outperform their offline counterparts. We provide a theoretical explanation for this phenomenon by analyzing how the sampling policy's coverage evolves throughout on-policy training. We propose and rigorously justify the \emph{coverage improvement principle}: with sufficient batch size, each update moves into a region around the target where coverage is uniformly better, making subsequent data increasingly informative and enabling rapid convergence. In the contextual bandit setting with Bradley-Terry preferences and linear softmax policy class, we show that on-policy DPO converges exponentially in the number of iterations for batch size exceeding a generalized coverage threshold. In contrast, any learner restricted to offline samples from the initial policy suffers a slower minimax rate, leading to a sharp separation in total sample complexity. Motivated by this analysis, we further propose a simple hybrid sampler based on a novel \emph{preferential} G-optimal design, which removes dependence on coverage and guarantees convergence in just two rounds. Finally, we develop principled on-policy schemes for reward distillation in the general function class setting, and show faster noiseless rates under an alternative deviation-based notion of coverage. Experimentally, we confirm that on-policy DPO and our proposed reward distillation algorithms outperform their off-policy counterparts and enjoy stable, monotonic performance gains across iterations.

