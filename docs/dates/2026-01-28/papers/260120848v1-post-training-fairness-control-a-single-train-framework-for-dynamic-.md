---
layout: default
title: Post-Training Fairness Control: A Single-Train Framework for Dynamic Fairness in Recommendation
---

# Post-Training Fairness Control: A Single-Train Framework for Dynamic Fairness in Recommendation
**arXiv**：[2601.20848v1](https://arxiv.org/abs/2601.20848) · [PDF](https://arxiv.org/pdf/2601.20848.pdf)  
**作者**：Weixin Chen, Li Chen, Yuhan Zhao  

**一句话要点**：提出Cofair框架以解决推荐系统中动态公平性控制问题，无需为不同公平要求重新训练模型。

**关键词**：推荐系统, 公平性控制, 后训练框架, 动态公平性, 用户嵌入, 正则化方法

## 3 点简述
- 现有公平性方法在训练时固定公平要求，缺乏后训练灵活性，难以适应现实场景中不同利益相关者的动态需求。
- Cofair引入共享表示层和公平条件适配器模块，结合用户级正则化项，实现用户嵌入针对不同公平水平的专门化生成和单调公平改进。
- 在多个数据集和骨干模型上的实验表明，该框架能提供动态公平性，公平性-准确性曲线优于或可比于先进基线，无需为每个新公平要求重新训练。

## 摘要（原文）

> Despite growing efforts to mitigate unfairness in recommender systems, existing fairness-aware methods typically fix the fairness requirement at training time and provide limited post-training flexibility. However, in real-world scenarios, diverse stakeholders may demand differing fairness requirements over time, so retraining for different fairness requirements becomes prohibitive. To address this limitation, we propose Cofair, a single-train framework that enables post-training fairness control in recommendation. Specifically, Cofair introduces a shared representation layer with fairness-conditioned adapter modules to produce user embeddings specialized for varied fairness levels, along with a user-level regularization term that guarantees user-wise monotonic fairness improvements across these levels. We theoretically establish that the adversarial objective of Cofair upper bounds demographic parity and the regularization term enforces progressive fairness at user level. Comprehensive experiments on multiple datasets and backbone models demonstrate that our framework provides dynamic fairness at different levels, delivering comparable or better fairness-accuracy curves than state-of-the-art baselines, without the need to retrain for each new fairness requirement. Our code is publicly available at https://github.com/weixinchen98/Cofair.

