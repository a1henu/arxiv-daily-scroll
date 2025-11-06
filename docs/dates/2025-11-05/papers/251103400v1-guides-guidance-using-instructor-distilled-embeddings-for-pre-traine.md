---
layout: default
title: GUIDES: Guidance Using Instructor-Distilled Embeddings for Pre-trained Robot Policy Enhancement
---

# GUIDES: Guidance Using Instructor-Distilled Embeddings for Pre-trained Robot Policy Enhancement
**arXiv**：[2511.03400v1](https://arxiv.org/abs/2511.03400) · [PDF](https://arxiv.org/pdf/2511.03400.pdf)  
**作者**：Minquan Gao, Xinyi Li, Qing Yan, Xiaojian Sun, Xiaopan Zhang, Chien-Ming Huang, Jiachen Li  

**一句话要点**：提出GUIDES框架以增强预训练机器人策略的语义感知能力

**关键词**：机器人策略增强, 语义指导, 视觉语言模型, 嵌入注入, 推理循环

## 3 点简述
- 预训练机器人策略缺乏语义感知，替换成本高且丢失知识
- 使用微调视觉语言模型生成指导嵌入，注入策略潜在空间
- 在模拟和真实机器人实验中显著提升任务成功率和运动精度

## 摘要（原文）

> Pre-trained robot policies serve as the foundation of many validated robotic
> systems, which encapsulate extensive embodied knowledge. However, they often
> lack the semantic awareness characteristic of foundation models, and replacing
> them entirely is impractical in many situations due to high costs and the loss
> of accumulated knowledge. To address this gap, we introduce GUIDES, a
> lightweight framework that augments pre-trained policies with semantic guidance
> from foundation models without requiring architectural redesign. GUIDES employs
> a fine-tuned vision-language model (Instructor) to generate contextual
> instructions, which are encoded by an auxiliary module into guidance
> embeddings. These embeddings are injected into the policy's latent space,
> allowing the legacy model to adapt to this new semantic input through brief,
> targeted fine-tuning. For inference-time robustness, a large language
> model-based Reflector monitors the Instructor's confidence and, when confidence
> is low, initiates a reasoning loop that analyzes execution history, retrieves
> relevant examples, and augments the VLM's context to refine subsequent actions.
> Extensive validation in the RoboCasa simulation environment across diverse
> policy architectures shows consistent and substantial improvements in task
> success rates. Real-world deployment on a UR5 robot further demonstrates that
> GUIDES enhances motion precision for critical sub-tasks such as grasping.
> Overall, GUIDES offers a practical and resource-efficient pathway to upgrade,
> rather than replace, validated robot policies.

