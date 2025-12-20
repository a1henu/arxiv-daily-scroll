---
layout: default
title: Dual-View Inference Attack: Machine Unlearning Amplifies Privacy Exposure
---

# Dual-View Inference Attack: Machine Unlearning Amplifies Privacy Exposure
**arXiv**：[2512.16126v1](https://arxiv.org/abs/2512.16126) · [PDF](https://arxiv.org/pdf/2512.16126.pdf)  
**作者**：Lulu Xue, Shengshan Hu, Linqiang Qian, Peijin Guo, Yechao Zhang, Minghui Li, Yanjun Zhang, Dayong Ye, Leo Yu Zhang  

**一句话要点**：提出双视图推理攻击DVIA，揭示机器遗忘在双视图设置下放大保留数据隐私风险

**关键词**：机器遗忘, 隐私攻击, 双视图推理, 信息论分析, 黑盒查询, 保留数据隐私

## 3 点简述
- 核心问题：机器遗忘技术虽保护被遗忘数据隐私，但保留数据隐私风险未知，双视图设置可能加剧泄露
- 方法要点：基于信息论提出隐私知识增益概念，设计DVIA攻击，通过黑盒查询双模型，无需训练攻击模型，使用轻量似然比推理模块
- 实验或效果：在不同数据集和模型架构上验证DVIA有效性，突显双视图设置固有隐私风险

## 摘要（原文）

> Machine unlearning is a newly popularized technique for removing specific training data from a trained model, enabling it to comply with data deletion requests. While it protects the rights of users requesting unlearning, it also introduces new privacy risks. Prior works have primarily focused on the privacy of data that has been unlearned, while the risks to retained data remain largely unexplored. To address this gap, we focus on the privacy risks of retained data and, for the first time, reveal the vulnerabilities introduced by machine unlearning under the dual-view setting, where an adversary can query both the original and the unlearned models. From an information-theoretic perspective, we introduce the concept of {privacy knowledge gain} and demonstrate that the dual-view setting allows adversaries to obtain more information than querying either model alone, thereby amplifying privacy leakage. To effectively demonstrate this threat, we propose DVIA, a Dual-View Inference Attack, which extracts membership information on retained data using black-box queries to both models. DVIA eliminates the need to train an attack model and employs a lightweight likelihood ratio inference module for efficient inference. Experiments across different datasets and model architectures validate the effectiveness of DVIA and highlight the privacy risks inherent in the dual-view setting.

