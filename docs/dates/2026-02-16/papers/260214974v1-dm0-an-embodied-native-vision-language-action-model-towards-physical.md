---
layout: default
title: DM0: An Embodied-Native Vision-Language-Action Model towards Physical AI
---

# DM0: An Embodied-Native Vision-Language-Action Model towards Physical AI
**arXiv**：[2602.14974v1](https://arxiv.org/abs/2602.14974) · [PDF](https://arxiv.org/pdf/2602.14974.pdf)  
**作者**：En Yu, Haoran Lv, Jianjian Sun, Kangheng Lin, Ruitao Zhang, Yukang Shi, Yuyang Chen, Ze Chen, Ziheng Zhang, Fan Jia, Kaixin Liu, Meng Zhang, Ruitao Hao, Saike Huang, Songhan Xie, Yu Liu, Zhao Wu, Bin Xie, Pengwei Zhang, Qi Yang, Xianchi Deng, Yunfei Wei, Enwen Zhang, Hongyang Peng, Jie Zhao, Kai Liu, Wei Sun, Yajun Wei, Yi Yang, Yunqiao Zhang, Ziwei Yan, Haitao Yang, Hao Liu, Haoqiang Fan, Haowei Zhang, Junwen Huang, Yang Chen, Yunchao Ma, Yunhuan Yang, Zhengyuan Du, Ziming Liu, Jiahui Niu, Yucheng Zhao, Daxin Jiang, Wenbin Tang, Xiangyu Zhang, Zheng Ge, Erjin Zhou, Tiancai Wang  

**一句话要点**：提出DM0，一种面向物理AI的具身原生视觉-语言-动作模型，统一学习异构数据以提升物理任务性能。

**关键词**：具身人工智能, 视觉-语言-动作模型, 异构数据学习, 流匹配动作专家, 具身空间支架策略, 机器人挑战基准

## 3 点简述
- 核心问题：传统方法依赖互联网预训练模型微调，难以有效处理物理任务中的具身交互与导航。
- 方法要点：采用三阶段训练流程，结合异构数据预训练，并引入流匹配动作专家与具身空间支架策略。
- 实验或效果：在RoboChallenge基准测试中，DM0在Table30上达到最先进性能，适用于专家和通用设置。

## 摘要（原文）

> Moving beyond the traditional paradigm of adapting internet-pretrained models to physical tasks, we present DM0, an Embodied-Native Vision-Language-Action (VLA) framework designed for Physical AI. Unlike approaches that treat physical grounding as a fine-tuning afterthought, DM0 unifies embodied manipulation and navigation by learning from heterogeneous data sources from the onset. Our methodology follows a comprehensive three-stage pipeline: Pretraining, Mid-Training, and Post-Training. First, we conduct large-scale unified pretraining on the Vision-Language Model (VLM) using diverse corpora--seamlessly integrating web text, autonomous driving scenarios, and embodied interaction logs-to jointly acquire semantic knowledge and physical priors. Subsequently, we build a flow-matching action expert atop the VLM. To reconcile high-level reasoning with low-level control, DM0 employs a hybrid training strategy: for embodied data, gradients from the action expert are not backpropagated to the VLM to preserve generalized representations, while the VLM remains trainable on non-embodied data. Furthermore, we introduce an Embodied Spatial Scaffolding strategy to construct spatial Chain-of-Thought (CoT) reasoning, effectively constraining the action solution space. Experiments on the RoboChallenge benchmark demonstrate that DM0 achieves state-of-the-art performance in both Specialist and Generalist settings on Table30.

