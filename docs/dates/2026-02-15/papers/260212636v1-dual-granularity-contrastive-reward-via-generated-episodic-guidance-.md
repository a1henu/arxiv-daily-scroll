---
layout: default
title: Dual-Granularity Contrastive Reward via Generated Episodic Guidance for Efficient Embodied RL
---

# Dual-Granularity Contrastive Reward via Generated Episodic Guidance for Efficient Embodied RL
**arXiv**：[2602.12636v1](https://arxiv.org/abs/2602.12636) · [PDF](https://arxiv.org/pdf/2602.12636.pdf)  
**作者**：Xin Liu, Yixuan Li, Yuhui Chen, Yuxing Qin, Haoran Li, Dongbin Zhao  

**一句话要点**：提出DEG框架，通过生成式情节指导与双粒度对比奖励，解决具身强化学习中无人工标注的密集奖励设计问题。

**关键词**：具身强化学习, 密集奖励设计, 视频生成模型, 对比自监督学习, 样本效率

## 3 点简述
- 核心问题：具身操作任务中，轨迹成功奖励稀疏，依赖人工标注或专家监督，限制强化学习样本效率。
- 方法要点：利用大型视频生成模型先验知识，基于少量专家视频生成任务指导，设计双粒度对比奖励平衡探索与匹配。
- 实验或效果：在18个模拟与真实任务中验证，DEG能高效探索并稳定收敛，无需人工标注或大量监督。

## 摘要（原文）

> Designing suitable rewards poses a significant challenge in reinforcement learning (RL), especially for embodied manipulation. Trajectory success rewards are suitable for human judges or model fitting, but the sparsity severely limits RL sample efficiency. While recent methods have effectively improved RL via dense rewards, they rely heavily on high-quality human-annotated data or abundant expert supervision. To tackle these issues, this paper proposes Dual-granularity contrastive reward via generated Episodic Guidance (DEG), a novel framework to seek sample-efficient dense rewards without requiring human annotations or extensive supervision. Leveraging the prior knowledge of large video generation models, DEG only needs a small number of expert videos for domain adaptation to generate dedicated task guidance for each RL episode. Then, the proposed dual-granularity reward that balances coarse-grained exploration and fine-grained matching, will guide the agent to efficiently approximate the generated guidance video sequentially in the contrastive self-supervised latent space, and finally complete the target task. Extensive experiments on 18 diverse tasks across both simulation and real-world settings show that DEG can not only serve as an efficient exploration stimulus to help the agent quickly discover sparse success rewards, but also guide effective RL and stable policy convergence independently.

