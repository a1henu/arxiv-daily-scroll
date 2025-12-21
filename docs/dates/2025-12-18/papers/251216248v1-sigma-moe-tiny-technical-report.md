---
layout: default
title: Sigma-Moe-Tiny Technical Report
---

# Sigma-Moe-Tiny Technical Report
**arXiv**：[2512.16248v1](https://arxiv.org/abs/2512.16248) · [PDF](https://arxiv.org/pdf/2512.16248.pdf)  
**作者**：Qingguo Hu, Zhenghao Lin, Ziyue Yang, Yucheng Ding, Xiao Liu, Yuting Jiang, Ruizhe Wang, Tianyu Chen, Zhongxin Guo, Yifan Xiong, Rui Gao, Lei Qu, Jinsong Su, Peng Cheng, Yeyun Gong  

**一句话要点**：提出渐进稀疏化调度以解决极高稀疏度MoE模型中的专家负载平衡问题

**关键词**：混合专家模型, 负载平衡, 渐进稀疏化, 语言模型, 稀疏训练

## 3 点简述
- 核心问题：极高稀疏度MoE模型在底层专家负载平衡失效，影响训练稳定性。
- 方法要点：采用渐进稀疏化调度，逐步增加稀疏度以平衡专家利用和训练稳定性。
- 实验或效果：模型激活仅0.5B参数，在可比规模中达到顶级性能，训练过程稳定无损失尖峰。

## 摘要（原文）

> Mixture-of-Experts (MoE) has emerged as a promising paradigm for foundation models due to its efficient and powerful scalability. In this work, we present Sigma-MoE-Tiny, an MoE language model that achieves the highest sparsity compared to existing open-source models. Sigma-MoE-Tiny employs fine-grained expert segmentation with up to 96 experts per layer, while activating only one expert for each token, resulting in 20B total parameters with just 0.5B activated. The major challenge introduced by such extreme sparsity lies in expert load balancing. We find that the widely-used load balancing loss tends to become ineffective in the lower layers under this setting. To address this issue, we propose a progressive sparsification schedule aiming to balance expert utilization and training stability. Sigma-MoE-Tiny is pre-trained on a diverse and high-quality corpus, followed by post-training to further unlock its capabilities. The entire training process remains remarkably stable, with no occurrence of irrecoverable loss spikes. Comprehensive evaluations reveal that, despite activating only 0.5B parameters, Sigma-MoE-Tiny achieves top-tier performance among counterparts of comparable or significantly larger scale. In addition, we provide an in-depth discussion of load balancing in highly sparse MoE models, offering insights for advancing sparsity in future MoE architectures.
>   Project page: https://qghuxmu.github.io/Sigma-MoE-Tiny
>   Code: https://github.com/microsoft/ltp-megatron-lm

