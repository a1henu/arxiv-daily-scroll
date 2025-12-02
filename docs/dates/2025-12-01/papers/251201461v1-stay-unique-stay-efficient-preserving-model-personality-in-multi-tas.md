---
layout: default
title: Stay Unique, Stay Efficient: Preserving Model Personality in Multi-Task Merging
---

# Stay Unique, Stay Efficient: Preserving Model Personality in Multi-Task Merging
**arXiv**：[2512.01461v1](https://arxiv.org/abs/2512.01461) · [PDF](https://arxiv.org/pdf/2512.01461.pdf)  
**作者**：Kuangpu Guo, Yuhe Ding, Jian Liang, Zilei Wang, Ran He  

**一句话要点**：提出DTS框架以在模型合并中高效保留任务特定信息

**关键词**：模型合并, 多任务学习, 奇异值分解, 个性化框架, 存储效率

## 3 点简述
- 核心问题：现有模型合并方法在相似任务上性能下降显著，需保留任务特定信息。
- 方法要点：基于奇异值分解、阈值分组和缩放因子，实现个性化合并，存储开销低。
- 实验或效果：DTS在多项任务上优于基线，每任务仅需1%额外存储，变体在未见任务上泛化性能好。

## 摘要（原文）

> Model merging has emerged as a promising paradigm for enabling multi-task capabilities without additional training. However, existing methods often experience substantial performance degradation compared with individually fine-tuned models, even on similar tasks, underscoring the need to preserve task-specific information. This paper proposes Decomposition, Thresholding, and Scaling (DTS), an approximation-based personalized merging framework that preserves task-specific information with minimal storage overhead. DTS first applies singular value decomposition to the task-specific information and retains only a small subset of singular values and vectors. It then introduces a novel thresholding strategy that partitions singular vector elements into groups and assigns a scaling factor to each group. To enable generalization to unseen tasks, we further extend DTS with a variant that fuses task-specific information in a data-free manner based on the semantic similarity of task characteristics. Extensive experiments demonstrate that DTS consistently outperforms state-of-the-art baselines while requiring only 1\% additional storage per task. Furthermore, experiments on unseen tasks show that the DTS variant achieves significantly better generalization performance. Our code is available at https://github.com/krumpguo/DTS.

