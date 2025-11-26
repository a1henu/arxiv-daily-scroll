---
layout: default
title: Image-Free Timestep Distillation via Continuous-Time Consistency with Trajectory-Sampled Pairs
---

# Image-Free Timestep Distillation via Continuous-Time Consistency with Trajectory-Sampled Pairs
**arXiv**：[2511.20410v1](https://arxiv.org/abs/2511.20410) · [PDF](https://arxiv.org/pdf/2511.20410.pdf)  
**作者**：Bao Tang, Shuai Zhang, Yueting Zhu, Jijun Xiang, Xin Yang, Li Yu, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出轨迹反向一致性模型以解决连续时间一致性蒸馏对数据和资源的依赖问题

**关键词**：一致性模型, 时间步蒸馏, 轨迹采样, 无图像蒸馏, 知识迁移, 生成效率

## 3 点简述
- 连续时间一致性蒸馏依赖训练数据和计算资源，限制资源受限场景部署
- 从教师模型生成轨迹提取潜在表示，无需外部数据，提升效率和简化性
- 实验显示一步生成FID 6.52，训练时间减少约40%，节省GPU内存

## 摘要（原文）

> Timestep distillation is an effective approach for improving the generation efficiency of diffusion models. The Consistency Model (CM), as a trajectory-based framework, demonstrates significant potential due to its strong theoretical foundation and high-quality few-step generation. Nevertheless, current continuous-time consistency distillation methods still rely heavily on training data and computational resources, hindering their deployment in resource-constrained scenarios and limiting their scalability to diverse domains. To address this issue, we propose Trajectory-Backward Consistency Model (TBCM), which eliminates the dependence on external training data by extracting latent representations directly from the teacher model's generation trajectory. Unlike conventional methods that require VAE encoding and large-scale datasets, our self-contained distillation paradigm significantly improves both efficiency and simplicity. Moreover, the trajectory-extracted samples naturally bridge the distribution gap between training and inference, thereby enabling more effective knowledge transfer. Empirically, TBCM achieves 6.52 FID and 28.08 CLIP scores on MJHQ-30k under one-step generation, while reducing training time by approximately 40% compared to Sana-Sprint and saving a substantial amount of GPU memory, demonstrating superior efficiency without sacrificing quality. We further reveal the diffusion-generation space discrepancy in continuous-time consistency distillation and analyze how sampling strategies affect distillation performance, offering insights for future distillation research. GitHub Link: https://github.com/hustvl/TBCM.

