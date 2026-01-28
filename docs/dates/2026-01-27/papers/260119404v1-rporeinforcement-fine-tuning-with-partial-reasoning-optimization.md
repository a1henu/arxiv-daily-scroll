---
layout: default
title: RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization
---

# RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization
**arXiv**：[2601.19404v1](https://arxiv.org/abs/2601.19404) · [PDF](https://arxiv.org/pdf/2601.19404.pdf)  
**作者**：Hongzhu Yi, Xinming Wang, Zhenghao zhang, Tianyu Zong, Yuanxiang Wang, Jun Xie, Tao Yu, Haopeng Jin, Zhepeng Wang, Kaixin Xu, Feng Chen, Jiahuan Chen, Yujia Yang, Zhenyu Guan, Bingkang Shi, Jungang Xu  

**一句话要点**：提出RPO以解决大语言模型强化微调中完整推理轨迹生成的高计算开销问题

**关键词**：强化学习微调, 推理优化, 计算效率, 大语言模型, 训练加速

## 3 点简述
- 核心问题：传统强化微调需生成完整推理路径，导致训练阶段计算开销大
- 方法要点：RPO通过经验缓存生成推理路径后缀，减少约95%的令牌生成
- 实验或效果：在1.5B和7B模型上分别降低训练时间90%和72%，性能与原始算法相当

## 摘要（原文）

> Within the domain of large language models, reinforcement fine-tuning algorithms necessitate the generation of a complete reasoning trajectory beginning from the input query, which incurs significant computational overhead during the rollout phase of training. To address this issue, we analyze the impact of different segments of the reasoning path on the correctness of the final result and, based on these insights, propose Reinforcement Fine-Tuning with Partial Reasoning Optimization (RPO), a plug-and-play reinforcement fine-tuning algorithm. Unlike traditional reinforcement fine-tuning algorithms that generate full reasoning paths, RPO trains the model by generating suffixes of the reasoning path using experience cache. During the rollout phase of training, RPO reduces token generation in this phase by approximately 95%, greatly lowering the theoretical time overhead. Compared with full-path reinforcement fine-tuning algorithms, RPO reduces the training time of the 1.5B model by 90% and the 7B model by 72%. At the same time, it can be integrated with typical algorithms such as GRPO and DAPO, enabling them to achieve training acceleration while maintaining performance comparable to the original algorithms. Our code is open-sourced at https://github.com/yhz5613813/RPO.

